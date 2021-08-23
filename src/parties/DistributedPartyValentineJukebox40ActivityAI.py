
from toontown.parties.DistributedPartyJukeboxActivityBaseAI import DistributedPartyJukeboxActivityBaseAI

from toontown.parties import PartyGlobals

class DistributedPartyJukebox40ActivityAI(DistributedPartyJukeboxActivityBaseAI ):
    notify = directNotify.newCategory("DistributedPartyJukeboxActivityAI")
    
    def __init__(self, air, partyDoId, x, y, h):
        self.notify.debug("Intializing.")
        DistributedPartyJukeboxActivityBaseAI.__init__(self,
                                            air,
                                            partyDoId,
                                            x, y, h,
                                            PartyGlobals.ActivityIds.PartyJukebox40,
                                            PartyGlobals.PhaseToMusicData40,
                                            )
    
