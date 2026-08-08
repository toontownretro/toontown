from toontown.estate import DistributedStatuaryAI

class DistributedAnimatedStatuaryAI(DistributedStatuaryAI.DistributedStatuaryAI):
    """
    Regular statues and toon statues don't change once planted.
    This class does, initially created for the melting snowman
    """
    notify = directNotify.newCategory("DistributedAnimatedStatuaryAI")

    def __init__(self, typeIndex = 234, waterLevel = 0, growthLevel = 0, optional = None, ownerIndex = 0, plot = 0):
        DistributedStatuaryAI.DistributedStatuaryAI.__init__(self, typeIndex,
                                                             waterLevel, growthLevel,
                                                             optional, ownerIndex, plot)
