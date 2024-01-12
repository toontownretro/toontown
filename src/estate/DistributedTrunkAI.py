from otp.ai.AIBaseGlobal import *
from toontown.toonbase.ToontownModules import *
from direct.directnotify import DirectNotifyGlobal
from direct.fsm import ClassicFSM
from direct.distributed import ClockDelta
from . import DistributedFurnitureItemAI
from direct.task.Task import Task
from direct.fsm import State
from toontown.toon import ToonDNA
from toontown.ai import DatabaseObject
from toontown.toon import DistributedToonAI
from . import ClosetGlobals
from toontown.toon import InventoryBase
from toontown.estate.DistributedClosetAI import DistributedClosetAI

class DistributedTrunkAI(DistributedClosetAI):

    if __debug__:
        notify = DirectNotifyGlobal.directNotify.newCategory('DistributedTrunkAI')

    def setState(self, todo0, todo1, todo2, todo3, todo4, todo5, todo6, todo7):
        pass

    def removeItem(self, todo0, todo1, todo2, todo3):
        pass

    def setDNA(self, todo0, todo1, todo2, todo3, todo4, todo5, todo6, todo7, todo8, todo9, todo10, todo11, todo12, todo13):
        pass

    def setCustomerDNA(self, todo0, todo1, todo2, todo3, todo4, todo5, todo6, todo7, todo8, todo9, todo10, todo11, todo12, todo13):
        assert(self.notify.debug("setCustomerDNA"))
        # The AI doesn't set the DNA on swaps (finished=0) anymore.
        # This is to avoid bugged clothes on AI crashes while browsing.  Now the AI
        # just tells the clients the correct DNA for the current customer
        # and lets the clients set the value directly on the distributed
        # toon. The AI will still do a DNA change on purchase.

        # the av might be gone, so check first
        pass