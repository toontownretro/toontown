#-------------------------------------------------------------------------------
# Contact: Mark Wojtowicz
# Created: June 2010
#-------------------------------------------------------------------------------

from toontown.parties import PartyGlobals
from toontown.parties.DistributedPartyTrampolineActivityAI import DistributedPartyTrampolineActivityAI

class DistributedPartyWinterTrampolineActivityAI(DistributedPartyTrampolineActivityAI):
    """ Reskinned trampoline for winter holiday. """

    def __init__(self, air, partyDoId, x, y, h):
        DistributedPartyTrampolineActivityAI.__init__(self, air, partyDoId, x, y, h, actId=PartyGlobals.ActivityIds.PartyWinterTrampoline)
