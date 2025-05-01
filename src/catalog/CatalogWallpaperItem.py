from .CatalogSurfaceItem import *

## TODO:
# Get rid of XXX2 wallpaper pattens
# Initialize borderIndex and borderColorIndex

# Indicies into Wallpaper Textures Dictionary
WTTextureName = 0
WTColor = 1
WTBorderList = 2
WTBasePrice = 3

BDTextureName = 0
BDColor = 1

All = (1000,1010,1020,1030,1040,1050,1060,1070)


# These index numbers are written to the database.  Don't mess with them.
# Also see TTLocalizer.WallpaperNames.
# Each is a list of (model, colorlist, border list, price)
# 0 in border list means no border
WallpaperTypes = {
    # Parchment
    1000 : ("phase_5.5/maps/flat_wallpaper1.txo", CTFlatColor, (0,1000,), 180),
    # Milan
    1100 : ("phase_5.5/maps/big_stripes1.txo", CTWhite, (0,1010,), 180),
    1110 : ("phase_5.5/maps/big_stripes2.txo", CTWhite, (0,1040,), 180),
    1120 : ("phase_5.5/maps/big_stripes3.txo", CTWhite, (0,1030,), 180),
    1130 : ("phase_5.5/maps/big_stripes4.txo", CTWhite, (0,1010,), 180),
    1140 : ("phase_5.5/maps/big_stripes5.txo", CTWhite, (0,1020,), 180),
    1150 : ("phase_5.5/maps/big_stripes6.txo", CTWhite, (0,1020,), 180),
    # Dover
    1200 : ("phase_5.5/maps/stripeB1.txo", CTWhite, (0,1000,), 180),
    1210 : ("phase_5.5/maps/stripeB2.txo", CTWhite, (0,1000,), 180),
    1220 : ("phase_5.5/maps/stripeB3.txo", CTWhite, (0,1000,), 180),
    1230 : ("phase_5.5/maps/stripeB4.txo", CTWhite, (0,1000,), 180),
    # stripeB5 ends up in phase3.5 because it is placed on some of the
    # toon_interior walls.
    1240 : ("phase_3.5/maps/stripeB5.txo", CTWhite, (0,1000,), 180),
    1250 : ("phase_5.5/maps/stripeB6.txo", CTWhite, (0,1000,), 180),
    1260 : ("phase_5.5/maps/stripeB7.txo", CTWhite, (0,1000,), 180),
    # Victoria
    1300 : ("phase_5.5/maps/squiggle1.txo", CTWhite, (0,), 180),
    1310 : ("phase_5.5/maps/squiggle2.txo", CTWhite, (0,), 180),
    1320 : ("phase_5.5/maps/squiggle3.txo", CTWhite, (0,), 180),
    1330 : ("phase_5.5/maps/squiggle4.txo", CTWhite, (0,), 180),
    1340 : ("phase_5.5/maps/squiggle5.txo", CTWhite, (0,), 180),
    1350 : ("phase_5.5/maps/squiggle6.txo", CTWhite, (0,), 180),
    # Newport
    1400 : ("phase_5.5/maps/stripes_cyan.txo", CTWhite, (0,1000,), 180),
    1410 : ("phase_5.5/maps/stripes_green.txo", CTWhite, (0,1000,), 180),
    1420 : ("phase_5.5/maps/stripes_magenta.txo", CTWhite, (0,1000,), 180),
    1430 : ("phase_5.5/maps/two_stripes1.txo", CTWhite, (0,1000,), 180),
    1440 : ("phase_5.5/maps/two_stripes2.txo", CTWhite, (0,1000,), 180),
    1450 : ("phase_5.5/maps/two_stripes3.txo", CTWhite, (0,1000,), 180),
    # Pastoral
    1500 : ("phase_5.5/maps/leaves1.txo", CTWhite, (0,), 180),
    1510 : ("phase_5.5/maps/leaves2.txo", CTWhite, (0,), 180),
    1520 : ("phase_5.5/maps/leaves3.txo", CTWhite, (0,), 180),
    # Harlequin
    1600 : ("phase_5.5/maps/diamonds2_cherries.txo", CTWhite, (0,1000,), 180),
    1610 : ("phase_5.5/maps/diamonds3_cherries.txo", CTWhite, (0,1000,), 180),
    1620 : ("phase_5.5/maps/diamonds3_cherry.txo", CTWhite, (0,1000,), 180),
    1630 : ("phase_5.5/maps/diamonds4_cherries.txo", CTWhite, (0,1000,), 180),
    1640 : ("phase_5.5/maps/diamonds4_cherry.txo", CTWhite, (0,1000,), 180),
    1650 : ("phase_5.5/maps/diamonds5_cherries.txo", CTWhite, (0,1000,), 180),
    1660 : ("phase_5.5/maps/diamonds6_cherry.txo", CTWhite, (0,1000,), 180),
    # Moon
    1700 : ("phase_5.5/maps/moon1.txo", CTWhite, (0,), 180),
    1710 : ("phase_5.5/maps/moon2.txo", CTWhite, (0,), 180),
    1720 : ("phase_5.5/maps/moon3.txo", CTWhite, (0,), 180),
    1730 : ("phase_5.5/maps/moon4.txo", CTWhite, (0,), 180),
    1740 : ("phase_5.5/maps/moon5.txo", CTWhite, (0,), 180),
    1750 : ("phase_5.5/maps/moon6.txo", CTWhite, (0,), 180),
    1760 : ("phase_5.5/maps/moon7.txo", CTWhite, (0,), 180),
    # Stars
    1800 : ("phase_5.5/maps/stars1.txo", CTWhite, (0,), 180),
    1810 : ("phase_5.5/maps/stars2.txo", (CT_BLUE2, CT_PINK2, CT_RED), (0,), 180),
    1820 : ("phase_5.5/maps/stars3.txo", (CT_BLUE2, CT_PINK2, CT_RED, CT_WHITE), (0,), 180),
    1830 : ("phase_5.5/maps/stars4.txo", CTWhite, (0,), 180),
    1840 : ("phase_5.5/maps/stars5.txo", CTWhite, (0,), 180),
    1850 : ("phase_5.5/maps/stars6.txo", CTWhite, (0,), 180),
    1860 : ("phase_5.5/maps/stars7.txo", (CT_BEIGE2, CT_WHITE), (0,), 180),
    # Flowers
    1900 : ("phase_5.5/maps/wall_paper_flower1.txo", CTWhite, (0,1000), 180),
    1910 : ("phase_5.5/maps/wall_paper_flower2.txo", CTWhite, (0,1000), 180),
    1920 : ("phase_5.5/maps/wall_paper_flower3.txo", CTWhite, (0,1000), 180),
    1930 : ("phase_5.5/maps/wall_paper_flower4.txo", CTWhite, (0,1000), 180),
    1940 : ("phase_5.5/maps/wall_paper_flower5.txo", CTWhite, (0,1000), 180),
    1950 : ("phase_5.5/maps/wall_paper_flower6.txo", CTWhite, (0,1000), 180),
    # Spring Garden
    2000 : ("phase_5.5/maps/flat_wallpaper1.txo", (CT_BEIGE, CT_BEIGE2, CT_RED), (1050,), 180),
    2010 : ("phase_5.5/maps/flat_wallpaper1.txo", (CT_BLUE2, CT_PINK2), (1060,), 180),
    2020 : ("phase_5.5/maps/flat_wallpaper1.txo", (CT_BEIGE2, CT_BLUE2, CT_PINK2, CT_BEIGE, CT_RED), (1070,), 180),
    # Formal Garden
    2100 : ("phase_5.5/maps/big_stripes1.txo", CTWhite, (1050,), 180),
    2110 : ("phase_5.5/maps/big_stripes2.txo", CTWhite, (1050,), 180),
    2120 : ("phase_5.5/maps/big_stripes3.txo", CTWhite, (1060,), 180),
    2130 : ("phase_5.5/maps/big_stripes3.txo", CTWhite, (1070,), 180),
    2140 : ("phase_5.5/maps/big_stripes6.txo", CTWhite, (1070,), 180),

    # Race Day
    2200 : ("phase_5.5/maps/wall_paper_car.txo", CTWhite, (0,1000), 180,),
    2210 : ("phase_5.5/maps/wall_paper_car_neutral.txo", CTFlatColor,
            (0,1000), 180,),

    # Touchdown
    2300 : ("phase_5.5/maps/wall_paper_football_neutral.txo",
            CTFlatColor, (0,1080), 180,),

    # Cloud 9
    2400 : ("phase_5.5/maps/wall_paper_clouds.txo", CTWhite, (0,1000), 180,),

    # Climbing Vine
    2500 : ("phase_5.5/maps/wall_paper_vine_neutral.txo",
            CTFlatColorAll, (0,1090), 180,),

    # Springtime
    2600 : ("phase_5.5/maps/basket.txo", CTWhite, (0,1000), 180,),
    2610 : ("phase_5.5/maps/basket_neutral.txo", CTFlatColor, (0, 1000), 180,),

    # Kokeshi
    2700 : ("phase_5.5/maps/doll.txo", CTWhite, (0,1000,1110), 180,),
    2710 : ("phase_5.5/maps/doll_neutral.txo",CTFlatColor,(0,1100,1110),180,),

    # Posies
    2800 : ("phase_5.5/maps/littleFlowers.txo", CTWhite, (0,1000), 180,),
    2810 : ("phase_5.5/maps/littleFlowers_neutral.txo",CTFlatColor,(0,1000),180,),

    # Underwater
    # Angel Fish
    2900 : ("phase_5.5/maps/UWwallPaperAngelFish.txo", CTWhite, (0,1120,1160), 180,),
    2910 : ("phase_5.5/maps/UWwallPaperAngelFishColor.txo", CTWhite, (0,1120,1160), 180,),

    # keep here temporarily so DB doesn't freak out.  These keys were originally offered
    # on the test server, but it turns out this indexing scheme doesn't work right, so
    # they weren't offered on live.  If we get rid of these indices (2920-2980) we shoul
    # patch the DB on TEST
    2920 : ("phase_5.5/maps/UWwallPaperBubbles.txo", CTWhite, (0,1120,1160), 180,),
    2930 : ("phase_5.5/maps/UWwallPaperBubbles2.txo", CTWhite, (0,1120,1160), 180,),
    2940 : ("phase_5.5/maps/UWwallPaperGreenFish.txo", CTWhite, (0,1120,1160), 180,),
    2950 : ("phase_5.5/maps/UWwallPaperRedFish.txo", CTWhite, (0,1120,1160), 180,),
    2960 : ("phase_5.5/maps/UWwallPaperSea_horse.txo", CTWhite, (0,1120,1160), 180,),
    2970 : ("phase_5.5/maps/UWwallPaperShells.txo", CTWhite, (0,1140,1150), 180),
    2980 : ("phase_5.5/maps/UWwaterFloor1.txo", (CT_WHITE, CT_PALE_GREEN, CT_LIGHT_BLUE), (0,), 180),

    # Bubbles
    3000 : ("phase_5.5/maps/UWwallPaperBubbles.txo", CTWhite, (0,1120,1160), 180,),
    3100 : ("phase_5.5/maps/UWwallPaperBubbles2.txo", CTWhite, (0,1120,1160), 180,),

    # Fish
    3200 : ("phase_5.5/maps/UWwallPaperGreenFish.txo", CTWhite, (0,1120,1160), 180,),
    3300 : ("phase_5.5/maps/UWwallPaperRedFish.txo", CTWhite, (0,1120,1160), 180,),
    3400 : ("phase_5.5/maps/UWwallPaperSea_horse.txo", CTWhite, (0,1120,1160), 180,),

    # Shells
    3500 : ("phase_5.5/maps/UWwallPaperShells.txo", (CT_WHITE, CT_SEA_GREEN, CT_LIGHT_BLUE), (0,1140,1150), 180),

    # Water
    3600 : ("phase_5.5/maps/UWwaterFloor1.txo", (CT_WHITE, CT_PALE_GREEN, CT_LIGHT_BLUE), (0,), 180),

    # Western
    3700 : ("phase_5.5/maps/WesternBootWallpaper1.txo", CTWhite, (0,1170,1180), 180,),
    3800 : ("phase_5.5/maps/WesternCactusWallpaper1.txo", CTWhite, (0,1170,1180), 180,),
    3900 : ("phase_5.5/maps/WesternHatWallpaper1.txo", CTWhite, (0,1170,1180), 180,),

    # Holiday themed wallpapers

    # Halloween
    10100 : ("phase_5.5/maps/cats1.txo", CTWhite, (0, 10010, 10020), 400),
    10200 : ("phase_5.5/maps/bats2.txo", CTWhite, (0, 10010, 10020), 400),

    # Christmas
    # Snowflake
    11000 : ("phase_5.5/maps/wall_paper_snowflakes.txo", CTWhite,
             (0,11000,11010), 400,),
    # Hollyleaf
    11100 : ("phase_5.5/maps/wall_paper_hollyleaf.txo", CTWhite,
             (0,11000,11010), 400,),
    # Snowman
    11200 : ("phase_5.5/maps/wall_paper_snowman.txo", CTWhite,
             (0,11000,11010), 400,),

    # Valentines
    # add valentines here
    #
    12000 : ("phase_5.5/maps/VdayWall1.txo", CTWhite,
             (0,12000,12010,12020), 400,),
    #
    12100 : ("phase_5.5/maps/VdayWall2.txo", CTWhite,
             (0,12000,12010,12020), 400,),
    #
    12200 : ("phase_5.5/maps/VdayWall3.txo", CTWhite,
             (0,12000,12010,12020), 400,),
    #
    12300 : ("phase_5.5/maps/VdayWall4.txo", CTWhite,
             (0,12000,12010,12020), 400,),

    # St. Patrick's day
    #
    13000 : ("phase_5.5/maps/StPatWallpaper1.txo", CTWhite, (0,13000), 400),
    #
    13100 : ("phase_5.5/maps/StPatWallpaper2.txo", CTWhite, (0,13000), 400),
    #
    13200 : ("phase_5.5/maps/StPatWallpaper3.txo", CTWhite, (0,13000), 400),
    #
    13300 : ("phase_5.5/maps/StPatWallpaper4.txo", CTWhite, (0,13000), 400),
    }

WallpaperGroups = {
    1100 : (1100, 1110, 1120, 1130, 1140, 1150,),
    1200 : (1200, 1210, 1220, 1230, 1240, 1250, 1260,),
    1300 : (1300, 1310, 1320, 1330, 1340, 1350,),
    1400 : (1400, 1410, 1420, 1430, 1440, 1450,),
    1500 : (1500, 1510, 1520,),
    1600 : (1600, 1610, 1620, 1630, 1640, 1650, 1660,),
    1700 : (1700, 1710, 1720, 1730, 1740, 1750, 1760,),
    1800 : (1800, 1810, 1820, 1830, 1840, 1850, 1860,),
    1900 : (1900, 1910, 1920, 1930, 1940, 1950,),
    2000 : (2000, 2010, 2020,),
    2100 : (2100, 2110, 2120, 2130, 2140,),
    2200 : (2200, 2210,),
    2600 : (2600, 2610,),
    2700 : (2700, 2710,),
    2800 : (2800, 2810,),
    2900 : (2900, 2910,),
    }


# Possible border types
BorderTypes = {
    # Index of 0 means no border
    1000 : ("phase_5.5/maps/bd_grey_border1.txo", CTFlatColorDark),
    1010 : ("phase_5.5/maps/diamonds_border2.txo", CTWhite),
    1020 : ("phase_5.5/maps/diamonds_border2ch.txo", CTWhite),
    1030 : ("phase_5.5/maps/diamonds_border3ch.txo", CTWhite),
    1040 : ("phase_5.5/maps/diamonds_border4ch.txo", CTWhite),
    1050 : ("phase_5.5/maps/flower_border2.txo", CTWhite),
    1060 : ("phase_5.5/maps/flower_border5.txo", CTWhite),
    1070 : ("phase_5.5/maps/flower_border6.txo", CTWhite),
    1080 : ("phase_5.5/maps/football_border_neutral.txo", CTFlatColorDark),
    1090 : ("phase_5.5/maps/vine_border1.txo", CTFlatColorDark),
    1100 : ("phase_5.5/maps/doll_board.txo", CTWhite),
    1110 : ("phase_5.5/maps/doll_board_neutral.txo", CTFlatColorDark),
    # Underwater
    1120 : ("phase_5.5/maps/UWwallPaperPlantBorder.txo", CTWhite),
    1130 : ("phase_5.5/maps/UWwallPaperSea_horseBorder.txo", CTWhite),
    1140 : ("phase_5.5/maps/UWwallPaperShellBorder1.txo", CTWhite),
    1150 : ("phase_5.5/maps/UWwallPaperShellBorder2.txo", CTWhite),
    1160 : ("phase_5.5/maps/UWwallPaperWaveBorder.txo", CTWhite),
    # Western
    1170 : ("phase_5.5/maps/WesternSkullBorder.txo", CTWhite),
    1180 : ("phase_5.5/maps/WesternStarBorder.txo", CTWhite),

    # Holiday themed borders

    # Halloween
    10010 : ("phase_5.5/maps/border_ScarryMoon1.txo", CTWhite),
    10020 : ("phase_5.5/maps/border_candy1.txo", CTWhite),

    # Christmas
    11000 : ("phase_5.5/maps/flakes_border.txo", CTWhite),
    11010 : ("phase_5.5/maps/hollyleaf_border.txo", CTWhite),

    # Valentines
    12000 : ("phase_5.5/maps/Vborder1a.txo", CTWhite),
    12010 : ("phase_5.5/maps/Vborder1b.txo", CTWhite),
    12020 : ("phase_5.5/maps/Vborder2b.txo", CTWhite),

    # St Patrick's
    13000 : ("phase_5.5/maps/StPatBorder1.txo", CTWhite),
    }

class CatalogWallpaperItem(CatalogSurfaceItem):
    """
    This represents a texture/color combination for walls and trim.
    It includes wallpaper as well as moulding, wainscoting, and
    flooring.
    """

    def makeNewItem(self, patternIndex, colorIndex = None,
                    # Default to no border
                    borderIndex = 0, borderColorIndex = 0):
        self.patternIndex = patternIndex
        self.colorIndex = colorIndex
        # Index of 0 means no border
        self.borderIndex = borderIndex
        self.borderColorIndex = borderColorIndex
        CatalogSurfaceItem.makeNewItem(self)

    def needsCustomize(self):
        # Returns true if the item still needs to be customized by the
        # user (e.g. by choosing a color).
        return (self.colorIndex == None) or (self.borderIndex == None)

    def getTypeName(self):
        # e.g. "wallpaper", "wainscoting", etc.
        return TTLocalizer.SurfaceNames[STWallpaper]

    def getName(self):
        name = TTLocalizer.WallpaperNames.get(self.patternIndex)
        if name == None:
            century = self.patternIndex - (self.patternIndex % 100)
            name = TTLocalizer.WallpaperNames.get(century)
        if name:
            return name
        return self.getTypeName()

    def getSurfaceType(self):
        # Returns a value reflecting the type of surface this
        # pattern is intended to be applied to.
        return STWallpaper

    def getPicture(self, avatar):
        # Returns a (DirectWidget, Interval) pair to draw and animate a
        # little representation of the item, or (None, None) if the
        # item has no representation.  This method is only called on
        # the client.
        frame = self.makeFrame()

        sample = loader.loadModel('phase_5.5/models/estate/wallpaper_sample')
        a = sample.find('**/a')
        b = sample.find('**/b')
        c = sample.find('**/c')

        # Wallpaper gets applied to the top 2/3, with the border
        # on the bottom 1/3.
        a.setTexture(self.loadTexture(), 1)
        a.setColorScale(*self.getColor())
        b.setTexture(self.loadTexture(), 1)
        b.setColorScale(*self.getColor())
        c.setTexture(self.loadBorderTexture(), 1)
        c.setColorScale(*self.getBorderColor())

        sample.reparentTo(frame)
##        assert (not self.hasPicture)
        self.hasPicture=True

        return (frame, None)

    def output(self, store = ~0):
        return "CatalogWallpaperItem(%s, %s, %s, %s%s)" % (
            self.patternIndex, self.colorIndex,
            self.borderIndex, self.borderColorIndex,
            self.formatOptionalData(store))

    def getFilename(self):
        return WallpaperTypes[self.patternIndex][WTTextureName]
        
    def equalsTo(self, other):
        if self.patternIndex != other.patternIndex:
            return False
        elif self.colorIndex != other.colorIndex:
            return False
        elif self.borderIndex != other.borderIndex:
            return False
        return self.borderColorIndex == other.borderColorIndex

    def compareTo(self, other):
        if self.patternIndex != other.patternIndex:
            century = self.patternIndex - (self.patternIndex % 100)
            otherCentury = other.patternIndex - (other.patternIndex % 100)
            return century - otherCentury
        return 0

    def getHashContents(self):
        century = self.patternIndex - (self.patternIndex % 100)
        return century

    def getBasePrice(self):
        return WallpaperTypes[self.patternIndex][WTBasePrice]

    def loadTexture(self):
        from toontown.toonbase.ToontownModules import Texture
        filename = WallpaperTypes[self.patternIndex][WTTextureName]
        texture = loader.loadTexture(filename)
        texture.setMinfilter(Texture.FTLinearMipmapLinear)
        texture.setMagfilter(Texture.FTLinear)
        return texture

    def getColor(self):
        if self.colorIndex == None:
            # If no color index is set yet, use first color in color list
            colorIndex = 0
        else:
            colorIndex = self.colorIndex
        colors = WallpaperTypes[self.patternIndex][WTColor]
        if colorIndex < len(colors):
            return colors[colorIndex]
        else:
            print("Warning: colorIndex > len(colors). Returning white.")
            return CT_WHITE

    def loadBorderTexture(self):
        from toontown.toonbase.ToontownModules import Texture
        if ((self.borderIndex == None) or (self.borderIndex == 0)):
            # Border hasn't been picked or no border specified
            return self.loadTexture()
        borderInfo = BorderTypes[self.borderIndex]
        filename = borderInfo[BDTextureName]
        texture = loader.loadTexture(filename)
        texture.setMinfilter(Texture.FTLinearMipmapLinear)
        texture.setMagfilter(Texture.FTLinear)
        return texture

    def getBorderColor(self):
        if ((self.borderIndex == None) or (self.borderIndex == 0)):
            return self.getColor()
        else:
            colors = BorderTypes[self.borderIndex][BDColor]
        # Get specified color or return CT_WHITE as default
        if self.borderColorIndex < len(colors):
            return colors[self.borderColorIndex]
        else:
            return CT_WHITE

    def decodeDatagram(self, di, versionNumber, store):
        CatalogAtticItem.CatalogAtticItem.decodeDatagram(self, di, versionNumber, store)
        # Set some default values
        self.colorIndex = None
        if (store & CatalogItem.Customization):
            self.borderIndex = 0
        else:
            self.borderIndex = None
        self.borderColorIndex = 0
        # Update as needed
        if versionNumber < 3:
            self.patternIndex = di.getUint8()
            self.colorIndex = di.getUint8()
        elif versionNumber == 3:
            self.patternIndex = di.getUint16()
            self.colorIndex = di.getUint8()
        else:
            self.patternIndex = di.getUint16()
            if store & CatalogItem.Customization:
                self.colorIndex = di.getUint8()
                self.borderIndex = di.getUint16()
                self.borderColorIndex = di.getUint8()

        # The following will generate an exception if
        # self.patternIndex is invalid.  The other fields can take
        # care of themselves.
        wtype = WallpaperTypes[self.patternIndex]


    def encodeDatagram(self, dg, store):
        CatalogAtticItem.CatalogAtticItem.encodeDatagram(self, dg, store)
        dg.addUint16(self.patternIndex)
        if (store & CatalogItem.Customization):
            dg.addUint8(self.colorIndex)
            dg.addUint16(self.borderIndex)
            dg.addUint8(self.borderColorIndex)

def getWallpapers(*typeList):
    # This function returns a list of CatalogWallpaperItems
    # The returned items will all need to be customized (i.e
    # have a color chosen by the user.  Until customization,
    # use a default color index of 0 (if the pattern has a color
    # list) or CT_WHITE if the pattern has no color list
    wallpapers = []
    for type in typeList:
        wallpapers.append(CatalogWallpaperItem(type))
    return wallpapers


def getAllWallpapers(*typeList):
    # This function returns a list of all possible
    # CatalogWallpaperItems (that is, all color variants) for the
    # indicated type index(es).
    # If the specified type index is in the group dictionary
    # get all corresponding patterns from the wallpaperTypes dictionary
    # This returns an item that has already been customized
    allWallpapers = []
    for type in typeList:
        # If its a group, return a list of all associated textures,
        # otherwise, return a simple list of the type itself
        group = WallpaperGroups.get(type, [type])
        for index in group:
            borderKeys = WallpaperTypes[index][WTBorderList]
            for borderKey in borderKeys:
                borderData = BorderTypes.get(borderKey)
                if borderData:
                    numBorderColors = len(borderData[BDColor])
                else:
                    numBorderColors = 1
                for borderColorIndex in range(numBorderColors):
                    colors = WallpaperTypes[index][WTColor]
                    for n in range(len(colors)):
                        allWallpapers.append(CatalogWallpaperItem(
                            index, n, borderKey, borderColorIndex))
    return allWallpapers

def getWallpaperRange(fromIndex, toIndex, *otherRanges):
    # This function returns a list of all possible
    # CatalogWallpaperItems (that is, all color variants) for the
    # indicated type index(es).

    # Make sure we got an even number of otherRanges
    assert(len(otherRanges)%2 == 0)

    wallpaperRange = []

    froms = [fromIndex,]
    tos = [toIndex,]

    i = 0
    while i < len(otherRanges):
        froms.append(otherRanges[i])
        tos.append(otherRanges[i+1])
        i += 2

    for patternIndex in list(WallpaperTypes.keys()):
        for fromIndex, toIndex in zip(froms,tos):
            if patternIndex >= fromIndex and patternIndex <= toIndex:
                borderKeys = WallpaperTypes[patternIndex][WTBorderList]
                for borderKey in borderKeys:
                    borderData = BorderTypes.get(borderKey)
                    if borderData:
                        numBorderColors = len(borderData[BDColor])
                    else:
                        numBorderColors = 1
                    for borderColorIndex in range(numBorderColors):
                        colors = WallpaperTypes[patternIndex][WTColor]
                        for n in range(len(colors)):
                            wallpaperRange.append(CatalogWallpaperItem(patternIndex, n, borderKey, borderColorIndex))
    return wallpaperRange
