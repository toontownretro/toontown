
from direct.directnotify import DirectNotifyGlobal
from toontown.battle import BattlePlace
from direct.fsm import ClassicFSM, State
from direct.fsm import State
from toontown.toonbase.ToontownModules import *
from otp.distributed.TelemetryLimiter import RotationLimitToH, TLGatherAllAvs
from toontown.toon import Toon
from toontown.toonbase import ToontownGlobals
from toontown.hood import ZoneUtil
from toontown.toonbase import TTLocalizer
from toontown.toontowngui import TTDialog
from toontown.toonbase import ToontownBattleGlobals
from toontown.building import Elevator

class FactoryInterior(BattlePlace.BattlePlace):
    # create a notify category
    notify = DirectNotifyGlobal.directNotify.newCategory("FactoryInterior")

    # special methods
    def __init__(self, loader, parentFSM, doneEvent):
        assert(FactoryInterior.notify.debug("FactoryInterior()"))
        BattlePlace.BattlePlace.__init__(self, loader, doneEvent)
        self.parentFSM = parentFSM
        self.zoneId = ToontownGlobals.SellbotFactoryInt
        # any state that we might be in when someone beats the factory
        # needs to have a transition to teleportout
        self.elevatorDoneEvent = "elevatorDone"


    def load(self):
        self.fsm = ClassicFSM.ClassicFSM('FactoryInterior',
                           [State.State('start',
                                        self.enterStart,
                                        self.exitStart,
                                        ['walk',
                                         'teleportIn',
                                         'fallDown',
                                         ]),
                            State.State('walk',
                                        self.enterWalk,
                                        self.exitWalk,
                                        ['push', 'sit', 'stickerBook',
                                         'WaitForBattle', 'battle',
                                         'died', 'teleportOut', 'squished',
                                         'DFA', 'fallDown', 'elevator'
                                         ]),
                            State.State('stopped',
                                        self.enterStopped,
                                        self.exitStopped,
                                        ['walk', 'teleportOut',
                                         ]),
                            State.State('sit',
                                        self.enterSit,
                                        self.exitSit,
                                        ['walk', 'died', 'teleportOut',]),
                            State.State('push',
                                        self.enterPush,
                                        self.exitPush,
                                        ['walk', 'died', 'teleportOut',]),
                            State.State('stickerBook',
                                        self.enterStickerBook,
                                        self.exitStickerBook,
                                        ['walk', 'battle', 'DFA',
                                        'WaitForBattle', 'died', 'teleportOut',
                                         ]),
                            # This needs a transition to teleportOut to allow
                            # the toon to leave after beating the factory.
                            # When localToon leaves the battle, battle gets
                            # a setMembers with no localToon, enables its
                            # collision sphere, collides with localToon, puts
                            # localToon in WaitForBattle.
                            State.State('WaitForBattle',
                                        self.enterWaitForBattle,
                                        self.exitWaitForBattle,
                                        ['battle', 'walk', 'died',
                                         'teleportOut',]),
                            State.State('battle',
                                        self.enterBattle,
                                        self.exitBattle,
                                        ['walk', 'teleportOut', 'died',]),
                            State.State('fallDown',
                                        self.enterFallDown,
                                        self.exitFallDown,
                                        ['walk', 'died', 'teleportOut',]),
                            State.State('squished',
                                        self.enterSquished,
                                        self.exitSquished,
                                        ['walk', 'died', 'teleportOut',]),
                            State.State('teleportIn',
                                        self.enterTeleportIn,
                                        self.exitTeleportIn,
                                        ['walk', 'teleportOut', 'quietZone', 'died',]),
                            State.State('teleportOut',
                                        self.enterTeleportOut,
                                        self.exitTeleportOut,
                                        ['teleportIn', 'FLA', 'quietZone',
                                         'WaitForBattle']),
                            # Download Force Acknowledge
                            State.State('DFA',
                                        self.enterDFA,
                                        self.exitDFA,
                                        ['DFAReject', 'teleportOut']),
                            State.State('DFAReject',
                                        self.enterDFAReject,
                                        self.exitDFAReject,
                                        ['walk' 'teleportOut',]),
                            State.State('died',
                                        self.enterDied,
                                        self.exitDied,
                                        ['teleportOut']),
                            # Forced Leave Acknowledge
                            State.State('FLA',
                                        self.enterFLA,
                                        self.exitFLA,
                                        ['quietZone']),
                            State.State('quietZone',
                                        self.enterQuietZone,
                                        self.exitQuietZone,
                                        ['teleportIn']),
                            State.State('elevator',
                                        self.enterElevator,
                                        self.exitElevator,
                                        ['walk']),
                            State.State('final',
                                        self.enterFinal,
                                        self.exitFinal,
                                        ['start'])],

                           # Initial State
                           'start',
                           # Final State
                           'final',
                           )
        self.parentFSM.getStateNamed("factoryInterior").addChild(self.fsm)
        BattlePlace.BattlePlace.load(self)
        self.music = base.loadMusic('phase_9/audio/bgm/CHQ_FACT_bg.mid')

    def unload(self):
        self.parentFSM.getStateNamed("factoryInterior").removeChild(self.fsm)
        del self.fsm
        del self.music
        BattlePlace.BattlePlace.unload(self)

    def enter(self, requestStatus):
        self.fsm.enterInitialState()
        base.transitions.fadeOut(t=0)

        # While we are here, we ignore invasion credit.
        base.localAvatar.inventory.setRespectInvasions(0)

        # wait until the factory and any distributed entities have been
        # created before moving on
        def commence(self=self):
            # Turn on the little red arrows.
            NametagGlobals.setMasterArrowsOn(1)
            self.fsm.request(requestStatus["how"], [requestStatus])
            base.playMusic(self.music, looping = 1, volume = 0.8)
            base.transitions.irisIn()
        # did the factory beat us here?
        if hasattr(base, 'factoryReady'):
            commence()
        else:
            # wait for the factory to tell us it's ready for prime time.
            self.acceptOnce('FactoryReady', commence)

        self.factoryDefeated = 0
        self.acceptOnce('FactoryWinEvent', self.handleFactoryWinEvent)
        if __debug__ and 0:
            # make F10 simulate someone else winning the factory
            self.accept('f10', lambda: messenger.send('FactoryWinEvent'))

        self.confrontedForeman = 0
        def handleConfrontedForeman(self=self):
            self.confrontedForeman = 1
        self.acceptOnce('localToonConfrontedForeman', handleConfrontedForeman)

    def exit(self):
        # Turn off the little red arrows.
        NametagGlobals.setMasterArrowsOn(0)

        if hasattr(base, 'factoryReady'):
            del base.factoryReady

        # Respect invasions again.
        base.localAvatar.inventory.setRespectInvasions(1)

        self.fsm.requestFinalState()
        self.loader.music.stop()
        self.music.stop()
        self.ignoreAll()

    # walk state inherited from BattlePlace.py
    # Override to turn off teleport
    def enterWalk(self, teleportIn=0):
        BattlePlace.BattlePlace.enterWalk(self, teleportIn)
        self.ignore('teleportQuery')
        base.localAvatar.setTeleportAvailable(0)

    # push state inherited from Place.py
    # Override to turn off teleport
    def enterPush(self):
        BattlePlace.BattlePlace.enterPush(self)
        self.ignore('teleportQuery')
        base.localAvatar.setTeleportAvailable(0)

    # waitForBattle state inherited from BattlePlace.py
    def enterWaitForBattle(self):
        FactoryInterior.notify.info('enterWaitForBattle')
        BattlePlace.BattlePlace.enterWaitForBattle(self)
        # make sure we're under render, and make sure everyone else knows it
        if base.localAvatar.getParent() != render:
            base.localAvatar.wrtReparentTo(render)
            base.localAvatar.b_setParent(ToontownGlobals.SPActors)

    def exitWaitForBattle(self):
        FactoryInterior.notify.info('exitWaitForBattle')
        BattlePlace.BattlePlace.exitWaitForBattle(self)

    # battle state inherited from BattlePlace.py
    # Override to turn off teleport and control music
    def enterBattle(self, event):
        FactoryInterior.notify.info('enterBattle')
        self.music.stop()
        BattlePlace.BattlePlace.enterBattle(self, event)
        self.ignore('teleportQuery')
        base.localAvatar.setTeleportAvailable(0)

    # Override to set bldg flag and creditMultiplier
    def enterTownBattle(self, event):
        # this assumes that our 'zoneId' is going to be set to the appropriate
        # faux-zone, and that we continue to use the faux-zone as the factory
        # ID
        mult = ToontownBattleGlobals.getFactoryCreditMultiplier(self.zoneId)
        base.localAvatar.inventory.setBattleCreditMultiplier(mult)
        self.loader.townBattle.enter(event, self.fsm.getStateNamed("battle"),
                                     bldg=1, creditMultiplier=mult)

    # Override to control our own music
    def exitBattle(self):
        FactoryInterior.notify.info('exitBattle')
        BattlePlace.BattlePlace.exitBattle(self)
        self.loader.music.stop()
        base.playMusic(self.music, looping = 1, volume = 0.8)

    # sticker book state inherited from BattlePlace.py
    # Override to turn off teleport
    def enterStickerBook(self, page = None):
        BattlePlace.BattlePlace.enterStickerBook(self, page)
        self.ignore('teleportQuery')
        base.localAvatar.setTeleportAvailable(0)

    # sit state inherited from BattlePlace.py
    # Override to turn off teleport
    def enterSit(self):
        BattlePlace.BattlePlace.enterSit(self)
        self.ignore('teleportQuery')
        base.localAvatar.setTeleportAvailable(0)

    def enterZone(self, zoneId):
        pass

    def enterTeleportOut(self, requestStatus):
        FactoryInterior.notify.info('enterTeleportOut()')
        BattlePlace.BattlePlace.enterTeleportOut(self, requestStatus,
                        self.__teleportOutDone)

    def __processLeaveRequest(self, requestStatus):
        hoodId = requestStatus["hoodId"]
        if (hoodId == ToontownGlobals.MyEstate):
            self.getEstateZoneAndGoHome(requestStatus)
        else:
            # Different hood or zone, exit the safe zone
            self.doneStatus = requestStatus
            messenger.send(self.doneEvent)

    def __teleportOutDone(self, requestStatus):
        FactoryInterior.notify.info('__teleportOutDone()')
        messenger.send('leavingFactory')
        messenger.send("localToonLeft")

        # we've played the teleport-out sequence; if we just got booted
        # out of the factory because the foreman was defeated, and we
        # were not in the battle, show a dialog to let the player know
        # what happened
        if self.factoryDefeated and (not self.confrontedForeman):
            # Forced Leave Ack
            self.fsm.request('FLA', [requestStatus])
        else:
            self.__processLeaveRequest(requestStatus)

    def exitTeleportOut(self):
        FactoryInterior.notify.info('exitTeleportOut()')
        BattlePlace.BattlePlace.exitTeleportOut(self)

    def detectedElevatorCollision(self, distElevator):
        assert(self.notify.debug("detectedElevatorCollision()"))
        self.fsm.request("elevator", [distElevator])

    def enterElevator(self, distElevator):
        assert(self.notify.debug("enterElevator()"))
        self.accept(self.elevatorDoneEvent, self.handleElevatorDone)
        self.elevator = Elevator.Elevator(self.fsm.getStateNamed("elevator"),
                                          self.elevatorDoneEvent,
                                          distElevator)
        #elevatorFSM is now on the DO
        distElevator.elevatorFSM=self.elevator
        self.elevator.load()
        self.elevator.enter()

    def exitElevator(self):
        assert(self.notify.debug("exitElevator()"))
        self.ignore(self.elevatorDoneEvent)
        self.elevator.unload()
        self.elevator.exit()
        #del self.elevator

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
        elif (where == 'factoryInterior' or where == 'suitInterior'):
            self.doneStatus = doneStatus
            self.doneEvent = "lawOfficeFloorDone"
            messenger.send(self.doneEvent)
            #messenger.send(self.doneEvent)
        else:
            self.notify.error("Unknown mode: " + where +
                              " in handleElevatorDone")

    def handleFactoryWinEvent(self):
        """this handler is called when the factory foreman has been defeated"""
        FactoryInterior.notify.info('handleFactoryWinEvent')

        # if we're in the process of dying, ignore this
        if (base.cr.playGame.getPlace().fsm.getCurrentState().getName() ==
            'died'):
            return

        # update our flag
        self.factoryDefeated = 1

        if 1:
            # go back to HQ
            zoneId = ZoneUtil.getHoodId(self.zoneId)
        else:
            # go back to the playground
            zoneId = ZoneUtil.getSafeZoneId(base.localAvatar.defaultZone)
        self.fsm.request('teleportOut', [{
            "loader": ZoneUtil.getLoaderName(zoneId),
            "where": ZoneUtil.getToonWhereName(zoneId),
            "how": "teleportIn",
            "hoodId": zoneId,
            "zoneId": zoneId,
            "shardId": None,
            "avId": -1,
            }])

    # died state
    def enterDied(self, requestStatus, callback = None):
        FactoryInterior.notify.info('enterDied')
        def diedDone(requestStatus, self=self, callback=callback):
            if callback is not None:
                callback()
            messenger.send('leavingFactory')
            self.doneStatus = requestStatus
            messenger.send(self.doneEvent)
        BattlePlace.BattlePlace.enterDied(self, requestStatus, diedDone)

    # Forced Leave Ack state
    def enterFLA(self, requestStatus):
        FactoryInterior.notify.info('enterFLA')
        # inform the player about why they got booted from the factory
        self.flaDialog = TTDialog.TTGlobalDialog(
            message = TTLocalizer.ForcedLeaveFactoryAckMsg,
            doneEvent = 'FLADone', style = TTDialog.Acknowledge,
            fadeScreen = 1,
            )
        def continueExit(self=self, requestStatus=requestStatus):
            self.__processLeaveRequest(requestStatus)
        self.accept('FLADone', continueExit)
        self.flaDialog.show()

    def exitFLA(self):
        FactoryInterior.notify.info('exitFLA')
        if hasattr(self, 'flaDialog'):
            self.flaDialog.cleanup()
            del self.flaDialog
