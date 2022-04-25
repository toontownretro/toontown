#-------------------------------------------------------------------------------
# Contact: 
# Created: 2011
#-------------------------------------------------------------------------------
from toontown.parties import PartyGlobals
from toontown.parties.DistributedPartyDanceActivityBase import DistributedPartyDanceActivityBase
from toontown.toonbase import TTLocalizer

class DistributedPartyValentineDanceActivity(DistributedPartyDanceActivityBase):
    notify = directNotify.newCategory("DistributedPartyValentineDanceActivity")

    def __init__(self, cr):
        DistributedPartyDanceActivityBase.__init__(self,
                                                   cr,
                                                   PartyGlobals.ActivityIds.PartyDance,
                                                   PartyGlobals.DancePatternToAnims,
                                                   model = "phase_13/models/parties/tt_m_ara_pty_danceFloorValentine"
                                                   )

    def getInstructions(self):
        return TTLocalizer.PartyDanceActivityInstructions

    def getTitle(self):
        return TTLocalizer.PartyDanceActivityTitle

    def load(self):
        """Load the dance floor, and handle 10 and 20 versions of disco ball."""
        DistributedPartyDanceActivityBase.load(self)
        parentGroup = self.danceFloor.find("**/discoBall_mesh")
        correctBall = self.danceFloor.find("**/discoBall_10")
        origBall = self.danceFloor.find("**/discoBall_mesh_orig")
        if not correctBall.isEmpty():
            numChildren = parentGroup.getNumChildren()
            for i in range(numChildren):
                child = parentGroup.getChild(i)
                if child != correctBall:
                    child.hide()
