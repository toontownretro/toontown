#################################################
# CrashLeaderBoard decorator class for non-dna based
# decoration changes to hoods
#################################################

# Panda3D imports
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.ClockDelta import *
from direct.interval.IntervalGlobal import *

from . import HolidayDecorator
from toontown.toonbase import ToontownGlobals
from toontown.toonbase.ToontownModules import Vec4, loadDNAFile, CSDefault, TransformState, NodePath, TransparencyAttrib
from toontown.hood import GSHood

class CrashedLeaderBoardDecorator(HolidayDecorator.HolidayDecorator):

    notify = DirectNotifyGlobal.directNotify.newCategory("CrashedLeaderBoardDecorator")

    def __init__(self):
        HolidayDecorator.HolidayDecorator.__init__(self)


    def decorate(self):
        # Load the specified seasonal storage file
        self.updateHoodDNAStore()
        self.swapIval = self.getSwapVisibleIval()
        if self.swapIval:
            self.swapIval.start()

        holidayIds = base.cr.newsManager.getDecorationHolidayId()
        if ToontownGlobals.CRASHED_LEADERBOARD not in holidayIds:
            return

        if ConfigVariableBool('want-crashedLeaderBoard-Smoke', 1).getValue():
            self.startSmokeEffect()

    def startSmokeEffect(self):
        if isinstance(base.cr.playGame.getPlace().loader.hood, GSHood.GSHood):
            base.cr.playGame.getPlace().loader.startSmokeEffect()

    def stopSmokeEffect(self):
        if isinstance(base.cr.playGame.getPlace().loader.hood, GSHood.GSHood):
            base.cr.playGame.getPlace().loader.stopSmokeEffect()

    def undecorate(self):
        if ConfigVariableBool('want-crashedLeaderBoard-Smoke', 1).getValue():
            self.stopSmokeEffect()

        # if there are any other decoration holidays running
        holidayIds = base.cr.newsManager.getDecorationHolidayId()
        if len(holidayIds)>0:
            self.decorate()
            return

        # Reload the regular storage file
        storageFile = base.cr.playGame.hood.storageDNAFile
        if storageFile:
            loadDNAFile(self.dnaStore, storageFile, CSDefault)
        self.swapIval = self.getSwapVisibleIval()
        if self.swapIval:
            self.swapIval.start()
