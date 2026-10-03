from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.task import Task
from otp.distributed.OtpDoGlobals import *
from otp.distributed.DistributedDistrictAI import DistributedDistrictAI
from toontown.distributed import ToontownDistrictStatsAI
from direct.directutil import Throttler

class ToontownDistrictAI(DistributedDistrictAI):
    """
    See Also: "toontown/src/distributed/DistributedDistrict.py"
    """
    notify = directNotify.newCategory("ToontownDistrictAI")
    
    def __init__(self, air, name="untitled"):
        DistributedDistrictAI.__init__(self, air, name)
        self.stats = None
        self.allowAHNN = simbase.config.GetBool('want-ahnn-logging', 1)
        
        self.throttler = Throttler.Throttler(simbase.config.GetBool('want-throttler', 1))
        self.throttler.setDecay(simbase.config.GetInt('throttler-decay', 0))

    def generate(self):        
        DistributedDistrictAI.generate(self)
        self.stats = ToontownDistrictStatsAI.ToontownDistrictStatsAI(self.air)
        self.stats.toontownDistrictId = self.doId
        self.stats.generateOtpObject(self.stats.defaultParent, self.stats.defaultZone)
        self.throttler.updateCallback(self.b_allowAHNNLog)

    def delete(self):
        DistributedDistrictAI.delete(self)        
        if(self.stats is not None):
            self.stats.requestDelete()
            self.stats = None
        self.throttler.updateCallback(None)

    def recordSuspiciousEventData(self, eventData):
        self.throttler.recordData(eventData)

    def allowAHNNLog(self, allow):
        self.allowAHNN = allow

    def d_allowAHNNLog(self, allow):
        self.sendUpdate("allowAHNNLog", [allow])

    def b_allowAHNNLog(self, allow):
        self.allowAHNNLog(allow)
        self.d_allowAHNNLog(allow)

    def getAllowAHNNLog(self):
        return self.allowAHNN
