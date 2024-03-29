
from toontown.toonbase.ToontownModules import *
from . import ToonHood
from toontown.town import DLTownLoader
from toontown.safezone import DLSafeZoneLoader
from toontown.toonbase.ToontownGlobals import *

class DLHood(ToonHood.ToonHood):
    def __init__(self, parentFSM, doneEvent, dnaStore, hoodId):
        ToonHood.ToonHood.__init__(self, parentFSM, doneEvent, dnaStore, hoodId)
        self.id = DonaldsDreamland
        # Create the town state data
        self.townLoaderClass = DLTownLoader.DLTownLoader
        # Create the safe zone state data
        self.safeZoneLoaderClass = DLSafeZoneLoader.DLSafeZoneLoader
        self.storageDNAFile = "phase_8/dna/storage_DL.dna"
        # Dictionary which holds holiday specific lists of Storage DNA Files
        # Keyed off of the News Manager holiday IDs stored in ToontownGlobals
        self.holidayStorageDNADict = {WINTER_DECORATIONS : ['phase_8/dna/winter_storage_DL.dna'],
                                      WACKY_WINTER_DECORATIONS: ['phase_8/dna/winter_storage_DL.dna'],
                                      HALLOWEEN_PROPS : ['phase_8/dna/halloween_props_storage_DL.dna'],
                                      SPOOKY_PROPS: ['phase_8/dna/halloween_props_storage_DL.dna']}
        self.skyFile = "phase_8/models/props/DL_sky"
        self.titleColor = (1.0, 0.9, 0.5, 1.0)

        # Begin Shaders #
        self.ambientTemp = 7000
        self.ambientIntensity = 0.08
        self.sunTemp = 7500
        self.sunIntensity = 0.1
        self.skyLightScale = 0.2
        # End Shaders

    def load(self):
        ToonHood.ToonHood.load(self)
        self.parentFSM.getStateNamed("DLHood").addChild(self.fsm)

    def unload(self):
        self.parentFSM.getStateNamed("DLHood").removeChild(self.fsm)
        ToonHood.ToonHood.unload(self)

    def enter(self, *args):
        ToonHood.ToonHood.enter(self, *args)

    def exit(self):
        ToonHood.ToonHood.exit(self)
