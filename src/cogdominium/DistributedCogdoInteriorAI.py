import copy
import random
from direct.directnotify import DirectNotifyGlobal
from direct.distributed import DistributedObjectAI
from direct.distributed.ClockDelta import *
from direct.fsm import ClassicFSM, State
from direct.task import Timer

from toontown.toon import NPCToons

from otp.ai.AIBaseGlobal import *

from toontown.ai import ToonBarrier
from toontown.battle import BattleBase
from toontown.cogdominium import DistributedCogdoBattleBldgAI
from toontown.building.ElevatorConstants import *
from toontown.suit.SuitDNA import SuitDNA
from toontown.toonbase.ToontownBattleGlobals import *
from toontown.hood import ZoneUtil
from toontown.minigame.MinigameGlobals import SafeZones
from toontown.toon import NPCToons

from .DistributedCogdoElevatorIntAI import DistributedCogdoElevatorIntAI

from toontown.cogdominium import CogdoBarrelRoomConsts
from toontown.cogdominium import CogdoBarrelRoomAI

from .DistCogdoBoardroomGameAI import DistCogdoBoardroomGameAI

from toontown.cogdominium.DistCogdoCraneGameAI import DistCogdoCraneGameAI
from toontown.cogdominium.DistCogdoMazeGameAI import DistCogdoMazeGameAI
from toontown.cogdominium.DistCogdoFlyingGameAI import DistCogdoFlyingGameAI
from toontown.cogdominium import CogdoGameConsts

CogdoGames = {
    "boardroom" : DistCogdoBoardroomGameAI,
    "crane" : DistCogdoCraneGameAI,
    "maze" : DistCogdoMazeGameAI,
    "flying" : DistCogdoFlyingGameAI,
    }

IntGames = set([
    "boardroom",
    "crane",
    "flying",
    "defense",
    ])

simbase.forcedCogdoGame = ConfigVariableString('cogdo-game', '').getValue()

GameRequests = {}

class DistributedCogdoInteriorAI(DistributedObjectAI.DistributedObjectAI):
    """
    DistributedCogdoInteriorAI class:
    """

    if __debug__:
        notify = DirectNotifyGlobal.directNotify.newCategory(
                                                'DistributedCogdoInteriorAI')

    def __init__(self, air, elevator):
        self.air = air
        DistributedObjectAI.DistributedObjectAI.__init__(self, air)
        self.extZoneId, self.zoneId = elevator.bldg.getExteriorAndInteriorZoneId()
        self._numFloors = elevator.bldg.planner.numFloors
        self.layout = elevator.bldg._cogdoLayout
        assert(len(elevator.seats) == 4)

        self.avatarExitEvents = []
        self.toons = []
        self.toonSkillPtsGained = {}
        self.toonExp = {}
        self.toonOrigQuests = {}
        self.toonItems = {}
        self.toonOrigMerits = {}
        self.toonMerits = {}
        self.toonParts = {}
        self.helpfulToons = []
        self.shopOwnerNpcId = 0

        npcDesc = NPCToons.zone2NpcDict.get(self.zoneId)
        if npcDesc:
            self.shopOwnerNpcId = npcDesc[0]

        if not self.shopOwnerNpcId:
            self.notify.warning('No npcs found for current cogdo building')

        self.currentFloor = 0
        self.bldg = elevator.bldg
        self.elevator = elevator

        self._game = None

        self._CogdoGameRepeat = ConfigVariableBool('cogdo-game-repeat', 0).getValue()

        self.suits = []
        self.activeSuits = []
        self.reserveSuits = []
        self.joinedReserves = []
        self.suitsKilled = []
        self.suitsKilledPerFloor = []
        self.battle = None

        self.timer = Timer.Timer()

        self._wantBarrelRoom = ConfigVariableBool('cogdo-want-barrel-room', 0).getValue()
        self.barrelRoom = None

        self.responses = {}
        self.ignoreResponses = 0
        self.ignoreElevatorDone = 0
        self.ignoreReserveJoinDone = 0

        # Register all the toons
        self.toonIds = copy.copy(elevator.seats)
        for toonId in self.toonIds:
            if (toonId != None):
                self.__addToon(toonId)
        assert(len(self.toons) > 0)

        # Build a map of id:(name, style) pairs to have around for the
        # end in case the toons are successful.  These elements are
        # filled in as each toon registers with the building.
        self.savedByMap = {}

        self.fsm = ClassicFSM.ClassicFSM(
            'DistributedCogdoInteriorAI',
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
                         ['Resting', 'Failed', 'BattleIntro', 'Off']),
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
             State.State('BattleIntro',
                         self.enterBattleIntro,
                         self.exitBattleIntro,
                         ['Battle', 'ReservesJoining', 'Off']),
             State.State('Battle',
                         self.enterBattle,
                         self.exitBattle,
                         ['ReservesJoining',
                          'BattleDone',
                          'Off']),
             State.State('ReservesJoining',
                         self.enterReservesJoining,
                         self.exitReservesJoining,
                         ['Battle',
                          'Off']),
             State.State('BattleDone',
                         self.enterBattleDone,
                         self.exitBattleDone,
                         ['Resting',
                          'Reward',
                          'Off']),
             State.State('Resting',
                         self.enterResting,
                         self.exitResting,
                         ['Elevator',
                          'Off']),
             State.State('Reward',
                         self.enterReward,
                         self.exitReward,
                         ['Off']),
            State.State('Failed', self.enterFailed, self.exitFailed, [
                'Off']),
             State.State('Off',
                         self.enterOff,
                         self.exitOff,
                         ['WaitForAllToonsInside'])],
            # Initial state
            'Off',
            # Final state
            'Off',
            onUndefTransition = ClassicFSM.ClassicFSM.ALLOW)
        self.fsm.enterInitialState()
        safeZone = ZoneUtil.getCanonicalHoodId(self.extZoneId)
        difficulty = SafeZones.index(safeZone)
        self.SOSCard = self.chooseSOSCard(difficulty)

    def generateWithRequired(self, zoneId):
        self._disCleanupTask = None
        self._sadCleanupTask = None
        DistributedObjectAI.DistributedObjectAI.generateWithRequired(self, zoneId)

    def delete(self):
        assert(self.notify.debug('delete()'))
        self.ignoreAll()
        self.toons = []
        self.toonIds = []
        self.fsm.requestFinalState()
        del self.fsm
        del self.bldg
        del self.elevator
        self.timer.stop()
        del self.timer
        self._cogdoLayout = None
        self.__cleanupFloorBattle()
        if self.barrelRoom:
            self.barrelRoom.destroy()
            self.barrelRoom = None

        taskName = self.taskName('deleteInterior')
        taskMgr.remove(taskName)
        if self._disCleanupTask:
            taskMgr.remove(self._disCleanupTask)

        if self._sadCleanupTask:
            taskMgr.remove(self._sadCleanupTask)

        DistributedObjectAI.DistributedObjectAI.delete(self)

    def requestDelete(self):
        if self._game:
            self._game.requestDelete()
        DistributedObjectAI.DistributedObjectAI.requestDelete(self)

    def getShopOwnerNpcId(self):
        return self.shopOwnerNpcId

    def getSOSNpcId(self):
        return self.SOSCard

    def __handleUnexpectedExit(self, toonId):
        self.notify.warning('toon: %d exited unexpectedly' % toonId)
        self.__removeToon(toonId)
        if self._game:
            self._game.handleToonDisconnected(toonId)
        if (len(self.toons) == 0):
            assert(self.notify.debug('last toon is gone!'))
            self.timer.stop()
            # The last toon exited unexpectedly - if we're in a battle, let
            # the battle clean up first, if we're in Resting state, let
            # the interior elevator clean up first, otherwise, just
            # reset the suit interior.
            if (self.fsm.getCurrentState().getName() == 'Resting'):
                pass
            elif (self.battle == None):
                self.fsm.requestFinalState()
                self._disCleanupTask = taskMgr.doMethodLater(20, self._cleanupAfterLastToonWentDis, self.uniqueName('discleanup'))

    def _cleanupAfterLastToonWentDis(self, task):
        self._disCleanupTask = None
        self.bldg.deleteCogdoInterior()
        return task.done

    def _handleToonWentSad(self, toonId):
        # for the game only, the battle handles this differently
        self.notify.info('toon: %d went sad' % toonId)
        self.__removeToon(toonId)
        toon = self.air.getDo(toonId)
        if toon:
            self.ignore(toon.getGoneSadMessage())
        if self._game:
            self._game.handleToonWentSad(toonId)
        if (len(self.toons) == 0):
            assert(self.notify.debug('last toon is gone!'))
            self.timer.stop()
            # The last toon exited unexpectedly - if we're in a battle, let
            # the battle clean up first, if we're in Resting state, let
            # the interior elevator clean up first, otherwise, just
            # reset the suit interior.
            if (self.fsm.getCurrentState().getName() == 'Resting'):
                pass
            elif (self.battle == None):
                # give the last client out time to play out the sad animation sequence
                self._sadCleanupTask = taskMgr.doMethodLater(
                    20, self._cleanupAfterLastToonWentSad, self.uniqueName('sadcleanup'))

    def _cleanupAfterLastToonWentSad(self, task):
        self._sadCleanupTask = None
        self.bldg.deleteCogdoInterior()
        return task.done

    def __addToon(self, toonId):
        assert(self.notify.debug('addToon(%d)' % toonId))
        if (toonId not in self.air.doId2do):
            self.notify.warning('addToon() - no toon for doId: %d' % toonId)
            return

        # Handle unexpected exits for the toon
        event = self.air.getAvatarExitEvent(toonId)
        self.avatarExitEvents.append(event)
        self.accept(event, self.__handleUnexpectedExit, extraArgs=[toonId])

        self.toons.append(toonId)
        assert(toonId not in self.responses)
        self.responses[toonId] = 0

    def __removeToon(self, toonId):
        assert(self.notify.debug('removeToon(%d)' % toonId))

        if self.toons.count(toonId):
            self.toons.remove(toonId)

        if self.toonIds.count(toonId):
            self.toonIds[self.toonIds.index(toonId)] = None

        if toonId in self.responses:
            del self.responses[toonId]

        # Ignore future exit events for the toon
        event = self.air.getAvatarExitEvent(toonId)
        if self.avatarExitEvents.count(event):
            self.avatarExitEvents.remove(event)
        self.ignore(event)

    def __resetResponses(self):
        self.responses = {}
        for toon in self.toons:
            self.responses[toon] = 0
        self.ignoreResponses = 0

    def __allToonsResponded(self):
        for toon in self.toons:
            assert(toon in self.responses)
            if (self.responses[toon] == 0):
                return 0
        self.ignoreResponses = 1
        return 1

    # Distributed Messages

    # setZoneIdAndBlock

    def getZoneId(self):
        assert(self.notify.debug('network:getZoneId()'))
        return self.zoneId

    def getExtZoneId(self):
        return self.extZoneId

    def getDistBldgDoId(self):
        return self.bldg.getDoId()

    def getNumFloors(self):
        return self._numFloors

    # setToons()

    def d_setToons(self):
        assert(self.notify.debug('network:setToons()'))
        self.sendUpdate('setToons', self.getToons())

    def getToons(self):
        sendIds = []
        for toonId in self.toonIds:
            if (toonId == None):
                sendIds.append(0)
            else:
                sendIds.append(toonId)
        assert(self.notify.debug('getToons(): %s' % sendIds))
        return [sendIds, 0]

    # setSuits()
    def getDroneCogDNA(self):
        dna = SuitDNA()
        dna.newSuitRandom(level = 2)
        return dna

    def d_setSuits(self):
        assert(self.notify.debug('network:setSuits()'))
        self.sendUpdate('setSuits', self.getSuits())

    def getSuits(self):
        suitIds = []
        for suit in self.activeSuits:
            suitIds.append(suit.doId)
        reserveIds = []
        values = []
        for info in self.reserveSuits:
            reserveIds.append(info[0].doId)
            values.append(info[1])
        return [suitIds, reserveIds, values]

    # setState()

    def b_setState(self, state):
        self.d_setState(state)
        self.setState(state)

    def d_setState(self, state):
        assert(self.notify.debug('network:setState(%s)' % state))
        stime = globalClock.getRealTime() + BattleBase.SERVER_BUFFER_TIME
        self.sendUpdate('setState', [state, globalClockDelta.localToNetworkTime(stime)])

    def setState(self, state):
        self.fsm.request(state)

    def getState(self):
        return [self.fsm.getCurrentState().getName(),
               globalClockDelta.getRealNetworkTime()]

    ##### Messages from the clients #####

    def setAvatarJoined(self):
        """setAvatarJoined(self)
        This message is sent from a client toon to indicate that it
        has finished loading the interior.
        """
        avId = self.air.getAvatarIdFromSender()
        if (self.toons.count(avId) == 0):
            self.air.writeServerEvent('suspicious', avId, 'DistributedCogdoInteriorAI.setAvatarJoined from toon not in %s.' % (self.toons))
            self.notify.warning('setAvatarJoined() - av: %d not in list' % \
                avId)
            return
        if self.fsm.getCurrentState().getName() != 'WaitForAllToonsInside':
            self.air.writeServerEvent('suspicious', avId, 'CogdoInteriorAI.setAvatarJoined: not in wait state')
            return
        avatar = self.air.doId2do.get(avId)
        if avatar == None:
            self.air.writeServerEvent('suspicious', avId, 'CogdoInteriorAI.setAvatarJoined: avatar not present')
            return
        else:
            self.savedByMap[avId] = (avatar.getName(), avatar.dna.asTuple())

        if avId not in self.responses:
            self.air.writeServerEvent('suspicious', avId, 'CogdoInteriorAI.setAvatarJoined: avId not in responses')
            self.notify.warning('CogdoInteriorAI.setAvatarJoined: avId not in responses')
            return
        if self.responses[avId] > 0:
            self.air.writeServerEvent('suspicious', avId, 'CogdoInteriorAI.setAvatarJoined: av already responded')
            return
        assert(avId in self.responses)
        self.responses[avId] += 1
        assert(self.notify.debug('toon: %d in suit interior' % avId))
        if (self.__allToonsResponded()):
            self.fsm.request('Elevator')

    def elevatorDone(self):
        """elevatorDone(self)
        This message is sent from a client toon to indicate that it has
        finished viewing the elevator movie.
        """
        toonId = self.air.getAvatarIdFromSender()
        if (self.ignoreResponses == 1):
            assert(self.notify.debug('elevatorDone() ignoring toon: %d' % \
                toonId))
            return
#        elif (self.fsm.getCurrentState().getName() != 'Elevator'):
#            self.notify.warning('elevatorDone() - in state: %s' % \
#                self.fsm.getCurrentState().getName())
#            return
        elif (self.toons.count(toonId) == 0):
            self.air.writeServerEvent('suspicious', toonId, 'CogdoInteriorAI.elevatorDone: toon not in participant list')
            self.notify.warning('elevatorDone() - toon not in toon list: %d' \
                % toonId)
            assert(self.notify.debug('toons: %s toonIds: %s' % \
                        (self.toons, self.toonIds)))
            return
        if self.fsm.getCurrentState().getName() != 'Elevator':
            self.air.writeServerEvent('suspicious', toonId, 'CogdoInteriorAI.elevatorDone: not in Elevator state')
            return
        if toonId not in self.responses:
            self.air.writeServerEvent('suspicious', toonId, 'CogdoInteriorAI.elevatorDone: toon not in responses')
            self.notify.warning('CogdoInteriorAI.elevatorDone: avId not in responses')
            return
        assert(toonId in self.responses)
        self.responses[toonId] += 1
        assert(self.notify.debug('toon: %d done with elevator' % toonId))
        if (self.__allToonsResponded() and
            self.ignoreElevatorDone == 0):
            self.b_setState('Game')

    def reserveJoinDone(self):
        """reserveJoinDone(self)
        This message is sent from a client toon to indicate that it has
        finished viewing the ReservesJoining movie.
        """
        toonId = self.air.getAvatarIdFromSender()
        if (self.ignoreResponses == 1):
            assert(self.notify.debug('reserveJoinDone() ignoring toon: %d' % \
                toonId))
            return
#        elif (self.fsm.getCurrentState().getName() != 'ReservesJoining'):
#            self.notify.warning('reserveJoinDone() - in state: %s' % \
#                self.fsm.getCurrentState().getName())
#            return
        elif (self.toons.count(toonId) == 0):
            self.air.writeServerEvent('suspicious', toonId, 'CogdoInteriorAI.reserveJoinDone: toon not in participant list')
            self.notify.warning('reserveJoinDone() - toon not in list: %d' \
                % toonId)
            assert(self.notify.debug('toons: %s toonIds: %s' % \
                        (self.toons, self.toonIds)))
            return
        if self.fsm.getCurrentState().getName() != 'ReservesJoining':
            self.air.writeServerEvent('suspicious', toonId, 'CogdoInteriorAI.reserveJoinDone: not in ReservesJoining state')
            return
        if toonId not in self.responses:
            self.air.writeServerEvent('suspicious', toonId, 'CogdoInteriorAI.reserveJoinDone: toon not in responses')
            self.notify.warning('CogdoInteriorAI.reserveJoinDone: avId not in responses')
            return
        assert(toonId in self.responses)
        self.responses[toonId] += 1
        assert(self.notify.debug('toon: %d done with joining reserves' % \
                                toonId))
        if (self.__allToonsResponded() and
            self.ignoreReserveJoinDone == 0):
            self.b_setState('Battle')

    def isBossFloor(self, floorNum):
        if self.layout.hasBossBattle():
            if self.layout.getBossBattleFloor() == floorNum:
                return True
        return False

    def isTopFloor(self, floorNum):
        return (self.layout.getNumFloors()-1) == floorNum

    # Specific State Functions

    ##### Off state #####

    def enterOff(self):
        assert(self.notify.debug('enterOff()'))
        return None

    def exitOff(self):
        return None

    ##### WaitForAllToonsInside state #####

    def enterWaitForAllToonsInside(self):
        assert(self.notify.debug('enterWaitForAllToonsInside()'))
        self.__resetResponses()
        return None

    def exitWaitForAllToonsInside(self):
        self.__resetResponses()
        return None

    ##### Elevator state #####

    def enterElevator(self):
        assert(self.notify.debug('enterElevator()'))

        if self.isBossFloor(self.currentFloor):
            self._populateFloorSuits()
        else:
            self.d_setToons()

        self.__resetResponses()
        if self._wantBarrelRoom:
            if self.barrelRoom:
                self.barrelRoom.reset()
            else:
                self.barrelRoom = CogdoBarrelRoomAI.CogdoBarrelRoomAI(self)

        # create the game here so the players see something when the doors open
        self._game = self._createGame()
        if self._game:
            self._game.makeVisible()

        self.d_setState('Elevator')

        self.timer.startCallback(BattleBase.ELEVATOR_T + \
                       ElevatorData[ELEVATOR_NORMAL]['openTime'] + \
                       BattleBase.SERVER_BUFFER_TIME, self.__serverElevatorDone)
        return None

    def _createGame(self):
        game = None
        if not self.isBossFloor(self.currentFloor):
            for toonId in self.toonIds:
                if toonId:
                    toon = self.air.getDo(toonId)
                    if toon:
                        self.accept(toon.getGoneSadMessage(), Functor(self._handleToonWentSad, toonId))

            forcedGame = simbase.forcedCogdoGame
            diff = None
            pgId = None
            for toonId in self.toonIds:
                if toonId:
                    if toonId in GameRequests:
                        (forcedGame, keep, diff, pgId) = GameRequests[toonId]
                        if not keep:
                            GameRequests.pop(toonId)

            if forcedGame:
                gameCtor = CogdoGames[forcedGame]
            else:
                name = None
                while name is None or name in IntGames:
                    name = random.choice(list(CogdoGames.keys()))
                gameCtor = CogdoGames[name]
            game = gameCtor(self.air, self)
            game.setExteriorZone(self.extZoneId)
            game.setDifficultyOverrides(diff, pgId)
            game.generateWithRequired(self.zoneId)
        return game

    def __serverElevatorDone(self):
        assert(self.notify.debug('serverElevatorDone()'))
        self.ignoreElevatorDone = 1
        self.b_setState('Game')

    def exitElevator(self):
        self.timer.stop()
        self.__resetResponses()
        return None

    ##### Game state #####

    def enterGame(self):
        assert(self.notify.debug('enterGame()'))

        self.notify.info('Entering Maze Game')
        self._gameScore = None
        self._rewardedLaff = {}
        self._penaltyLaff = {}
        self.d_setState('Game')
        self.elevator.d_setFloor(self.currentFloor)

        # no game on the top floor, breeze on through
        if self._game:
            self._game.start()
        else:
            self._gameDone()

    def _populateFloorSuits(self):
        # Create the suits and place them in their initial positions on
        # the floor
        assert(self.currentFloor < self.layout.getNumFloors())
        suitHandles = self.bldg.planner.genFloorSuits(self.currentFloor)
        self.suits = suitHandles['activeSuits']
        assert(len(self.suits) > 0)
        self.activeSuits = []
        for suit in self.suits:
            self.activeSuits.append(suit)
        self.reserveSuits = suitHandles['reserveSuits']

        self.d_setToons()
        # do this before setting state to 'battle' otherwise client show will get messed up
        self.d_setSuits()

    def _setGameScore(self, score):
        self._gameScore = score

    def getGameScore(self):
        return self._gameScore

    def _gameDone(self):
        self.__calcLaff()
        for (toonId, reward) in list(self._rewardedLaff.items()):
            if reward:
                av = self.air.doId2do.get(toonId)
                av.toonUp(reward)

        for (toonId, penalty) in list(self._penaltyLaff.items()):
            if penalty:
                av = self.air.doId2do.get(toonId)
                if ConfigVariableBool('want-cogdo-maze-no-sad', 1).getValue():
                    avHp = av.getHp()
                    if avHp < 1:
                        avHp = 1

                    if penalty >= avHp:
                        penalty = avHp - 1

                if penalty:
                    av.takeDamage(penalty, quietly = 0)

        if self._game and self._game.wasEnded():
            self.b_setState('Resting')
        elif self._game and self._game.isDoorOpen():
            self.b_setState('Resting')
        elif self._game and not self._game.isDoorOpen():
            self.b_setState('Failed')
        else:
            self.b_setState('BattleIntro')

    def exitGame(self):
        self.sendUpdate('setSOSNpcId', [
            self.SOSCard])
        self.sendUpdate('setFOType', [
            ord(self.bldg.track)])

    def __calcLaff(self):
        self.notify.debug('__calcLaff()')
        self._rewardedLaff = {}
        self._penaltyLaff = {}
        if self._game:
            score = self.getGameScore()
            if score:
                maxToAward = self._game.getDifficulty() * CogdoGameConsts.LaffRewardRange + CogdoGameConsts.LaffRewardMin
                reward = score * maxToAward
                for toonId in self.toons:
                    if self._game.isToonInDoor(toonId):
                        self._rewardedLaff[toonId] = reward

                if self._rewardedLaff:
                    self.air.writeServerEvent('CogdoLaffReward', list(self._rewardedLaff.keys()), 'Awarded %s Laff for difficulty %s and score %s' % (reward, self._game.getDifficulty(), score))

            penalty = self._game.getDifficulty() * CogdoGameConsts.LaffPenalty
            for toonId in self.toons:
                if not self._game.isToonInDoor(toonId):
                    self._penaltyLaff[toonId] = penalty

            if self._penaltyLaff:
                self.air.writeServerEvent('CogdoLaffPenalty', list(self._penaltyLaff.keys()), 'Penalized %s Laff for difficulty %s (did not reach exit)' % (penalty, self._game.getDifficulty()))

    def toonBarrelRoomIntroDone(self):
        avId = self.air.getAvatarIdFromSender()
        if self.fsm.getCurrentState().getName() != 'BarrelRoomIntro':
            self.air.writeServerEvent('suspicious', avId, 'CogdoInteriorAI.toonBarrelRoomIntroDone: not in BarrelRoomIntro state')
            return

        if avId not in self.responses:
            self.air.writeServerEvent('suspicious', avId, 'CogdoInteriorAI.toonBarrelRoomIntroDone: unknown avId')
            return

        if hasattr(self, 'brBarrier'):
            self.brBarrier.clear(avId)
        else:
            self.notify.warning('toonBarrelRoomIntroDone from %s in invalid state' % avId)

    def __brIntroDone(self, clearedAvIds = []):
        self.b_setState('CollectBarrels')

    def enterBarrelRoomIntro(self):
        if not self._wantBarrelRoom:
            pass
        if self._wantBarrelRoom and not self.isBossFloor(self.currentFloor):
            self.barrelRoom.setScore(1.0)
            self.brBarrier = ToonBarrier.ToonBarrier('waitBrIntroDone', self.uniqueName('waitBrIntroDone'), self.toons, CogdoBarrelRoomConsts.BarrelRoomIntroTimeout, doneFunc = self.__brIntroDone)
        else:
            self.__brIntroDone()

    def exitBarrelRoomIntro(self):
        if hasattr(self, 'brBarrier'):
            self.brBarrier.cleanup()
            del self.brBarrier

    def __endCollectBarrels(self):
        if len(self.toons) > 0:
            self.notify.info('%d toons in barrel room.' % len(self.toons))
            self.b_setState('BarrelRoomReward')
        else:
            self.notify.warning('0 toons in barrel room.')
            self.bldg.deleteCogdoInterior()

    def toonLeftBarrelRoom(self):
        avId = self.air.getAvatarIdFromSender()
        self.notify.info('avId=%s left the barrel room via teleport' % avId)
        if self.fsm.getCurrentState().getName() != 'CollectBarrels':
            self.air.writeServerEvent('suspicious', avId, 'CogdoInteriorAI.toonLeftBarrelRoom called outside of CollectBarrels state')
            return

        if avId not in self.responses:
            self.air.writeServerEvent('suspicious', avId, 'CogdoInteriorAI.toonLeftBarrelRoom: unknown avId')
            return

        self.__removeToon(avId)
        self.notify.info('%d toon(s) remaining in barrel room.' % len(self.toons))
        if len(self.toons) == 0:
            # all toons went sad but game is still running so that the game doesn't disappear
            # on the player's client as he watches sad animation. ignore this event
            self.notify.warning('0 toons in barrel room.')
            self.bldg.deleteCogdoInterior()

    def enterCollectBarrels(self):
        if self._wantBarrelRoom and not self.isBossFloor(self.currentFloor):
            self.acceptOnce(self.barrelRoom.collectionDoneEvent, self.__endCollectBarrels)
            self.barrelRoom.activate()
        else:
            self.__endCollectBarrels()

    def exitCollectBarrels(self):
        if self.barrelRoom:
            self.ignore(self.barrelRoom.collectionDoneEvent)
            self.barrelRoom.deactivate()

    def toonBarrelRoomRewardDone(self):
        avId = self.air.getAvatarIdFromSender()
        if self.fsm.getCurrentState().getName() != 'BarrelRoomReward':
            self.air.writeServerEvent('suspicious', avId, 'CogdoInteriorAI.toonBarrelRoomIntroDone: not in BarrelRoomReward state')
            return

        if avId not in self.responses:
            self.air.writeServerEvent('suspicious', avId, 'CogdoInteriorAI.toonBarrelRoomRewardDone: unknown avId')
            return

        if hasattr(self, 'brBarrier'):
            self.brBarrier.clear(avId)
        else:
            self.notify.warning('toonBarrelRoomRewardDone from %s in invalid state' % avId)

    def __brRewardDone(self, clearedAvIds = []):
        if len(self.toons) > 0:
            if not self.isBossFloor(self.currentFloor):
                self._populateFloorSuits()
                self.b_setState('Battle')
            else:
                self.b_setState('BattleIntro')
        else:
            self.notify.warning('0 toons in barrel room.')
            self.bldg.deleteCogdoInterior()

    def enterBarrelRoomReward(self):
        if self._wantBarrelRoom and not self.isBossFloor(self.currentFloor):
            self.sendUpdate('setBarrelRoomReward', self.barrelRoom.results)
            self.brBarrier = ToonBarrier.ToonBarrier(
                'waitBrRewardDone',
                self.uniqueName('waitBrRewardDone'),
                self.toons, CogdoBarrelRoomConsts.RewardUiTime + 5.0,
                doneFunc = self.__brRewardDone)
        else:
            self.__brRewardDone()

    def exitBarrelRoomReward(self):
        if hasattr(self, 'brBarrier'):
            self.brBarrier.cleanup()
            del self.brBarrier

    ##### Battle state #####

    def __createFloorBattle(self):
        assert(len(self.toons) > 0)
        if self.isBossFloor(self.currentFloor):
            assert(self.notify.debug('createFloorBattle() - boss battle'))
            self.notify.info('%d toon(s) in boss battle' % len(self.toons))
            bossBattle = 1
        else:
            self.notify.info('%d toon(s) in barrel battle' % len(self.toons))
            bossBattle = 0
        # Create the battle for the floor
        self.battle = DistributedCogdoBattleBldgAI.DistributedCogdoBattleBldgAI(
            self.air, self.zoneId,
            self.__handleRoundDone, self.__handleBattleDone,
            bossBattle=bossBattle)

        # We store the lists of experience gained and suits killed in
        # the DistributedCogdoInterior object, and share these pointers
        # in all battles created for this building.  This way, each
        # battle will actually be modifying the same objects, these,
        # and will thus accumulate the experience from previous
        # battles.
        self.battle.suitsKilled = self.suitsKilled
        self.battle.suitsKilledPerFloor = self.suitsKilledPerFloor
        self.battle.battleCalc.toonSkillPtsGained = self.toonSkillPtsGained
        self.battle.toonExp = self.toonExp
        self.battle.toonOrigQuests = self.toonOrigQuests
        self.battle.toonItems = self.toonItems
        self.battle.toonOrigMerits = self.toonOrigMerits
        self.battle.toonMerits = self.toonMerits
        self.battle.toonParts = self.toonParts
        self.battle.helpfulToons = self.helpfulToons

        # We must set the members of a building battle before we
        # generate it.
        self.battle.setInitialMembers(self.toons, self.suits)
        self.battle.generateWithRequired(self.zoneId)

        # We get a bonus factor applied toward each attack's experience credit.
        mult = getCreditMultiplier(self.currentFloor)

        # If there is an invasion, multiply the exp for the duration of this battle
        # Now, if the invasion ends midway through this battle, the players will
        # continue getting credit. This is ok I guess.
        if self.air.suitInvasionManager.getInvading():
            mult *= getInvasionMultiplier()

        self.battle.battleCalc.setSkillCreditMultiplier(mult)

    def __cleanupFloorBattle(self):
        for suit in self.suits:
            self.notify.debug('cleaning up floor suit: %d' % suit.doId)
            if suit.isDeleted():
                self.notify.debug('whoops, suit %d is deleted.' % suit.doId)
            else:
                suit.requestDelete()
        self.suits = []
        self.reserveSuits = []
        self.activeSuits = []
        if (self.battle != None):
            self.battle.requestDelete()
        self.battle = None

    def __handleRoundDone(self, toonIds, totalHp, deadSuits):
        # Determine if any reserves need to join
        assert(self.notify.debug('handleRoundDone() - hp: %d' % totalHp))
        # Calculate the total max HP for all the suits currently on the floor
        totalMaxHp = 0
        for suit in self.suits:
            totalMaxHp += suit.maxHP

        for suit in deadSuits:
            self.activeSuits.remove(suit)

        # Determine if any reserve suits need to join
        if (len(self.reserveSuits) > 0 and len(self.activeSuits) < 4):
            assert(self.notify.debug('potential reserve suits: %d' % \
                len(self.reserveSuits)))
            self.joinedReserves = []
            assert(totalHp <= totalMaxHp)
            hpPercent = 100 - (totalHp / totalMaxHp * 100.0)
            assert(self.notify.debug('totalHp: %d totalMaxHp: %d percent: %f' \
                % (totalHp, totalMaxHp, hpPercent)))
            for info in self.reserveSuits:
                if (info[1] <= hpPercent and
                    len(self.activeSuits) < 4):
                    assert(self.notify.debug('reserve: %d joining percent: %f' \
                        % (info[0].doId, info[1])))
                    self.suits.append(info[0])
                    self.activeSuits.append(info[0])
                    self.joinedReserves.append(info)
            for info in self.joinedReserves:
                self.reserveSuits.remove(info)
            if (len(self.joinedReserves) > 0):
                # setSuits() triggers the state change on the client
                self.fsm.request('ReservesJoining')
                self.d_setSuits()
                return

        # See if the battle is done
        if (len(self.activeSuits) == 0):
            self.fsm.request('BattleDone', [toonIds])
        else:
            # No reserve suits to join - tell the battle to continue
            self.battle.resume()

    def __handleBattleDone(self, zoneId, toonIds):
        assert(self.notify.debug('%s.handleBattleDone(%s, %s)' % (self.doId, zoneId, toonIds)))
        #self.fsm.request('BattleDone', [toonIds])
        if (len(toonIds) == 0):
            self.notify.info('handleBattleDone() - last toon gone')

            # Rather than shutting down immediately, we give the last
            # toon a few seconds to finish playing his teleport-out
            # animation before the world goes away.

            taskName = self.taskName('deleteInterior')
            taskMgr.doMethodLater(10, self.__doDeleteInterior, taskName)

        elif self.isTopFloor(self.currentFloor):
            # This is not b_setState, because enterReward has to do
            # some things before the broadcast takes place. enterReward
            # will call d_setState when it is ready.
            self.setState('Reward')
        else:
            self.b_setState('Resting')

    def __doDeleteInterior(self, task):
        self.bldg.deleteCogdoInterior()

    def enterBattleIntro(self):
        timeLeft = 7.0
        self._battleIntroTaskName = self.taskName('BattleIntro')
        taskMgr.doMethodLater(timeLeft, self._battleIntroDone, self._battleIntroTaskName)

    def _battleIntroDone(self, task):
        self.b_setState('Battle')
        return task.done

    def exitBattleIntro(self):
        taskMgr.remove(self._battleIntroTaskName)
        self._battleIntroTaskName = None

    def enterBattle(self):
        assert(self.notify.debug('enterBattle()'))

        if (self.battle == None):
            self.__createFloorBattle()

    def exitBattle(self):
        return None

    ##### ReservesJoining state #####

    def enterReservesJoining(self):
        assert(self.notify.debug('enterReservesJoining()'))
        self.__resetResponses()
        self.timer.startCallback(
            ElevatorData[ELEVATOR_NORMAL]['openTime'] + \
            SUIT_HOLD_ELEVATOR_TIME + \
            BattleBase.SERVER_BUFFER_TIME,
            self.__serverReserveJoinDone)
        return None

    def __serverReserveJoinDone(self):
        """__serverReserveJoinDone()
        This callback is made only if some of the toons don't send
        their reserveJoinDone() message in a reasonable time--rather
        than waiting for everyone, we simply carry on without them.
        """
        assert(self.notify.debug('serverReserveJoinDone()'))
        self.ignoreReserveJoinDone = 1
        self.b_setState('Battle')

    def exitReservesJoining(self):
        self.timer.stop()
        self.__resetResponses()
        # Join the suits to the battle and tell it to resume
        for info in self.joinedReserves:
            self.battle.suitRequestJoin(info[0])
        self.battle.resume()
        self.joinedReserves = []
        return None

    ##### BattleDone state #####

    def enterBattleDone(self, toonIds):
        assert(self.notify.debug('enterBattleDone()'))
        # Find out if any toons are gone
        if (len(toonIds) != len(self.toons)):
            deadToons = []
            for toon in self.toons:
                if (toonIds.count(toon) == 0):
                    deadToons.append(toon)
            for toon in deadToons:
                self.__removeToon(toon)
        self.d_setToons()

        if (len(self.toons) == 0):
            self.bldg.deleteCogdoInterior()
        elif self.isTopFloor(self.currentFloor):
            self.notify.info('%d Toon(s) beat the executive suite building' % len(self.toons))
            self.battle.resume(self.currentFloor, topFloor = 1)
        else:
 #           if self.isTopFloor(self.currentFloor):
 #               # Toons beat the building
 #               self.battle.resume(self.currentFloor, topFloor=1)
 #           else:
            # The building isn't finished yet - gather up experience and
            # activate the elevator
            self.battle.resume(self.currentFloor, topFloor=0)
        return None

    def exitBattleDone(self):
        self.__cleanupFloorBattle()
        self.d_setSuits()
        return None

    ##### Resting state #####

    def __handleEnterElevator(self):
        self.fsm.request('Elevator')

    def enterResting(self):
        assert(self.notify.debug('enterResting()'))
        if self._game:
            self._game.requestDelete()
            self._game = None
            for toonId in self.toonIds:
                if toonId:
                    toon = self.air.getDo(toonId)
                    if toon:
                        self.ignore(toon.getGoneSadMessage())

        self.handleAllAboard()

    def handleAllAboard(self, seats = None):
        if seats == None:
            seats = copy.copy(self.toonIds)
        if not hasattr(self, "fsm"):
            # If we've already been cleaned up, never mind.
            return None

        assert(self.fsm.getCurrentState().getName() == "Resting")
        assert(self.notify.debug('handleAllAboard() - toons: %s' % self.toons))

        # Make sure the number of empty seats is correct. If it is empty,
        # reset and get us out of here.
        numOfEmptySeats = seats.count(None)
        if (numOfEmptySeats == 4):
            self.bldg.deleteCogdoInterior()
            return None
        elif (numOfEmptySeats >= 0) and (numOfEmptySeats <=3):
            pass
        else:
            self.error("Bad number of empty seats: %s" % numOfEmptySeats)

        for toon in self.toons:
            if seats.count(toon) == 0:
                self.__removeToon(toon)
        self.toonIds = copy.copy(seats)
        self.toons = []
        for toonId in self.toonIds:
            if (toonId != None):
                self.toons.append(toonId)

        self.d_setToons()

        if not self._CogdoGameRepeat:
            # Increment the floor number
            self.currentFloor += 1
        self.fsm.request('Elevator')

    def exitResting(self):
#        self.intElevator.requestDelete()
#        del self.intElevator
        return None

    ##### Reward state #####

    def enterReward(self):
        assert(self.notify.debug('enterReward()'))
        # Tell the building to get ready for the victors to come outside.

        # We pass in a *copy* of the toonIds list, not the list
        # itself, so that when we pull toons out of our list (for
        # instance, if they disconnect unexpectedly), it won't affect
        # the building's victor list.
        victors = self.toonIds[:]

        # Build a new savedBy list that includes only the Toons that
        # made it to the end.
        savedBy = []
        for v in victors:
            tuple = self.savedByMap.get(v)
            if tuple:
                savedBy.append([v, tuple[0], tuple[1]])
                toon = self.air.doId2do.get(v)
                if toon:
                    self.notify.info('Reward State: toonId:%d laff:%d/%d get ready for the victors to come outside' % (toon.doId, toon.hp, toon.maxHp))
                    if not toon.attemptAddNPCFriend(self.SOSCard, numCalls = 1):
                        self.notify.info('%s.unable to add NPCFriend %s to %s.' % (self.doId, self.SOSCard, v))


        # Going to waitForVictors deletes the elevator
        self.bldg.fsm.request("waitForVictorsFromCogdo", [victors, savedBy])
        # Tell the players to go back outside.
        self.d_setState('Reward')
        return None

    def exitReward(self):
        return None

    ##### Failed state #####

    def enterFailed(self):
        victors = self.toonIds[:]
        savedBy = []
        anyVictors = victors.count(None) < 4
        if anyVictors:
            self.bldg.fsm.request('waitForVictorsFromCogdo', [
                victors,
                savedBy])

    def exitFailed(self):
        return None

    def chooseSOSCard(self, difficulty):
        if difficulty < 0 or difficulty > 5:
            return None

        if difficulty <= 1:
            card = random.choice(NPCToons.npcFriendsMinMaxStars(0, 1))
        elif difficulty <= 3:
            card = random.choice(NPCToons.npcFriendsMinMaxStars(1, 1))
        else:
            card = random.choice(NPCToons.npcFriendsMinMaxStars(2, 2))
        return card

    ##### Reset state #####

    #def enterReset(self):
    #    assert(self.notify.debug('enterReset()'))
    #    # Unload all floor and suit models, but keep the suit database -
    #    # the contents of the building should remain the same until the
    #    # toons retake the building
    #    self.__cleanupFloorBattle()
    #    self.currentFloor = 0
    #    # -1 means the lobby.
    #    self.elevator.d_setFloor(-1)
    #    # Get rid of the toons
    #    for toon in copy.copy(self.toons):
    #        self.__removeToon(toon)
    #    self.savedByMap = {}
    #    self.b_setState('Off')
    #    self.elevator.open()
    #    self.requestDelete()

    #def exitReset(self):
    #    return None
