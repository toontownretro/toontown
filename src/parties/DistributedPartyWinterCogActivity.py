#-------------------------------------------------------------------------------
# Contact: Mark Wojtowicz
# Created: June 2010
#-------------------------------------------------------------------------------

from toontown.parties.DistributedPartyCogActivity import DistributedPartyCogActivity

class DistributedPartyWinterCogActivity(DistributedPartyCogActivity):
    """ Reskinned cog for winter holiday. """

    def __init__( self, cr ):
        DistributedPartyCogActivity.__init__(self, cr, "phase_13/models/parties/tt_m_ara_pty_cogPieArenaWinter")
