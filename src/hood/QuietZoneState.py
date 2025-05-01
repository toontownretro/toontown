"""QuietZoneState module: contains the quiet state which is used by
   multiple FSMs"""

from toontown.toonbase.ToontownModules import *
from direct.showbase.PythonUtil import Functor, PriorityCallbacks
from direct.task import Task
from toontown.distributed.ToontownMsgTypes import *
from otp.otpbase import OTPGlobals
from direct.directnotify import DirectNotifyGlobal
from direct.fsm import StateData
from direct.fsm import ClassicFSM, State
from direct.fsm import State
from . import ZoneUtil

class QuietZoneState(StateData.StateData):
    """QuietZoneState state class"""

    # create a notify category
    notify = DirectNotifyGlobal.directNotify.newCategory("QuietZoneState")

    Disable = False
    Queue = []

    def __init__(self, doneEvent):
        """__init__(self, string)
        QuietZoneState state constructor
        """
        StateData.StateData.__init__(self, doneEvent)
        self.fsm = ClassicFSM.ClassicFSM('QuietZoneState',
                           [State.State('off',
                                        self.enterOff,
                                        self.exitOff,
                                        ['waitForQuietZoneResponse']),
                            State.State('waitForQuietZoneResponse',
                                        self.enterWaitForQuietZoneResponse,
                                        self.exitWaitForQuietZoneResponse,
                                        ['waitForZoneRedirect']),
                            State.State('waitForZoneRedirect',
                                        self.enterWaitForZoneRedirect,
                                        self.exitWaitForZoneRedirect,
                                        ['waitForSetZoneResponse']),
                            State.State('waitForSetZoneResponse',
                                        self.enterWaitForSetZoneResponse,
                                        self.exitWaitForSetZoneResponse,
                                        ['waitForSetZoneComplete']),
                            State.State('waitForSetZoneComplete',
                                        self.enterWaitForSetZoneComplete,
                                        self.exitWaitForSetZoneComplete,
                                        ['waitForLocalAvatarOnShard']),
                            State.State('waitForLocalAvatarOnShard',
                                        self.enterWaitForLocalAvatarOnShard,
                                        self.exitWaitForLocalAvatarOnShard,
                                        ['off']),
                            ],
                           # Initial State
                           'off',
                           # Final State
                           'off',
                           )
        self._enqueueCount = 0
        self.fsm.enterInitialState()

    def load(self):
        self.notify.debug("load()")

    def unload(self):
        self._dequeue()
        self.notify.debug("unload()")
        del self.fsm

    @classmethod
    def enqueueState(cls, state, requestStatus):
        cls.Queue = [(state, requestStatus)] + cls.Queue
        state._enqueueCount += 1
        if len(cls.Queue) == 1:
            cls.startNextQueuedState()

    @classmethod
    def dequeueState(cls, state):
        s, requestStatus = cls.Queue.pop()
        s._enqueueCount -= 1
        if len(cls.Queue) > 0:
            cls.startNextQueuedState()

    @classmethod
    def startNextQueuedState(cls):
        state, requestStatus = cls.Queue[-1]
        state._start(requestStatus)

    def _dequeue(self):
        newQ = []
        for item in self.__class__.Queue:
            state, requestStatus = item
            if state is not self:
                newQ.append(item)

        self.__class__.Queue = newQ

    def getEnterWaitForSetZoneResponseMsg(self):
        return 'enterWaitForSetZoneResponse-%s' % (id(self),)

    def getQuietZoneLeftEvent(self):
        return '%s-%s' % (base.cr.getQuietZoneLeftEvent(), id(self))

    def getSetZoneCompleteEvent(self):
        return 'setZoneComplete-%s' % (id(self),)

    def enter(self, requestStatus):
        self.notify.debug("enter(requestStatus="+str(requestStatus)+")")
        #base.transitions.fadeScreen(1.0)
        self._requestStatus = requestStatus
        self._leftQuietZoneCallbacks = None
        self._setZoneCompleteCallbacks = None
        self._leftQuietZoneLocalCallbacks = {}
        self._setZoneCompleteLocalCallbacks = {}
        self.enqueueState(self, requestStatus)

    def _start(self, requestStatus):
        base.transitions.fadeScreen(1.0)
        self.fsm.request("waitForQuietZoneResponse")

    def getRequestStatus(self):
        return self._requestStatus

    def exit(self):
        self.notify.debug("exit()")
        del self._requestStatus
#        base.transitions.noFade()
        base.transitions.noTransitions()
        self.fsm.request("off")
        self._dequeue()

    def waitForDatabase(self, description):
        if base.endlessQuietZone:
            return None
        base.cr.waitForDatabaseTimeout(requestName='quietZoneState-%s' % description)
        
    def clearWaitForDatabase(self):
        base.cr.cleanupWaitingForDatabase()

    def addLeftQuietZoneCallback(self, callback, priority = None):
        if self._leftQuietZoneCallbacks:
            return self._leftQuietZoneCallbacks.add(callback, priority)
        else:
            token = PriorityCallbacks.GetToken()
            fdc = SubframeCall(callback, taskMgr.getCurrentTask().getPriority() - 1)
            self._leftQuietZoneLocalCallbacks[token] = fdc
            return token

    def removeLeftQuietZoneCallback(self, token):
        if token is not None:
            lc = self._leftQuietZoneLocalCallbacks.pop(token, None)
            if lc:
                lc.cleanup()
            if self._leftQuietZoneCallbacks:
                self._leftQuietZoneCallbacks.remove(token)

    def addSetZoneCompleteCallback(self, callback, priority = None):
        if self._setZoneCompleteCallbacks:
            return self._setZoneCompleteCallbacks.add(callback, priority)
        else:
            token = PriorityCallbacks.GetToken()
            fdc = SubframeCall(callback, taskMgr.getCurrentTask().getPriority() - 1)
            self._setZoneCompleteLocalCallbacks[token] = fdc
            return token

    def removeSetZoneCompleteCallback(self, token):
        if token is not None:
            lc = self._setZoneCompleteLocalCallbacks.pop(token, None)
            if lc:
                lc.cleanup()
            if self._setZoneCompleteCallbacks:
                self._setZoneCompleteCallbacks.remove(token)

    ##### handlers #####

    def handleWaitForQuietZoneResponse(self, msgType, di):
        #self.notify.debug("handleWaitForQuietZoneResponse(msgType=%s, di=%s)" % (str(msgType), str(di)))
        if msgType == CLIENT_CREATE_OBJECT_REQUIRED:
            # Call the special filtered quiet zone generate handler
            base.cr.handleQuietZoneGenerateWithRequired(di)
        elif msgType == CLIENT_CREATE_OBJECT_REQUIRED_OTHER:
            # Call the special filtered quiet zone generate handler
            base.cr.handleQuietZoneGenerateWithRequiredOther(di)
        elif msgType == CLIENT_OBJECT_UPDATE_FIELD:
            # Call the special filtered quiet zone field update handler
            base.cr.handleQuietZoneUpdateField(di)
        elif msgType in QUIET_ZONE_IGNORED_LIST:
            # These are messages from the previous zone that we can
            # safely ignore. Going to the quiet zone before hand will
            # prevent most of these from even being sent to us, but
            # there still may be some on the wire on the way to us
            self.notify.debug("ignoring unwanted message from previous zone")
        else:
            # Dispatch back to the cr
            base.cr.handlePlayGame(msgType, di)

    def handleWaitForZoneRedirect(self, msgType, di):
        #self.notify.debug("handleWaitForZoneRedirect("+"msgType="+str(msgType)+", di="+str(di)+")")
        if msgType == CLIENT_CREATE_OBJECT_REQUIRED:
            # Call the special filtered quiet zone generate handler
            base.cr.handleQuietZoneGenerateWithRequired(di)
        elif msgType == CLIENT_CREATE_OBJECT_REQUIRED_OTHER:
            # Call the special filtered quiet zone generate handler
            base.cr.handleQuietZoneGenerateWithRequiredOther(di)
        elif msgType == CLIENT_OBJECT_UPDATE_FIELD:
            # Call the special filtered quiet zone field update handler
            base.cr.handleQuietZoneUpdateField(di)
        else:
            # Dispatch back to the cr
            base.cr.handlePlayGame(msgType, di)

    ##### Off #####

    def enterOff(self):
        self.notify.debug("enterOff()")

    def exitOff(self):
        self.notify.debug("exitOff()")
        self._leftQuietZoneCallbacks = PriorityCallbacks()
        self._setZoneCompleteCallbacks = PriorityCallbacks()
        self._leftQuietZoneLocalCallbacks = {}
        self._setZoneCompleteLocalCallbacks = {}

    ##### WaitForQuietZoneResponse #####

        # In this state, we request a transition to the quiet zone and
        # wait until we get there.

    def enterWaitForQuietZoneResponse(self):
        self.notify.debug("enterWaitForQuietZoneResponse(doneStatus="
                +str(self._requestStatus)+")")
        # Setup our handlers:
        if not self.Disable:
            base.cr.handler = self.handleWaitForQuietZoneResponse
            base.cr.handlerArgs = self._requestStatus
            base.cr.setInQuietZone(True)
        self.setZoneDoneEvent = base.cr.getNextSetZoneDoneEvent()
        self.acceptOnce(self.setZoneDoneEvent,
                        self._handleQuietZoneComplete)
        self.waitForDatabase('WaitForQuietZoneResponse')
        if base.slowQuietZone:
            def sQZR(task):
                base.cr.sendQuietZoneRequest()
                return Task.done
            taskMgr.doMethodLater(base.slowQuietZoneDelay,
                                  sQZR,
                                  'slowQuietZone-sendQuietZoneRequest')
        else:
            base.cr.sendQuietZoneRequest()

    def _handleQuietZoneComplete(self):
        self.fsm.request("waitForZoneRedirect")

    def exitWaitForQuietZoneResponse(self):
        self.notify.debug("exitWaitForQuietZoneResponse()")
        self.clearWaitForDatabase()
        # Put the handlers back
        base.cr.handler = base.cr.handlePlayGame
        base.cr.handlerArgs = None
        base.cr.setInQuietZone(False)
        self.ignore(self.setZoneDoneEvent)
        del self.setZoneDoneEvent

    ##### WaitForZoneRedirect #####

        # In this state, we may request a message from the AI to tell
        # us which zone we really want to be going to.  In most cases
        # we just bypass this and move directly to
        # WaitForSetZoneResponse.

    def enterWaitForZoneRedirect(self):
        self.notify.debug("enterWaitForZoneRedirect(requestStatus="
                +str(self._requestStatus)+")")
        # Setup our handlers:
        if not self.Disable:
            base.cr.handler = self.handleWaitForZoneRedirect
            base.cr.handlerArgs = self._requestStatus
            base.cr.setInQuietZone(True)

        self.waitForDatabase('WaitForZoneRedirect')

        zoneId = self._requestStatus["zoneId"]
        avId = self._requestStatus.get("avId", -1)
        allowRedirect = self._requestStatus.get("allowRedirect", 1)
        if avId != -1:
            # If we're going to a particular avatar, we can't redirect.
            allowRedirect = 0

        if not base.cr.welcomeValleyManager:
            # If we don't have a welcomeValleyManager, we must be running
            # in the dev environment without an AI; always put the
            # avatar in the canonical zone.
            newZoneId = ZoneUtil.getCanonicalZoneId(zoneId)
            if newZoneId != zoneId:
                self.gotZoneRedirect(newZoneId)
                return

        if allowRedirect and ZoneUtil.isWelcomeValley(zoneId):
            # We're going to a WelcomeValley zone, and redirects are
            # not forbidden, so give the AI a chance to pick a zoneId
            # for us.

            self.notify.info("Requesting AI redirect from zone %s." % (zoneId))
            if base.slowQuietZone:
                def rZI(task, zoneId=zoneId, self=self):
                    base.cr.welcomeValleyManager.requestZoneId(
                        zoneId, self.gotZoneRedirect)
                    return Task.done
                taskMgr.doMethodLater(
                    base.slowQuietZoneDelay,
                    rZI,
                    'slowQuietZone-welcomeValleyRedirect')
            else:
                base.cr.welcomeValleyManager.requestZoneId(
                    zoneId, self.gotZoneRedirect)

        else:
            # No, we're just going directly to the zone we asked to go
            # to.
            self.fsm.request("waitForSetZoneResponse")

    def gotZoneRedirect(self, zoneId):
        self.notify.info("Redirecting to zone %s." % (zoneId))
        base.cr.handlerArgs["zoneId"] = zoneId
        base.cr.handlerArgs["hoodId"] = ZoneUtil.getHoodId(zoneId)

        self.fsm.request("waitForSetZoneResponse")

    def exitWaitForZoneRedirect(self):
        self.notify.debug("exitWaitForZoneRedirect()")
        self.clearWaitForDatabase()
        # Put the handlers back
        base.cr.handler = base.cr.handlePlayGame
        base.cr.handlerArgs = None
        base.cr.setInQuietZone(False)

    ##### WaitForSetZoneResponse #####

        # In this state, we request a transition to our destination
        # zone and wait until we get there.

    def enterWaitForSetZoneResponse(self):
        self.notify.debug("enterWaitForSetZoneResponse(requestStatus="
                +str(self._requestStatus)+")")
        if not self.Disable:
            # Tell anyone who wants to know, that we're in this funciton:
            messenger.send(self.getEnterWaitForSetZoneResponseMsg(), [self._requestStatus])
            base.cr.handlerArgs = self._requestStatus
            # Put us in the destination zone:
            zoneId = self._requestStatus["zoneId"]
            ##self.acceptOnce(base.cr.getNextSetZoneDoneEvent(),
            ##                self.WaitForSetZoneResponse)
            # dump all of the shard objects
            base.cr.dumpAllSubShardObjects()
            # we're starting fresh now in terms of sub-shard objects
            base.cr.resetDeletedSubShardDoIds()
            base.cr.sendSetZoneMsg(zoneId)
            self.waitForDatabase('WaitForSetZoneResponse')
            self.fsm.request("waitForSetZoneComplete")

# now done locally on the AI
##         if base.cr.welcomeValleyManager:
##             base.cr.welcomeValleyManager.d_clientSetZone(zoneId)


    def exitWaitForSetZoneResponse(self):
        self.notify.debug("exitWaitForSetZoneResponse()")
        self.clearWaitForDatabase()
        # Put the handlers back
        base.cr.handler = base.cr.handlePlayGame
        base.cr.handlerArgs = None

    ##### WaitForSetZoneComplete #####

        # In this state, we have already transitioned to our
        # destination zone, and we are waiting for all objects to be
        # manifested.

    def enterWaitForSetZoneComplete(self):
        self.notify.debug("enterWaitForSetZoneComplete(requestStatus="
                +str(self._requestStatus)+")")
        if not self.Disable:
            # Setup our handlers:
            base.cr.handlerArgs = self._requestStatus
            if base.slowQuietZone:
                def delayFunc(self=self):
                    def hSZC(task):
                        self._handleSetZoneComplete()
                        return Task.done
                    taskMgr.doMethodLater(base.slowQuietZoneDelay,
                                          hSZC,
                                          'slowQuietZone-sendSetZoneComplete')
                nextFunc = delayFunc
            else:
                nextFunc = self._handleSetZoneComplete
            self.waitForDatabase('WaitForSetZoneComplete')
            self.setZoneDoneEvent = base.cr.getLastSetZoneDoneEvent()
            self.acceptOnce(self.setZoneDoneEvent, nextFunc)
            if base.placeBeforeObjects:
                self._leftQuietZoneCallbacks()
                self._leftQuietZoneCallbacks = None
                fdcs = list(self._leftQuietZoneLocalCallbacks.values())
                self._leftQuietZoneLocalCallbacks = {}
                for fdc in fdcs:
                    if not fdc.isFinished():
                        fdc.finish()

                messenger.send(self.getQuietZoneLeftEvent())

    def _handleSetZoneComplete(self):
        self.fsm.request("waitForLocalAvatarOnShard")

    def exitWaitForSetZoneComplete(self):
        self.notify.debug("exitWaitForSetZoneComplete()")
        self.clearWaitForDatabase()

        # Put the handlers back
        base.cr.handler = base.cr.handlePlayGame
        base.cr.handlerArgs = None
        self.ignore(self.setZoneDoneEvent)
        del self.setZoneDoneEvent

    def enterWaitForLocalAvatarOnShard(self):
        self.notify.debug("enterWaitForLocalAvatarOnShard()")
        if not self.Disable:
            base.cr.handlerArgs = self._requestStatus
            self._onShardEvent = localAvatar.getArrivedOnDistrictEvent()
            self.waitForDatabase('WaitForLocalAvatarOnShard')
            if localAvatar.isGeneratedOnDistrict(localAvatar.defaultShard):
                self._announceDone()
            else:
                self.acceptOnce(self._onShardEvent, self._announceDone)

    def _announceDone(self):
        # Now you are in a real zone, you can chat
        base.localAvatar.startChat()
        if base.endlessQuietZone:
            self._dequeue()
        doneEvent = self.doneEvent
        requestStatus = self._requestStatus
        self._setZoneCompleteCallbacks()
        self._setZoneCompleteCallbacks = None
        fdcs = list(self._setZoneCompleteLocalCallbacks.values())
        self._setZoneCompleteLocalCallbacks = {}
        for fdc in fdcs:
            if not fdc.isFinished():
                fdc.finish()
        # Send a message in case anyone in the world cares
        # whether we've just completely entered the zone.
        #messenger.send("setZoneComplete", self._requestStatus)
        messenger.send(self.getSetZoneCompleteEvent(), [requestStatus])
        # Tell our parent that we're done:
        messenger.send(self.doneEvent)
        self._dequeue()

    def exitWaitForLocalAvatarOnShard(self):
        self.notify.debug("exitWaitForLocalAvatarOnShard()")
        self.clearWaitForDatabase()
        self.ignore(self._onShardEvent)
        base.cr.handlerArgs = None
        del self._onShardEvent
