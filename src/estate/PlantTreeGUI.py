from direct.directnotify import DirectNotifyGlobal
from direct.showbase.ShowBase import *
from toontown.toonbase import TTLocalizer
import string
from direct.fsm import StateData
from toontown.toonbase.ToontownBattleGlobals import gagIsPaidOnly
from toontown.toontowngui.TeaserPanel import TeaserPanel

class PlantTreeGUI(StateData.StateData):
    notify = DirectNotifyGlobal.directNotify.newCategory('PlantTreeGUI')

    def __init__(self, doneEvent):
        assert self.notify.debugStateCall(self)
        self.doneEvent = doneEvent
        self.oldActivateMode = base.localAvatar.inventory.activateMode
        self._teaserPanel = None
        base.localAvatar.inventory.setActivateMode('plantTree')
        base.localAvatar.inventory.show()
        # If someone clicks an item, we want to know about it.
        self.accept('inventory-selection', self.__handleInventory)
        self.accept('inventory-pass', self.__handleCancel)

    def destroy(self):
        assert self.notify.debugStateCall(self)
        # Ignore the inventory selection
        self.ignore('inventory-selection')
        self.ignore('inventory-pass')
        # Put the inventory away
        base.localAvatar.inventory.setActivateMode(self.oldActivateMode)
        base.localAvatar.inventory.hide()
        if self._teaserPanel:
            self._teaserPanel.destroy()
            self._teaserPanel = None

    def __handleInventory(self, track, level):
        assert self.notify.debugStateCall(self)
        if (gagIsPaidOnly(track, level) and not base.cr.isPaid()):
            self._teaserPanel = TeaserPanel('plantGags')
            return
        if (base.localAvatar.inventory.numItem(track, level) > 0):
            # Report the selection
            messenger.send(self.doneEvent, [True, track, level])
        else:
            self.notify.error(
                "An item we don't have: track %s level %s was selected." %
                (track, level))
        return

    def __handleCancel(self):
        assert self.notify.debugStateCall(self)
        messenger.send(self.doneEvent, [False, None, None])
