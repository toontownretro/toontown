
from toontown.parties.DistributedPartyJukeboxActivityBaseAI import DistributedPartyJukeboxActivityBaseAI

from toontown.parties import PartyGlobals

class DistributedPartyValentineJukeboxActivityAI(DistributedPartyJukeboxActivityBaseAI ):
    """ Reskinned jukebox for valentine holiday. """
    
    def __init__(self, air, partyDoId, x, y, h):
        self.notify.debug("Intializing.")
        DistributedPartyJukeboxActivityBaseAI.__init__(self,
                                            air,
                                            partyDoId,
                                            x, y, h,
                                            PartyGlobals.ActivityIds.PartyJukebox,
                                            PartyGlobals.PhaseToMusicData,
                                            )
    
