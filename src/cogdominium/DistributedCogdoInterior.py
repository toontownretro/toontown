""" DistributedCogdoInterior module"""

import random
from direct.interval.IntervalGlobal import *
from direct.distributed.ClockDelta import *
from toontown.building.ElevatorConstants import *
from toontown.toon import NPCToons
from toontown.toonbase.ToontownModules import NodePath
from toontown.building import ElevatorUtils
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import ToontownBattleGlobals
from direct.directnotify import DirectNotifyGlobal
from direct.fsm import ClassicFSM, State
from direct.distributed import DistributedObject
from direct.fsm import State
from direct.fsm.StatePush import StateVar, FunctionCall
from toontown.battle import BattleBase
from toontown.hood import ZoneUtil
from toontown.cogdominium.CogdoLayout import CogdoLayout
from toontown.cogdominium import CogdoGameConsts
from toontown.cogdominium import CogdoBarrelRoom, CogdoBarrelRoomConsts
from toontown.distributed import DelayDelete
from toontown.toonbase import TTLocalizer
from .CogdoExecutiveSuiteMovies import CogdoExecutiveSuiteIntro
from .CogdoElevatorMovie import CogdoElevatorMovie

PAINTING_DICT = {'s' : 'tt_m_ara_crg_paintingMoverShaker',
                 'l' : 'tt_m_ara_crg_paintingLegalEagle',
                 'm' : 'tt_m_ara_crg_paintingMoverShaker',
                 'c' : 'tt_m_ara_crg_paintingMoverShaker',}

class DistributedCogdoInterior(DistributedObject.DistributedObject):
    """
    """

    if __debug__:
        notify = DirectNotifyGlobal.directNotify.newCategory(
                                                   'DistributedCogdoInterior')

    id = 0

    cageHeights = [11.36, 0.01]

    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)

        self.toons = []
        self.activeIntervals = {}

        self.openSfx = base.loader.loadSfx("phase_5/audio/sfx/elevator_door_open.mp3")
        self.closeSfx = base.loader.loadSfx("phase_5/audio/sfx/elevator_door_close.mp3")

        self.suits = []
        self.reserveSuits = []
        self.joiningReserves = []

        self.distBldgDoId = None

        self._CogdoGameRepeat = ConfigVariableBool('cogdo-game-repeat', 0).getValue()

        # we increment this each time we come out of an elevator:
        self.currentFloor = -1

        self.elevatorName = self.__uniqueName('elevator')
        self.floorModel = None

        self.elevatorOutOpen = 0

        # initial cog positions vary based on the cog office model
        self.BottomFloor_SuitPositions = [
                         Point3(0, 15, 0),
                         Point3(10, 20, 0),
                         Point3(-7, 24, 0),
                         Point3(-10, 0, 0)]
        self.BottomFloor_SuitHs = [75, 170, -91, -44]   # Heading angles

        self.Cubicle_SuitPositions = [
                         Point3(0, 18, 0),
                         Point3(10, 12, 0),
                         Point3(-9, 11, 0),
                         Point3(-3, 13, 0)]
        self.Cubicle_SuitHs = [170, 56, -52, 10]

        self.BossOffice_SuitPositions = [
                         Point3(0, 15, 0),
                         Point3(10, 20, 0),
                         Point3(-10, 6, 0),
                         Point3(-17, 30, 0),
                         ]
        self.BossOffice_SuitHs = [170, 120, 12, 38]

        self._wantBarrelRoom = ConfigVariableBool('cogdo-want-barrel-room', 0).getValue()
        self.barrelRoom = CogdoBarrelRoom.CogdoBarrelRoom()
        self.brResults = [[], []]
        self.barrelRoomIntroTrack = None

        self.penthouseOutroTrack = None
        self.penthouseOutroChatDoneTrack = None
        self.penthouseIntroTrack = None

        self.waitMusic = base.loader.loadMusic(
            'phase_7/audio/bgm/encntr_toon_winning_indoor.mid')
        self.elevatorMusic = base.loader.loadMusic(
            'phase_7/audio/bgm/tt_elevator.mid')

        self.fsm = ClassicFSM.ClassicFSM('DistributedCogdoInterior',
                        [State.State('WaitForAllToonsInside',
                                self.enterWaitForAllToonsInside,
                                self.exitWaitForAllToonsInside,
                                ['Elevator']),
                        State.State('Elevator',
                                self.enterElevator,
                                self.exitElevator,
                                ['Game']),
                        State.State('Game',
                                self.enterGame,
                                self.exitGame,
                                ['Resting', 'Failed', 'BattleIntro']),
                        State.State('BarrelRoomIntro',
                                self.enterBarrelRoomIntro,
                                self.exitBarrelRoomIntro,
                                ['CollectBarrels', 'Off']),
                        State.State('CollectBarrels',
                                self.enterCollectBarrels,
                                self.exitCollectBarrels,
                                ['BarrelRoomReward', 'Off']),
                        State.State('BarrelRoomReward',
                                self.enterBarrelRoomReward,
                                self.exitBarrelRoomReward,
                                ['Battle', 'ReservesJoining', 'BattleIntro', 'Off']),
         State.State('BattleIntro', self.enterBattleIntro, self.exitBattleIntro, ['Battle', 'ReservesJoining', 'Off']),

                        State.State('Battle',
                                self.enterBattle,
                                self.exitBattle,
                                ['Resting',
                                'Reward',
                                'ReservesJoining']),
                        State.State('ReservesJoining',
                                self.enterReservesJoining,
                                self.exitReservesJoining,
                                ['Battle']),
                        State.State('Resting',
                                self.enterResting,
                                self.exitResting,
                                ['Elevator']),
                        State.State('Reward',
                                self.enterReward,
                                self.exitReward,
                                ['Off']),
         State.State('Failed', self.enterFailed, self.exitFailed, ['Off']),

                        State.State('Off',
                                self.enterOff,
                                self.exitOff,
                                ['Elevator',
                                'WaitForAllToonsInside',
                                'Battle']),
                ],
                # Initial State
                'Off',
                # Final State
                'Off',
                )

        # make sure we're in the initial state
        self.fsm.enterInitialState()
        self._haveEntranceElevator = StateVar(False)
        self._stashEntranceElevator = StateVar(False)
        self._stashEntranceElevatorFC = FunctionCall(self._doStashEntranceElevator,
                                                     self._haveEntranceElevator,
                                                     self._stashEntranceElevator)
        self._entranceElevCallbacks = []
        self._doEntranceElevCallbacksFC = FunctionCall(self._doEntranceElevCallbacks,
                                                       self._haveEntranceElevator)
        self.cage = None
        self.shopOwnerNpcId = None
        self.shopOwnerNpc = None
        self._movie = None
        self.SOSToonName = None
        self.FOType = None

    def setShopOwnerNpcId(self, npcId):
        self.shopOwnerNpcId = npcId

    def setSOSNpcId(self, npcId):
        self.SOSToonName = NPCToons.getNPCName(npcId)

    def setFOType(self, typeId):
        self.FOType = chr(typeId)

    def __uniqueName(self, name):
        DistributedCogdoInterior.id += 1
        return (name + '%d' % DistributedCogdoInterior.id)

    def generate(self):
        """generate(self)
        This method is called when the DistributedObject is reintroduced
        to the world, either for the first time or from the cache.
        """
        assert(self.notify.debug("generate()"))
        DistributedObject.DistributedObject.generate(self)

        # listen for the generate event, which will be thrown after the
        # required fields are filled in
        self.announceGenerateName = self.uniqueName('generate')
        self.accept(self.announceGenerateName, self.handleAnnounceGenerate)

        # Load the elevator model
        self.elevatorModelIn = loader.loadModel(
                                'phase_5/models/cogdominium/tt_m_ara_csa_elevatorB')
        self.leftDoorIn = self.elevatorModelIn.find('**/left_door')
        self.rightDoorIn = self.elevatorModelIn.find('**/right_door')

        self.elevatorModelOut = loader.loadModel(
                                'phase_5/models/cogdominium/tt_m_ara_csa_elevatorB')
        self.leftDoorOut = self.elevatorModelOut.find('**/left_door')
        self.rightDoorOut = self.elevatorModelOut.find('**/right_door')

    def __makeShopOwnerNpc(self):
        if self.shopOwnerNpc:
            return
        self.shopOwnerNpc = NPCToons.createLocalNPC(self.shopOwnerNpcId)
        if not self.shopOwnerNpc:
            self.notify.warning("No shopkeeper in this cogdominium, using FunnyFarm Sellbot FO NPCToons")
            random.seed(self.doId)
            shopkeeper = random.randint(7001, 7009)
            self.shopOwnerNpc = NPCToons.createLocalNPC(shopkeeper)
        self.shopOwnerNpc.addActive()
        self.shopOwnerNpc.reparentTo(self.cage)
        self.shopOwnerNpc.setPosHpr(0, -2, 0, 180, 0, 0)
        self.shopOwnerNpc.loop('neutral')

    def setElevatorLights(self, elevatorModel):
        """
        Sets up the lights on the interior elevators to represent the
        number of floors in the building, and to light up the current
        floor number.
        """
        npc=elevatorModel.findAllMatches("**/floor_light_?;+s")
        for i in range(npc.getNumPaths()):
            np=npc.getPath(i)
            # Get the last character, and make it zero based:
            floor=int(np.getName()[-1:])-1

            if (floor == self.currentFloor):
                np.setColor(LIGHT_ON_COLOR)
            elif floor < self.layout.getNumGameFloors():
                if self.isBossFloor(self.currentFloor):
                    np.setColor(LIGHT_ON_COLOR)
                else:
                    np.setColor(LIGHT_OFF_COLOR)
            else:
                np.hide()

    def startAlertElevatorLightIval(self, elevatorModel):
        light = elevatorModel.find("**/floor_light_%s" % (self.currentFloor + 1))
        track = Sequence(Func(light.setColor, Vec4(1.0, 0.6, 0.6, 1.0)), Wait(0.9), Func(light.setColor, LIGHT_ON_COLOR), Wait(0.9))
        self.activeIntervals["alertElevatorLight"] = track
        track.loop()

    def stopAlertElevatorLightIval(self, elevatorModel):
        self.__finishInterval("alertElevatorLight")
        self.setElevatorLights(elevatorModel)

    def handleAnnounceGenerate(self, obj):
        """
        handleAnnounceGenerate is called after all of the required fields are
        filled in
        'obj' is another copy of self
        """
        self.ignore(self.announceGenerateName)

        self.cageDoorSfx = loader.loadSfx('phase_5/audio/sfx/CHQ_SOS_cage_door.mp3')
        self.cageLowerSfx = loader.loadSfx('phase_5/audio/sfx/CHQ_SOS_cage_lower.mp3')

        assert(self.notify.debug('joining DistributedCogdoInterior'))
        # Update the minigame AI to join our local toon doId
        self.sendUpdate('setAvatarJoined', [])

    def disable(self):
        assert(self.notify.debug('disable()'))
        self.fsm.requestFinalState()
        self.__cleanupIntervals()
        self.ignoreAll()
        self.__cleanup()
        self.__cleanupShopOwnerNpc()
        self.__cleanupPenthouseIntro()
        DistributedObject.DistributedObject.disable(self)

    def __cleanupShopOwnerNpc(self):
        if self.shopOwnerNpc:
            self.shopOwnerNpc.removeActive()
            self.shopOwnerNpc.delete()
            self.shopOwnerNpc = None

    def __cleanupPenthouseIntro(self):
        if hasattr(self, '_movie') and self._movie:
            self._movie.unload()
            self._movie = None

    def delete(self):
        assert(self.notify.debug('delete()'))
        self._stashEntranceElevatorFC.destroy()
        self._doEntranceElevCallbacksFC.destroy()
        self._haveEntranceElevator.destroy()
        self._stashEntranceElevator.destroy()
        self._entranceElevCallbacks = None
        del self.waitMusic
        del self.elevatorMusic
        del self.openSfx
        del self.closeSfx
        del self.fsm
        # No more battle multiplier
        base.localAvatar.inventory.setBattleCreditMultiplier(1)
        DistributedObject.DistributedObject.delete(self)

    def isBossFloor(self, floorNum):
        if self.layout.hasBossBattle():
            if self.layout.getBossBattleFloor() == floorNum:
                return True
        return False

    def __cleanup(self):
        self.toons = []
        self.suits = []
        self.reserveSuits = []
        self.joiningReserves = []
        # Clean up elevator models
        if (self.elevatorModelIn != None):
            self.elevatorModelIn.removeNode()
        if (self.elevatorModelOut != None):
            self.elevatorModelOut.removeNode()
        # Clean up current floor
        if (self.floorModel != None):
            self.floorModel.removeNode()
        # Clean up current cage
        if (self.cage != None):
            self.cage = None
        # Clean up current barrel room
        if (self.barrelRoom != None):
            self.barrelRoom.destroy()
            self.barrelRoom = None
        self.leftDoorIn = None
        self.rightDoorIn = None
        self.leftDoorOut = None
        self.rightDoorOut = None

    def __addToon(self, toon):
        assert(self.notify.debug('addToon(%d)' % toon.doId))
        self.accept(toon.uniqueName('disable'),
                        self.__handleUnexpectedExit, extraArgs=[toon])

    def __handleUnexpectedExit(self, toon):
        self.notify.warning('handleUnexpectedExit() - toon: %d' % toon.doId)
        self.__removeToon(toon, unexpected=1)

    def __removeToon(self, toon, unexpected=0):
        assert(self.notify.debug('removeToon() - toon: %d' % toon.doId))
        if (self.toons.count(toon) == 1):
            self.toons.remove(toon)
        self.ignore(toon.uniqueName('disable'))

    def __finishInterval(self, name):
        """ Force the specified interval to jump to the end
        """
        if (name in self.activeIntervals):
            interval = self.activeIntervals[name]
            if (interval.isPlaying()):
                assert(self.notify.debug('finishInterval(): %s' % \
                        interval.getName()))
                interval.finish()

    def __cleanupIntervals(self):
        for interval in list(self.activeIntervals.values()):
            interval.finish()
        self.activeIntervals = {}

    def __closeInElevator(self):
        self.leftDoorIn.setPos(3.5, 0, 0)
        self.rightDoorIn.setPos(-3.5, 0, 0)

    ##### Messages from the server #####

    def getZoneId(self):
        return self.zoneId

    def setZoneId(self, zoneId):
        self.zoneId = zoneId

    def getExtZoneId(self):
        return self.extZoneId

    def setExtZoneId(self, extZoneId):
        self.extZoneId = extZoneId

    def getDistBldgDoId(self):
        return self.distBldgDoId

    def setDistBldgDoId(self, distBldgDoId):
        self.distBldgDoId = distBldgDoId

    def setNumFloors(self, numFloors):
        self.layout = CogdoLayout(numFloors)

    def getToonIds(self):
        toonIds = []
        for toon in self.toons:
            toonIds.append(toon.doId)
        return toonIds

    def setToons(self, toonIds, hack):
        assert(self.notify.debug('setToons(): %s' % toonIds))
        self.toonIds = toonIds
        oldtoons = self.toons
        self.toons = []
        for toonId in toonIds:
            if (toonId != 0):
                if (toonId in self.cr.doId2do):
                    toon = self.cr.doId2do[toonId]
                    toon.stopSmooth()
                    self.toons.append(toon)
                    if (oldtoons.count(toon) == 0):
                        assert(self.notify.debug('setToons() - new toon: %d' % \
                                toon.doId))
                        self.__addToon(toon)
                else:
                    self.notify.warning('setToons() - no toon: %d' % toonId)
        for toon in oldtoons:
            if (self.toons.count(toon) == 0):
                self.__removeToon(toon)

    def setSuits(self, suitIds, reserveIds, values):
        assert(self.notify.debug('setSuits(): active %s reserve %s values %s' \
                % (suitIds, reserveIds, values)))
        oldsuits = self.suits
        self.suits = []
        self.joiningReserves = []
        for suitId in suitIds:
            if (suitId in self.cr.doId2do):
                suit = self.cr.doId2do[suitId]
                self.suits.append(suit)
                # Set this on the client
                suit.fsm.request('Battle')
                # This will allow client to respond to setState() from the
                # server from here on out
                suit.buildingSuit = 1
                suit.reparentTo(render)
                if (oldsuits.count(suit) == 0):
                    assert(self.notify.debug('setSuits() suit: %d joining' % \
                        suit.doId))
                    self.joiningReserves.append(suit)
            else:
                self.notify.warning('setSuits() - no suit: %d' % suitId)
        self.reserveSuits = []
        assert(len(reserveIds) == len(values))
        for index in range(len(reserveIds)):
            suitId = reserveIds[index]
            if (suitId in self.cr.doId2do):
                suit = self.cr.doId2do[suitId]
                self.reserveSuits.append((suit, values[index]))
            else:
                self.notify.warning('setSuits() - no suit: %d' % suitId)

        if (len(self.joiningReserves) > 0):
            assert(self.notify.debug('setSuits() reserves joining'))
            self.fsm.request('ReservesJoining')

    def setState(self, state, timestamp):
        assert(self.notify.debug("setState(%s, %d)" % \
                                (state, timestamp)))
        self.fsm.request(state, [globalClockDelta.localElapsedTime(timestamp)])

    def stashElevatorIn(self, stash = True):
        self._stashEntranceElevator.set(stash)

    def getEntranceElevator(self, callback):
        if self._haveEntranceElevator.get():
            callback(self.elevIn)
        else:
            self._entranceElevCallbacks.append(callback)

    def _doEntranceElevCallbacks(self, haveElev):
        if haveElev:
            while len(self._entranceElevCallbacks):
                cbs = self._entranceElevCallbacks[:]
                self._entranceElevCallbacks = []
                for callback in cbs:
                    callback(self.elevIn)

    def _doStashEntranceElevator(self, haveElev, doStash):
        if haveElev:
            if doStash:
                self.elevIn.stash()
            else:
                self.elevIn.unstash()

    ##### Messages to the server #####

    def d_elevatorDone(self):
        assert(self.notify.debug('network:elevatorDone(%d)' % base.localAvatar.doId))
        self.sendUpdate('elevatorDone', [])

    def d_reserveJoinDone(self):
        assert(self.notify.debug('network:reserveJoinDone(%d)' % base.localAvatar.doId))
        self.sendUpdate('reserveJoinDone', [])

    # Specific State Functions

    ##### Off state #####

    def enterOff(self, ts=0):
        assert(self.notify.debug('enterOff()'))
        messenger.send('sellbotFieldOfficeChanged', [False])
        return None

    def exitOff(self):
        return None

    ##### WaitForAllToonsInside state #####

    def enterWaitForAllToonsInside(self, ts=0):
        assert(self.notify.debug('enterWaitForAllToonsInside()'))
        base.transitions.fadeOut(0)
        return None

    def exitWaitForAllToonsInside(self):
        return None

    def enterGame(self, ts = 0):
        assert(self.notify.debug('enterElevator()'))
        base.cr.forbidCheesyEffects(1)

    def exitGame(self):
        base.cr.forbidCheesyEffects(0)

    ##### Elevator state #####

    def __playElevator(self, ts, name, callback):
        # Load the floor model

        SuitHs = []   # Heading angles
        SuitPositions = []

        if self.floorModel:
            self.floorModel.removeNode()
            self.floorModel = None
        if self.cage:
            self.cage = None

        if (self.currentFloor == 0):
            # bottom floor
            SuitHs = self.BottomFloor_SuitHs
            SuitPositions = self.BottomFloor_SuitPositions
        if self.isBossFloor(self.currentFloor):
            # Top floor
            self.barrelRoom.unload()
            self.floorModel = loader.loadModel('phase_5/models/cogdominium/tt_m_ara_crg_penthouse')
            self.cage = self.floorModel.find('**/cage')
            pos = self.cage.getPos()
            self.cagePos = []
            for height in self.cageHeights:
                self.cagePos.append(Point3(pos[0], pos[1], height))

            self.cageDoor = self.floorModel.find('**/cage_door')
            self.cageDoor.wrtReparentTo(self.cage)
            if self.FOType:
                paintingModelName = PAINTING_DICT.get(self.FOType)
                for i in range(4):
                    paintingModel = loader.loadModel('phase_5/models/cogdominium/%s' % paintingModelName)
                    loc = self.floorModel.find('**/loc_painting%d' % (i + 1))
                    paintingModel.reparentTo(loc)
            SuitHs = self.BossOffice_SuitHs
            SuitPositions = self.BossOffice_SuitPositions
            self.__makeShopOwnerNpc()
        else:
            if self._wantBarrelRoom:
                self.barrelRoom.load()
                self.barrelRoom.hide()
            # middle floor
            SuitHs = self.Cubicle_SuitHs
            SuitPositions = self.Cubicle_SuitPositions

        if self.floorModel:
            self.floorModel.reparentTo(render)

            if self.isBossFloor(self.currentFloor):
                self.notify.debug('Load boss_suit_office')
                elevIn = self.floorModel.find(CogdoGameConsts.PenthouseElevatorInPath).copyTo(render)
                elevOut = self.floorModel.find(CogdoGameConsts.PenthouseElevatorOutPath)
                frame = self.elevatorModelOut.find('**/frame')
                if not frame.isEmpty():
                    frame.hide()
                frame = self.elevatorModelIn.find('**/frame')
                if not frame.isEmpty():
                    frame.hide()
                self.elevatorModelOut.reparentTo(elevOut)
            else:
                # We need to name this something more useful (and we'll need the
                # location of the opposite elevator as well)
                elevIn = self.floorModel.find('**/elevator-in')
                elevOut = self.floorModel.find('**/elevator-out')
        elif self._wantBarrelRoom and self.barrelRoom.isLoaded():
            elevIn = self.barrelRoom.dummyElevInNode
            elevOut = self.barrelRoom.model.find(CogdoBarrelRoomConsts.BarrelRoomElevatorOutPath)
            y = elevOut.getY(render)
            elevOut = elevOut.copyTo(render)
            elevOut.setY(render, y - 0.75)
        else:
            # TODO: TEMP
            floorModel = loader.loadModel('phase_7/models/modules/boss_suit_office')
            elevIn = floorModel.find('**/elevator-in').copyTo(render)
            elevOut = floorModel.find('**/elevator-out').copyTo(render)
            floorModel.removeNode()
        self.elevIn = elevIn

        # store elevOut until it's needed
        self.elevOut = elevOut
        self._haveEntranceElevator.set(True)

        # Position the suits

        assert(len(self.suits) <= 4)
        for index in range(len(self.suits)):
            assert(self.notify.debug('setting suit: %d to pos: %s' % \
                (self.suits[index].doId, SuitPositions[index])))
            self.suits[index].setPos(SuitPositions[index])
            if (len(self.suits) > 2):
                self.suits[index].setH(SuitHs[index])
            else:
                self.suits[index].setH(170)  # if there's 2 or 1 suits, make them face fwd since there's no other suits they would be to be talking to
            self.suits[index].loop('neutral')

        # Position the toons
        for toon in self.toons:
            toon.reparentTo(self.elevatorModelIn)
            assert(self.toonIds.count(toon.doId) == 1)
            index = self.toonIds.index(toon.doId)
            assert(index >= 0 and index <= 3)
            toon.setPos(ElevatorPoints[index][0],
                        ElevatorPoints[index][1],
                        ElevatorPoints[index][2])
            toon.setHpr(180, 0, 0)
            toon.loop('neutral')

        # Show the elevator and position it in the correct place for the floor
        self.elevatorModelIn.reparentTo(elevIn)
        # Start with the doors in closed position
        self.leftDoorIn.setPos(3.5, 0, 0)
        self.rightDoorIn.setPos(-3.5, 0, 0)

        # Position the camera behind the toons
        camera.reparentTo(self.elevatorModelIn)
        camera.setH(180)
        camera.setP(0)
        camera.setPos(0, 14, 4)

        # Play elevator music
        base.playMusic(self.elevatorMusic, looping=1, volume=0.8)

        # Ride the elevator, then open the doors.
        track = Sequence(Func(base.transitions.noTransitions),
            ElevatorUtils.getRideElevatorInterval(ELEVATOR_NORMAL),
            ElevatorUtils.getOpenInterval(self, self.leftDoorIn, self.rightDoorIn,
                                          self.openSfx, None, type = ELEVATOR_NORMAL),
            Func(camera.wrtReparentTo, render),
            )

        for toon in self.toons:
            track.append(Func(toon.wrtReparentTo, render))
        track.append(Func(callback))
        track.start(ts)
        self.activeIntervals[name] = track

    def enterElevator(self, ts=0):
        # Load model for the current floor and the suit models for the floor
        assert(self.notify.debug('enterElevator()'))

        if not self._CogdoGameRepeat:
            self.currentFloor += 1
        self.cr.playGame.getPlace().currentFloor = self.currentFloor
        self.setElevatorLights(self.elevatorModelIn)
        self.setElevatorLights(self.elevatorModelOut)

        # hide elevator from previous floor (if any)
        # unless it's the top floor, in that case leave it where it is
        if not self.isBossFloor(self.currentFloor):
            self.elevatorModelOut.detachNode()
            messenger.send('sellbotFieldOfficeChanged', [True])
        else:
            self._movie = CogdoElevatorMovie()
            self._movie.load()
            self._movie.play()

        self.__playElevator(ts, self.elevatorName, self.__handleElevatorDone)

        # Get the floor multiplier
        mult = ToontownBattleGlobals.getCreditMultiplier(self.currentFloor)
        # Now set the inventory battleCreditMult
        base.localAvatar.inventory.setBattleCreditMultiplier(mult)

    def __handleElevatorDone(self):
        assert(self.notify.debug('handleElevatorDone()'))
        self.d_elevatorDone()

    def exitElevator(self):
        self.elevatorMusic.stop()
        if self._movie:
            self._movie.end()
            self.__cleanupPenthouseIntro()
        self.__finishInterval(self.elevatorName)
        return None

    def __setupBarrelRoom(self):
        base.cr.playGame.getPlace().fsm.request('stopped')
        base.transitions.irisOut(0.0)
        self.elevatorModelIn.detachNode()
        self._showExitElevator()
        self.barrelRoom.show()
        self.barrelRoom.placeToonsAtEntrance(self.toons)

    def barrelRoomIntroDone(self):
        self.sendUpdate('toonBarrelRoomIntroDone', [])

    def enterBarrelRoomIntro(self, ts = 0):
        if not self.isBossFloor(self.currentFloor):
            if self._wantBarrelRoom:
                self.__setupBarrelRoom()
                self.barrelRoomIntroTrack, trackName = self.barrelRoom.getIntroInterval()
                self.barrelRoomIntroDoneEvent = trackName
                self.accept(self.barrelRoomIntroDoneEvent, self.barrelRoomIntroDone)
                self.activeIntervals[trackName] = self.barrelRoomIntroTrack
                self.barrelRoomIntroTrack.start(ts)
            else:
                self._showExitElevator()

    def exitBarrelRoomIntro(self):
        if self._wantBarrelRoom and not self.isBossFloor(self.currentFloor):
            self.ignore(self.barrelRoomIntroDoneEvent)
            if self.barrelRoomIntroTrack:
                self.barrelRoomIntroTrack.finish()
                DelayDelete.cleanupDelayDeletes(self.barrelRoomIntroTrack)
                self.barrelRoomIntroTrack = None

    def __handleLocalToonLeftBarrelRoom(self):
        self.notify.info('Local toon teleported out of barrel room.')
        self.sendUpdate('toonLeftBarrelRoom', [])
        self.barrelRoom.deactivate()

    def enterCollectBarrels(self, ts = 0):
        if not self.isBossFloor(self.currentFloor):
            if self._wantBarrelRoom:
                self.acceptOnce('localToonLeft', self.__handleLocalToonLeftBarrelRoom)
                self.barrelRoom.activate()
                base.playMusic(self.waitMusic, looping=1, volume=0.7)

    def exitCollectBarrels(self):
        if self._wantBarrelRoom and not self.isBossFloor(self.currentFloor):
            self.ignore('localToonLeft')
            self.barrelRoom.deactivate()
            self.waitMusic.stop()

    def __brRewardDone(self, task = None):
        self.notify.info('Toon finished watching the barrel room reward.')
        self.sendUpdate('toonBarrelRoomRewardDone', [])

    def setBarrelRoomReward(self, avIds, laffs):
        self.brResults = [avIds, laffs]
        self.barrelRoom.setRewardResults(self.brResults)

    def enterBarrelRoomReward(self, ts = 0):
        if self._wantBarrelRoom and not self.isBossFloor(self.currentFloor):
            base.cr.playGame.getPlace().fsm.request('stopped')
            self.startAlertElevatorLightIval(self.elevatorModelOut)
            track, trackName = self.barrelRoom.showRewardUi(self.brResults, callback=self.__brRewardDone)
            self.activeIntervals[trackName] = track
            track.start()
            self.barrelRoom.placeToonsNearBattle(self.toons)

    def exitBarrelRoomReward(self):
        if self._wantBarrelRoom and not self.isBossFloor(self.currentFloor):
            base.cr.playGame.getPlace().fsm.request('walk')
            self.stopAlertElevatorLightIval(self.elevatorModelOut)
            self.barrelRoom.hideRewardUi()

    def enterBattleIntro(self, ts = 0):
        self._movie = CogdoExecutiveSuiteIntro(self.shopOwnerNpc)
        self._movie.load()
        self._movie.play()

    def exitBattleIntro(self):
        self._movie.end()
        self.__cleanupPenthouseIntro()

    ##### Battle state #####

    def __playCloseElevatorOut(self, name, delay = 0):
        # Close the elevator doors
        track = Sequence(
            Wait(delay + SUIT_LEAVE_ELEVATOR_TIME),
            Parallel(SoundInterval(self.closeSfx),
                     LerpPosInterval(self.leftDoorOut,
                                     ElevatorData[ELEVATOR_NORMAL]['closeTime'],
                                     ElevatorUtils.getLeftClosePoint(ELEVATOR_NORMAL),
                                     startPos=Point3(0, 0, 0),
                                     blendType='easeOut'),
                     LerpPosInterval(self.rightDoorOut,
                                     ElevatorData[ELEVATOR_NORMAL]['closeTime'],
                                     ElevatorUtils.getRightClosePoint(ELEVATOR_NORMAL),
                                     startPos=Point3(0, 0, 0),
                                     blendType='easeOut')
                     ),
            )
        track.start()
        self.activeIntervals[name] = track

    def enterBattle(self, ts=0):
        assert(self.notify.debug('enterBattle()'))

        if self._wantBarrelRoom and self.elevatorOutOpen == 1:
            self.__playCloseElevatorOut(self.uniqueName('close-out-elevator'), delay=2)
            camera.setPos(0, -15, 6)
            camera.headsUp(self.elevatorModelOut)

    def _showExitElevator(self):

        # now that we're in the barrel room, show the exit elevator
        # Show the elevator and position it in the correct place for the floor
        self.elevatorModelOut.reparentTo(self.elevOut)
        # Start with the doors in closed position
        self.leftDoorOut.setPos(3.5, 0, 0)
        self.rightDoorOut.setPos(-3.5, 0, 0)

        if not (self._wantBarrelRoom and self.elevatorOutOpen == 1):
            self.__playCloseElevatorOut(self.uniqueName('close-out-elevator'))
            # Watch reserve suits as they walk from the elevator
            camera.setPos(0, -15, 6)
            camera.headsUp(self.elevatorModelOut)
        return None

    def exitBattle(self):
        if (self.elevatorOutOpen == 1):
            self.__finishInterval(self.uniqueName('close-out-elevator'))
            self.elevatorOutOpen = 0
        return None

    ##### ReservesJoining state #####

    def __playReservesJoining(self, ts, name, callback):
        # Position the joining suits
        index = 0
        assert(len(self.joiningReserves) <= 4)
        for suit in self.joiningReserves:
            suit.reparentTo(render)
            suit.setPos(self.elevatorModelOut, Point3(ElevatorPoints[index][0],
                                                      ElevatorPoints[index][1],
                                                      ElevatorPoints[index][2]))
            index += 1
            suit.setH(180)
            suit.loop('neutral')

        if len(self.suits) == len(self.joiningReserves):
            camSequence = Sequence(
                Func(camera.wrtReparentTo, localAvatar),
                Func(camera.setPos, Point3(0, 5, 5)),
                Func(camera.headsUp, self.elevatorModelOut))
        else:
            camSequence = Sequence(
                Func(camera.wrtReparentTo, self.elevatorModelOut),
                Func(camera.setPos, Point3(0, -8, 2)),
                Func(camera.setHpr, Vec3(0, 10, 0)))

        # Aim the camera at the far elevator
        track = Sequence(
            Func(camera.wrtReparentTo, self.elevatorModelOut),
            Func(camera.setPos, Point3(0, -8, 2)),
            Func(camera.setHpr, Vec3(0, 10, 0)),

            # Open the elevator doors
            Parallel(SoundInterval(self.openSfx),
                     LerpPosInterval(self.leftDoorOut,
                                     ElevatorData[ELEVATOR_NORMAL]['closeTime'],
                                     Point3(0, 0, 0),
                                     startPos=ElevatorUtils.getLeftClosePoint(ELEVATOR_NORMAL),
                                     blendType='easeOut'),
                     LerpPosInterval(self.rightDoorOut,
                                     ElevatorData[ELEVATOR_NORMAL]['closeTime'],
                                     Point3(0, 0, 0),
                                     startPos=ElevatorUtils.getRightClosePoint(ELEVATOR_NORMAL),
                                     blendType='easeOut'),
                     ),

            # Hold the camera angle for a couple of beats
            Wait(SUIT_HOLD_ELEVATOR_TIME),

            # Reparent the camera to render (enterWaitForInput will
            # position it properly again by the battle)
            Func(camera.wrtReparentTo, render),
            Func(callback),
            )
        track.start(ts)
        self.activeIntervals[name] = track

    def enterReservesJoining(self, ts=0):
        assert(self.notify.debug('enterReservesJoining()'))
        self.__playReservesJoining(ts, self.uniqueName('reserves-joining'),
                                       self.__handleReserveJoinDone)
        return None

    def __handleReserveJoinDone(self):
        assert(self.notify.debug('handleReserveJoinDone()'))
        self.joiningReserves = []
        self.elevatorOutOpen = 1
        self.d_reserveJoinDone()

    def exitReservesJoining(self):
        self.__finishInterval(self.uniqueName('reserves-joining'))
        return None

    ##### Resting state #####

    def enterResting(self, ts=0):
        assert(self.notify.debug('enterResting()'))
        self._showExitElevator()
        self._setAvPosFDC = FrameDelayedCall('setAvPos', self._setAvPosToExit)
        if self._wantBarrelRoom:
            self.barrelRoom.showBattleAreaLight(True)
        base.playMusic(self.waitMusic, looping=1, volume=0.7)
        self.__closeInElevator()
        self._haveEntranceElevator.set(False)
        self._stashEntranceElevator.set(False)

    def _setAvPosToExit(self):
        base.localAvatar.setPos(self.elevOut, 0, -10, 0)
        base.localAvatar.setHpr(self.elevOut, 0, 0, 0)
        base.cr.playGame.getPlace().fsm.request('walk')

    def exitResting(self):
        self._setAvPosFDC.destroy()
        self.waitMusic.stop()

    ##### Reward state #####

    def enterReward(self, ts=0):
        assert(self.notify.debug('enterReward()'))
        if self.isBossFloor(self.currentFloor):
            self.penthouseOutroTrack = self.__outroPenthouse()
            self.penthouseOutroTrack.start(ts)
        else:
            self.exitCogdoBuilding()
        return None

    def exitReward(self):
        self.notify.debug('exitReward')
        if self.penthouseOutroTrack:
            self.penthouseOutroTrack.finish()
            DelayDelete.cleanupDelayDeletes(self.penthouseOutroTrack)
            self.penthouseOutroTrack = None
            if not self.penthouseOutroChatDoneTrack:
                self.notify.debug('exitReward: instanting outroPenthouseChatDone track')
                self.__outroPenthouseChatDone()
            self.penthouseOutroChatDoneTrack.finish()
            self.penthouseOutroChatDoneTrack = None

    ##### Failed state #####

    def enterFailed(self, ts = 0):
        self.exitCogdoBuilding()
        return None

    def exitFailed(self):
        self.notify.debug('exitFailed()')
        self.exitCogdoBuilding()
        return None

    def exitCogdoBuilding(self):
        if base.localAvatar.hp < 0:
            return
        base.localAvatar.b_setParent(ToontownGlobals.SPHidden)
        request = {
            'loader' : ZoneUtil.getBranchLoaderName(self.extZoneId),
            'where' : ZoneUtil.getToonWhereName(self.extZoneId),
            'how' : 'elevatorIn',
            'hoodId' : ZoneUtil.getHoodId(self.extZoneId),
            'zoneId' : self.extZoneId,
            'shardId' : None,
            'avId' : -1,
            'bldgDoId' : self.distBldgDoId,
            }
        messenger.send('DSIDoneEvent', [request])

    def displayBadges(self):
        numFloors = self.layout.getNumGameFloors()
        if numFloors > 5 or numFloors < 3:
            pass
        else:
            self.notify.warning('Invalid floor number for display badges.')
        for player in range(len(self.toons)):
            goldBadge = loader.loadModel('phase_5/models/cogdominium/tt_m_ara_crg_goldTrophy')
            goldBadge.setScale(1.2)
            goldNode = render.find('**/gold_0' + str(player + 1))
            goldBadge.reparentTo(goldNode)
            for floor in range(numFloors):
                silverBadge = loader.loadModel('phase_5/models/cogdominium/tt_m_ara_crg_silverTrophy.bam')
                silverBadge.setScale(1.2)
                silverNode = render.find('**/silver_0' + str(floor * 4 + (player + 1)))
                silverBadge.reparentTo(silverNode)

    ##### Outro state #####

    def __outroPenthouse(self):
        avatar = base.localAvatar
        trackName = '__outroPenthouse-%d' % avatar.doId
        track = Parallel(name=trackName)
        base.cr.playGame.getPlace().fsm.request('stopped')
        speech = TTLocalizer.CogdoExecutiveSuiteToonThankYou % self.SOSToonName
        track.append(Sequence(Func(camera.wrtReparentTo, localAvatar),
                              Func(camera.setPos, 0, -9, 9),
                              Func(camera.lookAt, Point3(5, 15, 0)),
                              Parallel(self.cage.posInterval(0.75, self.cagePos[1], blendType='easeOut'),
                              SoundInterval(self.cageLowerSfx, duration=0.5)),
                              Parallel(self.cageDoor.hprInterval(0.5, VBase3(0, 90, 0), blendType='easeOut'),
                              Sequence(SoundInterval(self.cageDoorSfx), duration=0)), Wait(0.25),
                              Func(self.shopOwnerNpc.wrtReparentTo, render),
                              Func(self.shopOwnerNpc.setScale, 1),
                              Func(self.shopOwnerNpc.loop, 'walk'),
                              Func(self.shopOwnerNpc.headsUp, Point3(0, 10, 0)),
                              ParallelEndTogether(self.shopOwnerNpc.posInterval(1.5, Point3(0, 10, 0)),
                              self.shopOwnerNpc.hprInterval(0.5, VBase3(180, 0, 0), blendType='easeInOut')),
                              Func(self.shopOwnerNpc.setChatAbsolute, TTLocalizer.CagedToonYippee, CFSpeech),
                              ActorInterval(self.shopOwnerNpc, 'jump'),
                              Func(self.shopOwnerNpc.loop, 'neutral'),
                              Func(self.shopOwnerNpc.headsUp, localAvatar),
                              Func(self.shopOwnerNpc.setLocalPageChat, speech, 0),
                              Func(camera.lookAt, self.shopOwnerNpc, Point3(0, 0, 2))))
        self.activeIntervals[trackName] = track
        self.accept('doneChatPage', self.__outroPenthouseChatDone)
        return track

    def __outroPenthouseChatDone(self, elapsed = None):
        self.shopOwnerNpc.setChatAbsolute(TTLocalizer.CogdoExecutiveSuiteToonBye, CFSpeech)
        self.ignore('doneChatPage')
        track = Parallel(Sequence(ActorInterval(self.shopOwnerNpc, 'wave'),
                                  Func(self.shopOwnerNpc.loop, 'neutral')),
                                  Sequence(Wait(2.0),
                                  Func(self.exitCogdoBuilding),
                                  Func(base.camLens.setMinFov, ToontownGlobals.DefaultCameraFov),
                                  ),
                        )
        track.start()
        self.penthouseOutroChatDoneTrack = track

    ##### Reset state #####

    #def enterReset(self, ts=0):
    #    assert(self.notify.debug('enterReset()'))
    #    self.__cleanup()
    #    return None

    #def exitReset(self):
    #    return None
