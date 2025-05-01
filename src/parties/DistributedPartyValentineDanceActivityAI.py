#-------------------------------------------------------------------------------
# Contact: 
# Created: 2011
#
# Purpose: AI component that manages which toons are currently dancing, who entered
#          and exited the dance floor, and broadcasts dance moves to all clients.
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