"""DistributedDivingGame module: contains the DistributedDivingGame class"""

from direct.showbase.ShowBaseGlobal import *
from toontown.toonbase.ToonBaseGlobal import *
from direct.interval.IntervalGlobal import *
from toontown.toonbase import ToontownTimer
from .DistributedMinigame import *
from direct.distributed.ClockDelta import *
from direct.fsm import ClassicFSM
from direct.fsm import State
from direct.task import Task
from direct.actor import Actor
from toontown.toon import LaffMeter
from direct.distributed import DistributedSmoothNode
from . import ArrowKeys
from . import Ring
from . import RingTrack
from . import DivingGameGlobals
#import DistributedShark

from . import RingGroup
from . import RingTrackGroups
import random
from . import DivingGameToonSD
from . import DivingFishSpawn
from . import DivingTreasure
import math
from . import TreasureScorePanel

from otp.distributed.TelemetryLimiter import TelemetryLimiter, TLGatherAllAvs

from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer

class DivingGameRotationLimiter(TelemetryLimiter):

    def __init__(self, h, p):
        self._h = h
        self._p = p

    def __call__(self, obj):
        obj.setHpr(self._h, self._p, obj.getR())

class DistributedDivingGame(DistributedMinigame):

    COLLISION_WATCH_TASK = "DivingGameCollisionWatchTask"
    TREASURE_BOUNDS_TASK     = "DivingGameTreasureBoundsTask"
    CRAB_TASK = "DivingGameCrabTask"
    UPDATE_LOCALTOON_TASK = "DivingGameUpdateLocalToonTask"
    COLLISION_DETECTION_PRIORITY = 5

    MAP_DIV = 2.8
    MAP_OFF = 14.0
    LAG_COMP = 1.25

    def __init__(self, cr):
        DistributedMinigame.__init__(self, cr)

        self.gameFSM = ClassicFSM.ClassicFSM('DistributedDivingGame',
                               [
                                State.State('off',
                                            self.enterOff,
                                            self.exitOff,
                                            ['swim']),
                                State.State('swim',
                                            self.enterSwim,
                                            self.exitSwim,
                                            ['cleanup']),
                                State.State('cleanup',
                                            self.enterCleanup,
                                            self.exitCleanup,
                                            []),
                                ],
                               # Initial State
                               'off',
                               # Final State
                               'cleanup',
                               )

        # Add our game ClassicFSM to the framework ClassicFSM
        self.addChildGameFSM(self.gameFSM)

        self.iCount = 0
        self.reachedFlag = 0
        self.dead = 0

    def getTitle(self):
        return TTLocalizer.DivingGameTitle

    def getInstructions(self):
        p = self.avIdList.index(self.localAvId)

        if self.isSinglePlayer():
            text = TTLocalizer.DivingInstructionsSinglePlayer
        else:
            text = TTLocalizer.DivingInstructionsMultiPlayer
        return text

    def load(self):
        self.notify.debug("load")
        DistributedMinigame.load(self)

        # loading the environment a
        loadBase = "phase_4/models/minigames/"
        loadBaseShip = "phase_5/models/props/"

        self.sndAmbience = base.loader.loadSfx(
            'phase_4/audio/sfx/AV_ambient_water.mp3')

        self.environModel = loader.loadModel(loadBase + "diving_game.bam")
        #self.environModel = loader.loadModel(loadBase + "seafloor.bam")
        #self.blue = loader.loadModel(loadBase + "blue.bam")
        #self.brown = loader.loadModel(loadBase + "brown.bam")

        #self.boatModel = loader.loadModel(loadBase + "boat.bam")
        self.boatModel = self.environModel.find('**/boat')
        self.skyModel = self.environModel.find('**/sky')
        #self.cliffModel = self.environModel.find('**/cliffs1')
        self.waterModel = self.environModel.find('**/seawater')
        self.frontMap = self.environModel.find('**/sea_front')
        self.frontMap.setY(3)
        self.frontMap.setBin("fixed", 0)
        self.frontMap.setDepthTest(0)
        #self.boatModel = loader.loadModel(loadBaseShip + "ship.bam")

        #self.cliffModel.setY(-0.5)
        self.waterModel.setY(1.0)

        bubbleModel = self.environModel.find('**/bubbles1')
        bubbleModel.setY(1.0)
        bubbleModel = self.environModel.find('**/bubbles2')
        bubbleModel.setY(1.0)
        bubbleModel = self.environModel.find('**/bubbles3')
        bubbleModel.setY(1.0)
        bubbleModel = self.environModel.find('**/bubbles4')
        bubbleModel.setY(1.0)
        bubbleModel = self.environModel.find('**/bubbles5')
        bubbleModel.setY(1.0)

        #self.seaBottom = loader.loadModel(loadBase + "seabottom.bam")

        self.mapModel = loader.loadModel(loadBase + "diving_game.bam")

        boatMap = self.mapModel.find('**/boat')
        skyMap = self.mapModel.find('**/sky')
        frontMap = self.mapModel.find('**/sea_front')
        skyMap.hide()
        frontMap.hide()
        boatMap.setZ(28.5)
        #self.mapModel = loader.loadModel(loadBase + "seafloor.bam")
        #self.borderModel = loader.loadModel(loadBase + "seafloor.bam")

        # the array for the crabs
        self.crabs = []

        # the array for DivingFishSpawns
        self.spawners=[]

        # store the toon states
        self.toonSDs = {}
        # add the local toon now, add remote toons as they join
        avId = self.localAvId
        toonSD = DivingGameToonSD.DivingGameToonSD(avId, self)
        self.toonSDs[avId] = toonSD
        toonSD.load()

        crabSoundName = "King_Crab.mp3"
        crabSoundPath = ("phase_4/audio/sfx/%s" % (crabSoundName))
        self.crabSound = loader.loadSfx(crabSoundPath)

        treasureSoundName = "SZ_DD_treasure.mp3"
        treasureSoundPath = ("phase_4/audio/sfx/%s" % (treasureSoundName))
        self.treasureSound = loader.loadSfx(treasureSoundPath)

        hitSoundName = "diving_game_hit.mp3"
        hitSoundPath = ("phase_4/audio/sfx/%s" % (hitSoundName))
        self.hitSound = loader.loadSfx(hitSoundPath)

        self.music = base.loadMusic("phase_4/audio/bgm/MG_Target.mid")

        self.addSound('dropGold', "diving_treasure_drop_off.mp3", "phase_4/audio/sfx/")
        self.addSound('getGold', "diving_treasure_pick_up.mp3", "phase_4/audio/sfx/")


        self.swimSound = loader.loadSfx("phase_4/audio/sfx/diving_swim_loop.wav")
        self.swimSound.setVolume(0.0)
        self.swimSound.setPlayRate(1.0)
        self.swimSound.setLoop(True)
        self.swimSound.play()

    def addSound(self, name, soundName, path = None):
        if not hasattr(self, "soundTable"):
            self.soundTable = {}
        if path:
            self.soundPath = path
        soundSource = ("%s%s" % (self.soundPath, soundName))
        #print(soundSource)
        self.soundTable[name] = loader.loadSfx(soundSource)

    def playSound(self, name, volume = 1.0):
        self.soundTable[name].setVolume(1.0)
        self.soundTable[name].play()

    def unload(self):
        self.notify.debug("unload")
        DistributedMinigame.unload(self)

        self.mapModel.removeNode()
        del self.mapModel

        #self.borderModel.removeNode()
        #del self.borderModel

        #self.blue.removeNode()
        #del self.blue

        #self.brown.removeNode()
        #del self.brown

        if hasattr(self, "soundTable"):
            del self.soundTable

        del self.sndAmbience
        del self.hitSound
        del self.crabSound
        del self.treasureSound
        self.swimSound.stop()
        del self.swimSound

        self.environModel.removeNode()
        del self.environModel

        # remove our game ClassicFSM from the framework ClassicFSM
        self.removeChildGameFSM(self.gameFSM)
        for avId in list(self.toonSDs.keys()):
            toonSD = self.toonSDs[avId]
            toonSD.unload()
        del self.toonSDs
        del self.gameFSM

        del self.music

    # called when a toon collides with a fish/crab
    # will send a message to the AI about the kind of collision so the AI
    # can handle it for all clients
    def fishCollision(self,collEntry):
        avId = int(collEntry.getFromNodePath().getName())
        toonSD = self.toonSDs[avId]
        name = (collEntry.getIntoNodePath().getName())
        if len(name) >= 7:
            if name[0:6] == "crabby":
                #print("fish collision() - crab")
                self.sendUpdate("handleCrabCollision", [avId, toonSD.status])
        else:
            # send information on the spawning location and the id of the fish
            spawnerId = int(name[2])
            spawnId = int(name[3:len(name)])
            if spawnId in self.spawners[spawnerId].fishArray:
                #print("fish collision() - fish")
                self.sendUpdate("handleFishCollision", [avId, spawnId, spawnerId, toonSD.status])

    # called from the AI to create a fish, create its moveLerp, and set it moving
    # @timestamp        when the AI sent the call
    # @fishcode         type of fish to be spawned
    # @spawnerId        which DivingFishSpawn the fish will be created in
    # @offset           random element created by the AI to add some difference to fish
    def fishSpawn(self, timestamp, fishcode, spawnerId, offset):

        # hack to make sure this never executes if the program is closing
        # using it to avoid some edge conditions before I more extensively
        # try to nail them down
        if self.dead == 1:
            return

        # calculated to make sure all Lerps will start at the same time
        ts = globalClockDelta.localElapsedTime(timestamp)

        # band-aid: make sure this message didn't come in after cleanup
        if not hasattr(self, 'spawners'):
            return

        # make sure we're ignore accidental double message so we don't have two
        # very close fish
        if abs(self.spawners[spawnerId].lastSpawn - timestamp) < 150:
            return

        # returns an Actor nodepath
        fish = self.spawners[spawnerId].createFish(fishcode)


        fish.offset = offset

        fish.setPos(self.spawners[spawnerId].position)
        func = Func(self.fishRemove, fish.code)
        self.spawners[spawnerId].lastSpawn = timestamp

        iName = ("%s %s" % (fish.name, self.iCount))
        self.iCount += 1


        if fish.name == 'clown':
            # clowns move steadily across
            fish.moveLerp = Sequence(LerpPosInterval(fish,duration=8*self.SPEEDMULT*self.LAG_COMP,startPos=self.spawners[spawnerId].position, pos=self.spawners[spawnerId].position+Point3(50*self.spawners[spawnerId].direction,0,((offset-4)/2.0)), name = iName),
                                          func)
            fish.specialLerp = Sequence()
        elif fish.name == 'piano':
            # piano tuna move steadily across, but faster than clowns
            fish.moveLerp = Sequence(LerpPosInterval(fish,duration=5*self.SPEEDMULT*self.LAG_COMP,startPos=self.spawners[spawnerId].position, pos=self.spawners[spawnerId].position+Point3(50*self.spawners[spawnerId].direction,0,((offset-4)/2.0)), name = iName),
                                          func)
            fish.specialLerp = Sequence()
        elif fish.name == 'pbj':
            # pbj fish move slowly, but in a sin wave
            fish.moveLerp = Sequence(LerpFunc(fish.setX,duration=12*self.SPEEDMULT*self.LAG_COMP,fromData=self.spawners[spawnerId].position.getX(), toData=self.spawners[spawnerId].position.getX()+50*self.spawners[spawnerId].direction, name = iName),
                                          func)
            fish.specialLerp = LerpFunc(self.pbjMove, duration=5*self.SPEEDMULT*self.LAG_COMP, fromData=0, toData=2.0*3.14159, extraArgs=[fish,self.spawners[spawnerId].position.getZ()], blendType='easeInOut')
            #fish.specialLerp = Sequence()
        elif fish.name == 'balloon':
            # balloon fish move slowly, but randomly get very big
            fish.moveLerp = Sequence(LerpPosInterval(fish,duration=10*self.SPEEDMULT*self.LAG_COMP,startPos=self.spawners[spawnerId].position, pos=self.spawners[spawnerId].position+Point3(50*self.spawners[spawnerId].direction,0,((offset-4)/2.0)), name = iName),
                                          func)
                                          #[0...10]

            fish.specialLerp = Sequence(Wait(offset/10.0*2+1.5),
                                        Parallel(
                                            LerpScaleInterval(fish, duration=.3, startScale=Vec3(2,2,2), scale=Vec3(5,3,5), blendType='easeInOut'),
                                        ),
                                        Wait(1.0),
                                        Parallel(
                                            LerpScaleInterval(fish, duration=.4, startScale=Vec3(5,3,5), scale=Vec3(2,2,2), blendType='easeInOut'),
                                        ),
                                        )
            #fish.specialLerp = Sequence()
        elif fish.name == 'bear' or fish.name == 'nurse':
            # bear-acude and nurse sharks currently just move steadily across at a slow rate
            # NOTE: the nurse shark would be very cool to have a behavior where it's Lerp causes it to cross the toon with the treasure
            fish.moveLerp = Sequence(LerpPosInterval(fish,duration=20*self.LAG_COMP,startPos=self.spawners[spawnerId].position, pos=self.spawners[spawnerId].position+Point3(50*self.spawners[spawnerId].direction,0,0), name = iName),
                                          func)
            fish.specialLerp = Sequence()

        #fish.moveLerp.setT(ts)
        #fish.specialLerp.setT(ts)

        fish.moveLerp.start(ts)
        fish.specialLerp.loop(ts)

    # small function for the pbjFish.  Basically a sin wave
    def pbjMove(self, x, fish,Z):
        z = math.sin(x+fish.offset*3)*3
        fish.setZ(z+Z)




    # movie goes from where the toons are near the boat, pans to the bottom, then pans up to the toons
    def getIntroMovie(self):
        seq = Sequence()
        seq.append(Wait(2.0))
        seq.append(LerpFunc(camera.setZ, duration=5, fromData=36, toData=-23, blendType='easeInOut', name='intro'))
        seq.append(Wait(2.0))
        seq.append(LerpFunc(camera.setZ, duration=5, fromData=-23, toData=36+3, blendType='easeInOut', name='intro'))
        return seq

    def onstage(self):
        self.notify.debug("onstage")
        DistributedMinigame.onstage(self)
        base.localAvatar.collisionsOff()

        # turn on predictive smoothing
        DistributedSmoothNode.activateSmoothing(1, 1)

        # number of treasures related to number of players
        numToons = self.numPlayers
        self.NUMTREASURES = numToons

        # set camera values and start the intro movie

        camera.reparentTo(render)
        camera.setZ(36)
        camera.setH(0)
        camera.setX(0)
        #camera.setP(-7)
        base.camLens.setMinFov(45 * ToontownGlobals.OriginalAspectRatio)
        camera.setY(-54)
        base.camLens.setFar(1500)

        self.introMovie = self.getIntroMovie()
        self.introMovie.start()

        # this is a message sent from the DivingFishSpawns when one of their
        # fish gets collided into
        self.accept("FishHit",self.fishCollision)

        # put the local toon into a normal state and place them
        toonSD = self.toonSDs[self.localAvId]
        toonSD.enter()
        toonSD.fsm.request('normal')

        toon = base.localAvatar
        toon.reparentTo(render)
        toon.setPos(-9,-1,36)

        self.__placeToon(self.localAvId)

        self.arrowKeys = ArrowKeys.ArrowKeys()

        # the velocities of the toon.  X is left/right.  Z is up/down
        # Y is not used.  This is a 2-D game
        self.xVel = 0
        self.zVel = 0

        # used for trigonometry node for calculating velocity
        self.orientNode = toon.attachNewNode("orientNode")
        self.orientNode.setPos(0,0,1)
        self.orientNode2= toon.attachNewNode("orientNode")
        self.orientNode2.setPos(0,0,-1)

        # load up the environment
        self.environNode = render.attachNewNode("environNode")
        self.environModel.reparentTo(self.environNode)
        self.environModel.setScale(2.8,2.8,2.73)
        self.environModel.setPos(0,.5,-41)



        self.skyModel.setScale(1.3,1.0,1.0)

        # boat also has collision associated with it
        boatoff = 6.75
        self.boatModel.reparentTo(self.environNode)
        self.boatModel.setPos(0,3.0,40-boatoff)
        self.boatModel.setScale(2.8)
        #self.boatModel.setH(90)

        cSphere = CollisionSphere(0.0, 0.0, 0.0 + 2.0,3.0)
        cSphere.setTangible(0)
        name = 'boat'
        cSphereNode = CollisionNode(name)

        cSphereNode.setIntoCollideMask(DivingGameGlobals.CollideMask)
        cSphereNode.addSolid(cSphere)
        self.boatNode = cSphereNode
        self.boatCNP = self.boatModel.attachNewNode(cSphereNode)

        self.accept('reach-boat',self.__boatReached)

        # boat also rocks back and forth
        self.boatTilt = Sequence(LerpFunc(self.boatModel.setR, duration=5, fromData=5, toData=-5, blendType='easeInOut',name = 'tilt'),
                                 LerpFunc(self.boatModel.setR, duration=5, fromData=-5, toData=5, blendType='easeInOut',name='tilt'))
        self.boatTilt.loop()

        # weeds at the bottom for a parallax effect
        #self.seaBottom.reparentTo(self.environNode)
        #self.seaBottom.setPos(0,-5,-35)
        #self.seaBottom.setScale(50,10,15)
        # sky
        #self.blue.reparentTo(render)
        #self.blue.setPos(0,.6,36)
        #self.blue.setScale(50,1,40)
        # dirt
        #self.brown.reparentTo(render)
        #self.brown.setPos(0,.6,-36)
        #self.brown.setScale(50,1,40)

        # minimap stuff.  The bordermodel is just going to be a black border.
        # hackish programmer art
        # they hide until the game starts, although I suppose they don't have to
        # the minimap is intended to help the players work together
        #self.borderModel.reparentTo(aspect2d)
        #self.borderModel.setScale(.56)
        #self.borderModel.setPos(1.15,.1,.35)
        #self.borderModel.setColorScale(0,0,0,.5)
        #self.borderModel.setTransparency(1)
        #self.borderModel.hide()

        self.mapScaleRatio = 40
        self.mapModel.reparentTo(base.a2dTopRight)
        self.mapModel.setScale((1.0 / self.mapScaleRatio))
        self.mapModel.setTransparency(1)
        self.mapModel.setPos(-0.22, 0.0, -1.30)
        self.mapModel.setColorScale(1,1,1,.7)
        self.mapModel.hide()

        if None != self.sndAmbience:
            #base.playSfx(self.sndAmbience, looping = 1, volume = 0.8)
            self.sndAmbience.setLoop(True)
            self.sndAmbience.play()
            self.sndAmbience.setVolume(0.01)

    def offstage(self):
        self.notify.debug("offstage")
        DistributedMinigame.offstage(self)
        self.introMovie.finish()
        self.boatTilt.finish()
        self.mapModel.hide()

        # Restore normal non-predictive smoothing.
        DistributedSmoothNode.activateSmoothing(1, 0)

        for avId in list(self.toonSDs.keys()):
            self.toonSDs[avId].exit()

        # Restore camera
        base.camLens.setFar(ToontownGlobals.DefaultCameraFar)
        base.camLens.setMinFov(ToontownGlobals.DefaultCameraFov)

        # Restore the background color
        base.setBackgroundColor(ToontownGlobals.DefaultBackgroundColor)

        self.arrowKeys.destroy()
        del self.arrowKeys

        self.environNode.removeNode()
        del self.environNode

        if None != self.sndAmbience:
            self.sndAmbience.stop()

        # reset the toons' LODs and show their drop shadows again
        for avId in self.avIdList:
            av = self.getAvatar(avId)
            if av:
                av.showShadow()
                av.resetLOD()
                av.setAnimState('neutral', 1.0)

        self.dead = 1
        self.__killCrabTask()

        # destory the spawners, which will also destroy the fish they have
        for spawner in self.spawners:
            spawner.destroy()
            del spawner
        del self.spawners

        # destroy the crabs
        for crab in self.crabs:
            crab.moveLerp.finish()
            crab.moveLerp = None
            crab.removeNode()
            del crab

        if hasattr(self, 'treasures') and self.treasures:
            for i in range(self.NUMTREASURES):
                self.treasures[i].destroy()
            del self.treasures


        if hasattr(self, "cSphereNodePath1"):
            self.cSphereNodePath1.removeNode()
            del self.cSphereNodePath1

        if hasattr(self, "cSphereNodePath1"):
            self.cSphereNodePath2.removeNode()
            del self.cSphereNodePath2

        if hasattr(self, "remoteToonCollNPs"):
            for np in list(self.remoteToonCollNPs.values()):
                np.removeNode()
            del self.remoteToonCollNPs

        self.pusher = None
        self.cTrav = None
        self.cTrav2 = None

        base.localAvatar.collisionsOn()

    def handleDisabledAvatar(self, avId):
        """This will be called if an avatar exits unexpectedly"""
        self.dead = 1
        self.notify.debug("handleDisabledAvatar")
        self.notify.debug("avatar " + str(avId) + " disabled")
        # remove the disabled toon's shadow, so that the shadow
        # task doesn't crash when it tries to find the toon
        # also, it would look funny to have a shadow and no toon
        #self.__removeToonDropShadow(self.remoteToons[avId])
        self.toonSDs[avId].exit(unexpectedExit = True)
        del self.toonSDs[avId]
        #DistributedMinigame.handleDisabledAvatar(self, avId)

    # places toons organized left to right
    def __placeToon(self,avId):
        toon = self.getAvatar(avId)
        i = self.avIdList.index(avId)
        numToons = float(self.numPlayers)
        x = -10 + i * 5
        toon.setPos(x, -1, 36)
        toon.setHpr(180,180,0)

    def getTelemetryLimiter(self):
        return TLGatherAllAvs('DivingGame',
                              Functor(DivingGameRotationLimiter,
                              180, 180))


    def setGameReady(self):
        self.notify.debug("setGameReady")
        if not self.hasLocalToon:
            return
        if DistributedMinigame.setGameReady(self):
            return
        self.dead = 0

        # difficulty patterns for each zone
        # NUMCRABS, SPEEDMULT, TIME
        self.difficultyPatterns = {
            ToontownGlobals.ToontownCentral:
            [ 1, 1.5, 65, 3
              ],
            ToontownGlobals.DonaldsDock:
            [ 1, 1.3, 65, 1
              ],
            ToontownGlobals.DaisyGardens:
            [ 2, 1.2, 65, 1
              ],
            ToontownGlobals.MinniesMelodyland:
            [ 2, 1.0, 65, 1
              ],
            ToontownGlobals.TheBrrrgh:
            [ 3, 1.0, 65, 1
              ],
            ToontownGlobals.DonaldsDreamland:
            [ 3, 1.0, 65, 1
              ],
            }

        pattern = self.difficultyPatterns[self.getSafezoneId()]
        self.NUMCRABS = pattern[0]
        self.SPEEDMULT = pattern[1]
        self.TIME = pattern[2]



        # load up the crabs.  They stay at the bottom and their movement
        # is regulated by the AI because they tend to cluster around the
        # x midpoint of all the treasures.  They also can push the player
        loadBase = "phase_4/models/char/"

        for i in range(self.NUMCRABS):
            self.crabs.append(Actor.Actor(loadBase + 'kingCrab-zero.bam',{'anim': loadBase + 'kingCrab-swimLOOP.bam'}))

        for i in range(len(self.crabs)):
            crab = self.crabs[i]
            crab.reparentTo(render)
            crab.name = 'king'
            crab.crabId = i
            cSphere = CollisionSphere(0.0,0.0,1,1.3)

            cSphereNode = CollisionNode("crabby"+str(i))
            cSphereNode.addSolid(cSphere)
            cSphereNode.setFromCollideMask(BitMask32.allOff())
            cSphereNode.setIntoCollideMask(DivingGameGlobals.CollideMask)
            cSphereNodePath = crab.attachNewNode(cSphereNode)
            cSphereNodePath.setScale(1,3,1)

            self.accept('hitby-'+'crabby'+str(i), self.fishCollision)

            if i % 2 == 0:
                crab.setPos(20, 0, -40)
                crab.direction = -1
            else:
                crab.setPos(-20, 0, -40)
                crab.direction = 1
            crab.loop("anim")
            crab.setScale(1,.3,1)
            crab.moveLerp=Sequence()

        # collision setup
        # the first traverser is for the handler event, the second is for the pusher
        self.collHandEvent=CollisionHandlerEvent()
        self.cTrav = CollisionTraverser("DistributedDiverGame")
        self.cTrav2 = CollisionTraverser("DistributedDiverGame")

        # for the boat
        self.collHandEvent.addInPattern('reach-%in')
        self.collHandEvent.addAgainPattern('reach-%in')

        # for the chest and the crab
        self.collHandEvent.addInPattern('into-%in')
        self.collHandEvent.addInPattern('hitby-%in')

        # loading the treasures
        loadBase = "phase_4/models/minigames/"

        self.treasures = []
        # chestIcons is for the minimap
        self.chestIcons = {}
        for i in range(self.NUMTREASURES):
            self.chestIcons[i] = loader.loadModel(loadBase + "treasure_chest.bam")
            self.chestIcons[i].reparentTo(self.mapModel)
            self.chestIcons[i].setScale(1.5)

            treasure = DivingTreasure.DivingTreasure(i)

            self.accept('grab-'+str(i),self.__treasureGrabbed)
            self.collHandEvent.addInPattern('grab-%in')
            self.collHandEvent.addAgainPattern('grab-%in')
            self.treasures.append(treasure)

        self.cTrav.traverse(render)

        spawnX = 24 * self.LAG_COMP
        spawnY = 0.6
        # create the DivingFishSpawns, they are placed around the sides of the map
        self.spawners.append(DivingFishSpawn.DivingFishSpawn(0,1, Point3(-spawnX,spawnY,25), self.collHandEvent))
        self.spawners.append(DivingFishSpawn.DivingFishSpawn(1,-1, Point3(spawnX,spawnY,16), self.collHandEvent))
        self.spawners.append(DivingFishSpawn.DivingFishSpawn(2,1, Point3(-spawnX,spawnY,6), self.collHandEvent))
        self.spawners.append(DivingFishSpawn.DivingFishSpawn(3,-1, Point3(spawnX,spawnY,-4), self.collHandEvent))
        self.spawners.append(DivingFishSpawn.DivingFishSpawn(4,1, Point3(-spawnX,spawnY,-15), self.collHandEvent))
        self.spawners.append(DivingFishSpawn.DivingFishSpawn(5,-1, Point3(spawnX,spawnY,-23), self.collHandEvent))

        # value for fishSpawn()
        for spawner in self.spawners:
            spawner.lastSpawn = 0

        # player collision load
        # currently made up of two spheres
        # might eventually make it so you can only pick up the treasure with
        # the front sphere, to avoid people picking it up with their feet
        cSphere = CollisionSphere(0.0,0.0,0.0,1.4)
        cSphereNode = CollisionNode('%s' % self.localAvId)
        cSphereNode.addSolid(cSphere)
        cSphereNode.setFromCollideMask(DivingGameGlobals.CollideMask)
        cSphereNode.setIntoCollideMask(BitMask32.allOff())

        headparts = base.localAvatar.getHeadParts()
        pos = headparts[2].getPos()
        self.cSphereNodePath1 = base.localAvatar.attachNewNode(cSphereNode)
        self.cSphereNodePath1.setPos(pos+Point3(0,1.5,1))
        self.cTrav.addCollider(self.cSphereNodePath1 , self.collHandEvent)

        cSphere = CollisionSphere(0.0,0.0,0.0,1.4)
        cSphereNode = CollisionNode('%s' % self.localAvId)
        cSphereNode.addSolid(cSphere)
        cSphereNode.setFromCollideMask(DivingGameGlobals.CollideMask)
        cSphereNode.setFromCollideMask(BitMask32.allOff())
        cSphereNode.setIntoCollideMask(BitMask32.allOff())

        headparts = base.localAvatar.getHeadParts()
        pos = headparts[2].getPos()
        self.cSphereNodePath2 = base.localAvatar.attachNewNode(cSphereNode)
        self.cSphereNodePath2.setPos(pos+Point3(0,1.5,-1))
        self.cTrav.addCollider(self.cSphereNodePath2 , self.collHandEvent)

        self.pusher = CollisionHandlerPusher()
        self.pusher.addCollider(self.cSphereNodePath1, base.localAvatar)
        self.pusher.addCollider(self.cSphereNodePath2, base.localAvatar)

        # if we don't clear this, the toons will stick to each other
        # when moving purely along the X-axis
        self.pusher.setHorizontal(0)

        # add to the pusher
        self.cTrav2.addCollider(self.cSphereNodePath1, self.pusher)
        self.cTrav2.addCollider(self.cSphereNodePath2, self.pusher)

        # create collision spheres on the remote toons
        self.remoteToonCollNPs = {}
        for avId in self.remoteAvIdList:
            toon = self.getAvatar(avId)

            if toon:
                headparts = toon.getHeadParts()
                pos = headparts[2].getPos()

                cSphere = CollisionSphere(0.0, 0.0, 0.0,1.4)
                cSphereNode = CollisionNode('%s' % avId)
                cSphereNode.addSolid(cSphere)
                cSphereNode.setCollideMask(DivingGameGlobals.CollideMask)
                cSphereNP = toon.attachNewNode(cSphereNode)
                cSphereNP.setPos(pos + Point3(0,1.5,1))
                #cSphereNP.show()
                self.remoteToonCollNPs[int(str(avId)+str(1))] = cSphereNP

                cSphere = CollisionSphere(0.0, 0.0, 0.0,1.4)
                cSphereNode = CollisionNode('%s' % avId)
                cSphereNode.addSolid(cSphere)
                cSphereNode.setCollideMask(DivingGameGlobals.CollideMask)
                cSphereNP = toon.attachNewNode(cSphereNode)
                cSphereNP.setPos(pos + Point3(0,1.5,-1))
                #cSphereNP.show()
                self.remoteToonCollNPs[int(str(avId)+str(1))] = cSphereNP

                # create the toonSD for this toon
                toonSD = DivingGameToonSD.DivingGameToonSD(avId, self)
                self.toonSDs[avId] = toonSD
                toonSD.load()
                toonSD.enter()
                toonSD.fsm.request('normal')

        # show the remote toons
        for avId in self.remoteAvIdList:
            toon = self.getAvatar(avId)
            if toon:
                toon.reparentTo(render)
                self.__placeToon(avId)
                toon.startSmooth()

        # make a table of the remote toons
        self.remoteToons = {}
        for avId in self.remoteAvIdList:
            toon = self.getAvatar(avId)
            self.remoteToons[avId] = toon

    def setGameStart(self, timestamp):
        if not self.hasLocalToon: return
        DistributedMinigame.setGameStart(self, timestamp)
        self.notify.debug("setGameStart")

        # score panel in the upper left
        self.treasurePanel = TreasureScorePanel.TreasureScorePanel()
        self.treasurePanel.setPos(0.145, 0, -0.27)
        self.treasurePanel.reparentTo(base.a2dTopLeft)
        self.treasurePanel.makeTransparent(.7)

        # make sure intro is finished
        self.introMovie.finish()

        # base class will cause gameFSM to enter initial state
        self.gameFSM.request("swim")

    def enterOff(self):
        self.notify.debug("enterOff")

    def exitOff(self):
        pass

    def enterSwim(self):
        self.notify.debug("enterSwim")

        # Start music
        base.playMusic(self.music, looping = 1, volume = 0.9)

        # lerp used to hold if a local toon gets hit and frozen
        self.localLerp = Sequence()

        # create the timer
        self.timer = ToontownTimer.ToontownTimer()
        self.timer.posInTopRightCorner()
        self.timer.setTime(self.TIME)
        self.timer.countdown(self.TIME, self.timerExpired)
        self.mapModel.show()
        #self.borderModel.show()

        # minimap avatars
        self.mapAvatars = {}

        avatarScale = (0.025 * self.mapScaleRatio)

        # remote avatars
        for avId in self.remoteAvIdList:
            # This statement crashes if avId is not in the dictionary
            # like when a toon exits unexpectedly
            #                   avatar = base.cr.doId2do[avId]
            # So instead let's try this get function which will tell us without crashing
            avatar = base.cr.doId2do.get(avId, False)
            if avatar != False:
                self.mapAvatars[avId] = LaffMeter.LaffMeter(avatar.style,
                                                            avatar.hp,
                                                            avatar.maxHp)
                self.mapAvatars[avId].reparentTo(self.mapModel)
                self.mapAvatars[avId].setScale(avatarScale)
                self.mapAvatars[avId].start()

        # local avatar
        avatar = base.cr.doId2do[self.localAvId]
        self.mapAvatars[self.localAvId] = LaffMeter.LaffMeter(avatar.style,
                                                        avatar.hp,
                                                        avatar.maxHp)
        self.mapAvatars[self.localAvId].reparentTo(self.mapModel)
        self.mapAvatars[self.localAvId].setScale(avatarScale)
        self.mapAvatars[self.localAvId].start()

        self.accept("resetClock", self.__resetClock)

        self.__spawnUpdateLocalToonTask()
        self.__spawnCrabTask()
        self.__spawnTreasureBoundsTask()

    def __resetClock(self, tOffset):
        self.notify.debug("resetClock")
        self.gameStartTime += tOffset
        self.timer.countdown(self.timer.currentTime + tOffset,
                             self.timerExpired)

    # called when the game ends
    def timerExpired(self):
        self.notify.debug("local timer expired")
        # uncomment these to actually end the game
        self.dead = 1
        self.gameOver()

    def __initPosBroadcast(self):
        self.__posBroadcastPeriod = 0.2
        self.__timeSinceLastPosBroadcast = 0.
        self.__lastPosBroadcast = self.getAvatar(self.localAvId).getPos()
        self.__storeStop = 0
        # do an initial broadcast of the full position
        lt = self.getAvatar(self.localAvId)
        lt.d_clearSmoothing()
        lt.sendCurrentPosition()

    def __posBroadcast(self, dt):
        self.__timeSinceLastPosBroadcast += dt
        if self.__timeSinceLastPosBroadcast > self.__posBroadcastPeriod:
            self.__timeSinceLastPosBroadcast -= self.__posBroadcastPeriod
            self.getAvatar(self.localAvId).cnode.broadcastPosHprFull()

    """
    TREASURE BOUNDS TASK
    """

    def __spawnTreasureBoundsTask(self):
        taskMgr.remove(self.TREASURE_BOUNDS_TASK)
        taskMgr.add(self.__treasureBoundsTask, self.TREASURE_BOUNDS_TASK)

    def __killTreasureBoundsTask(self):
        taskMgr.remove(self.TREASURE_BOUNDS_TASK)

    # currently just used to check that the treasure chest is in bounds,
    # and to update the minimap
    def __treasureBoundsTask(self, task):
        for i in range(self.NUMTREASURES):
            self.chestIcons[i].setPos(self.treasures[i].chest.getPos(render)/self.MAP_DIV)
            self.chestIcons[i].setZ(self.chestIcons[i].getZ() + self.MAP_OFF)

            if self.treasures[i].treasureNode.getZ() < -36:
                self.treasures[i].treasureNode.setZ(-36)

            if self.treasures[i].treasureNode.getX() < -20:
                self.treasures[i].treasureNode.setX(-20)

            if self.treasures[i].treasureNode.getX() > 20:
                self.treasures[i].treasureNode.setX(20)
        return Task.cont

    # called from the AI when a toon has reached the boat with a treasure chest
    # @avId             the toon that reached the boat
    # @newSpot          the new position of the next chest spawn
    # @timestamp        when the AI called it
    def incrementScore(self, avId, newSpot, timestamp):
        # protect against purchase tutorial
        if not self.hasLocalToon:
            return
        newSpot += -15
        ts = globalClockDelta.localElapsedTime(timestamp)
        toonSD = self.toonSDs[avId]
        if avId == self.localAvId:
            self.reachedFlag = 0
        # we do a quick check to make sure the toon really does have a treasure (and all the assets are still here)
        if toonSD.status == "treasure" and self.treasures and self.chestIcons:
            for i in range(self.NUMTREASURES):
                # make sure message matches our data
                if self.treasures[i].grabbedId == avId:
                    # reparent the treasure back to render, and have it jump and shrink onto the boat
                    # also have it shrink on the minimap
                    self.treasures[i].treasureNode.wrtReparentTo(render)
                    self.treasures[i].grabbedId = 0
                    seq = Sequence()
                    shrink = LerpScaleInterval(self.treasures[i].treasureNode, duration=1.0, startScale=self.treasures[i].treasureNode.getScale(),
                                               scale = Vec3(.001, .001, .001), blendType='easeIn')
                    shrinkIcon = LerpScaleInterval(self.chestIcons[i], duration=1.0, startScale=self.chestIcons[i].getScale(),
                                                   scale = Vec3(.001, .001, .001), blendType='easeIn')
                    jump = ProjectileInterval(self.treasures[i].treasureNode, duration = 1.0, startPos=self.treasures[i].treasureNode.getPos(),
                                              endPos=Point3(0, 0, 40), gravityMult = .7)

                    shrinkJump = Parallel(shrink, shrinkIcon, jump)

                    # return the toon to normal
                    toonSD.fsm.request("normal")

                    # respawn the treasure in a new spot at the bottom, along with updating minimap
                    grow = LerpScaleInterval(self.treasures[i].treasureNode, duration=1.0, scale=self.treasures[i].treasureNode.getScale(),
                                               startScale = Vec3(.001, .001, .001), blendType='easeIn')
                    growIcon = LerpScaleInterval(self.chestIcons[i], duration=1.0, scale=self.chestIcons[i].getScale(),
                                                   startScale = Vec3(.001, .001, .001), blendType='easeIn')

                    place = Parallel(Func(self.treasures[i].treasureNode.setPos, Vec3(newSpot, .25, -36)),
                                     Func(self.treasures[i].treasureNode.setHpr, Vec3(0, 0, 0)))

                    growItems = Parallel(grow, growIcon)

                    # set the collidemask back on
                    resetChest = Func(self.treasures[i].chestNode.setIntoCollideMask,DivingGameGlobals.CollideMask)

                    seq = Sequence(shrinkJump, Wait(1.5), place, growItems, resetChest)
                    self.treasures[i].moveLerp.pause()
                    self.treasures[i].moveLerp = seq
                    self.treasures[i].moveLerp.start(ts)

                    #play the sound
                    #self.treasureSound.play()
                    self.playSound("dropGold")

                    # increment the score panel
                    self.treasurePanel.incrScore()

    # called when a toon reaches the boat.  Sends a message to the AI
    def __boatReached(self, collEntry):
        toonSD = self.toonSDs[self.localAvId]
        if toonSD.status == "treasure" and not self.reachedFlag:
            self.sendUpdate("treasureRecovered")
            self.reachedFlag = 1

    # when the treasure is grabbed when a toon is normal,
    # a message is sent to the AI with the ID of the chest
    def __treasureGrabbed(self, collEntry):
        avId = int(collEntry.getFromNodePath().getName())
        chestId = int(collEntry.getIntoNodePath().getName())
        toonSD = self.toonSDs[avId]
        if toonSD.status == "normal":
            self.sendUpdate("pickupTreasure", [chestId])

    # called by the AI to have a toon drop a treasure
    def setTreasureDropped(self, avId, timestamp):
        if not hasattr(self, "treasures"):
            return
        ts = globalClockDelta.localElapsedTime(timestamp)

        # find the treasure that is currently grabbed by the avatar
        for i in range(self.NUMTREASURES):
            if self.treasures[i].grabbedId == avId:
                self.treasures[i].grabbedId = 0

                toonSD = self.toonSDs[avId]

                # for the chest to drop, we actually create a lerp that gets it
                # to the bottom, with the duration of the lerp being related to
                # the distance in z of the chest and the bottom
                dist = abs(36.0 + self.treasures[i].treasureNode.getZ(render))
                delta = dist/72.0
                dur = 10 * delta

                # we also make the chest collideable, making it so people can
                # catch it 1 second after it's dropped
                self.treasures[i].treasureNode.wrtReparentTo(render)
                self.treasures[i].chestNode.setIntoCollideMask(BitMask32.allOff())
                resetChest = Func(self.treasures[i].chestNode.setIntoCollideMask,DivingGameGlobals.CollideMask)
                self.treasures[i].moveLerp.pause()
                self.treasures[i].moveLerp = Parallel(Sequence(Wait(1.0), resetChest),
                                                         LerpFunc(self.treasures[i].treasureNode.setZ, duration=dur, fromData=self.treasures[i].treasureNode.getZ(render), toData=-36, blendType='easeIn'))
                self.treasures[i].moveLerp.start(ts)

    # called from the AI to make the toon freeze
    # basically a simplified version of fish collision
    def performCrabCollision(self, avId, timestamp):
        if not self.hasLocalToon: return
        ts = globalClockDelta.localElapsedTime(timestamp)
        toonSD = self.toonSDs[avId]

        toon = self.getAvatar(avId)
        distance = base.localAvatar.getDistance(toon)

        volume = 0
        soundRange = 15.0
        if distance < soundRange:
            volume = ((soundRange - distance) / soundRange)

        if toonSD.status == 'normal' or toonSD.status == 'treasure':
            self.localLerp.finish()
            self.localLerp = Sequence(Func(toonSD.fsm.request,'freeze'), Wait(3.0), Func(toonSD.fsm.request,'normal'))
            self.localLerp.start(ts)
            self.hitSound.play()
            self.hitSound.setVolume(volume)

    # called from the AI to make the toon freeze and have the fish respond
    # in a certain way (depending on the fish type)
    def performFishCollision(self, avId, spawnId, spawnerId, timestamp):
        if not hasattr(self, "spawners"):
            return
        toonSD = self.toonSDs[avId]
        ts = globalClockDelta.localElapsedTime(timestamp)

        toon = self.getAvatar(avId)
        distance = base.localAvatar.getDistance(toon)

        volume = 0
        soundRange = 15.0
        if distance < soundRange:
            volume = ((soundRange - distance) / soundRange)

        # if the toon is unfrozen, freeze him up
        # possibly make it so you freeze longer if you had the chest
        if toonSD.status == 'normal' or toonSD.status == 'treasure':
            self.localLerp.finish()
            self.localLerp = Sequence(Func(toonSD.fsm.request,'freeze'), Wait(3.0), Func(toonSD.fsm.request,'normal'))
            self.localLerp.start(ts)

        if spawnId in self.spawners[spawnerId].fishArray:
            fish = self.spawners[spawnerId].fishArray[spawnId]
            endX = self.spawners[spawnerId].position.getX()


            if fish.name == 'clown':
                fishSoundName = "Clownfish.mp3"
            elif fish.name == 'pbj':
                fishSoundName = "PBJ_Fish.mp3"
            elif fish.name == 'balloon':
                fishSoundName = "BalloonFish.mp3"
            elif fish.name == 'bear':
                fishSoundName = "Bear_Acuda.mp3"
            elif fish.name == 'nurse':
                fishSoundName = "Nurse_Shark.mp3"
            elif fish.name == 'piano':
                fishSoundName = "Piano_Tuna.mp3"
            else:
                fishSoundName = " "

            fishSoundPath = ("phase_4/audio/sfx/%s" % (fishSoundName))
            fish.sound = loader.loadSfx(fishSoundPath)

            if fish.sound:
                fish.sound.play()
                fish.sound.setVolume(volume)
                self.hitSound.play()
                self.hitSound.setVolume(volume)


            # bears and nurses don't care about you and will go about their merry way
            if fish.name == 'bear' or fish.name == 'nurse':
                return

            colList = fish.findAllMatches("**/fc*")
            for col in colList:
                col.removeNode()

            fish.moveLerp.pause()

            # clowns and pianos will turn around and head back to home
            if fish.name == 'clown' or fish.name == 'piano':
                ##print("here")
                if fish.name != 'piano':
                    endHpr = Vec3(fish.getH()*-1, 0, 0)
                else:
                    if fish.direction == -1:
                        endHpr = Vec3(180,0,0)
                    else:
                        endHpr = Vec3(0,0,0)
                fish.moveLerp = Sequence(LerpHprInterval(fish, duration=.4, startHpr=fish.getHpr(), hpr=endHpr),
                                         LerpFunc(fish.setX, duration=1.5, fromData=fish.getX(), toData=endX),
                                         Func(self.fishRemove,str(spawnerId)+str(spawnId)))
            elif fish.name == 'pbj':
                #pbjfish just reverse themselves
                fish.moveLerp = Sequence(LerpFunc(fish.setX, duration=2, fromData=fish.getX(), toData=endX),
                                         Func(self.fishRemove,str(spawnerId)+str(spawnId)))
            elif fish.name == 'balloon':
                # balloon fish pop
                fish.specialLerp.pause()
                anim = Func(fish.play, 'anim', fromFrame=110, toFrame=200)
                # setH here to make sure the fish won't intersect the environment
                fish.setH(180)

                speed = Func(fish.setPlayRate, 3.0, 'anim')
                fish.moveLerp = Sequence(Func(fish.stop,'anim'), speed, anim,Wait(1.0),
                                         LerpScaleInterval(fish, duration=.8, startScale=fish.getScale, scale=.001, blendType='easeIn'),
                                         Func(self.fishRemove,str(spawnerId)+str(spawnId)))
                fish.sound.setTime(11.5)



            fish.moveLerp.start(ts)

    # removes a given fish
    def fishRemove(self, code):
        spawnId = int(code[1:len(code)])
        spawnerId = int(code[0])

        #print("FISH REMOVE TOO")
        if spawnId in self.spawners[spawnerId].fishArray:
            fish = self.spawners[spawnerId].fishArray[spawnId]
            fish.specialLerp.finish()
            fish.moveLerp.finish()
            fish.specialLerp = None
            fish.moveLerp = None
            fish.removeNode()

            del fish
            del self.spawners[spawnerId].fishArray[spawnId]
        else:
            import pdb;pdb.setTrace()

    # AI calls to set the treasure as grabbed
    def setTreasureGrabbed(self, avId, chestId):
        if not self.hasLocalToon:
            return
        # we seem to be getting a number of client crashes here, let's use get()
        toonSD = self.toonSDs.get(avId)
        if toonSD and toonSD.status == 'normal':

            toonSD.fsm.request("treasure")
            self.treasures[chestId].moveLerp.pause()
            self.treasures[chestId].moveLerp = Sequence()
            self.treasures[chestId].chestNode.setIntoCollideMask(BitMask32.allOff())
            self.treasures[chestId].treasureNode.reparentTo(self.getAvatar(avId))

            # currently placed in relation to Head parts, should be at hands,
            # but that will wait till a hold swimming animation is done
            headparts = self.getAvatar(avId).getHeadParts()
            pos = headparts[2].getPos()
            self.treasures[chestId].treasureNode.setPos(pos+Point3(0,.2,3))
            self.treasures[chestId].grabbedId = avId
            timestamp = globalClockDelta.getFrameNetworkTime()

            self.playSound("getGold")

    """
    CRAB TASK
    """

    def __spawnCrabTask(self):
        taskMgr.remove(self.CRAB_TASK)
        taskMgr.add(self.__crabTask, self.CRAB_TASK)

    def __killCrabTask(self):
        taskMgr.remove(self.CRAB_TASK)

    def __crabTask(self, task):
        dt = globalClock.getDt()
        # if crab is not moving, tell the AI to get them moving with the new calc
        for crab in self.crabs:
            if not (crab.moveLerp.isPlaying()):
                # the looped Wait makes sure we don't send an update again next frame
                crab.moveLerp = Wait(1.0)
                crab.moveLerp.loop()
                self.sendUpdate("getCrabMoving", [crab.crabId, crab.getX(), crab.direction])
                return Task.cont
        return Task.cont

    # called from the AI to get the crab moving
    # the random elements is an int between 1 and 10 that will
    # be used for some randomness, but passed so all clients are uniform
    #
    # there is probably a better way to do this with randomNumGen
    #
    # @crabId           id of the crab
    # @timestamp        time the AI called
    # @rand1            'random' element
    # @rand2            'random' element
    # @crabX            x value of crab (for uniformity)
    # @dir              direction of crab (for uniformity)
    def setCrabMoving(self, crabId, timestamp, rand1, rand2, crabX, dir):

        # hackish way to protect from edge conditions (for now)
        if self.dead == 1:
            self.__killCrabTask()
            return

        # hackish way to prevent client crash
        if not hasattr(self, 'crabs'):
            return

        crab = self.crabs[crabId]

        ts = globalClockDelta.localElapsedTime(timestamp)
        x = 0

        # find mid point of treasure chests.  Crabs work around there
        for i in range(self.NUMTREASURES):
            x += self.treasures[i].treasureNode.getX(render)
        x /= self.NUMTREASURES


        goalX = int(x+dir*(rand1/10.0)*12+4.0)
        goalZ = -40+5+5*(rand2/10.0)
        xTime = 1+(rand1/10.0)*2
        zTime = .5+(rand2/10.0)
        wait = (rand1/10.0) + (rand2/10.0) + 1

        crab.direction *= -1

        if goalX > 20:
            goalX = 20
        elif goalX < -20:
            goalX = 20

        loc = crab.getPos(render)

        distance = base.localAvatar.getDistance(crab)

        crabVolume = 0
        soundRange = 25.0
        if distance < soundRange:
            crabVolume = ((soundRange - distance) / soundRange)

        crabSoundInterval = SoundInterval(
            self.crabSound,
            loop = 0,
            duration = 1.6,
            startTime = 0.0
        )

        # crab waits, a bit, moves, then jumps.
        seq = Sequence(Wait(wait),
                            LerpPosInterval(crab, duration=xTime, startPos = Point3(crabX,0,-40), pos=Point3(goalX,0,-40), blendType='easeIn'),
                            Parallel(
                                Func(self.grabCrabVolume, crab),
                                LerpPosInterval(crab, duration=zTime, startPos=Point3(goalX,0,-40), pos=Point3(goalX,0,goalZ), blendType='easeOut'),
                            ),
                            LerpPosInterval(crab, duration=zTime, startPos=Point3(goalX,0,goalZ), pos=Point3(goalX,0,-40), blendType='easeInOut')
                        )

        crab.moveLerp.pause()
        crab.moveLerp = seq
        crab.moveLerp.start(ts)

    """
    UPDATE LOCAL TASK
    """

    def grabCrabVolume(self, crab):
        if crab:
            distance = base.localAvatar.getDistance(crab)
            self.crabVolume = 0
            soundRange = 25.0
            if distance < soundRange:
                crabVolume = ((soundRange - distance) / soundRange)
                #crabSoundInterval.setVolume(crabVolume)
                crabSoundInterval = SoundInterval(
                    self.crabSound,
                    loop = 0,
                    duration = 1.6,
                    startTime = 0.0,
                    volume = crabVolume,)
                crabSoundInterval.start()



    def __spawnUpdateLocalToonTask(self):
        self.__initPosBroadcast()
        taskMgr.remove(self.UPDATE_LOCALTOON_TASK)
        taskMgr.add(self.__updateLocalToonTask, self.UPDATE_LOCALTOON_TASK)

    def __killUpdateLocalToonTask(self):
        taskMgr.remove(self.UPDATE_LOCALTOON_TASK)

    def __updateLocalToonTask(self, task):
        dt = globalClock.getDt()

        """
        NEED TO ADD A CLAMP TO AVATAR VELOCITY ADDS
        RIGHT NOW EVERY FRAME IT ADDS VELOCITY, WHICH IS TOO MUCH
        """
        toonPos = base.localAvatar.getPos()
        toonHpr = base.localAvatar.getHpr()

        self.xVel *= .99
        self.zVel *= .99

        pos = [toonPos[0], toonPos[1], toonPos[2]]
        hpr = [toonHpr[0], toonHpr[1], toonHpr[2]]

        r = 0

        toonSD = self.toonSDs[self.localAvId]
        if toonSD.status == "normal" or toonSD.status == "treasure":
            if self.arrowKeys.leftPressed():
                r -= 80
            if self.arrowKeys.rightPressed():
                r += 80
            hpr[2] += r * dt

            # VECTORS!
            pos1 = self.orientNode.getPos(render)
            pos2 = self.orientNode2.getPos(render)
            upVec = Vec2(pos1[0],pos1[2])
            bkVec = Vec2(pos2[0],pos2[2])
            forVec = upVec - Vec2(pos[0],pos[2])
            bckVec = bkVec - Vec2(pos[0],pos[2])


            r = 0
            if self.arrowKeys.upPressed():
                r += 20
                self.xVel = forVec[0]*8
                self.zVel = forVec[1]*8
            elif self.arrowKeys.downPressed():
                r -= 20
                self.xVel = bckVec[0]*4
                self.zVel = bckVec[1]*4

            if self.xVel > 20:
                self.xVel = 20
            elif self.xVel < -20:
                self.xVel = -20

            if self.zVel > 10:
                self.zVel = 10
            elif self.zVel < -10:
                self.zVel = -10

        swimVolume = (abs(self.zVel) + abs(self.xVel)) / 15.0
        self.swimSound.setVolume(swimVolume)

        pos[0] += (self.xVel * dt)
        pos[1] = -2
        pos[2] += (self.zVel * dt)

        # this creates a sink factor for those carrying the treasure,
        # and a float factor for those without the treasure
        found = 0
        for i in range (self.NUMTREASURES):
            if self.treasures[i].grabbedId == self.localAvId:
                found = 1
                i = self.NUMTREASURES + 1
                pos[2] -= 0.8 * dt
        if found == 0:
            pos[2] += 0.8 * dt

        # bounds checking
        if pos[2] < -38:
            pos[2] = -38
        elif pos[2] > 36:
            pos[2] = 36

        if pos[0] < -20:
            pos[0] = -20
        elif pos[0] > 20:
            pos[0] = 20

        base.localAvatar.setPos(pos[0], pos[1], pos[2])
        base.localAvatar.setHpr(hpr[0], hpr[1], hpr[2])

        # update the map icons as well

        posDiv = self.MAP_DIV

        self.mapAvatars[self.localAvId].setPos(pos[0]/posDiv,pos[1]/posDiv,pos[2]/posDiv + self.MAP_OFF)

        for avId in self.remoteAvIdList:
            toon = self.getAvatar(avId)
            if toon:
                pos = toon.getPos()
                self.mapAvatars[avId].setPos(pos/posDiv)
                self.mapAvatars[avId].setZ(self.mapAvatars[avId].getZ() + self.MAP_OFF)

        self.cTrav.traverse(render)
        self.cTrav2.traverse(render)

        # periodically send a position update
        self.__posBroadcast(dt)

        # camera stays near Z of the toon
        z = self.getAvatar(self.localAvId).getZ()+3
        if z < -25:
            z = -25
        #camera.setP(-7)
        camera.setZ(z)

        ambVolume = ((abs(z - 25.0)) / 50.0) + 0.1
        if ambVolume < 0.0:
            ambVolume = 0.0
        if ambVolume > 1.0:
            ambVolume = 1.0

        ambVolume = pow(ambVolume, 0.75)



        self.sndAmbience.setVolume(ambVolume)

        return Task.cont

    def exitSwim(self):
        # Stop music
        self.music.stop()

        self.ignore("resetClock")

        self.__killUpdateLocalToonTask()
        self.__killCrabTask()
        self.__killTreasureBoundsTask()

        self.timer.stop()
        self.timer.destroy()
        self.localLerp.finish()
        self.introMovie.finish()
        self.boatTilt.finish()

        # destroy UI stuff, including minimap
        self.treasurePanel.cleanup()
        self.mapAvatars[self.localAvId].destroy()
        del self.mapAvatars

        for i in range(self.NUMTREASURES):
            del self.chestIcons[i]

        del self.timer

    def enterCleanup(self):
        pass

    def exitCleanup(self):
        pass
