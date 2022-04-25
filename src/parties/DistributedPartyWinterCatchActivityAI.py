#-------------------------------------------------------------------------------
# Contact: 
# Created: 2010
#-------------------------------------------------------------------------------

from toontown.parties.DistributedPartyCatchActivityAI import DistributedPartyCatchActivityAI
from toontown.parties import PartyGlobals

class DistributedPartyWinterCatchActivityAI(DistributedPartyCatchActivityAI):
    """ Reskinned catch activity for winter party holiday. """
    
    def __init__(self, air, partyDoId, x, y, h):
        DistributedPartyCatchActivityAI.__init__(self, air, partyDoId, x, y, h, actId=PartyGlobals.ActivityIds.PartyWinterCatch)