"""DistributedGoofyAI module: contains the DistributedGoofyAI class"""

from otp.ai.AIBaseGlobal import *
from . import DistributedCCharBaseAI
from direct.directnotify import DirectNotifyGlobal
from direct.fsm import ClassicFSM, State
from direct.fsm import State
from direct.task import Task
import random
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer
from . import CharStateDatasAI

class DistributedGoofySpeedwayAI(DistributedCCharBaseAI.DistributedCCharBaseAI):

    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedGoofySpeedwayAI")

    def __init__(self, air):
        DistributedCCharBaseAI.DistributedCCharBaseAI.__init__(self, air, TTLocalizer.Goofy)
        self.fsm = ClassicFSM.ClassicFSM('DistributedGoofySpeedwayAI',
                          [State.State('Off',
                                        self.enterOff,
                                        self.exitOff,
                                        ['Lonely', 'TransitionToCostume', 'Walk']),
                            State.State('Lonely',
                                        self.enterLonely,
                                        self.exitLonely,
                                        ['Chatty', 'Walk', 'TransitionToCostume']),
                            State.State('Chatty',
                                        self.enterChatty,
                                        self.exitChatty,
                                        ['Lonely', 'Walk', 'TransitionToCostume']),
                            State.State('Walk',
                                        self.enterWalk,
                                        self.exitWalk,
                                        ['Lonely', 'Chatty', 'TransitionToCostume']),
                            State.State('TransitionToCostume',
                                            self.enterTransitionToCostume,
                                            self.exitTransitionToCostume,
                                            ['Off']),
                            ],
                           # Initial State
                           'Off',
                           # Final State
                           'Off',
                           )

        self.fsm.enterInitialState()
        self.handleHolidays()

    def delete(self):
        self.fsm.requestFinalState()
        DistributedCCharBaseAI.DistributedCCharBaseAI.delete(self)

        self.lonelyDoneEvent = None
        self.lonely = None
        self.chattyDoneEvent = None
        self.chatty = None
        self.walkDoneEvent = None
        self.walk = None

    def generate( self ):
        # all state data's that Goofy will need
        #
        DistributedCCharBaseAI.DistributedCCharBaseAI.generate(self)
        name = self.getName()
        self.lonelyDoneEvent = self.taskName(name + '-lonely-done')
        self.lonely = CharStateDatasAI.CharLonelyStateAI(
            self.lonelyDoneEvent, self)

        self.chattyDoneEvent = self.taskName(name + '-chatty-done')
        self.chatty = CharStateDatasAI.CharChattyStateAI(
            self.chattyDoneEvent, self)

        self.walkDoneEvent = self.taskName(name + '-walk-done')
        if self.diffPath == None:
            self.walk = CharStateDatasAI.CharWalkStateAI(
                self.walkDoneEvent, self)
        else:
            self.walk = CharStateDatasAI.CharWalkStateAI(
                self.walkDoneEvent, self, self.diffPath)

    def walkSpeed(self):
        return ToontownGlobals.GoofySpeed

    # this function kicks off Goofy
    def start(self):
        # poor lonely Goofy
        self.fsm.request('Lonely')

    def __decideNextState(self, doneStatus):
        """
        doneStatus, info about the finished state

        called when the current state Goofy is in
        decides that it is finished and a new state should
        be transitioned into
        """
        assert('status' in doneStatus)

        if(self.transitionToCostume == 1):
            curWalkNode = self.walk.getDestNode()
            if simbase.air.holidayManager:
                if ToontownGlobals.HALLOWEEN_COSTUMES in simbase.air.holidayManager.currentHolidays and \
                   simbase.air.holidayManager.currentHolidays[ToontownGlobals.HALLOWEEN_COSTUMES]:
                    simbase.air.holidayManager.currentHolidays[ToontownGlobals.HALLOWEEN_COSTUMES].triggerSwitch(curWalkNode, self)
                    self.fsm.request('TransitionToCostume')
                elif ToontownGlobals.APRIL_FOOLS_COSTUMES in simbase.air.holidayManager.currentHolidays and \
                   simbase.air.holidayManager.currentHolidays[ToontownGlobals.APRIL_FOOLS_COSTUMES]:
                    simbase.air.holidayManager.currentHolidays[ToontownGlobals.APRIL_FOOLS_COSTUMES].triggerSwitch(curWalkNode, self)
                    self.fsm.request('TransitionToCostume')
                else:
                    self.notify.warning('transitionToCostume == 1 but no costume holiday')
            else:
                self.notify.warning('transitionToCostume == 1 but no holiday Manager')

        if doneStatus['state'] == 'lonely' and \
           doneStatus['status'] == 'done':
            self.fsm.request('Walk')
        elif doneStatus['state'] == 'chatty' and \
             doneStatus['status'] == 'done':
            self.fsm.request('Walk')
        elif doneStatus['state'] == 'walk' and \
             doneStatus['status'] == 'done':
            if len(self.nearbyAvatars) > 0:
                self.fsm.request('Chatty')
            else:
                self.fsm.request('Lonely')
        else:
            assert 0, "Unknown status for Goofy"

    ### Off state ###
    def enterOff(self):
        pass

    def exitOff(self):
        DistributedCCharBaseAI.DistributedCCharBaseAI.exitOff(self)

    ### Lonely state ###
    def enterLonely(self):
        self.lonely.enter()
        self.acceptOnce(self.lonelyDoneEvent, self.__decideNextState)

    def exitLonely(self):
        self.ignore(self.lonelyDoneEvent)
        self.lonely.exit()

    def __goForAWalk(self, task):
        self.notify.debug("going for a walk")
        self.fsm.request('Walk')
        return Task.done

    ### Chatty state ###
    def enterChatty(self):
        self.chatty.enter()
        self.acceptOnce(self.chattyDoneEvent, self.__decideNextState)
        taskMgr.doMethodLater(CharStateDatasAI.CHATTY_DURATION + 10, self.forceLeaveChatty, self.taskName('forceLeaveChatty'))

    def forceLeaveChatty(self, task):
        self.notify.warning('Had to force change of state from Chatty state')
        doneStatus = {}
        doneStatus['state'] = 'chatty'
        doneStatus['status'] = 'done'
        self.__decideNextState(doneStatus)
        return Task.done

    def cleanUpChattyTasks(self):
        taskMgr.removeTasksMatching(self.taskName('forceLeaveChatty'))

    def exitChatty(self):
        self.ignore(self.chattyDoneEvent)
        self.chatty.exit()
        self.cleanUpChattyTasks()


    ### Walk state ###
    def enterWalk(self):
        self.notify.debug("going for a walk")
        self.walk.enter()
        self.acceptOnce(self.walkDoneEvent, self.__decideNextState)

    def exitWalk(self):
        self.ignore(self.walkDoneEvent)
        self.walk.exit()


    def avatarEnterNextState(self):
        """
        decide what to do with the state machine when
        a toon gets near Goofy
        """
        # if this is the only avatar, start talking
        if len(self.nearbyAvatars) == 1:
            if self.fsm.getCurrentState().getName() != 'Walk':
                self.fsm.request('Chatty')
            else:
                self.notify.debug("avatarEnterNextState: in walk state")
        else:
            self.notify.debug("avatarEnterNextState: num avatars: " +
                              str(len(self.nearbyAvatars)))

    def avatarExitNextState(self):
        """
        decide what to do with the state machine when a
        toon is no longer near Goofy
        """
        # no need to re-sort av list after removal
        if len(self.nearbyAvatars) == 0:
            if self.fsm.getCurrentState().getName() != 'Walk':
                self.fsm.request('Lonely')                
                                
    def handleHolidays(self):        
        """        
        Handle Holiday specific behaviour        
        """        
        DistributedCCharBaseAI.DistributedCCharBaseAI.handleHolidays(self)
        if hasattr(simbase.air, "holidayManager"):
            if ToontownGlobals.APRIL_FOOLS_COSTUMES in simbase.air.holidayManager.currentHolidays:
                if simbase.air.holidayManager.currentHolidays[ToontownGlobals.APRIL_FOOLS_COSTUMES] != None \
                    and simbase.air.holidayManager.currentHolidays[ToontownGlobals.APRIL_FOOLS_COSTUMES].getRunningState():
                    self.diffPath = TTLocalizer.Donald

    def getCCLocation(self):
        if self.diffPath == None:
            return 1
        else:
            return 0

    ##TransitionToCostumeState##
    def enterTransitionToCostume(self):
        pass

    def exitTransitionToCostume(self):
        pass
