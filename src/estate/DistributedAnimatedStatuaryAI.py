from toontown.estate import DistributedStatuaryAI
from direct.directnotify import DirectNotifyGlobal
from otp.ai.AIBase import *
from . import GardenGlobals

class DistributedAnimatedStatuaryAI(DistributedStatuaryAI.DistributedStatuaryAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedAnimatedStatuaryAI')

    def __init__(self, typeIndex = 234, waterLevel = 0, growthLevel = 0, optional = None, ownerIndex = 0, plot = 0):
        DistributedStatuaryAI.DistributedStatuaryAI.__init__(self, typeIndex, waterLevel, growthLevel, optional, ownerIndex, plot)
        self.notify.debug('constructing DistributedAnimatedStatuaryAI')
