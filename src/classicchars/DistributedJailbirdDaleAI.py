"""DistributedJailbirdDaleAI module: contains the DistributedMickeyAI class"""

from otp.ai.AIBaseGlobal import *
from toontown.classicchars import DistributedDaleAI
from direct.directnotify import DirectNotifyGlobal
from direct.fsm import ClassicFSM, State
from direct.fsm import State
from direct.task import Task
import random
from . import DistributedCCharBaseAI
from . import CharStateDatasAI
from toontown.toonbase import TTLocalizer

class DistributedJailbirdDaleAI(DistributedDaleAI.DistributedDaleAI):

    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedJailbirdDaleAI")

    def __init__(self, air, chipId):
        DistributedCCharBaseAI.DistributedCCharBaseAI.__init__(self, air, TTLocalizer.JailbirdDale)
        self.chipId =chipId
        self.chip = air.doId2do.get(chipId)
        self.fsm = ClassicFSM.ClassicFSM('DistributedJailbirdDaleAI',
                           [State.State('Off',
                                        self.enterOff,
                                        self.exitOff,
                                        ['Lonely']),
                            State.State('Lonely',
                                        self.enterLonely,
                                        self.exitLonely,
                                        ['Chatty', 'FollowChip', 'Walk']),
                            State.State('Chatty',
                                        self.enterChatty,
                                        self.exitChatty,
                                        ['Lonely', 'FollowChip', 'Walk']),
                            State.State('Walk',
                                        self.enterWalk,
                                        self.exitWalk,
                                        ['Lonely', 'Chatty']),
                            State.State('FollowChip',
                                        self.enterFollowChip,
                                        self.exitFollowChip,
                                        ['Lonely', 'Chatty', 'FollowChip']),                            
                            ],
                           # Initial State
                           'Off',
                           # Final State
                           'Off',
                           )

        self.fsm.enterInitialState()
        self.handleHolidays()
