"""DistributedTargetGame module: contains the DistributedTargetGame class"""

from toontown.toonbase.ToontownModules import *
from toontown.toonbase.ToonBaseGlobal import *
from direct.interval.IntervalGlobal import *
from .DistributedMinigame import *
from direct.distributed.ClockDelta import *
from direct.fsm import ClassicFSM, State
from direct.fsm import State
from direct.task import Task
from . import ArrowKeys
from . import TargetGameGlobals
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer
import math
from math import *
import random
import random
from . import RubberBand
from . import FogOverlay

def circleX(angle, radius, centerX, centerY):
    x = radius * cos(angle) + centerX
    return x

def circleY(angle, radius, centerX, centerY):
    y = radius * sin(angle) + centerY
    return y

def getCirclePoints(segCount, centerX, centerY, radius, wideX= 1.0, wideY = 1.0):
    returnShape = []
    for seg in range(0, int(segCount)):
        coordX = wideX * (circleX(((pi * 2.0) * float(float(seg) / float(segCount))), radius, centerX, centerY))
        coordY = wideY * (circleY(((pi * 2.0) * float(float(seg) / float(segCount))), radius, centerX, centerY))
        returnShape.append((coordX, coordY, 1))

    coordX =  wideX * (circleX(((pi * 2.0) * float(0 / segCount)), radius, centerX, centerY))
    coordY =  wideY * (circleY(((pi * 2.0) * float(0 / segCount)), radius, centerX, centerY))
    returnShape.append((coordX, coordY, 1))
    return returnShape

def getRingPoints(segCount, centerX, centerY, radius, thickness = 2.0 ,wideX= 1.0, wideY = 1.0):
    returnShape = []
    for seg in range(0, int(segCount)):
        coordX = wideX * (circleX(((pi * 2.0) * float(float(seg) / float(segCount))), radius - thickness, centerX, centerY))
        coordY = wideY * (circleY(((pi * 2.0) * float(float(seg) / float(segCount))), radius - thickness, centerX, centerY))
        returnShape.append((coordX, coordY, 1))

        coordX = wideX * (circleX(((pi * 2.0) * float(float(seg) / float(segCount))), radius, centerX, centerY))
        coordY = wideY * (circleY(((pi * 2.0) * float(float(seg) / float(segCount))), radius, centerX, centerY))
        returnShape.append((coordX, coordY, 1))

    return returnShape


def addRing(attachNode, color, vertexCount, radius, layer = 0, thickness = 1.0 ):
    targetGN=GeomNode("target Circle")
    zFloat = 0.025
    targetCircleShape = getRingPoints(5 + (vertexCount), 0.0, 0.0, radius, thickness)
    gFormat = GeomVertexFormat.getV3cp()
    targetCircleVertexData = GeomVertexData("holds my vertices", gFormat, Geom.UHDynamic)
    targetCircleVertexWriter = GeomVertexWriter(targetCircleVertexData, "vertex")
    targetCircleColorWriter = GeomVertexWriter(targetCircleVertexData, "color")

    for vertex in targetCircleShape:
        targetCircleVertexWriter.addData3f(0.0 + vertex[0] , 0.0 + vertex[1] , zFloat)
        targetCircleColorWriter.addData4f(1.0, 1.0, 1.0, 1.0)

    targetTris=GeomTristrips(Geom.UHStatic) # triangle obejcet

    sizeTarget = len(targetCircleShape)
    for countVertex in range(0, sizeTarget):
        targetTris.addVertex(countVertex)
    targetTris.addVertex(0)
    targetTris.addVertex(1)
    targetTris.closePrimitive()

    targetGeom=Geom(targetCircleVertexData)
    targetGeom.addPrimitive(targetTris)
    attachNode.addGeom(targetGeom)
    return targetGeom

def addCircle(attachNode, color, vertexCount, radius, layer = 0):
    targetGN=GeomNode("target Circle")
    zFloat = 0.025
    targetCircleShape = getCirclePoints(5 + (vertexCount), 0.0, 0.0, radius)
    gFormat = GeomVertexFormat.getV3cp()
    targetCircleVertexData = GeomVertexData("holds my vertices", gFormat, Geom.UHDynamic)
    targetCircleVertexWriter = GeomVertexWriter(targetCircleVertexData, "vertex")
    targetCircleColorWriter = GeomVertexWriter(targetCircleVertexData, "color")
    targetCircleVertexWriter.addData3f(0.0, 0.0, zFloat) #center
    targetCircleColorWriter.addData4f(1.0, 1.0, 1.0, 1.0)

    for vertex in targetCircleShape:
        targetCircleVertexWriter.addData3f(0.0 + vertex[0] , 0.0 + vertex[1] , zFloat)
        targetCircleColorWriter.addData4f(1.0, 1.0, 1.0, 1.0)

    targetTris=GeomTrifans(Geom.UHStatic) # triangle obejcet

    sizeTarget = len(targetCircleShape)
    targetTris.addVertex(0)
    for countVertex in range(1, sizeTarget + 1):
        targetTris.addVertex(countVertex)
    targetTris.addVertex(1)
    targetTris.closePrimitive()

    targetGeom=Geom(targetCircleVertexData)
    targetGeom.addPrimitive(targetTris)
    attachNode.addGeom(targetGeom)
    return targetGeom

def checkPlace(placeX, placeY, fillSize, placeList):
    goodPlacement = 1
    for place in placeList:
        distance = math.sqrt(((place[0] - placeX) * (place[0] - placeX)) + ((place[1] - placeY) * (place[1] - placeY)))
        distance = distance - (fillSize + place[2])
        if distance <= 0.0:
            goodPlacement = 0
            break
    return goodPlacement




class DistributedTargetGame(DistributedMinigame):

    UPDATE_ENVIRON_TASK   = "TargetGameUpdateEnvironTask"
    UPDATE_LOCALTOON_TASK = "TargetGameUpdateLocalToonTask"
    UPDATE_SHADOWS_TASK   = "TargetGameUpdateShadowsTask"
    COLLISION_DETECTION_TASK = "TargetGameCollisionDetectionTask"
    END_GAME_WAIT_TASK    = "TargetGameCollisionDetectionTask"
    UPDATE_POWERBAR_TASK = "TargetGameUpdatePowerBarTask"
    GAME_DONE_TASK = "gameDoneTask"
    UPDATE_COUNTDOWN_TASK = "countdown task"

    FLY2FALL_CAM_TASK = "fly2FallCameraTask"
    PRELAUNCH_CAM_TASK = "prelaunchCameraTask"
    SCORE_CAM_TASK = "scoreCameraTask"
    TOONSTRETCHTASK = "tooncamtask"

    UPDATE_LOCAL_TOON_PRIORITY = 0
    UPDATE_POWER_BAR_PRIORITY = 1
    UPDATE_RUBBER_BAND_PRIORITY = 2
    COLLISION_DETECTION_PRIORITY = 5
    # update the shadow positions after collisions have been performed
    # but before render
    UPDATE_SHADOWS_PRIORITY = 47

    UMBRELLA_TEXTURE_LIST = ['phase_4/maps/mg_slingshot_umbrella_blue.txo',
                             'phase_4/maps/mg_slingshot_umbrella_purple.txo',
                             'phase_4/maps/mg_slingshot_umbrella_red.txo',
                             'phase_4/maps/mg_slingshot_umbrella_yellow.txo',]

    # result types
    RT_UNKNOWN      = 0
    RT_SUCCESS      = 1
    RT_GROUPSUCCESS = 2
    RT_FAILURE      = 3

    def __init__(self, cr):
        DistributedMinigame.__init__(self, cr)

        self.gameFSM = ClassicFSM.ClassicFSM('DistributedTargetGame',
                               [
                                State.State('off',
                                            self.enterOff,
                                            self.exitOff,
                                            ['prelaunch']),
                                State.State('prelaunch',
                                            self.enterPrelaunch,
                                            self.exitPrelaunch,
                                            ['launch']),
                                State.State('launch',
                                            self.enterLaunch,
                                            self.exitLaunch,
                                            ['fly']),
                                State.State('fly',
                                            self.enterFly,
                                            self.exitFly,
                                            ['fall', 'bouncing', 'score']),
                                State.State('fall',
                                            self.enterFall,
                                            self.exitFall,
                                            ['bouncing', 'score']),
                                State.State('bouncing',
                                            self.enterBouncing,
                                            self.exitBouncing,
                                            ['score']),
                                State.State('score',
                                            self.enterScore,
                                            self.exitScore,
                                            ['cleanup', 'prelaunch']),
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
        self.targets = None
        self.round = 1
        self.signalLaunch = 0
        self.stretchX = 0
        self.stretchY = 0
        self.targetsPlaced = []



        self.pattern = None
        self.maxDist = 50

        self.targetMarker = None

        self.umbrellaColorSelect = [1,1,1,1]

        self.localTrack = None
        self.hitInfo = None
        #base.targetGame = self


    def getTitle(self):
        return TTLocalizer.TargetGameTitle

    def getInstructions(self):
        p = self.avIdList.index(self.localAvId)

        if self.isSinglePlayer():
            text = TTLocalizer.TargetGameInstructionsSinglePlayer
        else:
            text = TTLocalizer.TargetGameInstructionsMultiPlayer

        return text

    def getMaxDuration(self):
        # calling this here could be problematic; it's easy for now
        #self.defineConstants()
        return (60)

    def defineConstants(self):
        # Z is up, Y is forward
        # define some tweakable constants
        #self.CAMERA_Y = -35
        #self.CAMERA_Z = -2
        self.CAMERA_Y = -25
        self.TOON_Y = 0
        self.FAR_PLANE_DIST = 370
        tScreenCenterToEdge = 1.
        self.TOONXZ_SPEED = TargetGameGlobals.MAX_TOONXZ/tScreenCenterToEdge
        self.WATER_DEPTH = 75.
        self.ENVIRON_LENGTH = TargetGameGlobals.ENVIRON_LENGTH
        self.ENVIRON_WIDTH = TargetGameGlobals.ENVIRON_WIDTH
        self.ENVIRON_START_OFFSET = 20. # start _ feet into the environment
        self.TOON_INITIAL_SPACING = 14.
        waterZOffset = 28.
        self.SEA_FLOOR_Z = (-self.WATER_DEPTH/2.) + waterZOffset

        self.FOGDISTGROUND = 600
        self.FOGDISTCLOUD = 200

        # in world coordinates
        farPlaneDist = (self.CAMERA_Y + self.FAR_PLANE_DIST) - self.TOON_Y

        # how many seconds between each ring group arrival?
        self.ringGroupArrivalPeriod = 3.
        # how much space is there between successive ring groups?

        #self.TOON_SWIM_VEL = (self.RING_GROUP_SPACING /
        #                      self.ringGroupArrivalPeriod)


        self.AMB_COLOR = Vec4(0.75,0.8,1.00,1.0)
        self.CLOUD_COLOR = Vec4(1.0, 1.0, 1.0, 1.0)

        self.SHADOW_Z_OFFSET = 0.1
        #self.SHADOW_MAX_SCALE = 0.6
        #self.SHADOW_MIN_SCALE = 0.35

        self.Y_VIS_MAX = self.FAR_PLANE_DIST
        self.Y_VIS_MIN = self.CAMERA_Y

        targetRadius = TargetGameGlobals.TARGET_RADIUS * 1.025

        self.GAME_END_DELAY = 1.


        self.TOON_LOD = 1000


        self.speedLaunch = 60
        self.speedStall = 30
        self.speedForward = 0
        self.airResistance = .1
        self.umbrellaResistance = .11
        self.distance = 0
        self.zVel = 0
        self.lastPressed = None
        self.lastPressTime = None
        self.driftX = 0
        self.driftY = 0
        self.launchLaterial = 0
        self.laterial = 0
        self.gravity = 12.5

        self.inList = []



        self.placeShift = 10

        self.startPower = 10
        self.canPressRight = 1
        self.canPressLeft = 1
        self.jumpCount = 0

        self.trampZ = 3.6
        self.trampBounceCount = 0
        self.cameraState = "Low"
        self.updateTick = 0

        self.hitInfo = None





    def load(self):
        self.notify.debug("load")
        DistributedMinigame.load(self)

        self.defineConstants()

        self.help = DirectLabel(
             parent = aspect2d,
             relief = None,
             pos = (-0.0, 0, -0.80),
             text = TTLocalizer.TargetGameCountdown,
             text_scale = 0.08,
             text_fg = (1, 1, 1, 1),
             )

        self.help.hide()

        self.fogOver = FogOverlay.FogOverlay(Point3(self.CLOUD_COLOR[0], self.CLOUD_COLOR[1], self.CLOUD_COLOR[2]))


        self.scoreboard = DirectFrame(
                             parent = aspect2d,
                             relief=None,
                             geom = DGG.getDefaultDialogGeom(),
                             geom_color = ToontownGlobals.GlobalDialogColor,
                             geom_scale = (1.75, 1, 0.75),
                             pos = (0, 0, 0.587),
                             )

        self.roundLabel = DirectLabel(
            parent = self.scoreboard,
            relief = None,
            pos = (0, 0, 0.28),
            text = (TTLocalizer.TargetGameBoard % (self.round)),
            text_scale = 0.08,
            )

        av1Label = DirectLabel(
            parent = self.scoreboard,
            relief = None,
            pos = (-0.8, 0, 0.14),
            text_align = TextNode.ALeft,
            text = " ",
            text_scale = 0.08,
            )

        av2Label = DirectLabel(
            parent = self.scoreboard,
            relief = None,
            pos = (-0.8, 0, 0.02),
            text_align = TextNode.ALeft,
            text = " ",
            text_scale = 0.08,
            )

        av3Label = DirectLabel(
            parent = self.scoreboard,
            relief = None,
            pos = (-0.8, 0, -0.10),
            text_align = TextNode.ALeft,
            text = " ",
            text_scale = 0.08,
            )

        av4Label = DirectLabel(
            parent = self.scoreboard,
            relief = None,
            pos = (-0.8, 0, -0.22),
            text_align = TextNode.ALeft,
            text = " ",
            text_scale = 0.08,
            )

        score1Label = DirectLabel(
            parent = self.scoreboard,
            relief = None,
            pos = (0.8, 0, 0.14),
            text_align = TextNode.ARight,
            text = " ",
            text_scale = 0.08,
            )

        score2Label = DirectLabel(
            parent = self.scoreboard,
            relief = None,
            pos = (0.8, 0, 0.02),
            text_align = TextNode.ARight,
            text = " ",
            text_scale = 0.08,
            )

        score3Label = DirectLabel(
            parent = self.scoreboard,
            relief = None,
            pos = (0.8, 0, -0.10),
            text_align = TextNode.ARight,
            text = " ",
            text_scale = 0.08,
            )

        score4Label = DirectLabel(
            parent = self.scoreboard,
            relief = None,
            pos = (0.8, 0, -0.22),
            text_align = TextNode.ARight,
            text = " ",
            text_scale = 0.08,
            )

        self.avLabels = [av1Label, av2Label, av3Label, av4Label]
        self.scoreLabels = [score1Label, score2Label, score3Label, score4Label]


        self.scoreboard.hide()
        self.music = base.loadMusic("phase_4/audio/bgm/MG_Diving.mid")
        #self.music = None

        self.sndAmbience = None


        self.skyListLow = []
        self.skyListMid = []

        # load the environment model (water, ground)
        loadBase = "phase_4/models/minigames/"
        self.modelName = "slingshot_game_desert4.bam"

        self.trampoline = loader.loadModel("phase_4/models/minigames/slingshot_game_tramp.bam")
        self.trampoline.setBin('ground', 100)
        self.trampoline.find("**/tramp_shadow").hide()
        #import pdb; pdb.set_trace()
        self.cacti = loader.loadModel("phase_4/models/minigames/slingshot_game_cacti.bam")
        self.cactusA = self.cacti.find('**/cactus_a')
        self.cactusB = self.cacti.find('**/cactus_b')

        self.findGround = '**/sand_layer1'
        self.findSky = '**/blue_sky_layer1'
        self.findCloudExtra = '**/cloud_layer1'
        self.findCloud = '**/cloud_layer_alpha'
        self.findLeftMount = '**/mountain_set_b'
        self.findRightMount = '**/mountain_c'
        self.findBack = '**/backdrop_layer1'

        self.environModel = loader.loadModel(loadBase + self.modelName)
        self.skyGN = GeomNode("sky Geometry")
        self.skyNode1 = self.environModel.attachNewNode(self.skyGN)

        leftMountModel = self.environModel.find(self.findLeftMount)
        rightMountModel = self.environModel.find(self.findRightMount)

        wrongCloud = self.environModel.find(self.findCloudExtra)
        wrongCloud.hide()

        backModel = self.environModel.find(self.findBack)
        backModel.hide()

        leftMountModel.hide()
        rightMountModel.hide()

        groundModel = self.environModel.find(self.findGround)
        groundModel.setBin('ground', 0)
        groundModel.setZ(-0.05)


        skyModel = self.environModel.find(self.findSky)


        skyModel2 = self.environModel.find(self.findCloud)

        skyModel3 = self.environModel.attachNewNode("skyLow")
        skyModel2.copyTo(skyModel3)


        skyModel.setZ(76.0)
        skyModel.setColorScale(1.0, 1.0, 1.0, 1.0)
        skyModel.setBin('ground', 2)


        skyModel2.setZ(63.0)
        skyModel2.setDepthWrite(0)
        skyModel2.setTransparency(1)
        skyModel2.setColorScale(1.0, 1.0, 1.0, 1.0)
        skyModel2.setTwoSided(True)
        skyModel2.setBin('fixed', 3)
        skyModel2.setR(180)

        skyModel3.setZ(50.0)
        skyModel3.setDepthWrite(0)
        skyModel3.setTransparency(1)
        skyModel3.setColorScale(1.0, 1.0, 1.0, 1.00)
        skyModel3.setTwoSided(True)
        skyModel3.setBin('fixed', 4)
        self.skyListLow.append(skyModel3)
        self.lowSky =  skyModel3


        self.environModel.setPos(0,-5.0,0)
        self.environModel.flattenMedium()
        self.environModel.setScale(15.0,15.0,2.0)


        # load the drop shadow
        self.dropShadowModel = loader.loadModel(
            "phase_3/models/props/drop_shadow")
        self.dropShadowModel.setColor(0,0,0,0.5)
        self.dropShadowModel.flattenMedium()

        self.toonDropShadows = []

        # this will be used to generate textnodes
        self.__textGen = TextNode("targetGame")
        self.__textGen.setFont(ToontownGlobals.getSignFont())
        self.__textGen.setAlign(TextNode.ACenter)

        self.powerBar = DirectWaitBar(
            guiId = 'launch power bar',
            pos = (0.0, 0, -0.65),
            relief = DGG.SUNKEN,
            frameSize = (-2.0,2.0,-0.2,0.2),
            borderWidth = (0.02,0.02),
            scale = 0.25,
            range = 100,
            sortOrder = 50,
            frameColor = (0.5,0.5,0.5,0.5),
            barColor = (1.0,0.0,0.0,1.0),
            text = "0%",
            text_scale = 0.26,
            text_fg = (1, 1, 1, 1),
            text_align = TextNode.ACenter,
            text_pos = (0,-0.05),
            )

        self.power = self.startPower
        self.powerBar['value'] = self.power
        self.powerBar.hide()

        self.rubberBands = []


        self.umbrella = loader.loadModel("phase_4/models/minigames/slingshot_game_umbrellas.bam")

        pick = random.randint(0, 3)
        self.umbrellaColorSelect[pick] = 0
        tex = loader.loadTexture(DistributedTargetGame.UMBRELLA_TEXTURE_LIST[pick])
        tex.setMinfilter(Texture.FTLinearMipmapLinear)
        tex.setMagfilter(Texture.FTLinear)
        self.umbrella.setTexture(tex, 1)

        open = self.umbrella.find('**/open_umbrella')
        open.hide()
        open.setPos(0.1, 0.2, -0.1)
        open.setHpr(-90.0, 0.0, 15.0)
        closed = self.umbrella.find('**/closed_umbrella')
        closed.show()
        hands = localAvatar.getRightHands()

        ce = CompassEffect.make(NodePath(), CompassEffect.PRot)
        closed.node().setEffect(ce)
        closed.setHpr(0.0,100.0,35.0)

        for hand in hands:
            self.umbrella.instanceTo(hand)

        self.remoteUmbrellas = {}

        self.addSound('wind1', "target_cloud.mp3", "phase_4/audio/sfx/")
        self.addSound('trampoline', "target_trampoline_2.mp3", "phase_4/audio/sfx/")
        self.addSound('launch', "target_launch.mp3", "phase_4/audio/sfx/")
        self.addSound('miss', "target_Lose.mp3", "phase_4/audio/sfx/")
        self.addSound('score', "target_happydance.mp3", "phase_4/audio/sfx/")
        self.addSound('impact', "target_impact_grunt1.mp3", "phase_4/audio/sfx/")
        self.addSound('umbrella', "target_chute.mp3", "phase_4/audio/sfx/")
        self.addSound('bounce', "target_impact_only.mp3", "phase_4/audio/sfx/")

        self.flySound = loader.loadSfx("phase_4/audio/sfx/target_wind_fly_loop.wav")
        self.flySound.setVolume(0.0)
        self.flySound.setPlayRate(1.0)
        self.flySound.setLoop(True)
        self.flySound.play()

        self.rubberSound = loader.loadSfx("phase_4/audio/sfx/target_stretching_aim_loop.mp3")
        self.rubberSound.setVolume(0.0)
        self.rubberSound.setPlayRate(1.0)
        self.rubberSound.setLoop(True)
        self.rubberSound.play()

        self.flutterSound = loader.loadSfx("phase_4/audio/sfx/target_wind_float_clothloop.wav")
        self.flutterSound.setVolume(1.0)
        self.flutterSound.setPlayRate(1.0)
        self.flutterSound.setLoop(True)


    def addSound(self, name, soundName, path = None):
        if not hasattr(self, "soundTable"):
            self.soundTable = {}
        if path:
            self.soundPath = path
        soundSource = ("%s%s" % (self.soundPath, soundName))
        self.soundTable[name] = loader.loadSfx(soundSource)

    def playSound(self, name, volume = 1.0):
        if hasattr(self, 'soundTable'):
            self.soundTable[name].setVolume(volume)
            self.soundTable[name].play()

    def addSkys(self, instance):
        low = instance.find('**/skyLow')
        mid = instance.find(self.findCloud)
        self.skyListLow.append(low)
        self.skyListMid.append(mid)

    def setTargetSeed(self, targetSeed, extra = None):
        if not self.hasLocalToon: return
        random.seed(targetSeed)
        self.pattern = TargetGameGlobals.difficultyPatterns[self.getSafezoneId()]
        print(("seed %s" % (targetSeed)))
        self.setupTargets()

    def setupTargets(self):
        fieldWidth = self.ENVIRON_WIDTH * 3
        fieldLength = self.ENVIRON_LENGTH * 3.70

        self.targetSubParts = [2,2,2,1]

        self.targetList = self.pattern[0]
        self.targetValue = self.pattern[1]
        self.targetSize = self.pattern[2]
        self.targetColors = self.pattern[3]
        self.targetSubParts = self.pattern[4]

        highestValue = 0

        for value in self.targetValue:
            if value > highestValue:
                highestValue = value

        placeList = []


        self.jumpColor = TargetGameGlobals.colorBlack
        self.placeValue = highestValue * 0.5

        self.jumpSize = self.pattern[5]
        self.jumpNum = self.pattern[6]

        self.accept("enterJump", self.jumpIn)
        self.accept("exitJump", self.jumpOut)

        self.targets = render.attachNewNode("targetGameTargets")

        for typeIndex in range(len(self.targetList)):
           for targetIndex in range(self.targetList[typeIndex]):
                goodPlacement = 0
                while not goodPlacement:
                    placeX = random.random()*(fieldWidth * 0.60) - ((fieldWidth * 0.60)  * 0.5)
                    placeY = ((random.random() * 0.60) + (0.00 + (0.40 * ((self.placeValue * 1.0) / (highestValue * 1.0))))) * fieldLength
                    fillSize = self.targetSize[typeIndex]
                    goodPlacement = checkPlace(placeX, placeY, fillSize, placeList)
                placeList.append((placeX, placeY, fillSize))

                subIndex = self.targetSubParts[typeIndex]
                first = 1
                while subIndex:
                    combinedIndex = typeIndex + subIndex - 1

                    targetGN=GeomNode("target Circle")
                    targetNodePathGeom = self.targets.attachNewNode(targetGN)

                    targetNodePathGeom.setPos(placeX,placeY,0)
                    points = (self.targetSize[combinedIndex] / 2) + 20
                    order = len(self.targetList) -combinedIndex + 10
                    if first:
                        first = 0
                        geo = addCircle(targetGN, self.targetColors[combinedIndex], points, self.targetSize[combinedIndex], order)
                    else:
                        thickness = abs(self.targetSize[combinedIndex] - self.targetSize[combinedIndex + 1]) - 0.0
                        geo = addRing(targetGN, self.targetColors[combinedIndex], points, self.targetSize[combinedIndex], order, thickness)

                    targetNodePathGeom.setBin('ground', (combinedIndex * 2) + 1)
                    targetNodePathGeom.setColorScale(self.targetColors[combinedIndex]['Red'], self.targetColors[combinedIndex]['Green'], self.targetColors[combinedIndex]['Blue'], self.targetColors[combinedIndex]['Alpha'])
                    targetNodePathGeom.setDepthWrite(False)
                    targetNodePathGeom.setDepthTest(False)
                    targetNodePathGeom.setTransparency(TransparencyAttrib.MAlpha)
                    self.targetsPlaced.append((placeX, placeY, combinedIndex, geo))

                    subIndex -= 1

        for jump in range(self.jumpNum):
                normJumpSize = 6.8

                goodPlacement = 0
                while not goodPlacement:
                    placeX = random.random()*(fieldWidth * 0.60) - ((fieldWidth * 0.60)  * 0.5)
                    placeY = ((random.random() * 0.60) + (0.00 + (0.40 * ((self.placeValue * 1.0) / (highestValue * 1.0))))) * fieldLength
                    fillSize = self.jumpSize
                    goodPlacement = checkPlace(placeX, placeY, fillSize, placeList)
                placeList.append((placeX, placeY, fillSize))

                target = CollisionSphere(0,0,0,self.jumpSize)
                target.setTangible(0)
                targetNode = CollisionNode("Jump")
                targetNode.addSolid(target)
                targetGN=GeomNode("target jump Circle")
                targetNodePathGeom = self.targets.attachNewNode(targetGN)

                trampI = self.trampoline.copyTo(self.targets)
                trampI.setPos(placeX,placeY,0.05)
                latScale = self.jumpSize / normJumpSize
                trampI.setScale(latScale,latScale,1.0)

                targetNodePath = self.targets.attachNewNode(targetNode)
                targetNodePath.setPos(placeX,placeY,0.0)
                targetNodePathGeom.setPos(placeX,placeY,0.05)
                points = (self.jumpSize / 2) + 20
                order = 0
                addCircle(targetGN, self.jumpColor, points, self.jumpSize + 0.5, order)
                targetNodePathGeom.setColorScale(self.jumpColor['Red'], self.jumpColor['Green'], self.jumpColor['Blue'], 0.25)
                targetNodePathGeom.setBin('ground', 20)
                targetNodePathGeom.setDepthWrite(True)
                targetNodePathGeom.setTransparency(TransparencyAttrib.MAlpha)

        cactusCount = 30

        for cactus in range(cactusCount):
                placeX = random.random() * (fieldWidth * 0.75) - ((fieldWidth * 0.75)  * 0.5)
                placeY = 5.0 + (random.random() * (fieldLength - 5.0))

                targetGN=GeomNode("cactus")
                cactus = random.choice([self.cactusA, self.cactusB])
                targetNodePathGeom = self.targets.attachNewNode(targetGN)
                targetNodePathGeom = self.targets.attachNewNode(targetGN)

                cactusI = cactus.copyTo(self.targets)
                cactusI.setPos(placeX,placeY,0)
                cactusI.setHpr(random.random() * 360 ,0,0)
                cactusI.setScale(0.5 + random.random())




    def unload(self):
        #print("unloading")
        self.notify.debug("unload")
        DistributedMinigame.unload(self)
        del self.__textGen
        del self.toonDropShadows
        self.dropShadowModel.removeNode()
        del self.dropShadowModel
        self.environModel.removeNode()
        del self.environModel
        self.fogOver.delete()
        self.umbrella.removeNode()
        del self.umbrella
        for umbrella in self.remoteUmbrellas:
            self.remoteUmbrellas[umbrella].removeNode()
        self.remoteUmbrellas.clear()
        del self.remoteUmbrellas

        self.flySound.stop()
        del self.flySound
        self.rubberSound.stop()
        del self.rubberSound
        self.flutterSound.stop()
        del self.flutterSound
        del self.music
        del self.sndAmbience
        # remove our game ClassicFSM from the framework ClassicFSM
        self.removeChildGameFSM(self.gameFSM)
        del self.gameFSM
        if self.targets:
            self.targets.remove()
        del self.targets
        self.scoreboard.destroy()
        del self.scoreboard
        self.powerBar.destroy()
        del self.powerBar
        self.help.destroy()
        del self.help

        if self.localTrack:
            self.localTrack.finish()
            del self.localTrack


    def onstage(self):
        self.notify.debug("onstage")
        DistributedMinigame.onstage(self)

        # arrow key manager
        self.arrowKeys = ArrowKeys.ArrowKeys()

        toon = base.localAvatar
        toon.reparentTo(render)
        toon.setAnimState('SitStart', 1.0)
        toon.useLOD(self.TOON_LOD)
        self.__placeToon(self.localAvId)
        self.localStartPos = toon.getPos()
        localBand = RubberBand.RubberBand(toon, Point3(0,-1.75,0),
                                          taskPriority=self.UPDATE_RUBBER_BAND_PRIORITY)
        tP = self.getToonPlace(self.localAvId)
        pos = Point3(tP[0], tP[1] + 10, tP[2])
        localBand.setPos(pos)
        self.rubberBands.append(localBand)
        # hide the avatar's dropshadow
        toon.dropShadow.hide()

        toonPos = base.localAvatar.getPos()



        camera.reparentTo(render)
        toonPos = self.getAvatar(self.localAvId).getPos()
        camera.setPosHpr(toonPos[0],toonPos[1] - 18,toonPos[2] + 10,0,-15,0)
        base.camLens.setMinFov(80 * ToontownGlobals.OriginalAspectRatio)


        # set the far plane
        base.camLens.setFar(self.FOGDISTGROUND)

        # set the background color
        base.setBackgroundColor(self.AMB_COLOR)

        # set up the fog
        self.__fog = Fog("ringGameFog")
        if base.wantFog:
            self.__fog.setColor(self.AMB_COLOR)
            self.__fog.setLinearRange(0.1, self.FOGDISTGROUND)
            render.setFog(self.__fog)

        # create a node to put all of the environment under
        self.environNode = render.attachNewNode("environNode")
        self.environBlocks = []
        maxI = 4
        self.maxDist = (maxI - 1) * self.ENVIRON_LENGTH
        for i in range(-1,maxI+1):
            instance = self.environModel.copyTo(self.environNode)
            y = self.ENVIRON_LENGTH*i
            instance.setY(y)
            self.addSkys(instance)
            self.environBlocks.append(instance)
            # add blocks on the left
            jRange = 3
            for j in range(0,jRange):
                instance = self.environModel.copyTo(self.environNode)
                x = self.ENVIRON_WIDTH*(j+1)
                instance.setY(y)
                instance.setX(-x)
                height = (random.random() * 5.0) + 5.0
                heading = (random.random() * 15.0) - 7.5
                self.addSkys(instance)
                self.environBlocks.append(instance)
                if j == (jRange - 2):
                    mount = instance.find(self.findLeftMount)
                    mount.setScale(1.0,1.1,height)
                    #mount.setHpr(heading, 0, 0)
                    mount.setBin('ground', 1)
                    mount.show()
                    sand = mount.find("**/sand_b")
                    sand.hide()
                    mount.setPos(mount.getX() + 8.5, 0, 0.0)
                    if i >= (maxI - 1):
                        mount.setHpr(310, 0, 0)
                        mount.setScale(1.0,1.5,height * 1.2)
                        mount.setPos(mount.getX() - 2.0, 0, 0.0)
                        if i == maxI:
                            mount.hide()
                    if i ==  -1:
                        mount.setHpr(50, 0, 0)
                        mount.setScale(1.0,1.5,height * 1.2)
                        mount.setPos(mount.getX() + 5.0, 3.0, 0.0)
                if j ==  (jRange - 1):
                    sand = instance.find(self.findGround)
                    sand.hide()


            # add blocks on the right
            for j in range(0,jRange):
                instance = self.environModel.copyTo(self.environNode)
                x = self.ENVIRON_WIDTH*(j+1)
                instance.setY(y)
                instance.setX(x)
                height = (random.random() * 5.0) + 5.0
                heading = (random.random() * 15.0) - 7.5
                self.addSkys(instance)
                self.environBlocks.append(instance)
                if j ==  (jRange - 2):
                    mount = instance.find(self.findRightMount)
                    mount.setScale(1.0,1.1,height)
                    #mount.setHpr(heading, 0, 0)
                    mount.setBin('ground', 1)
                    mount.show()
                    sand = mount.find("**/sand_c")
                    sand.hide()
                    mount.setPos(mount.getX() - 8.5, 0, 0.0)
                    if i >= (maxI - 1):
                        mount.setHpr(50, 0, 0)
                        mount.setScale(1.0,1.5,height * 1.2)
                        mount.setPos(mount.getX() + 2.0, 0, 0.0)
                        if i == maxI:
                            mount.hide()
                    if i ==  -1:
                        mount.setHpr(310, 0, 0)
                        mount.setScale(1.0,1.5,height * 1.2)
                        mount.setPos(mount.getX() - 5.0, 3.0, 0.0)
                if j ==  (jRange - 1):
                    sand = instance.find(self.findGround)
                    sand.hide()

        # create a node to put all of the targets under
        # this should not be put under the environ node;
        # the environ node periodically 'jumps' back
        #self.targetNode = render.attachNewNode("targetNode")




        # create a drop shadow for the local toon
        self.__addToonDropShadow(self.getAvatar(self.localAvId))

        self.__spawnUpdateEnvironTask()
        self.__spawnUpdateShadowsTask()
        self.__spawnUpdateLocalToonTask()

        # Start music
        if self.music:
            base.playMusic(self.music, looping = 1, volume = 0.8)
        if None != self.sndAmbience:
            base.playSfx(self.sndAmbience, looping = 1, volume = 0.8)




    def reset(self):
        toon = base.localAvatar
        toon.setAnimState('SitStart', 1.0)
        #toon.stopBobSwimTask()
        toon.useLOD(self.TOON_LOD)
        self.__placeToon(self.localAvId)
        # hide the avatar's dropshadow
        toon.dropShadow.hide()
        self.__spawnUpdateLocalToonTask()
        toonPos = base.localAvatar.getPos()
        camera.setPosHpr(toonPos[0],toonPos[1] - 26,toonPos[2] + 10,0,-15,0)
        #camera.setPosHpr(0, self.CAMERA_Y + self.TOON_Y + 12, 5,
        #                 0, -15, 0)
        base.camLens.setMinFov(80 * ToontownGlobals.OriginalAspectRatio)
        self.resetNums()

    def resetNums(self):
        self.stretchX = 0
        self.stretchY = 0
        self.driftX = 0
        self.driftY = 0
        self.driftY = 0
        self.jumpCount = 0
        self.trampBounceCount = 0
        self.cameraState = "Low"


    def offstage(self):
        self.notify.debug("offstage")
        DistributedMinigame.offstage(self)

        # Stop music
        if self.music:
            self.music.stop()
        if None != self.sndAmbience:
            self.sndAmbience.stop()

        self.__killUpdateLocalToonTask()
        self.__killUpdateShadowsTask()
        self.__killUpdateEnvironTask()
        self.__killCountDownTask()

        del self.soundTable

        # remove all toons' shadows
        self.__removeAllToonDropShadows()

        assert(len(self.toonDropShadows) == 0)

        render.clearFog()
        base.camLens.setFar(ToontownGlobals.DefaultCameraFar)
        base.camLens.setMinFov(ToontownGlobals.DefaultCameraFov)
        camera.setHpr(0,90,0)

        # Restore the background color
        base.setBackgroundColor(ToontownGlobals.DefaultBackgroundColor)

        self.arrowKeys.destroy()
        del self.arrowKeys

        for block in self.environBlocks:
            del block
        self.environNode.removeNode()
        del self.environNode

        #self.targetNode.removeNode()
        #del self.targetNode

        # reset the toons' LODs and show their dropshadows again
        for avId in self.avIdList:
            av = self.getAvatar(avId)
            if av:
                av.showShadow()
                av.resetLOD()
                #av.setAnimState('neutral', 1.0)

        for band in self.rubberBands:
            band.delete()

        rubberBands = []
        self.targetsPlaced = []

    def handleDisabledAvatar(self, avId):
        """This will be called if an avatar exits unexpectedly"""
        self.notify.debug("handleDisabledAvatar")
        self.notify.debug("avatar " + str(avId) + " disabled")
        # remove the disabled toon's shadow, so that the shadow
        # task doesn't crash when it tries to find the toon
        # also, it would look funny to have a shadow and no toon
        self.__removeToonDropShadow(self.remoteToons[avId])
        DistributedMinigame.handleDisabledAvatar(self, avId)

    def __genText(self, text):
        self.__textGen.setText(text)
        return self.__textGen.generate()

    def __placeToon(self, avId):
        """ places a toon in its starting position """
        toon = self.getAvatar(avId)
        i = self.avIdList.index(avId)
        numToons = float(self.numPlayers)
        x = i * self.TOON_INITIAL_SPACING
        x -= (self.TOON_INITIAL_SPACING * (numToons-1)) / 2.
        pos = self.getToonPlace(avId)
        toon.setPosHpr(pos[0], pos[1], pos[2],#TargetGameGlobals.MAX_TOONXZ,
                       0, 0, 0)

    def getToonPlace(self, avId):
        """ places a toon in its starting position """
        toon = self.getAvatar(avId)
        i = self.avIdList.index(avId)
        numToons = float(self.numPlayers)
        x = i * self.TOON_INITIAL_SPACING
        x -= (self.TOON_INITIAL_SPACING * (numToons-1)) / 2.
        pos = Point3(x + self.placeShift, self.TOON_Y, 1.0)
        return pos


    def setGameReady(self):
        if not self.hasLocalToon: return
        self.notify.debug("setGameReady")
        if DistributedMinigame.setGameReady(self):
            return





        if not self.isSinglePlayer():
            # turn off the normal collisions
            base.localAvatar.collisionsOff()

            # put a collision sphere on localToon
            cSphere = CollisionSphere(0.0, 0.0, 0.0,
                                      TargetGameGlobals.CollisionRadius)
            cSphereNode = CollisionNode('RingGameSphere-%s' % self.localAvId)
            cSphereNode.addSolid(cSphere)
            cSphereNode.setFromCollideMask(TargetGameGlobals.CollideMask)
            cSphereNode.setIntoCollideMask(BitMask32.allOff())
            self.cSphereNodePath = base.localAvatar.attachNewNode(cSphereNode)

            self.pusher = CollisionHandlerPusher()
            self.pusher.addCollider(self.cSphereNodePath, base.localAvatar)
            # if we don't clear this, the toons will stick to each other
            # when moving purely along the X-axis
            self.pusher.setHorizontal(0)

            # create our own collision traverser
            self.cTrav = CollisionTraverser("DistributedRingGame")
            self.cTrav.addCollider(self.cSphereNodePath, self.pusher)

            # create collision spheres on the remote toons
            self.remoteToonCollNPs = {}
            for avId in self.remoteAvIdList:
                toon = self.getAvatar(avId)
                if toon:
                    cSphere = CollisionSphere(0.0, 0.0, 0.0,
                                              TargetGameGlobals.CollisionRadius)
                    cSphereNode = CollisionNode('RingGameSphere-%s' % avId)
                    cSphereNode.addSolid(cSphere)
                    cSphereNode.setCollideMask(TargetGameGlobals.CollideMask)
                    cSphereNP = toon.attachNewNode(cSphereNode)
                    self.remoteToonCollNPs[avId] = cSphereNP

        # show the remote toons
        for avId in self.remoteAvIdList:
            toon = self.getAvatar(avId)
            if toon:
                toon.reparentTo(render)
                self.__placeToon(avId)
                toon.setAnimState('SitStart', 1.0)
                toon.useLOD(self.TOON_LOD)
                # hide the avatar's dropshadows
                toon.dropShadow.hide()
                self.__addToonDropShadow(toon)
                band = RubberBand.RubberBand(toon, Point3(0,-1.75,0),
                                             taskPriority=self.UPDATE_RUBBER_BAND_PRIORITY)
                #band.setPos(self.getToonPlace(avId))
                tP = self.getToonPlace(avId)
                pos = Point3(tP[0], tP[1] + 10, tP[2])
                band.setPos(pos)

                self.rubberBands.append(band)
                umbrella = self.umbrella.copyTo(render)
                self.remoteUmbrellas[avId] = umbrella

                test = 0
                kill = 16
                while test == 0 and kill > 0:
                    kill -= 1
                    pick = random.randint(0, 3)
                    if self.umbrellaColorSelect[pick]:
                        self.umbrellaColorSelect[pick] = 0
                        test = 1

                tex = loader.loadTexture(DistributedTargetGame.UMBRELLA_TEXTURE_LIST[pick])
                tex.setMinfilter(Texture.FTLinearMipmapLinear)
                tex.setMagfilter(Texture.FTLinear)
                umbrella.setTexture(tex, 1)

                open = umbrella.find('**/open_umbrella')
                open.hide()
                open.setPos(0.1, 0.2, -0.1)
                open.setHpr(-90.0, 180.0, 0.0)
                open.setScale(1.5)
                closed = umbrella.find('**/closed_umbrella')
                closed.show()
                if ConfigVariableBool('want-new-anims', 1).getValue():
                    if toon.find('**/def_joint_right_hold').isEmpty():
                        hand = toon.find('**/def_joint_right_hold')
                else:
                    hand = toon.find('**/joint*Rhold')
                ce = CompassEffect.make(NodePath(), CompassEffect.PRot)
                closed.node().setEffect(ce)
                closed.setHpr(0.0,90.0,35.0)

                umbrella.reparentTo(hand)
                # Start the smoothing task.
                toon.startSmooth()

        # make a table of the remote toons
        # this allows us to destroy the shadows of disabled toons
        self.remoteToons = {}
        for avId in self.remoteAvIdList:
            toon = self.getAvatar(avId)
            self.remoteToons[avId] = toon

        labelIndex = 0
        for avId in self.avIdList:
            av = self.getAvatar(avId)
            self.avLabels[labelIndex]['text'] = av.getName()
            labelIndex += 1


    def setGameStart(self, timestamp):
        if not self.hasLocalToon: return
        self.notify.debug("setGameStart")
        # base class will cause gameFSM to enter initial state
        DistributedMinigame.setGameStart(self, timestamp)
        self.gameFSM.request("prelaunch")

    def enterOff(self):
        self.notify.debug("enterOff")

    def exitOff(self):
        pass

    def enterPrelaunch(self):
        self.defineConstants()
        self.resetNums()
        self.gameFSM.request("launch")
        self.powerBar.show()
        self.powerBar['value'] = self.startPower
        camera.reparentTo(render)
        self.__placeToon(self.localAvId)
        toonPos = self.getAvatar(self.localAvId).getPos()
        newPos = Point3(toonPos[0],toonPos[1] - 25,toonPos[2] + 7)
        newHpr = Point3(0,-15,0)
        self.cameraWork =  camera.posHprInterval(2.5, newPos, newHpr,
                          blendType = "easeInOut")#,
        self.cameraWork.start()
        base.camLens.setMinFov(80 * ToontownGlobals.OriginalAspectRatio)
        self.stretchY = self.startPower
        self.power = self.startPower
        self.scoreboard.hide()

        open = self.umbrella.find('**/open_umbrella')
        open.hide()
        closed = self.umbrella.find('**/closed_umbrella')
        closed.show()
        self.umbrella.setScale(1.0)

        if self.targetMarker:
            self.targetMarker.removeNode()



    def exitPrelaunch(self):
        pass

    def enterLaunch(self):
        self.__spawnUpdatePowerBarTask()
        self.__spawnCountDownTask()
        self.help.show()
        self.help['text'] = TTLocalizer.TargetGameCountHelp

    def exitLaunch(self):
        self.cameraWork.finish()
        self.__killUpdatePowerBarTask()
        self.speedLaunch = self.power
        self.powerBar.hide()
        self.playSound('launch')
        pass

    def enterFly(self):
        self.notify.debug("enterFly")
        self.__spawnCollisionDetectionTask() # localToon/ring collisions
        self.__placeToon(self.localAvId)
        self.speedForward = self.speedLaunch
        self.laterial = -self.launchLaterial * 7
        self.zVel = self.speedForward * 0.5
        toon = base.localAvatar
        toon.b_setAnimState('swim', 1.0)
        toon.stopBobSwimTask()
        toon.dropShadow.hide()
        camera.reparentTo(base.localAvatar)
        camera.setPosHpr(0, self.CAMERA_Y + self.TOON_Y + 12, 5,
                         0, -15, 0)
        base.camLens.setMinFov(80 * ToontownGlobals.OriginalAspectRatio)
        self.help.show()
        self.help['text'] = TTLocalizer.TargetGameFlyHelp
        self.rubberSound.setVolume(0.0)
        self.rubberSound.setPlayRate(1.0)
        self.rubberSound.stop()



    def exitFly(self):
        taskMgr.remove(self.END_GAME_WAIT_TASK)
        self.__killCollisionDetectionTask()
        self.help.hide()



    def enterFall(self):
        self.notify.debug("enterLaunch")
        toon = base.localAvatar
        toon.b_setAnimState("jumpAirborne", 1.0)
        toon.dropShadow.hide()
        self.speedForward = self.speedForward * 0.50
        self.gravity = 4
        newHpr = Point3(0, -68, 0)
        newPos = Point3(0, self.CAMERA_Y + self.TOON_Y + 15, 15)
        camera.posHprInterval(2.5, newPos, newHpr,
                              blendType = "easeInOut",
                              name = self.FLY2FALL_CAM_TASK).start()

        open = self.umbrella.find('**/open_umbrella')
        open.show()
        closed = self.umbrella.find('**/closed_umbrella')
        closed.hide()
        self.umbrella.setHpr(0,180.0,-25.0)
        self.umbrella.setScale(1.5)
        self.help.show()
        self.help['text'] = TTLocalizer.TargetGameFallHelp
        self.playSound("umbrella")
        self.flutterSound.play()

    def exitFall(self):
        self.flutterSound.stop()
        pass

    def enterBouncing(self):
        self.notify.debug("enterLaunch")
        self.gravity = 12.5
        open = self.umbrella.find('**/open_umbrella')
        open.hide()
        closed = self.umbrella.find('**/closed_umbrella')
        closed.hide()
        self.umbrella.setHpr(0,0,0)
        self.umbrella.setScale(1.0)
        toon = base.localAvatar
        toon.b_setAnimState("neutral", 1.0)
        toon.dropShadow.hide()
        self.help.show()
        self.help['text'] = TTLocalizer.TargetGameBounceHelp

    def exitBouncing(self):
        pass

    def enterScore(self):
        def count(value, list):
            count = 0
            for item in list:
                if value == item:
                    count += 1
            return count

        self.notify.debug("enterScore")
        self.__killUpdateLocalToonTask()
        self.__spawnGameDoneTask()

        self.scoreboard.show()

        score = 1

        self.sendUpdate("setScore", [base.localAvatar.getX(), base.localAvatar.getY()])

        topValue = 0
        hitTarget = None
        for target in self.targetsPlaced:
            radius = self.targetSize[target[2]]
            value = self.targetValue[target[2]]
            posX = target[0]
            posY = target[1]
            dx = posX - base.localAvatar.getX()
            dy = posY - base.localAvatar.getY()
            distance = math.sqrt(dx*dx + dy*dy)
            if (distance < radius) and (topValue < value):
                topValue = value
                hitTarget = target
                hitX = posX
                hitY = posY


        if hitTarget:
            targetGN=GeomNode("target Circle")
            targetNodePathGeom = self.targets.attachNewNode(targetGN)
            targetNodePathGeom.setPos(hitX,hitY,0)
            addRing(targetGN, TargetGameGlobals.colorBlack, 100, self.targetSize[hitTarget[2]] + 0.5, 0)
            targetNodePathGeom.setColorScale(TargetGameGlobals.colorWhite['Red'], TargetGameGlobals.colorWhite['Green'], TargetGameGlobals.colorWhite['Blue'], TargetGameGlobals.colorWhite['Alpha'])
            targetNodePathGeom.setBin('ground', (hitTarget[2] * 2 + 100))
            targetNodePathGeom.setDepthWrite(False)
            targetNodePathGeom.setDepthTest(False)
            targetNodePathGeom.setTransparency(TransparencyAttrib.MAlpha)
            self.targetMarker = targetNodePathGeom

        score = topValue

        self.localTrack = Sequence()
        if self.hitInfo == "OnButt":
            self.localTrack.append(ActorInterval(base.localAvatar, 'slip-forward', startFrame= 25, endFrame = 55))
            self.hitInfo = "GettingUp"
        else:
            self.localTrack.append(ActorInterval(base.localAvatar, 'slip-forward', startFrame= 50, endFrame = 55))


        self.localTrack.append(Wait(0.5))
        if score <=1:
            self.localTrack.append(Parallel(
                Func(base.localAvatar.b_setAnimState,'Sad', 1.0),
                Func(self.playSound,'miss')))
        else:
            self.localTrack.append(Parallel(
                Func(base.localAvatar.b_setAnimState,'victory', 1.0),
                Func(self.playSound,'score')))

        newHpr = Point3(180, 10, 0)
        newPos = Point3(0, -(self.CAMERA_Y + self.TOON_Y + 12), 1)
        camera.posHprInterval(5.0, newPos, newHpr,
                              blendType = "easeInOut",
                              name = self.SCORE_CAM_TASK).start()

        self.help.hide()


        self.localTrack.start()



    def exitScore(self):
        pass


    def enterCleanup(self):
        self.notify.debug("enterCleanup")

        # toon/toon collisions were set up in setGameReady
        if not self.isSinglePlayer():
            # get rid of remote toon collisions
            for np in list(self.remoteToonCollNPs.values()):
                np.removeNode()
            del self.remoteToonCollNPs

            self.cSphereNodePath.removeNode()
            del self.cSphereNodePath
            del self.pusher
            del self.cTrav

            # turn the normal collisions back on
            base.localAvatar.collisionsOn()

    def exitCleanup(self):
        pass

    def signalDone(self):
        self.sendUpdate('setPlayerDone', [])


    def __spawnUpdatePowerBarTask(self):
        taskMgr.remove(self.UPDATE_POWERBAR_TASK)
        taskMgr.add(self.__updatePowerBarTask, self.UPDATE_POWERBAR_TASK,
                    priority=self.UPDATE_POWER_BAR_PRIORITY)
        self.rubberSound.play()
        self.bandVolume = 0.0

    def __killUpdatePowerBarTask(self):
        taskMgr.remove(self.UPDATE_POWERBAR_TASK)
        taskMgr.remove(self.TOONSTRETCHTASK)

    def __spawnCountDownTask(self):
        self.countDown = 10 #ttest
        self.signalLaunch = 0
        taskMgr.remove(self.UPDATE_COUNTDOWN_TASK)
        self.doCountDown()

    def __killCountDownTask(self):
        taskMgr.remove(self.UPDATE_COUNTDOWN_TASK)

    def __spawnGameDoneTask(self):
        taskMgr.remove(self.GAME_DONE_TASK)
        taskMgr.doMethodLater(5.0, self.__gameDone, self.GAME_DONE_TASK)

    def __killUpdateGameDoneTask(self):
        taskMgr.remove(self.GAME_DONE_TASK)


    def __spawnUpdateLocalToonTask(self):
        self.__initPosBroadcast()

        taskMgr.remove(self.UPDATE_LOCALTOON_TASK)
        taskMgr.add(self.__updateLocalToonTask, self.UPDATE_LOCALTOON_TASK,
                    priority=self.UPDATE_LOCAL_TOON_PRIORITY)

    def __killUpdateLocalToonTask(self):
        taskMgr.remove(self.UPDATE_LOCALTOON_TASK)

    def doCountDown(self, task = None):
        if self.countDown < 0:
            self.signalLaunch = 1
        else:
            self.powerBar['text'] = (TTLocalizer.TargetGameCountdown % (self.countDown))
            self.countDown -= 1
            taskMgr.doMethodLater(1.0, self.doCountDown, self.UPDATE_COUNTDOWN_TASK)

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

            # let DistributedSmoothNode figure out the deltas
            # we could optimize by creating a broadcastXZ func, but ehh
            self.getAvatar(self.localAvId).cnode.broadcastPosHprFull()

    def __spawnUpdateEnvironTask(self):
        taskMgr.remove(self.UPDATE_ENVIRON_TASK)
        taskMgr.add(self.__updateEnvironTask, self.UPDATE_ENVIRON_TASK)

    def __killUpdateEnvironTask(self):
        taskMgr.remove(self.UPDATE_ENVIRON_TASK)

    def __updateEnvironTask(self, task):
        return
        # move the environment
        dt = globalClock.getDt()
        self.speedForward = self.speedForward - (self.speedForward * self.airResistance * dt)
        t = globalClock.getFrameTime() - self.__timeBase
        self.distance = self.distance + (dt * self.speedForward)
        distance = self.distance
        distance %= self.ENVIRON_LENGTH
        self.environNode.setY(-distance)
        return Task.cont

    def __updatePowerBarTask(self, task):
        powerUp = 0
        timeDiff = 0

        if not self.arrowKeys.rightPressed():
            self.canPressRight = 1
        elif self.arrowKeys.rightPressed() and self.canPressRight:
                powerUp = 1
                self.canPressRight = 0

        if not self.arrowKeys.leftPressed():
            self.canPressLeft = 1
        elif self.arrowKeys.leftPressed() and self.canPressLeft:
                powerUp = 1
                self.canPressLeft = 0


        if self.lastPressTime:
            timeDiff = globalClock.getFrameTime() - self.lastPressTime

        if powerUp and not self.lastPressTime:
            self.lastPressTime = globalClock.getFrameTime()
            self.ticker = 0.0
        elif powerUp:
            splitTime = abs(timeDiff)
            if splitTime < 0.15:
                splitTime = 0.15
            self.power += (0.6 / abs(timeDiff)) + 5.0
            self.lastPressTime = globalClock.getFrameTime()
            self.powerBar['value'] = self.power

        if self.signalLaunch:
            self.lastPressTime = 1
            self.ticker = 1
            timeDiff = 100000

        if self.lastPressTime:
            self.ticker += globalClock.getDt()
            if self.ticker >= 0.1:
                self.ticker = 0.0
                powerDiv = 0.05
                self.power -= (1.0 + (0.20 * ((self.power * powerDiv) * (self.power * powerDiv))))
            if timeDiff > 0.5: #ttest
                self.power = self.powerBar['value']
                self.signalLaunch = 0
                if self.power > 120:
                    self.power = 120
                if self.power < 40:
                    self.power = 40
                self.gameFSM.request("fly")

        self.stretchY = (0.9 * self.stretchY) + (0.1 * self.power)
        self.stretchX = (0.9 * self.stretchX) + (0.1 * self.launchLaterial)

        base.localAvatar.setY(self.localStartPos[1] - (self.stretchY * 0.12))
        base.localAvatar.setX(self.localStartPos[0] + self.stretchX)

        # periodically send a position update
        dt = globalClock.getDt()
        self.__posBroadcast(dt)

        stretchDiff = abs(self.stretchY - self.power) * 0.2

        self.bandVolume += stretchDiff
        self.bandVolume -= globalClock.getDt()

        self.rubberSound.setVolume(self.bandVolume)
        self.rubberSound.setPlayRate(1.0 + (self.stretchY  / 120.0))


        return task.cont

    def __updateLocalToonTask(self, task):
        stateName = None
        if self.gameFSM.getCurrentState():
            stateName = self.gameFSM.getCurrentState().getName()

        toonPos = self.getAvatar(self.localAvId).getPos()



        # move the local toon
        dt = globalClock.getDt()
        if stateName == 'fall':
            self.speedForward = self.speedForward - (self.speedForward * self.umbrellaResistance * dt)
            self.laterial = self.laterial - (self.laterial * self.umbrellaResistance * dt)
            if toonPos[2] > 350.0:
                diff = toonPos[2] - 350.0
                self.speedForward += -diff * dt * 0.05
        else:
            self.speedForward = self.speedForward - (self.speedForward * self.airResistance * dt)
            self.laterial = self.laterial - (self.laterial * self.airResistance * dt)
        t = globalClock.getFrameTime() - self.__timeBase
        self.distance = self.distance + (dt * self.speedForward)

        if self.distance > self.maxDist:
            self.distance = self.maxDist

        if stateName in ["fall", 'bouncing']:
            if self.distance < 15.00:
                self.distance = 15.00

        # toonPos is a Point3, make a list
        pos = [toonPos[0], self.distance, toonPos[2]]


        if stateName in ["fly", "fall"]:
            pos[0] += (dt * self.laterial)

        liftMult = 0

        if stateName == 'fly':
            if self.arrowKeys.upPressed():
                pass
            if self.arrowKeys.downPressed():
                self.gameFSM.request('fall')

        elif stateName == 'fall':
            if self.driftX > self.TOONXZ_SPEED:
                self.driftX = self.TOONXZ_SPEED
            if self.driftX < -self.TOONXZ_SPEED:
                self.driftX = -self.TOONXZ_SPEED
            if self.driftY > self.TOONXZ_SPEED:
                self.driftY = self.TOONXZ_SPEED
            if self.driftY < -self.TOONXZ_SPEED:
                self.driftY = -self.TOONXZ_SPEED

            if self.arrowKeys.rightPressed():
                self.driftX += self.TOONXZ_SPEED * dt
            if self.arrowKeys.leftPressed():
                self.driftX -= self.TOONXZ_SPEED * dt

            if self.arrowKeys.upPressed():
                self.driftY += self.TOONXZ_SPEED * dt
            if self.arrowKeys.downPressed():
                self.driftY -= self.TOONXZ_SPEED * dt

            pos[0] += self.driftX * dt
            pos[1] += self.driftY * dt
            self.distance = pos[1]
            liftMult = 1

        elif stateName == 'bouncing':
            pos[0] += self.driftX * dt
            pos[1] += self.driftY * dt
            self.distance = pos[1]

        else:
            xVel = 0.
            if self.arrowKeys.leftPressed():
                xVel -= self.TOONXZ_SPEED
            if self.arrowKeys.rightPressed():
                xVel += self.TOONXZ_SPEED
            self.launchLaterial += xVel * dt
            if self.launchLaterial < -TargetGameGlobals.MAX_LAT:
                self.launchLaterial = -TargetGameGlobals.MAX_LAT
            if self.launchLaterial > TargetGameGlobals.MAX_LAT:
                self.launchLaterial = TargetGameGlobals.MAX_LAT
            #self.launchLaterial = pos[0]
            pos[0] =  self.getToonPlace(self.localAvId)[0] - self.launchLaterial
            pass


        lift = ((self.speedForward - self.speedStall) / self.speedStall) * liftMult
        #print("Vel %s Lift %s Gravity %s Pos %s" % (self.zVel, lift, gravity, pos[2]))
        onScreenDebug.removeAllWithPrefix(self.getDisplayPrefix())
        onScreenDebug.add("%s Vel" % (self.getDisplayPrefix()), self.zVel)
        onScreenDebug.add("%s Lift" % (self.getDisplayPrefix()), lift)
        onScreenDebug.add("%s Gravity" % (self.getDisplayPrefix()), self.gravity)
        onScreenDebug.add("%s Pos" % (self.getDisplayPrefix()), pos[2])
        onScreenDebug.add("%s Drifty" % (self.getDisplayPrefix()), self.driftY)

        if lift < 0:
            lift = 0

        upforce = (lift * 10.0) - (self.gravity)

        #self.zVel -= (0.1 * (self.speedStall - self.speedForward)) + 1.0 #Gravity
        self.zVel += (lift - self.gravity) * dt






        pos[2] += self.zVel * dt
        if pos[2] < self.trampZ:
            if self.jumpCount:
                self.playSound('trampoline')
                rebound = 0.75
                if (self.trampBounceCount >= 1):
                    #print("jump in")
                    rebound = 0.50
                    self.gameFSM.request('bouncing')
                pos[2] = self.trampZ
                if self.zVel != 0:
                    signZ = self.zVel / abs(self.zVel)
                else:
                    signZ = 1
                self.zVel = -((self.zVel * rebound) - (signZ * 1.0))
                self.trampBounceCount += 1

                if abs(self.zVel) < 1.0:
                    self.zVel = 0
                    toon = base.localAvatar
                    if stateName in ['fly', 'fall', 'bouncing']:
                        toon.b_setAnimState("neutral", 1.0)
                        toon.dropShadow.hide()
                        self.gameFSM.request('score')



            elif pos[2] < 0.1:
                toon = base.localAvatar
                if stateName == 'fall' or stateName == 'fly':
                    self.gameFSM.request('bouncing')
                if stateName == 'fly':
                    ivolume = math.sqrt(abs(self.zVel) / 40.0)
                    self.hitInfo = "OnButt"
                    self.localTrack = ActorInterval(toon, 'slip-forward', startFrame= 12, endFrame = 24)
                    self.localTrack.start()
                    self.playSound('impact', ivolume)
                    self.playSound('bounce', ivolume)

                elif stateName == 'fall' or stateName == 'bouncing':
                    ivolume = math.sqrt(abs(self.zVel) / 40.0)
                    if ivolume > 0.40:
                        if self.hitInfo == "OnButt":
                            self.localTrack = ActorInterval(toon, 'slip-forward', startFrame= 13, endFrame = 24)
                            self.localTrack.start()
                        else:
                            self.localTrack = ActorInterval(toon, 'jump-land', startFrame= 6, endFrame = 21)
                            self.localTrack.start()

                        self.playSound('bounce', ivolume)

                pos[2] = 0.1
                rebound = 0.5
                self.speedForward = self.speedForward * rebound
                self.driftX = self.driftX * rebound
                self.driftY = self.driftY * rebound
                toon = base.localAvatar
                if self.zVel != 0:
                    signZ = self.zVel / abs(self.zVel)
                else:
                    signZ = 1
                self.zVel = -((self.zVel * rebound) - (signZ * 1.0))
                if abs(self.zVel) < 1.0:
                    self.zVel = 0
                    if stateName == 'fly' or stateName == 'bouncing':
                        self.gameFSM.request('score')

        if pos[0] > TargetGameGlobals.MAX_FIELD_SPAN:
            pos[0] = TargetGameGlobals.MAX_FIELD_SPAN
            self.laterial = 0
        if pos[0] < -TargetGameGlobals.MAX_FIELD_SPAN:
            pos[0] = -TargetGameGlobals.MAX_FIELD_SPAN
            self.laterial = 0

        self.getAvatar(self.localAvId).setPos(pos[0], pos[1], pos[2])

        # this is only applicable in multiplayer, and this task also runs
        # before collisions are set up.
        if hasattr(self, 'cTrav'):
            self.cTrav.traverse(render)

        # periodically send a position update
        if stateName in ["fly", "fall", 'bouncing']:
            self.__posBroadcast(dt)


        visZ = camera.getZ(render)



        lowHeight = 100
        lowRange = 20
        opacityLow = 1
        baseOpLow = 0.6
        baseTransLow = 1.0 - baseOpLow
        if (visZ < lowHeight - lowRange) or (visZ > lowHeight + lowRange):
            transLow = 1.0
        else:
            dif = abs(visZ - lowHeight)
            transLow = dif / lowRange

        for item in self.skyListLow:
            item.setColorScale(1.0, 1.0, 1.0, transLow * baseOpLow)


        midHeight = 126
        midRange = 20
        opacityMid= 1
        baseOpMid = 1.0
        baseTransMid = 1.0 - baseOpMid
        if (visZ < midHeight - midRange) or (visZ > midHeight + midRange):
            transMid = 1.0
        else:
            dif = abs(visZ - midHeight)
            transMid = dif / midRange

        for item in self.skyListMid:
            item.setColorScale(1.0, 1.0, 1.0, transMid * baseOpMid)

        minTrans = min(1.0,transMid,transLow)
        fogVis = 1.0 - minTrans

        fogColor = (self.AMB_COLOR * minTrans) + (self.CLOUD_COLOR * fogVis)
        fogRange = (minTrans * self.FOGDISTGROUND) + (fogVis * self.FOGDISTCLOUD)

        newCamState = "Low"

        if visZ > midHeight:
            newCamState = "High"
            if self.cameraState != newCamState:
                self.cameraState = newCamState
                self.cloudRendering("High")
        elif visZ > lowHeight:
            newCamState = "Mid"
            if self.cameraState != newCamState:
                if self.cameraState == "Low":
                    self.playSound('wind1')
                self.cameraState = newCamState
                self.cloudRendering("Mid")

        else:
            newCamState = "Low"
            if self.cameraState != newCamState:
                self.cameraState = newCamState
                self.cloudRendering("Low")




        overlayOp = 0.5
        self.fogOver.setOpacity(fogVis * overlayOp)
        vol = (self.speedForward + abs(self.zVel)) / 120.0

        self.flySound.setVolume(vol)
        self.flySound.setPlayRate(1.0 + (abs(self.zVel) * 0.0050))

        # Remote Umbrella updating
        if self.updateTick % 5 == 0: # do this every 5 frames

            for avId in self.remoteAvIdList:
                toon = self.getAvatar(avId)
                if toon:
                    state = toon.animFSM.getCurrentState().getName()
                    umbrella = self.remoteUmbrellas.get(avId)
                    if umbrella:
                        if state == "Sit":
                            open = umbrella.find('**/open_umbrella')
                            open.hide()
                            closed = umbrella.find('**/closed_umbrella')
                            closed.show()
                        elif state == "swim":
                            open = umbrella.find('**/open_umbrella')
                            open.hide()
                            closed = umbrella.find('**/closed_umbrella')
                            closed.show()
                        elif state == "jumpAirborne":
                            open = umbrella.find('**/open_umbrella')
                            open.show()
                            closed = umbrella.find('**/closed_umbrella')
                            closed.hide()
                        elif state == "neutral":
                            open = umbrella.find('**/open_umbrella')
                            open.hide()
                            closed = umbrella.find('**/closed_umbrella')
                            closed.hide()
                        else:
                            open = umbrella.find('**/open_umbrella')
                            open.hide()
                            closed = umbrella.find('**/closed_umbrella')
                            closed.hide()

        self.updateTick += 1
        return Task.cont

    def cloudRendering(self, layer):

        if layer == "Low":
            #print("Flipping to Low")
            for item in self.skyListMid:
                item.setBin('fixed', 3)
            for item in self.skyListLow:
                item.setBin('fixed', 4)
            #self.playSound('wind1')
        elif layer == "Mid":
            #print("Flipping to Mid")
            for item in self.skyListMid:
                item.setBin('fixed', 3)
            for item in self.skyListLow:
                item.setBin('fixed', 3)
            #self.playSound('wind2')
        elif layer == "High":
            #print("Flipping to High")
            for item in self.skyListMid:
                item.setBin('fixed', 4)
            for item in self.skyListLow:
                item.setBin('fixed', 3)
            #self.playSound('wind3')




    def __addDropShadow_INTERNAL(self, object, scale_x, scale_y, scale_z,  list):
        """DO NOT CALL THIS DIRECTLY, only from __addToonDropShadow
        and __addRingDropShadow"""
        shadow = self.dropShadowModel.copyTo(render)
        # put the shadow at some ridiculous off-screen location
        shadow.setPos(0,self.CAMERA_Y,-100)
        shadow.setBin('shadow', 100)
        shadow.setDepthWrite(False)
        shadow.setDepthTest(True)
        # And give it the indicated initial scale.
        shadow.setScale(scale_x,scale_y,scale_z)
        list.append([shadow, object])

    def __removeDropShadow_INTERNAL(self, object, list):
        """DO NOT CALL THIS DIRECTLY, only from __removeToonDropShadow
        and __removeRingDropShadow"""
        for i in range(len(list)):
            entry = list[i]
            if entry[1] == object:
                entry[0].removeNode()
                list.pop(i)
                return
        self.notify.warning("parent object " + str(object) +
                            " not found in drop shadow list!")

    def __addToonDropShadow(self, object):
        self.__addDropShadow_INTERNAL(object, 0.5, 0.5, 0.5, self.toonDropShadows)

    def __removeToonDropShadow(self, object):
        self.__removeDropShadow_INTERNAL(object, self.toonDropShadows)

    def __removeAllToonDropShadows(self):
        """this removes ALL toon drop shadows; if we unexpectedly have
        to end the game, we may no longer have instances of the
        remote toons, so to be safe, we can just delete them all"""
        for entry in self.toonDropShadows:
            entry[0].removeNode()
        self.toonDropShadows = []


    def __spawnUpdateShadowsTask(self):
        taskMgr.remove(self.UPDATE_SHADOWS_TASK)
        taskMgr.add(self.__updateShadowsTask,
                    self.UPDATE_SHADOWS_TASK,
                    priority = self.UPDATE_SHADOWS_PRIORITY)

    def __killUpdateShadowsTask(self):
        taskMgr.remove(self.UPDATE_SHADOWS_TASK)

    def __updateShadowsTask(self, task):
        # move the drop shadows
        list = self.toonDropShadows
        for entry in list:
            object = entry[1]
            y = object.getY(render)
            # if the shadow is beyond the far plane, let it be
            #if y > self.Y_VIS_MAX:
            #    continue
            x = object.getX(render)
            #y = 10.0
            if self.jumpCount and object == base.localAvatar:
                z = self.trampZ + self.SHADOW_Z_OFFSET
            else:
                z = 0.0 + self.SHADOW_Z_OFFSET
            shadow = entry[0]
            shadow.setPos(x, y, z)

        return Task.cont



    def __spawnCollisionDetectionTask(self):
        self.__ringGroupsPassed = 0
        # do this task after localtoon has been moved
        taskMgr.remove(self.COLLISION_DETECTION_TASK)
        taskMgr.add(self.__collisionDetectionTask,
                    self.COLLISION_DETECTION_TASK,
                    priority = self.COLLISION_DETECTION_PRIORITY)

    def __killCollisionDetectionTask(self):
        taskMgr.remove(self.COLLISION_DETECTION_TASK)


    def __collisionDetectionTask(self, task):
        # check for localToon/ring collisions
        return Task.cont

    def __endGameDolater(self, task):
        self.gameOver()
        return Task.done

    # network messages
    def setTimeBase(self, timestamp):
        if not self.hasLocalToon: return
        self.__timeBase = \
                    globalClockDelta.networkToLocalTime(timestamp)

    def setColorIndices(self, a, b, c, d):
        if not self.hasLocalToon: return
        self.colorIndices = [a, b, c, d]



    def getDisplayPrefix(self):
        return 'TargetGame'

    def __gameDone(self, task = None):
        self.signalDone()
        #self.gameOver()
        return task.done

    def setGameDone(self, extra = None):
        self.gameOver()

    def setRoundDone(self):
        if not self.hasLocalToon: return
        self.round += 1
        self.roundLabel['text'] = (TTLocalizer.TargetGameBoard % (self.round))
        self.reset()
        self.gameFSM.request('prelaunch')

    def setSingleScore(self, score, avId):
        if not self.hasLocalToon: return
        for existIndex in range(len(self.avIdList)):
            if self.avIdList[existIndex] == avId:
                self.scoreLabels[existIndex]['text'] = ("%s" % (score))

    def jumpIn(self, colEntry):
        #print("In ***********************JUMP")
        self.jumpCount += 1

    def jumpOut(self, colEntry):
        #print("Out ***********************JUMP")
        self.jumpCount -= 1
        if self.jumpCount < 0:
            self.jumpCount = 0
