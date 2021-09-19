"""DistributedJailbirdDale module: contains the DistributedJailbirdDale class"""

from direct.showbase.ShowBaseGlobal import *
from . import DistributedCCharBase
from direct.directnotify import DirectNotifyGlobal
from direct.fsm import ClassicFSM
from direct.fsm import State
from . import CharStateDatas
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer
from . import DistributedDale

class DistributedJailbirdDale(DistributedDale.DistributedDale):
    """DistributedDale class"""

    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedJailbirdDale')

    def __init__(self, cr):
        try:
            self.DistributedDale_initialized
        except:
            self.DistributedDale_initialized = 1
            DistributedCCharBase.DistributedCCharBase.__init__(self, cr,
                                                               TTLocalizer.JailbirdDale,
                                                               'jda')
            self.fsm = ClassicFSM.ClassicFSM('DistributedJailbirdDale',
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

            self.handleHolidays()

            self.nametag.setName(TTLocalizer.Dale)

