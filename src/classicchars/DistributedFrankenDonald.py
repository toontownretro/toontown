"""DistributedDonald module: contains the DistributedDonald class"""

from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
import DistributedCCharBase
import DistributedDonald
from direct.directnotify import DirectNotifyGlobal
from direct.fsm import ClassicFSM, State
from direct.fsm import State
import CharStateDatas
import CCharChatter
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer
from toontown.hood import GSHood

class DistributedFrankenDonald(DistributedDonald.DistributedDonald):
    """DistributedDonald class"""

    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedFrankenDonald")

    def __init__(self, cr):
        try:
            self.DistributedFrankenDonald_initialized
        except:
            self.DistributedFrankenDonald_initialized = 1
            DistributedCCharBase.DistributedCCharBase.__init__(self, cr,
                                                               TTLocalizer.FrankenDonald,
                                                               'fd')
            self.fsm = ClassicFSM.ClassicFSM(self.getName(),
                            [State.State('Off',
                                         self.enterOff,
                                         self.exitOff,
                                         ['Neutral']),
                             State.State('Neutral',
                                         self.enterNeutral,
                                         self.exitNeutral,
                                         ['Walk']),
                             State.State('Walk',
                                         self.enterWalk,
                                         self.exitWalk,
                                         ['Neutral']),
                             ],
                             # Initial State
                             'Off',
                             # Final State
                             'Off',
                             )

            self.fsm.enterInitialState()

            # We want him to show up as Donald
            self.nametag.setName(TTLocalizer.Donald)

            self.handleHolidays()

    def disable(self):
        self.fsm.requestFinalState()
        DistributedCCharBase.DistributedCCharBase.disable(self)

        del self.neutralDoneEvent
        del self.neutral
        del self.walkDoneEvent
        del self.walk
        self.fsm.requestFinalState()

    def generate(self):
        """
        create Donald and state data information
        """
        DistributedCCharBase.DistributedCCharBase.generate(self, self.diffPath)
        name = self.getName()
        self.neutralDoneEvent = self.taskName(name + '-neutral-done')
        self.neutral = CharStateDatas.CharNeutralState(self.neutralDoneEvent, self)

        self.walkDoneEvent = self.taskName(name + '-walk-done')
        if self.diffPath == None:
            self.walk = CharStateDatas.CharWalkState(
            self.walkDoneEvent, self)
        else:
            self.walk = CharStateDatas.CharWalkState(
            self.walkDoneEvent, self, self.diffPath)
        self.fsm.request('Neutral')

    ### Neutral state ###
    def enterNeutral(self):
        self.notify.debug('Neutral ' + self.getName() + '...')
        self.neutral.enter()
        self.acceptOnce(self.neutralDoneEvent, self.__decideNextState)

    ### Walk state ###
    def enterWalk(self):
        self.notify.debug('Walking ' + self.getName() + '...')
        self.walk.enter()
        self.acceptOnce(self.walkDoneEvent, self.__decideNextState)

    def __decideNextState(self, doneStatus):
        self.fsm.request('Neutral')

    def walkSpeed(self):
        return ToontownGlobals.FrankenDonaldSpeed
