from direct.directnotify import DirectNotifyGlobal
from toontown.estate import DistributedClosetAI

#dclass DistributedTrunk: DistributedCloset {
#  setState(uint8,
#           uint32, uint32,
#		   string,
#		   uint8array, uint8array, uint8array, uint8array)
#		   broadcast ram;
#  removeItem(uint8, uint8, uint8, uint8) airecv clsend;    //possible security breach: trashDNA and which need sanity check...need help = SAMIR
#  setDNA(uint8, uint8, uint8, uint8, uint8, uint8, uint8, uint8, uint8, uint8, uint8, uint8, int8, uint8) airecv clsend;       //security breach: invalid finished not checked, dna needs sanity check
#
#  // Server tells all clients how to clothe the current customer
#  setCustomerDNA(uint32, uint8, uint8, uint8, uint8, uint8, uint8, uint8, uint8, uint8, uint8, uint8, uint8, uint8) broadcast ram;
#};

class DistributedTrunkAI(DistributedClosetAI.DistributedClosetAI):

    if __debug__:
        notify = DirectNotifyGlobal.directNotify.newCategory('DistributedTrunkAI')

    def __init__(self, air, furnitureMgr, item):
        DistributedFurnitureItemAI.DistributedFurnitureItemAI.__init__(
            self, air, furnitureMgr, item)
        self.ownerId = self.furnitureMgr.house.ownerId
        self.ownerAv = None
        self.timedOut = 0
        self.busy = 0
        self.customerDNA = None
        self.customerId = None
        self.deletedHats = []
        self.deletedGlasses = []
        self.deletedBackpacks = []
        self.deletedShoes = []
        self.dummyToonAI = None #in case we open a closet of someone not online, keep track of it

    def delete(self):
        self.notify.debug("delete()")
        self.ignoreAll()
        self.customerDNA = None
        self.customerId = None
        del self.deletedHats
        del self.deletedGlasses
        del self.deletedBackpacks
        del self.deletedShoes
        taskMgr.remove(self.uniqueName('clearMovie'))
        DistributedFurnitureItemAI.DistributedFurnitureItemAI.delete(self)

    # self, trashBlob, which, ..., ...?
    def removeItem(self, todo0, todo1, todo2, todo3):
        pass

    def setDNA(self, hatIdx, hatTexture, hatColor,
                     glassesIdx, glassesTexture, glassesColor,
                     backpackIdx, backpackTexture, backpackColor,
                     shoesIdx, shoesTexture, shoesColor,
                     finished, which):
        pass


    if __debug__:
        def debugPrint(self, message):
            """for debugging"""
            return self.notify.debug(
                    str(self.__dict__.get('block', '?'))+' '+message)