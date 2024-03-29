
from toontown.toonbase.ToontownModules import *
from toontown.toonbase import TTLocalizer
from toontown.toonbase.ToontownBattleGlobals import *
from toontown.toonbase.ToontownGlobals import *
from .SuitBattleGlobals import *
from direct.interval.IntervalGlobal import *

from direct.directnotify import DirectNotifyGlobal
import string
from direct.gui import OnscreenText
from . import BattleBase

class PlayByPlayText(OnscreenText.OnscreenText):
    """
    This shows info about names of attacks as they happen, etc.
    """
    notify = DirectNotifyGlobal.directNotify.newCategory('PlayByPlayText')

    def __init__(self):
        OnscreenText.OnscreenText.__init__(
            self,
            mayChange = 1,
            pos = (0.0, 0.75),
            scale = TTLocalizer.PBPTonscreenText,
            fg = (1, 0, 0, 1),
            font = getSignFont(),
            wordwrap = 14
            )

    def getShowInterval(self, text, duration):
        return Sequence(
            Func(self.hide),
            Wait(duration * 0.3),
            Func(self.setText, text),
            Func(self.show),
            Wait(duration * 0.7),
            Func(self.hide),
            )

    def getToonsDiedInterval(self, textList, duration):
        assert len(textList) >= 0 and len(textList) <= 4
        track = Sequence(
            Func(self.hide),
            Wait(duration * 0.3)
            )
        waitGap = (0.6 / len(textList)) * duration
        for text in textList:
            newList = [
                Func(self.setText, text),
                Func(self.show),
                Wait(waitGap),
                Func(self.hide),
                ]
            track += newList
        track.append(
            Wait(duration * 0.1)
            )

        return track
