from . import CatalogItem
from .CatalogAccessoryItemGlobals import * 
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer
from toontown.toon import ToonDNA
import random, types
from direct.showbase import PythonUtil
from direct.gui.DirectGui import *
from toontown.toonbase.ToontownModules import *

class CatalogAccessoryItem(CatalogItem.CatalogItem):

    def makeNewItem(self, accessoryType, loyaltyDays = 0):
        self.accessoryType = accessoryType
        self.loyaltyDays = loyaltyDays
        CatalogItem.CatalogItem.makeNewItem(self)

    def storedInTrunk(self):
        # Returns true if this kind of item takes up space in the
        # avatar's trunk, false otherwise.
        return 1

    def notOfferedTo(self, avatar):
        # Boys can only buy boy clothing, and girls can only buy girl
        # clothing.  Sorry.
        article = AccessoryTypes[self.accessoryType][ATArticle]

        if article in [AHat, AGlasses, ABackpack, AShoes]:
            # This article is androgynous.
            return 0
            
        forBoys = article in [ABoysHat, ABoysGlasses, ABoysBackpack, ABoysShoes]
        if avatar.getStyle().getGender() == 'm':
            return not forBoys
        else:
            return forBoys

    def forBoysOnly(self):
        article = AccessoryTypes[self.accessoryType][ATArticle]
        if article in [ABoysHat, ABoysGlasses, ABoysBackpack, ABoysShoes]:
            return 1
        else:
            return 0

    def forGirlsOnly(self):
        article = AccessoryTypes[self.accessoryType][ATArticle]
        if article in [AGirlsHat, AGirlsGlasses, AGirlsBackpack, AGirlsShoes]:
            return 1
        else:
            return 0

    def getPurchaseLimit(self):
        # Returns the maximum number of this particular item an avatar
        # may purchase.  This is either 0, 1, or some larger number; 0
        # stands for infinity.
        return 1

    def reachedPurchaseLimit(self, avatar):
        # Returns true if the item cannot be bought because the avatar
        # has already bought his limit on this item.

        if avatar.onOrder.count(self) != 0:
            # It's on the way.
            return 1

        if avatar.onGiftOrder.count(self) != 0:
            # someone has given it to you
            return 1

        if avatar.mailboxContents.count(self) != 0:
            # It's waiting in the mailbox.
            return 1

        if self in avatar.awardMailboxContents or self in avatar.onAwardOrder:
            # check award queue and award mailbox too
            return 1

        str = AccessoryTypes[self.accessoryType][ATString]

        if self.isHat():
            # Check if the avatar is already wearing this hat.
            defn = ToonDNA.HatStyles[str]
            hat = avatar.getHat()
            if (hat[0] == defn[0] and
                hat[1] == defn[1] and
                hat[2] == defn[2]):
                return 1

            # Check if the shirt is in the avatar's closet.
            l = avatar.hatList
            for i in range(0, len(l), 3):
                if (l[i] == defn[0] and
                    l[i + 1] == defn[1] and
                    l[i + 2] == defn[2]):
                    return 1

        elif self.areGlasses():
            # Check if the avatar is already wearing these glasses.
            defn = ToonDNA.GlassesStyles[str]
            glasses = avatar.getGlasses()
            if (glasses[0] == defn[0] and
                glasses[1] == defn[1] and
                glasses[2] == defn[2]):
                return 1

            # Check if the shirt is in the avatar's closet.
            l = avatar.glassesList
            for i in range(0, len(l), 3):
                if (l[i] == defn[0] and
                    l[i + 1] == defn[1] and
                    l[i + 2] == defn[2]):
                    return 1

        elif self.isBackpack():
            # Check if the avatar is already wearing this backpack.
            defn = ToonDNA.BackpackStyles[str]
            backpack = avatar.getBackpack()
            if (backpack[0] == defn[0] and
                backpack[1] == defn[1] and
                backpack[2] == defn[2]):
                return 1

            # Check if the shirt is in the avatar's closet.
            l = avatar.backpackList
            for i in range(0, len(l), 3):
                if (l[i] == defn[0] and
                    l[i + 1] == defn[1] and
                    l[i + 2] == defn[2]):
                    return 1

        else:
            # Check if the avatar is already wearing these shoes.
            defn = ToonDNA.ShoesStyles[str]
            shoes = avatar.getShoes()
            if (shoes[0] == defn[0] and
                shoes[1] == defn[1] and
                shoes[2] == defn[2]):
                return 1

            # Check if the shirt is in the avatar's closet.
            l = avatar.shoesList
            for i in range(0, len(l), 3):
                if (l[i] == defn[0] and
                    l[i + 1] == defn[1] and
                    l[i + 2] == defn[2]):
                    return 1

        # Not found anywhere; go ahead and buy it.
        return 0


    def getTypeName(self):
        # e.g. "shirt", "shorts", etc.
        #article = ClothingTypes[self.clothingType][CTArticle]
        #return TTLocalizer.ClothingArticleNames[article]

        # Until we have descriptive names per-item below, just return
        # "Clothing" here.
        return TTLocalizer.AccessoryTypeName

    def getName(self):
        typeName = TTLocalizer.AccessoryTypeNames.get(self.accessoryType, 0)
        # check for a specific item name
        if typeName:
            return typeName
        # otherwise use a generic name
        else:
            article = AccessoryTypes[self.accessoryType][ATArticle]
            return TTLocalizer.AccessoryArticleNames[article]

    def recordPurchase(self, avatar, optional):
        # Updates the appropriate field on the avatar to indicate the
        # purchase (or delivery).  This makes the item available to
        # use by the avatar.  This method is only called on the AI side.

        if avatar.isTrunkFull():
            if avatar.getMaxAccessories() == 0:
                return ToontownGlobals.P_NoTrunk
            else:
                return ToontownGlobals.P_NoRoomForItem

        str = AccessoryTypes[self.accessoryType][ATString]

        if self.isHat():
            defn = ToonDNA.HatStyles[str]
            if not avatar.checkAccessorySanity(ToonDNA.HAT, defn[0], defn[1], defn[2]):
                self.notify.warning('Avatar %s lost hat %d %d %d; invalid item.' % (avatar.doId, defn[0], defn[1], defn[2]))
                return ToontownGlobals.P_ItemAvailable
            hat = avatar.getHat()
            added = avatar.addToAccessoriesList(ToonDNA.HAT, hat[0], hat[1], hat[2])
            if added:
                avatar.b_setHatList(avatar.getHatList())
                self.notify.info('Avatar %s put hat %d,%d,%d in trunk.' % (avatar.doId, hat[0], hat[1], hat[2]))
            else:
                self.notify.warning('Avatar %s lost current hat %d %d %d; trunk full.' % (avatar.doId, hat[0], hat[1], hat[2]))
            avatar.b_setHat(defn[0], defn[1], defn[2])

        elif self.areGlasses():
            defn = ToonDNA.GlassesStyles[str]
            if not avatar.checkAccessorySanity(ToonDNA.GLASSES, defn[0], defn[1], defn[2]):
                self.notify.warning('Avatar %s lost glasses %d %d %d; invalid item.' % (avatar.doId, defn[0], defn[1], defn[2]))
                return ToontownGlobals.P_ItemAvailable
            glasses = avatar.getGlasses()
            added = avatar.addToAccessoriesList(ToonDNA.GLASSES, glasses[0], glasses[1], glasses[2])
            if added:
                avatar.b_setGlassesList(avatar.getGlassesList())
                self.notify.info('Avatar %s put glasses %d,%d,%d in trunk.' % (avatar.doId, glasses[0], glasses[1], glasses[2]))
            else:
                self.notify.warning('Avatar %s lost current glasses %d %d %d; trunk full.' % (avatar.doId, glasses[0], glasses[1], glasses[2]))
            avatar.b_setGlasses(defn[0], defn[1], defn[2])

        elif self.isBackpack():
            defn = ToonDNA.BackpackStyles[str]
            if not avatar.checkAccessorySanity(ToonDNA.BACKPACK, defn[0], defn[1], defn[2]):
                self.notify.warning('Avatar %s lost backpack %d %d %d; invalid item.' % (avatar.doId, defn[0], defn[1], defn[2]))
                return ToontownGlobals.P_ItemAvailable
            backpack = avatar.getBackpack()
            added = avatar.addToAccessoriesList(ToonDNA.BACKPACK, backpack[0], backpack[1], backpack[2])
            if added:
                avatar.b_setBackpackList(avatar.getBackpackList())
                self.notify.info('Avatar %s put backpack %d,%d,%d in trunk.' % (avatar.doId, backpack[0], backpack[1], backpack[2]))
            else:
                self.notify.warning('Avatar %s lost current backpack %d %d %d; trunk full.' % (avatar.doId, backpack[0], backpack[1], backpack[2]))
            avatar.b_setBackpack(defn[0], defn[1], defn[2])

        else:
            defn = ToonDNA.ShoesStyles[str]
            if not avatar.checkAccessorySanity(ToonDNA.SHOES, defn[0], defn[1], defn[2]):
                self.notify.warning('Avatar %s lost shoes %d %d %d; invalid item.' % (avatar.doId, defn[0], defn[1], defn[2]))
                return ToontownGlobals.P_ItemAvailable
            shoes = avatar.getShoes()
            added = avatar.addToAccessoriesList(ToonDNA.SHOES, shoes[0], shoes[1], shoes[2])
            if added:
                avatar.b_setShoesList(avatar.getShoesList())
                self.notify.info('Avatar %s put shoes %d,%d,%d in trunk.' % (avatar.doId, shoes[0], shoes[1], shoes[2]))
            else:
                self.notify.warning('Avatar %s lost current shoes %d %d %d; trunk full.' % (avatar.doId, shoes[0], shoes[1], shoes[2]))
            avatar.b_setShoes(defn[0], defn[1], defn[2])
        avatar.d_catalogGenAccessories()
        return ToontownGlobals.P_ItemAvailable

    def getDeliveryTime(self):
        # Returns the elapsed time in minutes from purchase to
        # delivery for this particular item.
        return 60  # 1 hour.

    def getPicture(self, avatar):
        model = self.loadModel()
        spin = 1
        model.setBin('unsorted', 0, 1)

        assert (not self.hasPicture)
        self.hasPicture = True

        return self.makeFrameModel(model, spin)

    def applyColor(self, model, color):
        if model == None or color == None:
            return
        if isinstance(color, str):
            tex = loader.loadTexture(color)
            tex.setMinfilter(Texture.FTLinearMipmapLinear)
            tex.setMagfilter(Texture.FTLinear)
            model.setTexture(tex, 1)
        else:
            needsAlpha = color[3] != 1
            color = VBase4(color[0], color[1], color[2], color[3])
            model.setColorScale(color, 1)
            if needsAlpha:
                model.setTransparency(1)
        return

    def loadModel(self):
        modelPath = self.getFilename()
        if self.areShoes():
            str = AccessoryTypes[self.accessoryType][ATString]
            defn = ToonDNA.ShoesStyles[str]
            legModel = loader.loadModel('phase_3/models/char/tt_a_chr_dgm_shorts_legs_1000')
            model = legModel.find('**/' + modelPath)
        else:
            model = loader.loadModel(modelPath)
        texture = self.getTexture()
        if texture:
            self.applyColor(model, texture)
        colorVec4 = self.getColor()
        if colorVec4:
            modelColor = (colorVec4.getX(), colorVec4.getY(), colorVec4.getZ())
            self.applyColor(model, modelColor)
        model.flattenLight()
        return model

    def requestPurchase(self, phone, callback):
        # Orders the item via the indicated telephone.  Some items
        # will pop up a dialog querying the user for more information
        # before placing the order; other items will order
        # immediately.

        # In either case, the function will return immediately before
        # the transaction is finished, but the given callback will be
        # called later with two parameters: the return code (one of
        # the P_* symbols defined in ToontownGlobals.py), followed by the
        # item itself.

        # This method is only called on the client.
        from toontown.toontowngui import TTDialog
        avatar = base.localAvatar
        
        accessoriesOnOrder = 0
        for item in avatar.onOrder + avatar.mailboxContents:
            if item.storedInTrunk():
                accessoriesOnOrder += 1

        if avatar.isTrunkFull(accessoriesOnOrder):
            # If the avatar's closet is full, pop up a dialog warning
            # the user, and give him a chance to bail out.
            self.requestPurchaseCleanup()
            buttonCallback = PythonUtil.Functor(
                self.__handleFullPurchaseDialog, phone, callback)
            if avatar.getMaxAccessories() == 0:
                text = TTLocalizer.CatalogPurchaseNoTrunk
            else:
                text = TTLocalizer.CatalogPurchaseTrunkFull
            self.dialog = TTDialog.TTDialog(
                style = TTDialog.YesNo,
                text = text,
                text_wordwrap = 15,
                command = buttonCallback,
                )
            self.dialog.show()

        else:
            # The avatar's closet isn't full; just buy it.
            CatalogItem.CatalogItem.requestPurchase(self, phone, callback)

    def requestPurchaseCleanup(self):
        if hasattr(self, "dialog"):
            self.dialog.cleanup()
            del self.dialog

    def __handleFullPurchaseDialog(self, phone, callback, buttonValue):
        from toontown.toontowngui import TTDialog
        self.requestPurchaseCleanup()
        if buttonValue == DGG.DIALOG_OK:
            # Go ahead and purchase it.
            CatalogItem.CatalogItem.requestPurchase(self, phone, callback)
        else:
            callback(ToontownGlobals.P_UserCancelled, self)

    def getAcceptItemErrorText(self, retcode):
        # Returns a string describing the error that occurred on
        # attempting to accept the item from the mailbox.  The input
        # parameter is the retcode returned by recordPurchase() or by
        # mailbox.acceptItem().
        if retcode == ToontownGlobals.P_ItemAvailable:
            if self.isHat():
                return TTLocalizer.CatalogAcceptHat
            elif self.areGlasses():
                return TTLocalizer.CatalogAcceptGlasses
            elif self.isBackpack():
                return TTLocalizer.CatalogAcceptBackpack
            else:
                return TTLocalizer.CatalogAcceptShoes
        elif retcode == ToontownGlobals.P_NoRoomForItem:
            return TTLocalizer.CatalogAcceptTrunkFull
        elif retcode == ToontownGlobals.P_NoTrunk:
            return TTLocalizer.CatalogAcceptNoTrunk
        return CatalogItem.CatalogItem.getAcceptItemErrorText(self, retcode)

    def isHat(self):
        article = AccessoryTypes[self.accessoryType][ATArticle]
        return article in [AHat, ABoysHat, AGirlsHat]

    def areGlasses(self):
        article = AccessoryTypes[self.accessoryType][ATArticle]
        return article in [AGlasses, ABoysGlasses, AGirlsGlasses]

    def isBackpack(self):
        article = AccessoryTypes[self.accessoryType][ATArticle]
        return article in [ABackpack, ABoysBackpack, AGirlsBackpack]

    def areShoes(self):
        article = AccessoryTypes[self.accessoryType][ATArticle]
        return article in [AShoes, ABoysShoes, AGirlsShoes]

    def output(self, store = -1):
        return "CatalogAccessoryItem(%s, %s)" % (
            self.accessoryType,
            self.formatOptionalData(store))

    def getFilename(self):
        str = AccessoryTypes[self.accessoryType][ATString]
        if self.isHat():
            # It's a hat.
            defn = ToonDNA.HatStyles[str]
            modelPath = ToonDNA.HatModels[defn[0]]
        elif self.areGlasses():
            # They're glasses..
            defn = ToonDNA.GlassesStyles[str]
            modelPath = ToonDNA.GlassesModels[defn[0]]
        elif self.isBackpack():
            # It's a backpack.
            defn = ToonDNA.BackpackStyles[str]
            modelPath = ToonDNA.BackpackModels[defn[0]]
        else:
            # They're shoes.
            defn = ToonDNA.ShoesStyles[str]
            modelPath = ToonDNA.ShoesModels[defn[0]]
        return modelPath

    def getTexture(self):
        str = AccessoryTypes[self.accessoryType][ATString]
        if self.isHat():
            defn = ToonDNA.HatStyles[str]
            modelPath = ToonDNA.HatTextures[defn[1]]
        elif self.areGlasses():
            defn = ToonDNA.GlassesStyles[str]
            modelPath = ToonDNA.GlassesTextures[defn[1]]
        elif self.isBackpack():
            defn = ToonDNA.BackpackStyles[str]
            modelPath = ToonDNA.BackpackTextures[defn[1]]
        else:
            defn = ToonDNA.ShoesStyles[str]
            modelPath = ToonDNA.ShoesTextures[defn[1]]
        return modelPath

    def getColor(self):
        return None

    def compareTo(self, other):
        return self.accessoryType - other.accessoryType

    def getHashContents(self):
        return self.accessoryType

    def getBasePrice(self):
        return AccessoryTypes[self.accessoryType][ATBasePrice]

    def getEmblemPrices(self):
        result = ()
        info = AccessoryTypes[self.accessoryType]
        if ATEmblemPrices <= len(info) - 1:
            result = info[ATEmblemPrices]
        return result

    def decodeDatagram(self, di, versionNumber, store):
        CatalogItem.CatalogItem.decodeDatagram(self, di, versionNumber, store)
        self.accessoryType = di.getUint16()
        if versionNumber >= 6:
            self.loyaltyDays = di.getUint16()
        else:
            #RAU this seeems safe, as an old user would never have the new loyalty items
            self.loyaltyDays = 0

        # Now validate the indices by assigning into a variable,
        # color, which we don't care about other than to prove the
        # clothingType and colorIndex map to a valid definition.  If
        # they don't, the following will raise an exception.            
        str = AccessoryTypes[self.accessoryType][ATString]
        if self.isHat():
            defn = ToonDNA.HatStyles[str]
        elif self.areGlasses():
            defn = ToonDNA.GlassesStyles[str]
        elif self.isBackpack():
            defn = ToonDNA.BackpackStyles[str]
        else:
            defn = ToonDNA.ShoesStyles[str]
        color = ToonDNA.ClothesColors[defn[2]]

    def encodeDatagram(self, dg, store):
        CatalogItem.CatalogItem.encodeDatagram(self, dg, store)
        dg.addUint16(self.accessoryType)
        dg.addUint16(self.loyaltyDays)

    def isGift(self):
        if self.getEmblemPrices():
            return 0
        if (self.loyaltyRequirement() > 0):
            return 0
        elif self.accessoryType in LoyaltyAccessoryItems:
            # we can get this case through award manager
            # catalog generator is not creating the catalog item, hence no loyalty days
            return 0
        else:
            return 1


def getAllAccessories(*accessoryTypes):
    # This function returns a list of all possible
    # CatalogClothingItems (that is, all color variants) for the
    # indicated type index(es).

    accessories = []
    for accessoryType in accessoryTypes:
        base = CatalogAccessoryItem(accessoryType)
        accessories.append(base)

    return accessories
