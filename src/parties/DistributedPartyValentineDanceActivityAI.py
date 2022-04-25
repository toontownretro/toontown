#-------------------------------------------------------------------------------
# Contact: 
# Created: 2011
#-------------------------------------------------------------------------------
from toontown.parties import PartyGlobals
from toontown.parties.DistributedPartyDanceActivityBaseAI import DistributedPartyDanceActivityBaseAI

class DistributedPartyValentineDanceActivityAI(DistributedPartyDanceActivityBaseAI):
    """ Reskinned dance floor for valentines party holiday. """

    def __init__(elf, air, partyDoId, x, y, h):
        DistributedPartyDanceActivityBaseAI.__init__(self,
                                                     air,
                                                     partyDoId,
                                                     x,
                                                     y,
                                                     h,
                                                     actId=PartyGlobals.ActivityIds.PartyValentineDance
                                                     )