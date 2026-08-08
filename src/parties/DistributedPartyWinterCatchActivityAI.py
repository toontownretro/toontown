#-------------------------------------------------------------------------------
# Contact:
# Created:
#
# Purpose:
#-------------------------------------------------------------------------------

from toontown.parties import PartyGlobals
from toontown.parties.DistributedPartyCatchActivityAI import DistributedPartyCatchActivityAI

class DistributedPartyWinterCatchActivityAI(DistributedPartyCatchActivityAI):
    def __init__(self, air, partyDoId, x, y, h):
        DistributedPartyCatchActivityAI.__init__(self, air, partyDoId, x, y, h, actId=PartyGlobals.ActivityIds.PartyWinterCatch)
