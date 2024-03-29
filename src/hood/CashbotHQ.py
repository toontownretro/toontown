from toontown.toonbase.ToontownModules import *
from direct.directnotify import DirectNotifyGlobal
from . import CogHood
from toontown.toonbase import ToontownGlobals, TTLocalizer
from toontown.hood import ZoneUtil
from toontown.coghq import CashbotCogHQLoader

class CashbotHQ(CogHood.CogHood):
    notify = DirectNotifyGlobal.directNotify.newCategory('CashbotHQ')

    def __init__(self, parentFSM, doneEvent, dnaStore, hoodId):
        CogHood.CogHood.__init__(self, parentFSM, doneEvent, dnaStore, hoodId)
        self.id = ToontownGlobals.CashbotHQ
        self.cogHQLoaderClass = CashbotCogHQLoader.CashbotCogHQLoader
        # Create the safe zone state data
        self.storageDNAFile = None

        # this is a dummy skyfile... we're going to hide it after loading
        self.skyFile = "phase_3.5/models/props/TT_sky" # "phase_10/models/cogHQ/CashBotSky"

        self.titleColor = (0.5, 0.5, 0.5, 1.0)

    def load(self):
        CogHood.CogHood.load(self)
        self.parentFSM.getStateNamed("CashbotHQ").addChild(self.fsm)

    def unload(self):
        self.parentFSM.getStateNamed("CashbotHQ").removeChild(self.fsm)
        del self.cogHQLoaderClass
        CogHood.CogHood.unload(self)

    def enter(self, *args):
        CogHood.CogHood.enter(self, *args)
        localAvatar.setCameraFov(ToontownGlobals.CogHQCameraFov)
        base.camLens.setNearFar(ToontownGlobals.CashbotHQCameraNear,
                                ToontownGlobals.CashbotHQCameraFar)

    def exit(self):
        localAvatar.setCameraFov(ToontownGlobals.DefaultCameraFov)
        base.camLens.setNearFar(ToontownGlobals.DefaultCameraNear,
                                ToontownGlobals.DefaultCameraFar)
        CogHood.CogHood.exit(self)

    def spawnTitleText(self, zoneId, floorNum=None):
        if ZoneUtil.isMintInteriorZone(zoneId):
            # the mints display their name and a floor number
            text = '%s\n%s' % (
                ToontownGlobals.StreetNames[zoneId][-1],
                TTLocalizer.MintFloorTitle % (floorNum+1))
            self.doSpawnTitleText(text)
        else:
            CogHood.CogHood.spawnTitleText(self, zoneId)
