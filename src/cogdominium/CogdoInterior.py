from toontown.toonbase.ToontownModules import ModelPool, TexturePool

from direct.task.Task import Task
from direct.directnotify import DirectNotifyGlobal
from direct.fsm import ClassicFSM, State

from toontown.hood import Place
from toontown.toonbase.ToonBaseGlobal import *
from toontown.town import TownBattle
from toontown.suit import Suit
from toontown.building import Elevator
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import ToontownBattleGlobals

class CogdoInterior(Place.Place):
    """CogdoInterior class"""

    # create a notify category
    notify = DirectNotifyGlobal.directNotify.newCategory("CogdoInterior")

    # special methods

    def __init__(self, loader, parentFSM, doneEvent):
        """
        CogdoInterior constructor: create a play game ClassicFSM
        """
        Place.Place.__init__(self, loader, doneEvent)

        self.fsm = ClassicFSM.ClassicFSM('CogdoInterior',
                           [State.State('entrance',
                                        self.enterEntrance,
                                        self.exitEntrance,
                                        ['Game', 'walk']),
                            State.State('Elevator',
                                        self.enterElevator,
                                        self.exitElevator,
                                        ['Game', 'battle', 'walk', 'crane', ]),
                            State.State('Game',
                                        self.enterGame,
                                        self.exitGame,
                                        ['battle', 'died', 'crane', 'walk', ]),
                            State.State('battle',
                                        self.enterBattle,
                                        self.exitBattle,
                                        ['walk', 'died']),
                            State.State('crane',
                                        self.enterCrane,
                                        self.exitCrane,
                                        ['walk', 'battle', 'finalBattle',
                                        'died', 'ouch', 'squished']),
                            State.State('walk',
                                        self.enterWalk,
                                        self.exitWalk,
                                        ['stickerBook', 'stopped',
                                         'battle', 'sit', 'died',
                                         'teleportOut',
                                         'Elevator',
                                         'crane',
                                         'DFA', 'trialerFA',]),
                            State.State('sit',
                                        self.enterSit,
                                        self.exitSit,
                                        ['walk',]),
                            State.State('stickerBook',
                                        self.enterStickerBook,
                                        self.exitStickerBook,
                                        ['walk', 'stopped', 'sit', 'died',
                                         'DFA', 'trialerFA',
                                         'teleportOut', 'Elevator',]),
                            # Trialer Force Acknowledge:
                            State.State('trialerFA',
                                        self.enterTrialerFA,
                                        self.exitTrialerFA,
                                        ['trialerFAReject', 'DFA']),
                            State.State('trialerFAReject',
                                        self.enterTrialerFAReject,
                                        self.exitTrialerFAReject,
                                        ['walk']),
                            State.State('DFA',
                                        self.enterDFA,
                                        self.exitDFA,
                                        ['DFAReject', 'teleportOut']),
                            State.State('DFAReject',
                                        self.enterDFAReject,
                                        self.exitDFAReject,
                                        ['walk']),
                            State.State('teleportIn',
                                        self.enterTeleportIn,
                                        self.exitTeleportIn,
                                        ['walk']),
                            State.State('teleportOut',
                                        self.enterTeleportOut,
                                        self.exitTeleportOut,
                                        ['teleportIn']),
                            State.State('stopped',
                                        self.enterStopped,
                                        self.exitStopped,
                                        ['walk', 'elevatorOut', 'battle']),
                            State.State('died',
                                        self.enterDied,
                                        self.exitDied,
                                        []),
                            State.State('elevatorOut',
                                        self.enterElevatorOut,
                                        self.exitElevatorOut,
                                        [])],
                           # Initial State
                           'entrance',
                           # Final State
                           'elevatorOut',
                           )
        self.parentFSM = parentFSM
        self.elevatorDoneEvent = "elevatorDoneSI"

        # This is updated each floor by the DistributedCogdoInterior.
        self.currentFloor = 0

    def enter(self, requestStatus):
        assert(self.notify.debug("enter(requestStatus="+str(requestStatus)+")"))
        self.fsm.enterInitialState()
        # Let the safe zone manager know that we are here.
        #messenger.send("enterToonInterior")

        #self.geom.reparentTo(render)

        self.zoneId = requestStatus['zoneId']
        self.accept("DSIDoneEvent", self.handleDSIDoneEvent)

    def exit(self):
        assert(self.notify.debug("exit()"))
        self.ignoreAll()
        # Let the safe zone manager know that we are leaving
        #messenger.send("exitToonInterior")
        #self.geom.reparentTo(hidden)

        # Turn off the little red arrows.
        #NametagGlobals.setMasterArrowsOn(0)

    def load(self):
        assert(self.notify.debug("load()"))
        # Call up the chain
        Place.Place.load(self)
        self.parentFSM.getStateNamed("cogdoInterior").addChild(self.fsm)
        self.townBattle = TownBattle.TownBattle('town-battle-done')
        self.townBattle.load()
        for i in range(1, 3):
            Suit.loadSuits(i)

    def unload(self):
        assert(self.notify.debug("unload()"))
        # Call up the chain
        Place.Place.unload(self)

        self.parentFSM.getStateNamed("cogdoInterior").removeChild(self.fsm)
        del self.parentFSM
        del self.fsm
        #self.geom.removeNode()
        #del self.geom
        self.ignoreAll()
        # Get rid of any references to models or textures from this safe zone
        ModelPool.garbageCollect()
        TexturePool.garbageCollect()
        self.townBattle.unload()
        self.townBattle.cleanup()
        del self.townBattle

        for i in range(1, 3):
            Suit.unloadSuits(i)

    def setState(self, state, battleEvent=None):
        assert(self.notify.debug("setState(state="+str(state)
                +", battleEvent="+str(battleEvent)+")"))
        if (battleEvent):
            self.fsm.request(state, [battleEvent])
        else:
            self.fsm.request(state)

    def getZoneId(self):
        """
        Returns the current zone ID.
        """
        return self.zoneId

    def enterZone(self, zoneId):
        assert(self.notify.debug('enterZone() - %d' % zoneId))
        pass

    def isPeriodTimerEffective(self):
        """
        Returns true if the period timer will be honored if it expires
        in this kind of Place (and we're also in a suitable mode).
        Generally, CogdoInterior returns false, and other kinds of
        Place return true.
        """
        return 0

    def handleDSIDoneEvent(self, requestStatus):
        self.doneStatus = requestStatus
        messenger.send(self.doneEvent)

    def doRequestLeave(self, requestStatus):
        # when it's time to leave, check their trialer status first
        self.fsm.request('trialerFA', [requestStatus])

    # Elevator state

    def enterEntrance(self):
        return

    def exitEntrance(self):
        return

    def enterElevator(self, distElevator):
        assert(self.notify.debug('enterElevator()'))
        self.accept(self.elevatorDoneEvent, self.handleElevatorDone)
        self.elevator = Elevator.Elevator(self.fsm.getStateNamed("Elevator"),
                                          self.elevatorDoneEvent,
                                          distElevator)
        self.elevator.load()
        self.elevator.enter()
        # Disable leave to pay / set parent password
        base.localAvatar.cantLeaveGame = 1
        return

    def exitElevator(self):
        base.localAvatar.cantLeaveGame = 0
        self.ignore(self.elevatorDoneEvent)
        self.elevator.unload()
        self.elevator.exit()
        del self.elevator
        return None

    def detectedElevatorCollision(self, distElevator):
        assert(self.notify.debug("detectedElevatorCollision()"))
        self.fsm.request("Elevator", [distElevator])
        return None

    def handleElevatorDone(self, doneStatus):
        assert(self.notify.debug("handleElevatorDone()"))
        self.notify.debug("handling elevator done event")
        where = doneStatus['where']
        if (where == 'reject'):
            # If there has been a reject the Elevator should show an
            # elevatorNotifier message and put the toon in the stopped state.
            # Don't request the walk state here. Let the the toon be stuck in the
            # stopped state till the player removes that message from his screen.
            # Removing the message will automatically put him in the walk state there.
            # Put the player in the walk state only if there is no elevator message.
            if hasattr(base.localAvatar, "elevatorNotifier") and base.localAvatar.elevatorNotifier.isNotifierOpen():
                pass
            else:
                self.fsm.request("walk")
        elif (where == 'exit'):
            self.fsm.request("walk")
        elif (where == 'cogdoInterior'):
            pass
        else:
            self.notify.error("Unknown mode: " + where +
                              " in handleElevatorDone")

    # Game state

    def enterGame(self):
        base.localAvatar.setTeleportAvailable(0)
        base.localAvatar.laffMeter.start()
    def exitGame(self):
        base.localAvatar.laffMeter.stop()

    # Battle state

    def enterBattle(self, event):
        assert(self.notify.debug("enterBattle()"))

        # Get the floor multiplier
        mult = ToontownBattleGlobals.getCreditMultiplier(self.currentFloor)
        self.townBattle.enter(event, self.fsm.getStateNamed("battle"),
                              bldg=1, creditMultiplier=mult)

        # Make sure the toon's anim state gets reset
        base.localAvatar.b_setAnimState('off', 1)

        # Disable leave to pay / set parent password
        base.localAvatar.cantLeaveGame = 1

    def exitBattle(self):
        assert(self.notify.debug("exitBattle()"))
        self.townBattle.exit()
        base.localAvatar.cantLeaveGame = 0

    def enterCrane(self):
        assert(self.notify.debug("enterCrane()"))
        base.localAvatar.setTeleportAvailable(0)
        base.localAvatar.laffMeter.start()
        base.localAvatar.collisionsOn()

    def exitCrane(self):
        assert(self.notify.debug("exitCrane()"))
        base.localAvatar.collisionsOff()
        base.localAvatar.laffMeter.stop()

    # walk state inherited from Place.py
    def enterWalk(self, teleportIn=0):
        Place.Place.enterWalk(self, teleportIn)
        self.ignore('teleportQuery')
        base.localAvatar.setTeleportAvailable(0)

    # sticker book state inherited from Place.py
    def enterStickerBook(self, page = None):
        Place.Place.enterStickerBook(self, page)
        self.ignore('teleportQuery')
        base.localAvatar.setTeleportAvailable(0)

    # sit state inherited from Place.py
    def enterSit(self):
        Place.Place.enterSit(self)
        self.ignore('teleportQuery')
        base.localAvatar.setTeleportAvailable(0)

    # teleport in state

    def enterTeleportIn(self, requestStatus):
        # We can only teleport in if our goHome or teleport to toon
        # request failed.
        # Set localToon to the starting position within the
        # interior
        base.localAvatar.setPosHpr(2.5, 11.5, ToontownGlobals.FloorOffset,
                                     45.0, 0.0, 0.0)

        Place.Place.enterTeleportIn(self, requestStatus)

    # teleport out state

    def enterTeleportOut(self, requestStatus):
        assert(self.notify.debug('enterTeleportOut()'))
        Place.Place.enterTeleportOut(self, requestStatus,
                        self.__teleportOutDone)

    def __teleportOutDone(self, requestStatus):
        # Get out of here.
        hoodId = requestStatus["hoodId"]
        if hoodId == ToontownGlobals.MyEstate:
            # We are trying to go to an estate. This request might fail
            # if we are going to a toon's estate that we are not friends with.
            # So we don't want to tell the AI that we are leaving right away.
            # We will rely on the Place.Place.goHome function to do that if
            # the teleport to estate request is successful.
            self.getEstateZoneAndGoHome(requestStatus)
        else:
            # Let the DSI know that we are leaving.
            messenger.send("localToonLeft")
            self.doneStatus = requestStatus
            messenger.send(self.doneEvent)

    def exitTeleportOut(self):
        Place.Place.exitTeleportOut(self)

    def goHomeFailed(self, task):
        # it took too long to hear back from the server,
        # or we tried going to a non-friends house
        self.notifyUserGoHomeFailed()
        #  ignore the setLocalEstateZone message
        self.ignore("setLocalEstateZone")
        self.doneStatus["avId"] =  -1
        self.doneStatus["zoneId"] =  self.getZoneId()
        self.fsm.request("teleportIn", [self.doneStatus])
        return Task.done


    # elevatorOut state

    def enterElevatorOut(self):
        assert(self.notify.debug('enterElevatorOut()'))
        # TODO: Eventually, we will have a sequence here (like iris out)
        # and when it is done, it should find a way to call __elevatorOutDone.
        # for now, we'll just call it directly.
        #self.__elevatorOutDone(
        return None

    def __elevatorOutDone(self, requestStatus):
        self.doneStatus = requestStatus
        messenger.send(self.doneEvent)

    def exitElevatorOut(self):
        return None
