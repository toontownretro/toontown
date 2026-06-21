from direct.distributed import DistributedObjectAI
from direct.directnotify import DirectNotifyGlobal
from toontown.toonbase import ToontownGlobals
from toontown.golf import DistributedGolfHoleAI
from toontown.toonbase.ToontownModules import *

def GE():
    simbase.air.golf = DistributedGolfEntranceAI()
    simbase.air.golf.generateWithRequired(2000)
    return simbase.air.golf

class DistributedGolfEntranceAI(DistributedObjectAI.DistributedObjectAI):
    notify = directNotify.newCategory("DistributedGolfEntranceAI")
    
    def __init__(self):
        DistributedObjectAI.DistributedObjectAI.__init__(self, simbase.air)
        self.golfZone = None

    def generate(self):
        DistributedObjectAI.DistributedObjectAI.generate(self)

    def delete(self):
        DistributedObjectAI.DistributedObjectAI.delete(self)

    def sendToGolfCourse(self, avId):
        if self.golfZone == None:
            self.golfZone = self.air.allocateZone()
            someHole = DistributedGolfHoleAI.DistributedGolfHoleAI(self.golfZone)
            someHole.generateWithRequired(self.golfZone)
        self.notify.debug("Sending %s to course %s" % (avId, self.golfZone))
        self.sendUpdate("sendToGolfCourse", [avId, self.golfZone])
