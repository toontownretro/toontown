#-------------------------------------------------------------------------------
# Contact: Mark Wojtowicz
# Created: June 2010
#-------------------------------------------------------------------------------

from toontown.parties import PartyGlobals
from toontown.parties.DistributedPartyCogActivityAI import DistributedPartyCogActivityAI

class DistributedPartyWinterCogActivityAI(DistributedPartyCogActivityAI):
    """ Reskinned cog for winter holiday. """

    def __init__(self, air, partyDoId, x, y, h):
        DistributedPartyCogActivityAI.__init__(self, air, partyDoId, x, y, h, actId=PartyGlobals.ActivityIds.PartyWinterCog)
