from direct.directnotify import DirectNotifyGlobal
from . import CatalogItem
from . import CatalogItemList
from .CatalogFurnitureItem import CatalogFurnitureItem, nextAvailableCloset, getAllClosets, get50ItemCloset, getMaxClosets, get50ItemTrunk #nextAvailableBank, getAllBanks,
from .CatalogAnimatedFurnitureItem import CatalogAnimatedFurnitureItem
from .CatalogClothingItem import CatalogClothingItem, getAllClothes
from .CatalogChatItem import CatalogChatItem, getChatRange
from .CatalogEmoteItem import CatalogEmoteItem
from .CatalogWallpaperItem import CatalogWallpaperItem, getWallpapers
from .CatalogFlooringItem import CatalogFlooringItem, getFloorings
from .CatalogMouldingItem import CatalogMouldingItem, getAllMouldings
from .CatalogWainscotingItem import CatalogWainscotingItem, getAllWainscotings
from .CatalogWindowItem import CatalogWindowItem
from .CatalogPoleItem import nextAvailablePole, getAllPoles
from .CatalogPetTrickItem import CatalogPetTrickItem, getAllPetTricks
from .CatalogGardenItem import CatalogGardenItem
from .CatalogToonStatueItem import CatalogToonStatueItem
from .CatalogRentalItem import CatalogRentalItem
from .CatalogGardenStarterItem import CatalogGardenStarterItem
from .CatalogNametagItem import CatalogNametagItem
from .CatalogAccessoryItem import CatalogAccessoryItem
from direct.actor import Actor
from toontown.toonbase import TTLocalizer
from toontown.toonbase import ToontownGlobals
import types
import random
import time
from toontown.toonbase.ToontownModules import *

# Index numbers that stand for catalog items within this file,
# e.g. for MetaItems, are local to this file only.  These index
# numbers are not saved in the database or stored on a toon; they are
# used only to define the relationship between catalog items chosen at
# random.

MetaItems = {
    # Basic shirts
    100: getAllClothes(101, 102, 103, 104, 105, 106, 107, 108, 109,
                       109, 111, 115,
                       201, 202, 203, 204, 205, 206, 207, 208, 209,
                       209, 211, 215),

    # Basic shorts and/or skirts
    300: getAllClothes(301, 302, 303, 304, 305, 308,
                       401, 403, 404, 405, 407, 451, 452, 453),

    # Series 1 chat
    2000: getChatRange(0, 1999),
    # Series 2 chat
    2010: getChatRange(2000, 2999),
    # Series 3 chat
    2020: getChatRange(3000, 3999),
    # Series 4 chat
    2030: getChatRange(4000, 4999),
    # Series 6 chat
    2040: getChatRange(6000, 6999),
    # Series 7 chat
    2050: getChatRange(7000, 7999),

    # Halloween chat
    2900: getChatRange(10000, 10002, 10005, 10005, 10007, 10008, 10010, 10099),
    # Fall Festivus chat
    2910: getChatRange(11000, 11099),
    # Valentines love chat
    2920: getChatRange(12000, 12049),
    # Valentines love chat
    2921: getChatRange(12050, 12099),
    # St Patrick's Day chat
    2930: getChatRange(13000, 13099),
    # Estate Party Chat
    2940: getChatRange(14000, 14099),

    # Wallpaper Series 1
    3000: getWallpapers(1000, 1100, 1200, 1300,
                        1400, 1500, 1600, 1700,
                        1800, 1900, 2000, 2100),

    # Wallpaper Series 2
    3010: getWallpapers(2200, 2300, 2400, 2500,
                        2600, 2700, 2800),

    # Wallpaper Series 3
    3020: getWallpapers(2900,3000,3100,3200,3300,3400,3500,3600),

    # Wallpaper Series 4
    3030: getWallpapers(3700, 3800, 3900),

    # Basic wainscoting - Series 1
    3500 : getAllWainscotings(1000, 1010),
    # Basic wainscoting - Series 2
    3510 : getAllWainscotings(1020),
    # Valentines wainscoting
    3520 : getAllWainscotings(1030),
    # Underwater wainscoting
    3530 : getAllWainscotings(1040),

    # Basic flooring Series 1
    4000: getFloorings(1000, 1010, 1020, 1030,
                       1040, 1050, 1060, 1070,
                       1080, 1090, 1100),

    # Basic flooring Series 2
    4010: getFloorings(1110, 1120, 1130),

    # Basic flooring Series 3
    4020: getFloorings(1140, 1150, 1160, 1170, 1180, 1190),

    # Basic moulding
    4500: getAllMouldings(1000, 1010),
    4510: getAllMouldings(1020, 1030, 1040),
    4520: getAllMouldings(1070,),

    # A random pet trick.  Presently this selects from the entire pool
    # of available tricks; one day we may have level 1 pet tricks and
    # level 2 pet tricks (and level 3 tricks, etc.)
    5000: getAllPetTricks(),

    }

# some of the chat keys above are not sold, these keys are the ones sold in the catalog
MetaItemChatKeysSold = (2000, 2010, 2020, 2030, 2040, 2050, 2900, 2910, 2920, 2921, 2930)


def getAllChatItemsSold():
    """Give me a list of every single catalog chat item we offer."""
    result = []
    for key in MetaItemChatKeysSold:
        result += MetaItems[key]
    return result

# This class is used in the below schedules to wrap around a catalog
# week or a particular item to indicate that it is a "sale item" or
# that all items in the week are "sale items".
class Sale:
    def __init__(self, *args):
        self.args = args

MonthlySchedule = (

    # startMM, startDD, endMM, endDD, (item, item, item, ...)

    # Accessory items -- on sale 7/1 through 8/31.
    (7, 1, 8, 31,
     (
      CatalogAccessoryItem(101),
      CatalogAccessoryItem(103),
      CatalogAccessoryItem(117),
      CatalogAccessoryItem(118),
      CatalogAccessoryItem(123),
      CatalogAccessoryItem(124),
      CatalogAccessoryItem(125),
      CatalogAccessoryItem(126),
      CatalogAccessoryItem(127),
      CatalogAccessoryItem(128),
      CatalogAccessoryItem(129),
      CatalogAccessoryItem(130),
      CatalogAccessoryItem(202),
      CatalogAccessoryItem(204),
      CatalogAccessoryItem(205),
      CatalogAccessoryItem(206),
      CatalogAccessoryItem(208),
      CatalogAccessoryItem(209),
      CatalogAccessoryItem(210),
      CatalogAccessoryItem(302),
      CatalogAccessoryItem(308),
      CatalogAccessoryItem(309),
      CatalogAccessoryItem(310),
      CatalogAccessoryItem(317),
      CatalogAccessoryItem(402),
      CatalogAccessoryItem(403),
      CatalogAccessoryItem(405),
      CatalogAccessoryItem(406),
      CatalogAccessoryItem(407),
      CatalogAccessoryItem(408),
      CatalogAccessoryItem(409),
      CatalogAccessoryItem(410),
      CatalogAccessoryItem(411),
      CatalogAccessoryItem(412),
      CatalogAccessoryItem(413),
      )),

    # Accessory items -- on sale 9/1 through 10/31.
    (9, 1, 10, 31,
     (
      CatalogAccessoryItem(306),
      CatalogAccessoryItem(318),
      CatalogAccessoryItem(121),
      CatalogAccessoryItem(212),
      CatalogAccessoryItem(214),
      CatalogAccessoryItem(312),
      CatalogAccessoryItem(150),
      CatalogAccessoryItem(151),
      CatalogAccessoryItem(147),
      CatalogAccessoryItem(422),
      CatalogAccessoryItem(141),
      CatalogAccessoryItem(146),
      CatalogAccessoryItem(444),
      CatalogAccessoryItem(122),
      CatalogAccessoryItem(430),
      CatalogAccessoryItem(145),
      CatalogAccessoryItem(132),
      CatalogAccessoryItem(161),
      CatalogAccessoryItem(134),
      CatalogAccessoryItem(149),
      CatalogAccessoryItem(207),
      CatalogAccessoryItem(215),
      CatalogAccessoryItem(216),
      CatalogAccessoryItem(417),
      CatalogAccessoryItem(222),
      CatalogAccessoryItem(321),
      CatalogAccessoryItem(322),
      CatalogAccessoryItem(307),
      CatalogAccessoryItem(135),
      CatalogAccessoryItem(174),
      )),

    # Accessory items -- on sale 11/1 through 12/31.
    (11, 1, 12, 31,
     (
      CatalogAccessoryItem(434),
      CatalogAccessoryItem(435),
      CatalogAccessoryItem(441),
      CatalogAccessoryItem(446),
      CatalogAccessoryItem(429),
      CatalogAccessoryItem(110),
      CatalogAccessoryItem(148),
      CatalogAccessoryItem(443),
      CatalogAccessoryItem(426),
      CatalogAccessoryItem(439),
      CatalogAccessoryItem(143),
      CatalogAccessoryItem(313),
      CatalogAccessoryItem(311),
      CatalogAccessoryItem(437),
      CatalogAccessoryItem(415),
      CatalogAccessoryItem(167),
      CatalogAccessoryItem(157),
      CatalogAccessoryItem(106),
      CatalogAccessoryItem(109),
      CatalogAccessoryItem(421),
      CatalogAccessoryItem(401),
      CatalogAccessoryItem(447),
      CatalogAccessoryItem(213),
      CatalogAccessoryItem(330),
      )),

    # Accessory items -- on sale 1/1 through 2/29.
    (1, 1, 2, 29,
     (
      CatalogAccessoryItem(440),
      CatalogAccessoryItem(425),
      CatalogAccessoryItem(158),
      CatalogAccessoryItem(431),
      CatalogAccessoryItem(420),
      CatalogAccessoryItem(155),
      CatalogAccessoryItem(419),
      CatalogAccessoryItem(436),
      CatalogAccessoryItem(428),
      CatalogAccessoryItem(304),
      CatalogAccessoryItem(301),
      CatalogAccessoryItem(416),
      CatalogAccessoryItem(414),
      CatalogAccessoryItem(164),
      CatalogAccessoryItem(323),
      CatalogAccessoryItem(108),
      CatalogAccessoryItem(139),
      CatalogAccessoryItem(316),
      CatalogAccessoryItem(131),
      CatalogAccessoryItem(170),
      CatalogAccessoryItem(221),
      CatalogAccessoryItem(225),
      )),

    # Accessory items -- on sale 3/1 through 4/30.
    (3, 1, 4, 30,
     (
      CatalogAccessoryItem(305),
      CatalogAccessoryItem(303),
      CatalogAccessoryItem(144),
      CatalogAccessoryItem(120),
      CatalogAccessoryItem(116),
      CatalogAccessoryItem(217),
      CatalogAccessoryItem(218),
      CatalogAccessoryItem(219),
      CatalogAccessoryItem(445),
      CatalogAccessoryItem(418),
      CatalogAccessoryItem(432),
      CatalogAccessoryItem(427),
      CatalogAccessoryItem(423),
      CatalogAccessoryItem(137),
      CatalogAccessoryItem(163),
      CatalogAccessoryItem(165),
      CatalogAccessoryItem(153),
      CatalogAccessoryItem(319),
      CatalogAccessoryItem(154),
      CatalogAccessoryItem(159),
      CatalogAccessoryItem(162),
      CatalogAccessoryItem(315),
      CatalogAccessoryItem(160),
      CatalogAccessoryItem(102),
      )),

    # Accessory items -- on sale 5/1 through 6/30.
    (5, 1, 6, 30,
     (
      CatalogAccessoryItem(119),
      CatalogAccessoryItem(136),
      CatalogAccessoryItem(169),
      CatalogAccessoryItem(140),
      CatalogAccessoryItem(168),
      CatalogAccessoryItem(138),
      CatalogAccessoryItem(220),
      CatalogAccessoryItem(433),
      CatalogAccessoryItem(442),
      CatalogAccessoryItem(424),
      CatalogAccessoryItem(404),
      CatalogAccessoryItem(156),
      CatalogAccessoryItem(142),
      CatalogAccessoryItem(152),
      CatalogAccessoryItem(133),
      CatalogAccessoryItem(166),
      CatalogAccessoryItem(211),
      CatalogAccessoryItem(314),
      CatalogAccessoryItem(320),
      CatalogAccessoryItem(173),
      CatalogAccessoryItem(328),
      CatalogAccessoryItem(329),
      )),

    # Halloween items -- on sale 10/3 through 11/2.
    (10, 3, 11, 2,
     ((3, 2900),
      CatalogChatItem(10003),
      CatalogClothingItem(1001, 0),
      CatalogClothingItem(1002, 0),
      CatalogWallpaperItem(10100),
      CatalogWallpaperItem(10200),
      CatalogFurnitureItem(10000),
      CatalogFurnitureItem(10010),
      CatalogNametagItem(9),


      )),

   # Halloween items -- on sale 10/3 through 11/2.

    (10, 3, 11, 2,
     (
      # The following articles
      # were likely removed in
      # 2011 to remove accessory
      # parts, however
      # Bee and SuperToon skirts
      # were also removed and never
      # re-added so they should appear
      # in the catalog again to fix
      # this accidental removal
      CatalogClothingItem(1739, 0), # Bee Skirt
      CatalogClothingItem(1740, 0), # SuperToon Skirt
      CatalogClothingItem(1734, 0), # Bee Shorts
      CatalogClothingItem(1735, 0), # SuperToon Shorts
      CatalogClothingItem(1723, 0), # Bee Shirt
      CatalogClothingItem(1724, 0), # SuperToon Shirt
      CatalogClothingItem(1770, 0), # Vampire Shirt
      CatalogClothingItem(1772, 0), # Vampire Shorts
      CatalogClothingItem(1773, 0), # Vampire Shorts
      # End 2010 clothing + accessory items
      CatalogClothingItem(1744, 0),
      CatalogClothingItem(1745, 0),
      CatalogClothingItem(1748, 0),
      CatalogClothingItem(1771, 0),
      CatalogClothingItem(1774, 0),
      CatalogClothingItem(1775, 0),
      CatalogClothingItem(1743, 0),
      CatalogClothingItem(1746, 0),
      CatalogClothingItem(1747, 0),
      CatalogClothingItem(1112, 0),
      CatalogClothingItem(1113, 0),
      CatalogClothingItem(1114, 0),
      CatalogClothingItem(1115, 0),
      CatalogClothingItem(1116, 0),
      CatalogClothingItem(1117, 0),
      CatalogClothingItem(1118, 0),
      CatalogClothingItem(1119, 0),
      CatalogClothingItem(1120, 0),
      CatalogClothingItem(1121, 0),
      CatalogClothingItem(1122, 0),
      CatalogClothingItem(1123, 0),
      CatalogClothingItem(1124, 0),
      CatalogClothingItem(1125, 0),
      CatalogClothingItem(1126, 0),
      CatalogClothingItem(1127, 0),
      CatalogAccessoryItem(171),
      CatalogAccessoryItem(172),
      CatalogAccessoryItem(224),
      CatalogAccessoryItem(324),
      CatalogAccessoryItem(325),
      CatalogAccessoryItem(326),
      CatalogAccessoryItem(327),
      CatalogAccessoryItem(448),
      CatalogAccessoryItem(449),
      CatalogClothingItem(1801, 0),
      )),

    # Winter items -- on sale 11/18 through 12/31
    # moved a little earlier to get thanksgiving phrases
    # before thanksgiving happens
#    (11, 18, 1, 1,
#     ((3, 2910),
#      CatalogChatItem(11020), # Have a Wonderful Winter!
#      CatalogClothingItem(1100, 0),
#      CatalogClothingItem(1101, 0),
#      CatalogClothingItem(1102, 0),
#      CatalogClothingItem(1103, 0),
#      CatalogWallpaperItem(11000),
#      CatalogWallpaperItem(11100),
#      CatalogWallpaperItem(11200),
#      CatalogFlooringItem(10000),
#      CatalogFlooringItem(10010),
#      CatalogGardenItem(130, 1), # snowman
#      CatalogAnimatedFurnitureItem(10020), # winter tree
#      CatalogFurnitureItem(10030, 0), # winter wreath
#      )),

    # Valentines items -- on sale 2/1 through 2/28
    (2, 1, 2, 28,
     ((3, 2920),
      (2, 2921),
      CatalogClothingItem(1200, 0),
      CatalogClothingItem(1201, 0),
      CatalogClothingItem(1202, 0),
      CatalogClothingItem(1203, 0),
      CatalogClothingItem(1204, 0),
      CatalogClothingItem(1205, 0),
      CatalogWallpaperItem(12000),
      CatalogWallpaperItem(12100),
      CatalogWallpaperItem(12200),
      CatalogWallpaperItem(12300),
      CatalogWainscotingItem(1030, 0),
      CatalogWainscotingItem(1030, 1),
      CatalogMouldingItem(1060, 0),
      CatalogMouldingItem(1060, 1),

      # 2009 Valentines Day Items
      CatalogClothingItem(1206, 0), # Valentines Day Shirt 1
      CatalogClothingItem(1207, 0), # Valentines Day Shirt 2
      CatalogClothingItem(1208, 0), # Valentines Day Shorts 1
      CatalogClothingItem(1209, 0), # Valentines Day Shorts 2
      CatalogClothingItem(1210, 0), # Valentines Day Skirt 1
      CatalogClothingItem(1211, 0), # Valentines Day Skirt 2
      CatalogClothingItem(1212, 0), # Valentines Day Shirt 3 - 2010 VDay Shirt
      CatalogFurnitureItem(1670),   # Valentines Day Vase - Rose Vase
      CatalogFurnitureItem(1680),   # Valentines Day Vase - Rose Water Can
      CatalogFurnitureItem(1450),   # Valentines Day Painting - Mickey and Minnie
      CatalogMouldingItem(1100, 0), # Valentines Day Moulding - Cupid
      CatalogMouldingItem(1110, 0), # Valentines Day Moulding - Hearts 1
      CatalogMouldingItem(1120, 0), # Valentines Day Moulding - Hearts 2
      )),

    # St Patrick's items -- on sale 3/1 through 3/20
    (3, 1, 3, 20,
     ((3, 2930),
      CatalogClothingItem(1300, 0),
      CatalogClothingItem(1301, 0),
      CatalogClothingItem(1302, 0),
      CatalogClothingItem(1303, 0),
      CatalogClothingItem(1304, 0),
      CatalogClothingItem(1305, 0),
      CatalogClothingItem(1306, 0),
      CatalogWallpaperItem(13000),
      CatalogWallpaperItem(13100),
      CatalogWallpaperItem(13200),
      CatalogWallpaperItem(13300),
      CatalogFlooringItem(11000),
      CatalogFlooringItem(11010),
      )),

    # T-Shirt Contest items -- on sale 5/25 through 6/25
    (5, 25, 6, 25,
     (
      CatalogClothingItem(1400, 0),
      CatalogClothingItem(1401, 0),
      CatalogClothingItem(1402, 0),
      )
     ),

    # T-Shirt 2 Contest items -- on sale 8/1 through 8/31
    (8, 1, 8, 31,
     (
      CatalogClothingItem(1403, 0),
      CatalogClothingItem(1404, 0),
      CatalogClothingItem(1405, 0),
      CatalogClothingItem(1406, 0),
      )
     ),

     # Furniture Contest items -- on sale 9/24 through 10/24
    (9, 24, 10, 24,
     (
      CatalogFurnitureItem(450),  # Coral Fireplace
      CatalogAnimatedFurnitureItem(460), # Coral Fireplace with fire
      CatalogAnimatedFurnitureItem(270),  # Trolley Bed
      CatalogAnimatedFurnitureItem(990),  # Gag Fan
      )
     ),

    # Estate Party speedchat items -- on sale 6/15 through 8/15
    (6, 15, 8, 15,
#    (6, 15, 8, 15, 2010, 2010
     ((4, 2940),
      )
     ),

    # Flappy Cog -- on sale 9/1 through 9/30
    (9, 1, 9, 30,
     (CatalogGardenItem(135, 1),
      )
     ),

    # Flappy Cog -- on sale 1/1 through 1/31
    (1, 1, 1, 31,
     (CatalogGardenItem(135, 1),
      )
     ),

    # Flappy Cog -- on sale 4/1 through 4/30
    (4, 1, 4, 30,
     (CatalogGardenItem(135, 1),
      )
     ),

    # Flappy Cog -- on sale 6/1 through 6/30
    (6, 1, 6, 30,
     (CatalogGardenItem(135, 1),
      )
     ),

    # July 4th clothing items -- on sale 6/26 through 7/16
    (6, 26, 7, 16,
     (
      CatalogClothingItem(1500, 0),
      CatalogClothingItem(1501, 0),
      CatalogClothingItem(1502, 0),
      CatalogClothingItem(1503, 0),
      )
     ),

    # Winter Holiday items - on sale 12/4 through 1/4
    (12, 4, 1, 4,
     ((3, 2910),
     )),

    # Winter Holiday items - on sale 12/4 through 1/4
    (12, 4, 1, 4,
     (
      CatalogFurnitureItem(680),   # Candle
      CatalogFurnitureItem(681),   # Lit Candle
      CatalogGardenItem(130, 1),
      CatalogGardenItem(131, 1),
      CatalogAnimatedFurnitureItem(10020),
      CatalogFurnitureItem(10030, 0),
      )),

    # Winter Holiday items - on sale 12/4 to 1/4
    (12, 4, 1, 4,
     (
      CatalogWallpaperItem(11000),
      CatalogWallpaperItem(11100),
      CatalogFlooringItem(10010),
      CatalogMouldingItem(1090, 0), # Winter String Lights Moulding 3
      CatalogClothingItem(1100, 0),
      CatalogClothingItem(1101, 0),
      CatalogClothingItem(1104, 0),       # Winter Holiday Shorts Style 1
      CatalogClothingItem(1105, 0),       # Winter Holiday Shorts Style 2
      CatalogClothingItem(1108, 0),       # Winter Holiday Skirt Style 1
      CatalogClothingItem(1109, 0),       # Winter Holiday Skirt Style 2
      CatalogClothingItem(1802, 0),
      )
     ),

    # Winter Holiday items - on sale 12/11 to 1/4
    (12, 11, 1, 4,
     (
      CatalogFurnitureItem(1040),  # Presents
      CatalogFurnitureItem(1050),  # Sled
      CatalogWallpaperItem(11200),
      CatalogFlooringItem(10000),
      CatalogMouldingItem(1080, 0), # Winter String Lights Moulding 1
      CatalogMouldingItem(1085, 0), # Winter String Lights Moulding 2
      CatalogClothingItem(1102, 0),
      CatalogClothingItem(1103, 0),
      CatalogClothingItem(1106, 0),       # Winter Holiday Shorts Style 3
      CatalogClothingItem(1107, 0),       # Winter Holiday Shorts Style 4
      CatalogClothingItem(1110, 0),       # Winter Holiday Skirt Style 3
      CatalogClothingItem(1111, 0),       # Winter Holiday Skirt Style 4
      )
     ),

    # Silly Story Loony Labs Atom Shirt - on sale 6/9 to 7/15
    (6, 9, 7, 15, 2010, 2010,
     (
      CatalogClothingItem(1751, 0),       # Silly Story Loony Labs Atom Shirt
      )
     ),

     # Silly Story Cogbuster Outfit - on sale 6/14 to 7/15
    (6, 14, 7, 15, 2010, 2010,
     (
      CatalogClothingItem(1754, 0),       # Silly Story Silly Cogbuster Shirt
      CatalogClothingItem(1755, 0),       # Silly Story Silly Cogbuster Shorts
      CatalogClothingItem(1756, 0),       # Silly Story Silly Cogbuster Shorts

      )
     ),

    # Victory Party and Silly Story shirts - on sale 7/21 to 8/17
    (7, 21, 8, 17, 2010, 2010,
     (
      CatalogClothingItem(1749, 0),       # Silly Mailbox Shirt
      CatalogClothingItem(1750, 0),       # Silly Trash Can Shirt
      CatalogClothingItem(1757, 0),       # Victory Party Shirt 1
      CatalogClothingItem(1758, 0),       # Victory Party Shirt 2
      )
     ),

    # Sellbot Nerf shirt - on sale 8/25 to 9/21
    (8, 25, 9, 21, 2010, 2010,
     (
      CatalogClothingItem(1763, 0),       # Smashed Sellbot Shirt
      )
     ),

    # Jellybean Holiday shirts - on sale 6/5 to 7/1
    (6, 5, 7, 1,
     (
      CatalogClothingItem(1768, 0),       # Jellybean Bank Shirt
      CatalogClothingItem(1769, 0),       # Doodle Shirt
      )
     ),

    # Items - on sale 1/1 through 12/31, always available
    (1, 1, 12, 31,
     (
      # Gardening Items
      CatalogGardenItem(100, 1),
      CatalogGardenItem(101, 1),
      # save accelerator for later
      #CatalogGardenItem(102, 1),
      CatalogGardenItem(103, 1),
      CatalogGardenItem(104, 1),
      CatalogToonStatueItem(105, endPoseIndex = 108),

      # Rental Items
      CatalogRentalItem(1, 2880, 1000), # Renatl Cannon
##      CatalogRentalItem(2, 2880, 1000), # Rental Game Table
      CatalogGardenStarterItem(),

      # Basic Nametags
      CatalogNametagItem(100),
      CatalogNametagItem(0),

      # Loyalty Items # WARNING update CatalogClothingItem.LoyaltyItems if you add more
      CatalogClothingItem(1608, 0, 720),  # Purple Pajama girl pants
      CatalogClothingItem(1605, 0, 720),  # Purple Pajama boy pants
      CatalogClothingItem(1602, 0, 720),  # Purple Glasses Pajama
      CatalogClothingItem(1607, 0, 540),  # Red Pajama girl pants
      CatalogClothingItem(1604, 0, 540),  # Red Pajama boy pants
      CatalogClothingItem(1601, 0, 540),  # Red Horn Pajama
      CatalogClothingItem(1606, 0, 360),  # Blue Pajama girl pants
      CatalogClothingItem(1603, 0, 360),  # Blue Pajama boy pants
      CatalogClothingItem(1600, 0, 360),  # Blue Banana Pajama

      # WARNING update CatalogEmoteItem.LoyaltyItems if you add more loyalty emotes
      CatalogEmoteItem(20, 90), # surprise
      CatalogEmoteItem(21, 180), # cry
      CatalogEmoteItem(22, 360), # delighted
      CatalogEmoteItem(23, 540), # furious
      CatalogEmoteItem(24, 720), # laugh
      )
     ),

    # Anniversary hat - on sale 5/26 through 6/30 2013
    (5, 26, 6, 30, 2013, 2013,
     (
      CatalogAccessoryItem(175), # Anniversary Hat
      )
     ),

    (8, 27, 9, 5, 2013, 2013,
     ((3, 2900),
      CatalogChatItem(10003),
      CatalogClothingItem(1001, 0),
      CatalogClothingItem(1002, 0),
      CatalogWallpaperItem(10100),
      CatalogWallpaperItem(10200),
      CatalogFurnitureItem(10000),
      CatalogFurnitureItem(10010),
      CatalogNametagItem(9),
      CatalogClothingItem(1744, 0),
      CatalogClothingItem(1745, 0),
      CatalogClothingItem(1748, 0),
      CatalogClothingItem(1771, 0),
      CatalogClothingItem(1774, 0),
      CatalogClothingItem(1775, 0),
      CatalogClothingItem(1743, 0),
      CatalogClothingItem(1746, 0),
      CatalogClothingItem(1747, 0),
      CatalogClothingItem(1112, 0),
      CatalogClothingItem(1113, 0),
      CatalogClothingItem(1114, 0),
      CatalogClothingItem(1115, 0),
      CatalogClothingItem(1116, 0),
      CatalogClothingItem(1117, 0),
      CatalogClothingItem(1118, 0),
      CatalogClothingItem(1119, 0),
      CatalogClothingItem(1120, 0),
      CatalogClothingItem(1121, 0),
      CatalogClothingItem(1122, 0),
      CatalogClothingItem(1123, 0),
      CatalogClothingItem(1124, 0),
      CatalogClothingItem(1125, 0),
      CatalogClothingItem(1126, 0),
      CatalogClothingItem(1127, 0),
      CatalogAccessoryItem(171),
      CatalogAccessoryItem(172),
      CatalogAccessoryItem(224),
      CatalogAccessoryItem(324),
      CatalogAccessoryItem(325),
      CatalogAccessoryItem(326),
      CatalogAccessoryItem(327),
      CatalogAccessoryItem(448),
      CatalogAccessoryItem(449),
      CatalogClothingItem(1801, 0),
      CatalogAccessoryItem(175),
      )
    ),

    (9, 3, 9, 12, 2013, 2013,
     ((3, 2910),
      CatalogFurnitureItem(680),
      CatalogFurnitureItem(681),
      CatalogGardenItem(130, 1),
      CatalogGardenItem(131, 1),
      CatalogAnimatedFurnitureItem(10020),
      CatalogFurnitureItem(10030, 0),
      CatalogWallpaperItem(11000),
      CatalogWallpaperItem(11100),
      CatalogFlooringItem(10010),
      CatalogMouldingItem(1090, 0),
      CatalogClothingItem(1100, 0),
      CatalogClothingItem(1101, 0),
      CatalogClothingItem(1104, 0),
      CatalogClothingItem(1105, 0),
      CatalogClothingItem(1108, 0),
      CatalogClothingItem(1109, 0),
      CatalogClothingItem(1802, 0),
      CatalogFurnitureItem(1040),
      CatalogFurnitureItem(1050),
      CatalogWallpaperItem(11200),
      CatalogFlooringItem(10000),
      CatalogMouldingItem(1080, 0),
      CatalogMouldingItem(1085, 0),
      CatalogClothingItem(1102, 0),
      CatalogClothingItem(1103, 0),
      CatalogClothingItem(1106, 0),
      CatalogClothingItem(1107, 0),
      CatalogClothingItem(1110, 0),
      CatalogClothingItem(1111, 0),
      )
    ),

    (8, 20, 9, 19, 2013, 2013,
     (
      CatalogAccessoryItem(101),
      CatalogAccessoryItem(103),
      CatalogAccessoryItem(117),
      CatalogAccessoryItem(118),
      CatalogAccessoryItem(123),
      CatalogAccessoryItem(124),
      CatalogAccessoryItem(125),
      CatalogAccessoryItem(126),
      CatalogAccessoryItem(127),
      CatalogAccessoryItem(128),
      CatalogAccessoryItem(129),
      CatalogAccessoryItem(130),
      CatalogAccessoryItem(202),
      CatalogAccessoryItem(204),
      CatalogAccessoryItem(205),
      CatalogAccessoryItem(206),
      CatalogAccessoryItem(208),
      CatalogAccessoryItem(209),
      CatalogAccessoryItem(210),
      CatalogAccessoryItem(302),
      CatalogAccessoryItem(308),
      CatalogAccessoryItem(309),
      CatalogAccessoryItem(310),
      CatalogAccessoryItem(317),
      CatalogAccessoryItem(402),
      CatalogAccessoryItem(403),
      CatalogAccessoryItem(405),
      CatalogAccessoryItem(406),
      CatalogAccessoryItem(407),
      CatalogAccessoryItem(408),
      CatalogAccessoryItem(409),
      CatalogAccessoryItem(410),
      CatalogAccessoryItem(411),
      CatalogAccessoryItem(412),
      CatalogAccessoryItem(413),
      CatalogAccessoryItem(306),
      CatalogAccessoryItem(318),
      CatalogAccessoryItem(121),
      CatalogAccessoryItem(212),
      CatalogAccessoryItem(214),
      CatalogAccessoryItem(312),
      CatalogAccessoryItem(150),
      CatalogAccessoryItem(151),
      CatalogAccessoryItem(147),
      CatalogAccessoryItem(422),
      CatalogAccessoryItem(141),
      CatalogAccessoryItem(146),
      CatalogAccessoryItem(444),
      CatalogAccessoryItem(122),
      CatalogAccessoryItem(430),
      CatalogAccessoryItem(145),
      CatalogAccessoryItem(132),
      CatalogAccessoryItem(161),
      CatalogAccessoryItem(134),
      CatalogAccessoryItem(149),
      CatalogAccessoryItem(207),
      CatalogAccessoryItem(215),
      CatalogAccessoryItem(216),
      CatalogAccessoryItem(417),
      CatalogAccessoryItem(222),
      CatalogAccessoryItem(321),
      CatalogAccessoryItem(322),
      CatalogAccessoryItem(307),
      CatalogAccessoryItem(135),
      CatalogAccessoryItem(174),
      CatalogAccessoryItem(434),
      CatalogAccessoryItem(435),
      CatalogAccessoryItem(441),
      CatalogAccessoryItem(446),
      CatalogAccessoryItem(429),
      CatalogAccessoryItem(110),
      CatalogAccessoryItem(148),
      CatalogAccessoryItem(443),
      CatalogAccessoryItem(426),
      CatalogAccessoryItem(439),
      CatalogAccessoryItem(143),
      CatalogAccessoryItem(313),
      CatalogAccessoryItem(311),
      CatalogAccessoryItem(437),
      CatalogAccessoryItem(415),
      CatalogAccessoryItem(167),
      CatalogAccessoryItem(157),
      CatalogAccessoryItem(106),
      CatalogAccessoryItem(109),
      CatalogAccessoryItem(421),
      CatalogAccessoryItem(401),
      CatalogAccessoryItem(447),
      CatalogAccessoryItem(213),
      CatalogAccessoryItem(330),
      CatalogAccessoryItem(440),
      CatalogAccessoryItem(425),
      CatalogAccessoryItem(158),
      CatalogAccessoryItem(431),
      CatalogAccessoryItem(420),
      CatalogAccessoryItem(155),
      CatalogAccessoryItem(419),
      CatalogAccessoryItem(436),
      CatalogAccessoryItem(428),
      CatalogAccessoryItem(304),
      CatalogAccessoryItem(301),
      CatalogAccessoryItem(416),
      CatalogAccessoryItem(414),
      CatalogAccessoryItem(164),
      CatalogAccessoryItem(323),
      CatalogAccessoryItem(108),
      CatalogAccessoryItem(139),
      CatalogAccessoryItem(316),
      CatalogAccessoryItem(131),
      CatalogAccessoryItem(170),
      CatalogAccessoryItem(221),
      CatalogAccessoryItem(225),
      CatalogAccessoryItem(305),
      CatalogAccessoryItem(303),
      CatalogAccessoryItem(144),
      CatalogAccessoryItem(120),
      CatalogAccessoryItem(116),
      CatalogAccessoryItem(217),
      CatalogAccessoryItem(218),
      CatalogAccessoryItem(219),
      CatalogAccessoryItem(445),
      CatalogAccessoryItem(418),
      CatalogAccessoryItem(432),
      CatalogAccessoryItem(427),
      CatalogAccessoryItem(423),
      CatalogAccessoryItem(137),
      CatalogAccessoryItem(163),
      CatalogAccessoryItem(165),
      CatalogAccessoryItem(153),
      CatalogAccessoryItem(319),
      CatalogAccessoryItem(154),
      CatalogAccessoryItem(159),
      CatalogAccessoryItem(162),
      CatalogAccessoryItem(315),
      CatalogAccessoryItem(160),
      CatalogAccessoryItem(102),
      CatalogAccessoryItem(119),
      CatalogAccessoryItem(136),
      CatalogAccessoryItem(169),
      CatalogAccessoryItem(140),
      CatalogAccessoryItem(168),
      CatalogAccessoryItem(138),
      CatalogAccessoryItem(220),
      CatalogAccessoryItem(433),
      CatalogAccessoryItem(442),
      CatalogAccessoryItem(424),
      CatalogAccessoryItem(404),
      CatalogAccessoryItem(156),
      CatalogAccessoryItem(142),
      CatalogAccessoryItem(152),
      CatalogAccessoryItem(133),
      CatalogAccessoryItem(166),
      CatalogAccessoryItem(211),
      CatalogAccessoryItem(314),
      CatalogAccessoryItem(320),
      CatalogAccessoryItem(173),
      CatalogAccessoryItem(328),
      CatalogAccessoryItem(329),
      )
     ),
    )

WeeklySchedule = (

    ############################# SERIES 1 #############################

    # Series 1, week 1 (overall week 1)
    (100,                        # Basic shirt
     (5, 2000),                  # Basic chat
     3000,                       # Wallpaper
     3500,                       # Basic wainscoting
     4000,                       # Basic flooring
     4500,                       # Basic moulding
     CatalogEmoteItem(5),        # Shrug
     CatalogFurnitureItem(210, 0),  # Girly bed
     CatalogFurnitureItem(220, 0),  # Bathtub bed
     ),

    # Series 1, week 2 (overall week 2)
    (100,                        # Basic shirt
     (5, 2000),                  # Basic chat
     CatalogFurnitureItem(1400), # Painting: Cezanne Toon
     3000,                       # Wallpaper
     3500,                       # Basic wainscoting
     4000,                       # Basic flooring
     4500,                       # Basic moulding
     CatalogFurnitureItem(600),  # Short lamp
     CatalogFurnitureItem(610),  # Tall lamp
     CatalogClothingItem(116, 0),   # Exclusive boy shirt (yellow hooded sweatshirt)
     CatalogClothingItem(216, 0),   # Exclusive girl shirt (yellow hooded sweatshirt)
     ),

    # Series 1, week 3 (overall week 3)
    (300,                        # Basic bottoms
     (5, 2000),                  # Basic chat
     CatalogFurnitureItem(1410), # Painting: Flowers
     3000,                       # Wallpaper
     3500,                       # Basic wainscoting
     4000,                       # Basic flooring
     4500,                       # Basic moulding
     CatalogFurnitureItem(1100), # Cabinet Red Wood
     CatalogFurnitureItem(1020), # Rug Round B
     CatalogClothingItem(408, 0),   # Exclusive girl skirt (blue and tan skirt)
     5000,                       # Pet trick
     ),

    # Series 1, week 4 (overall week 4)
    (100,                        # Basic shirt
     (5, 2000),                  # Basic chat
     CatalogWindowItem(40),      # Window view: City
     3000,                       # Wallpaper
     3500,                       # Basic wainscoting
     4000,                       # Basic flooring
     4500,                       # Basic moulding
     CatalogFurnitureItem(110),  # Chair
     CatalogFurnitureItem(100),  # Chair A
     nextAvailablePole,
     ),

    # Series 1, week 5 (overall week 5)
    (100,                        # Basic shirt
     (5, 2000),                  # Basic chat
     CatalogFurnitureItem(1420), # Painting: Modern Mickey
     CatalogEmoteItem(9),        # Applause
     3000,                       # Wallpaper
     3500,                       # Basic wainscoting
     4000,                       # Basic flooring
     4500,                       # Basic moulding
     CatalogFurnitureItem(700),  # Small couch
     CatalogFurnitureItem(710),  # Large couch
     ),

    # Series 1, week 6 (overall week 6)
    (300,                        # Basic bottoms
     (5, 2000),                  # Basic chat
     3000,                       # Wallpaper
     3500,                       # Basic wainscoting
     4000,                       # Basic flooring
     4500,                       # Basic moulding
     CatalogFurnitureItem(410),  # Girly Fireplace
     CatalogAnimatedFurnitureItem(490), # Girly Fireplace with fire
     CatalogFurnitureItem(1000), # Rug square
     #nextAvailableBank,          # Bank
     CatalogClothingItem(117, 0),   # Exclusive boy shirt (yellow with palm)
     CatalogClothingItem(217, 0),   # Exclusive girl shirt (yellow with palm)
     ),

    # Series 1, week 7 (overall week 7)
    (100,                        # Basic shirt
     (5, 2000),                  # Basic chat
     CatalogFurnitureItem(1430), # Painting: Rembrandt Toon
     3000,                       # Wallpaper
     3500,                       # Basic wainscoting
     4000,                       # Basic flooring
     4500,                       # Basic moulding
     CatalogFurnitureItem(1510), # Radio B
     CatalogFurnitureItem(1610), # Vase B
     5000,                       # Pet trick
     CatalogNametagItem(1),
     ),

    # Series 1, week 8 (overall week 8)
    (100,                        # Basic shirt
     (5, 2000),                  # Basic chat
     CatalogWindowItem(70),      # Window view: Tropical Island
     3000,                       # Wallpaper
     3500,                       # Basic wainscoting
     4000,                       # Basic flooring
     4500,                       # Basic moulding
     CatalogFurnitureItem(1210), # Table
     CatalogClothingItem(409, 0),   # Exclusive girl shirt (pink and purple skirt)
     nextAvailablePole,
     ),

    # Series 1, week 9 (overall week 9)
    (300,                        # Basic bottoms
     (5, 2000),                  # Basic chat
     CatalogEmoteItem(13),       # Bow
     3000,                       # Wallpaper
     3500,                       # Basic wainscoting
     4000,                       # Basic flooring
     4500,                       # Basic moulding
     CatalogFurnitureItem(1200), # Night Stand (end table)
     CatalogFurnitureItem(900),  # Umbrella Stand
     ),

    # Series 1, week 10 (overall week 10)
    (100,                        # Basic shirt
     (5, 2000),                  # Basic chat
     3000,                       # Wallpaper
     3500,                       # Basic wainscoting
     4000,                       # Basic flooring
     4500,                       # Basic moulding
     CatalogFurnitureItem(910),  # Coat Rack
     CatalogFurnitureItem(1600), # Vase A
     CatalogClothingItem(118, 0),   # Exclusive boy shirt (blue with blue and white stripes)
     CatalogClothingItem(218, 0),   # Exclusive girl shirt (blue with 3 yellow stripes)
     ),

    # Series 1, week 11 (overall week 11)
    (100,                        # Basic shirt
     (5, 2000),                  # Basic chat
     3000,                       # Wallpaper
     3500,                       # Basic wainscoting
     4000,                       # Basic flooring
     4500,                       # Basic moulding
     CatalogFurnitureItem(800),  # Desk
     CatalogFurnitureItem(1010), # Round Rug A
     CatalogClothingItem(410, 0),   # Exclusive girl shirt (green and yellow with star)
     5000,                       # Pet trick
     ),

    # Series 1, week 12 (overall week 12)
    (300,                        # Basic bottoms
     (5, 2000),                  # Basic chat
     3000,                       # Wallpaper
     3500,                       # Basic wainscoting
     4000,                       # Basic flooring
     4500,                       # Basic moulding
     CatalogFurnitureItem(620),  # Lamp A
     #nextAvailableBank,          # Bank
     nextAvailablePole,          # Pole
     nextAvailableCloset,        # Wardrobe
     ),

    # Series 1, week 13 (overall week 13)
    (300,                        # Basic bottoms
     (5, 2000),                  # Basic chat
     3000,                       # Wallpaper
     3500,                       # Basic wainscoting
     4000,                       # Basic flooring
     4500,                       # Basic moulding
     CatalogClothingItem(119, 0),   # Exclusive boy shirt (orange)
     CatalogClothingItem(219, 0),   # Exclusive girl shirt (pink and beige)
     ),

    ############################# SERIES 2 #############################

    # Series 2, week 1 (overall week 14)
    (100,                        # Basic shirt
     (2, 2000),                  # Basic chat from series 1
     (3, 2010),                  # Basic chat from series 2
     3010,                       # Wallpaper
     3510,                       # Basic wainscoting
     4010,                       # Basic flooring
     4510,                       # Basic moulding
     CatalogFurnitureItem(1110), # Yellow Wood Cabinet
     CatalogFurnitureItem(630),  # Bug Room Daisy Lamp 1
     CatalogFurnitureItem(1630), # Vase B tall
     CatalogEmoteItem(11),       # Emote: Confused
     CatalogNametagItem(11),
     ),

    # Series 2, week 2 (overall week 15)
    (100,                        # Basic shirt
     (2, 2000),                  # Basic chat from series 1
     (3, 2010),                  # Basic chat from series 2
     3010,                       # Wallpaper
     3510,                       # Basic wainscoting
     4010,                       # Basic flooring
     4510,                       # Basic moulding
     CatalogFurnitureItem(230),  # Bug Room Bed
     CatalogFurnitureItem(920),  # Trashcan
     CatalogFurnitureItem(1440), # Painting: Toon Landscape
     ),

    # Series 2, week 3 (overall week 16)
    (300,                        # Basic bottoms
     (2, 2000),                  # Basic chat from series 1
     (3, 2010),                  # Basic chat from series 2
     3010,                       # Wallpaper
     3510,                       # Basic wainscoting
     4010,                       # Basic flooring
     4510,                       # Basic moulding
     CatalogFurnitureItem(420),  # Round Fireplace
     CatalogAnimatedFurnitureItem(480), # Round Fireplace with fire
     CatalogFurnitureItem(120),  # Desk chair
     CatalogClothingItem(120, 0),# Exclusive boy shirt
     CatalogClothingItem(220, 0),# Exclusive girl shirt
     nextAvailablePole,          # Next Fishing pole
     5000,                       # Pet trick
     ),

    # Series 2, week 4 (overall week 17)
    (100,                        # Basic shirt
     (2, 2000),                  # Basic chat from series 1
     (3, 2010),                  # Basic chat from series 2
     3010,                       # Wallpaper
     3510,                       # Basic wainscoting
     4010,                       # Basic flooring
     4510,                       # Basic moulding
     CatalogFurnitureItem(1700), # Popcorn cart
     CatalogFurnitureItem(640),  # Bug Room Daisy Lamp 2
     CatalogWindowItem(50),      # Window view: Western
     ),

    # Series 2, week 5 (overall week 18)
    (100,                        # Basic shirt
     (2, 2000),                  # Basic chat from series 1
     (3, 2010),                  # Basic chat from series 2
     3010,                       # Wallpaper
     3510,                       # Basic wainscoting
     4010,                       # Basic flooring
     4510,                       # Basic moulding
     CatalogFurnitureItem(1120), # Bookcase - Tall
     CatalogFurnitureItem(930),  # Bug Room Red Pot
     CatalogFurnitureItem(1500), # Radio A
     CatalogEmoteItem(6),        # Emote: Victory Dance
     nextAvailableCloset,        # Wardrobe
     ),

    # Series 2, week 6 (overall week 19)
    (300,                        # Basic bottoms
     (2, 2000),                  # Basic chat from series 1
     (3, 2010),                  # Basic chat from series 2
     3010,                       # Wallpaper
     3510,                       # Basic wainscoting
     4010,                       # Basic flooring
     4510,                       # Basic moulding
     CatalogFurnitureItem(430),  # Bug Room Fireplace
     CatalogAnimatedFurnitureItem(491), # Bug Room Fireplace with fire
     CatalogFurnitureItem(1620), # Vase B short
     CatalogFurnitureItem(1442), # Painting: Degas Toon Star
     #nextAvailableBank,          # Bank
     ),

    # Series 2, week 7 (overall week 20)
    (100,                        # Basic shirt
     (2, 2000),                  # Basic chat from series 1
     (3, 2010),                  # Basic chat from series 2
     3010,                       # Wallpaper
     3510,                       # Basic wainscoting
     4010,                       # Basic flooring
     4510,                       # Basic moulding
     CatalogFurnitureItem(610),  # Tall lamp
     CatalogFurnitureItem(940),  # Bug Room Yellow Pot
     CatalogClothingItem(121, 0),# Exclusive boy shirt
     CatalogClothingItem(221, 0),# Exclusive girl shirt
     nextAvailablePole,          # Next Fishing pole
     5000,                       # Pet trick
     ),

    # Series 2, week 8 (overall week 21)
    (100,                        # Basic shirt
     (2, 2000),                  # Basic chat from series 1
     (3, 2010),                  # Basic chat from series 2
     3010,                       # Wallpaper
     3510,                       # Basic wainscoting
     4010,                       # Basic flooring
     4510,                       # Basic moulding
     CatalogFurnitureItem(1710), # Bug Room Ladybug
     CatalogFurnitureItem(1030), # Bug Room Leaf Mat
     CatalogWindowItem(60),      # Window view: Underwater
     CatalogNametagItem(7),
     ),

    # Series 2, week 9 (overall week 22)
    (300,                        # Basic bottoms
     (2, 2000),                  # Basic chat from series 1
     (3, 2010),                  # Basic chat from series 2
     3010,                       # Wallpaper
     3510,                       # Basic wainscoting
     4010,                       # Basic flooring
     4510,                       # Basic moulding
     CatalogFurnitureItem(1130), # Bookcase - Low
     CatalogFurnitureItem(130),  # Bug room chair
     CatalogEmoteItem(8),        # Emote: Bored
     ),

    # Series 2, week 10 (overall week 23)
    (100,                        # Basic shirt
     (2, 2000),                  # Basic chat from series 1
     (3, 2010),                  # Basic chat from series 2
     3010,                       # Wallpaper
     3510,                       # Basic wainscoting
     4010,                       # Basic flooring
     4510,                       # Basic moulding
     CatalogFurnitureItem(1530), # Bug Room TV
     CatalogFurnitureItem(1640), # Vase C short
     CatalogFurnitureItem(1441), # Painting: Whistler's horse
     ),

    # Series 2, week 11 (overall week 24)
    (100,                        # Basic shirt
     (2, 2000),                  # Basic chat from series 1
     (3, 2010),                  # Basic chat from series 2
     3010,                       # Wallpaper
     3510,                       # Basic wainscoting
     4010,                       # Basic flooring
     4510,                       # Basic moulding
     CatalogFurnitureItem(300),  # Piano
     CatalogFurnitureItem(1220), # Coffee table
     nextAvailablePole,          # Next Fishing pole
     5000,                       # Pet trick
     ),

    # Series 2, week 12 (overall week 25)
    (300,                        # Basic bottoms
     (2, 2000),                  # Basic chat from series 1
     (3, 2010),                  # Basic chat from series 2
     3010,                       # Wallpaper
     3510,                       # Basic wainscoting
     4010,                       # Basic flooring
     4510,                       # Basic moulding
     CatalogFurnitureItem(810),  # Bug Room Desk
     CatalogFurnitureItem(1230), # Coffee table
     CatalogFurnitureItem(1443), # Painting: Magritte Toon Pie
     #nextAvailableBank,          # Bank
     ),

    # Series 2, week 13 (overall week 26)
    (300,                        # Basic bottoms
     (2, 2000),                  # Basic chat from series 1
     (3, 2010),                  # Basic chat from series 2
     3010,                       # Wallpaper
     3510,                       # Basic wainscoting
     4010,                       # Basic flooring
     4510,                       # Basic moulding
     CatalogFurnitureItem(310),  # Organ
     CatalogFurnitureItem(1520), # Radio C
     CatalogFurnitureItem(1650), # Vase D short
     CatalogWindowItem(80),      # Window view: Starry night
     #CatalogClothingItem(120, 0),# Exclusive boy shirt
     CatalogClothingItem(222, 0),# Exclusive girl shirt
     nextAvailableCloset,        # Wardrobe
     ),

    ############################# SERIES 3 #############################

    # Series 3, week 1 (overall week 27)
     (100,                        # Basic shirt
      (1, 2000),                  # Basic chat from series 1
      (2, 2010),                  # Basic chat from series 2
      (3, 2020),                  # Basic chat from series 3
      3020,                       # Wallpaper
      3530,                       # Basic wainscoting
      4020,                       # Basic flooring
      4520,                       # Basic moulding
      CatalogFurnitureItem(1240), # Snorkelers Table
      CatalogFurnitureItem(1661), # Shell Vase
      CatalogEmoteItem(5),        # Shrug
      ),
    # Series 3, week 2 (overall week 28)
     (100,                        # Basic shirt
      (1, 2000),                  # Basic chat from series 1
      (2, 2010),                  # Basic chat from series 2
      (3, 2020),                  # Basic chat from series 3
      3020,                       # Wallpaper
      3530,                       # Basic wainscoting
      4020,                       # Basic flooring
      4520,                       # Basic moulding
      CatalogFurnitureItem(1800), # Fish Bowl 1
      CatalogFurnitureItem(240),  # Boat bed
      CatalogFurnitureItem(1200), # Night Stand (end table)
      CatalogNametagItem(12),
      ),
    # Series 3, week 3 (overall week 29)
     (300,                        # Basic bottoms
      (1, 2000),                  # Basic chat from series 1
      (2, 2010),                  # Basic chat from series 2
      (3, 2020),                  # Basic chat from series 3
      3020,                       # Wallpaper
      3530,                       # Basic wainscoting
      4020,                       # Basic flooring
      4520,                       # Basic moulding
      CatalogFurnitureItem(145),  # Lifejacket chair
      CatalogClothingItem(123, 0),# Exclusive shirt (tie dye boy)
      CatalogClothingItem(224, 0),# Exclusive shirt (tie dye girl)
      nextAvailablePole,          # Next Fishing pole
      5000,                       # Pet trick
      ),
    # Series 3, week 4 (overall week 30)
     (100,                        # Basic shirt
      (1, 2000),                  # Basic chat from series 1
      (2, 2010),                  # Basic chat from series 2
      (3, 2020),                  # Basic chat from series 3
      3020,                       # Wallpaper
      3530,                       # Basic wainscoting
      4020,                       # Basic flooring
      4520,                       # Basic moulding
      CatalogWindowItem(100),     # Window view: Snow
      CatalogFurnitureItem(1810), # Fish Bowl 2
      nextAvailableCloset,        # Wardrobe
      ),
    # Series 3, week 5 (overall week 31)
     (100,                        # Basic shirt
      (1, 2000),                  # Basic chat from series 1
      (2, 2010),                  # Basic chat from series 2
      (3, 2020),                  # Basic chat from series 3
      3020,                       # Wallpaper
      3530,                       # Basic wainscoting
      4020,                       # Basic flooring
      4520,                       # Basic moulding
      CatalogFurnitureItem(650),  # Jellyfish Lamp 1
      CatalogFurnitureItem(1900), # Swordfish Trophy
      ),
    # Series 3, week 6 (overall week 32)
     (300,                        # Basic bottoms
      (1, 2000),                  # Basic chat from series 1
      (2, 2010),                  # Basic chat from series 2
      (3, 2020),                  # Basic chat from series 3
      3020,                       # Wallpaper
      3530,                       # Basic wainscoting
      4020,                       # Basic flooring
      4520,                       # Basic moulding
      CatalogFurnitureItem(1725), # Washing Machine
      #nextAvailableBank,          # Bank
      ),
    # Series 3, week 7 (overall week 33)
     (100,                        # Basic shirt
      (1, 2000),                  # Basic chat from series 1
      (2, 2010),                  # Basic chat from series 2
      (3, 2020),                  # Basic chat from series 3
      3020,                       # Wallpaper
      3530,                       # Basic wainscoting
      4020,                       # Basic flooring
      4520,                       # Basic moulding
      CatalogWindowItem(90),      # Window view: Pool
      CatalogClothingItem(124, 0),# Exclusive boy shirt
      CatalogClothingItem(411, 0),# Exclusive girl skirt, rainbow
      nextAvailablePole,          # Next Fishing pole
      ),
    # Series 3, week 8 (overall week 34)
     (100,                        # Basic shirt
      (1, 2000),                  # Basic chat from series 1
      (2, 2010),                  # Basic chat from series 2
      (3, 2020),                  # Basic chat from series 3
      3020,                       # Wallpaper
      3530,                       # Basic wainscoting
      4020,                       # Basic flooring
      4520,                       # Basic moulding
      CatalogFurnitureItem(140),  # Lobster chair
      CatalogFurnitureItem(1020), # Rug Round B
      CatalogEmoteItem(13),       # Bow
      ),
    # Series 3, week 9 (overall week 35)
     (300,                        # Basic bottoms
      (1, 2000),                  # Basic chat from series 1
      (2, 2010),                  # Basic chat from series 2
      (3, 2020),                  # Basic chat from series 3
      3020,                       # Wallpaper
      3530,                       # Basic wainscoting
      4020,                       # Basic flooring
      4520,                       # Basic moulding
      CatalogFurnitureItem(950),  # Coral Coat Rack
      CatalogFurnitureItem(1660), # Coral Vase
      CatalogClothingItem(310, 0),# Exclusive shorts (orange w/ blue side stripes)
      CatalogNametagItem(2),
      ),
    # Series 3, week 10 (overall week 36)
     (100,                        # Basic shirt
      (1, 2000),                  # Basic chat from series 1
      (2, 2010),                  # Basic chat from series 2
      (3, 2020),                  # Basic chat from series 3
      3020,                       # Wallpaper
      3530,                       # Basic wainscoting
      4020,                       # Basic flooring
      4520,                       # Basic moulding
      CatalogFurnitureItem(400),  # Square Fireplace
      CatalogAnimatedFurnitureItem(470), # Square Fireplace with fire
      CatalogFurnitureItem(660),  # Jellyfish Lamp 2
      CatalogFurnitureItem(1200), # Night Stand (end table)
      nextAvailableCloset,        # Wardrobe
      5000,                       # Pet trick
      ),
    # Series 3, week 11 (overall week 37)
     (100,                        # Basic shirt
      (1, 2000),                  # Basic chat from series 1
      (2, 2010),                  # Basic chat from series 2
      (3, 2020),                  # Basic chat from series 3
      3020,                       # Wallpaper
      3530,                       # Basic wainscoting
      4020,                       # Basic flooring
      4520,                       # Basic moulding
      CatalogFurnitureItem(1910), # Hammerhead trophy
      nextAvailablePole,          # Next Fishing pole
      CatalogFurnitureItem(1000), # Rug square
     ),
    # Series 3, week 12 (overall week 38)
     (300,                        # Basic bottoms
      (1, 2000),                  # Basic chat from series 1
      (2, 2010),                  # Basic chat from series 2
      (3, 2020),                  # Basic chat from series 3
      3020,                       # Wallpaper
      3530,                       # Basic wainscoting
      4020,                       # Basic flooring
      4520,                       # Basic moulding
      CatalogFurnitureItem(1720), # Fountain
      #nextAvailableBank,          # Bank
      CatalogEmoteItem(9),        # Applause
      ),
    # Series 3, week 13 (overall week 39)
     (300,                        # Basic bottoms
      (1, 2000),                  # Basic chat from series 1
      (2, 2010),                  # Basic chat from series 2
      (3, 2020),                  # Basic chat from series 3
      3020,                       # Wallpaper
      3530,                       # Basic wainscoting
      4020,                       # Basic flooring
      4520,                       # Basic moulding
      CatalogWindowItem(110),     # Window view: Farm
      CatalogClothingItem(311, 0),# Exclusive shorts (blue with yellow cuff)
      ),

    ############################# SERIES 4 #############################

    # Series 4, week 1 (overall week 40)
     (100,                        # Basic shirt
      (1, 2010),                  # Basic chat from series 2
      (2, 2020),                  # Basic chat from series 3
      (3, 2030),                  # Basic chat from series 4
      3020,                       # Wallpaper
      3530,                       # Basic wainscoting
      4020,                       # Basic flooring
      4520,                       # Basic moulding
      CatalogWindowItem(120),     # Window view: Native Camp.
      CatalogClothingItem(125, 0),# Cowboy shirts.
      5000,                       # Pet trick
      ),
    # Series 4, week 2 (overall week 41)
    (300,                        # Basic bottoms
     (1, 2010),                  # Basic chat from series 2
     (2, 2020),                  # Basic chat from series 3
     (3, 2030),                  # Basic chat from series 4
     3020,                       # Wallpaper
     3530,                       # Basic wainscoting
     4020,                       # Basic flooring
     4520,                       # Basic moulding
     CatalogClothingItem(412, 0),# Girls western skirts.
     CatalogClothingItem(312, 0),# Boys cowboy shorts.
     CatalogFurnitureItem(1920), # Hanging Horns.
     ),
    # Series 4, week 3 (overall week 42)
    (100,                        # Basic shirt
     (1, 2010),                  # Basic chat from series 2
     (2, 2020),                  # Basic chat from series 3
     (3, 2030),                  # Basic chat from series 4
     3020,                       # Wallpaper
     3530,                       # Basic wainscoting
     4020,                       # Basic flooring
     4520,                       # Basic moulding
     nextAvailablePole,          # Next Fishing pole
     CatalogWallpaperItem(3900), # Hat Wallpaper.
     CatalogFurnitureItem(980),  # Tepee.
     CatalogNametagItem(13),
     ),
    # Series 4, week 4 (overall week 43)
    (300,                        # Basic bottoms
     (1, 2010),                  # Basic chat from series 2
     (2, 2020),                  # Basic chat from series 3
     (3, 2030),                  # Basic chat from series 4
     3020,                       # Wallpaper
     3530,                       # Basic wainscoting
     4020,                       # Basic flooring
     4520,                       # Basic moulding
     CatalogClothingItem(130, 0),# Cowboy shirts.
     CatalogFurnitureItem(150),  # Saddle Stool.
     nextAvailableCloset,        # Wardrobe
     ),
    # Series 4, week 5 (overall week 44)
    (100,                        # Basic shirt
     (1, 2010),                  # Basic chat from series 2
     (2, 2020),                  # Basic chat from series 3
     (3, 2030),                  # Basic chat from series 4
     3020,                       # Wallpaper
     3530,                       # Basic wainscoting
     4020,                       # Basic flooring
     4520,                       # Basic moulding
     CatalogClothingItem(128, 0),# Cowboy shirts.
     CatalogWallpaperItem(3700), # Boot Wallpaper.
     CatalogFurnitureItem(160),  # Native Chair.
     ),
    # Series 4, week 6 (overall week 45)
    (300,                        # Basic bottoms
     (1, 2010),                  # Basic chat from series 2
     (2, 2020),                  # Basic chat from series 3
     (3, 2030),                  # Basic chat from series 4
     3020,                       # Wallpaper
     3530,                       # Basic wainscoting
     4020,                       # Basic flooring
     4520,                       # Basic moulding
     #nextAvailableBank,          # Bank
     CatalogClothingItem(313, 0),# Boys cowboy shorts.
     CatalogClothingItem(413, 0),# Girls western skirts.
     CatalogFurnitureItem(960),  # Barrel Stand.
     CatalogEmoteItem(7),        # Think
     ),
    # Series 4, week 7 (overall week 46)
    (100,                        # Basic shirt
     (1, 2010),                  # Basic chat from series 2
     (2, 2020),                  # Basic chat from series 3
     (3, 2030),                  # Basic chat from series 4
     3020,                       # Wallpaper
     3530,                       # Basic wainscoting
     4020,                       # Basic flooring
     4520,                       # gBasic moulding
     nextAvailablePole,          # Next Fishing pole
     CatalogFurnitureItem(1930), # Simple Sombrero.
     CatalogFurnitureItem(670),  # Cowboy Lamp.
     ),
    # Series 4, week 8 (overall week 47)
    (300,                        # Basic bottoms
     (1, 2010),                  # Basic chat from series 2
     (2, 2020),                  # Basic chat from series 3
     (3, 2030),                  # Basic chat from series 4
     3020,                       # Wallpaper
     3530,                       # Basic wainscoting
     4020,                       # Basic flooring
     4520,                       # Basic moulding
     CatalogClothingItem(126, 0),# Cowboy shirts.
     CatalogFurnitureItem(1970), # Bison portrait.
     5000,                       # Pet trick
     ),
    # Series 4, week 9 (overall week 48)
    (100,                        # Basic shirt
     (1, 2010),                  # Basic chat from series 2
     (2, 2020),                  # Basic chat from series 3
     (3, 2030),                  # Basic chat from series 4
     3020,                       # Wallpaper
     3530,                       # Basic wainscoting
     4020,                       # Basic flooring
     4520,                       # Basic moulding
     CatalogFurnitureItem(720),  # Hay Couch.
     CatalogFurnitureItem(970),  # Fat Cactus.
     nextAvailableCloset,        # Wardrobe
     ),
    # Series 4, week 10 (overall week 49)
    (300,                        # Basic bottoms
     (1, 2010),                  # Basic chat from series 2
     (2, 2020),                  # Basic chat from series 3
     (3, 2030),                  # Basic chat from series 4
     3020,                       # Wallpaper
     3530,                       # Basic wainscoting
     4020,                       # Basic flooring
     4520,                       # Basic moulding
     CatalogClothingItem(127, 0),# Cowboy shirts.
     CatalogFurnitureItem(1950), # Coyote paw wall hanging.
     CatalogNametagItem(4),
     ),
    # Series 4, week 11 (overall week 50)
    (100,                        # Basic shirt
     (1, 2010),                  # Basic chat from series 2
     (2, 2020),                  # Basic chat from series 3
     (3, 2030),                  # Basic chat from series 4
     3020,                       # Wallpaper
     3530,                       # Basic wainscoting
     4020,                       # Basic flooring
     4520,                       # Basic moulding
     nextAvailablePole,          # Next Fishing pole
     CatalogFurnitureItem(1940), # Fancy Sombrero.
     CatalogWindowItem(130),     # Main Street View.
     ),
    # Series 4, week 12 (overall week 51)
    (300,                        # Basic bottoms
     (1, 2010),                  # Basic chat from series 2
     (2, 2020),                  # Basic chat from series 3
     (3, 2030),                  # Basic chat from series 4
     3020,                       # Wallpaper
     3530,                       # Basic wainscoting
     4020,                       # Basic flooring
     4520,                       # Basic moulding
     #nextAvailableBank,          # Bank
     CatalogWallpaperItem(3800), # Cactus Wallpaper.
     CatalogClothingItem(129, 0),# Cowboy shirts.
     CatalogEmoteItem(10),       # Cringe
     ),
    # Series 4, week 13 (overall week 52)
    (100,                        # Basic shirt
     (1, 2010),                  # Basic chat from series 2
     (2, 2020),                  # Basic chat from series 3
     (3, 2030),                  # Basic chat from series 4
     3020,                       # Wallpaper
     3530,                       # Basic wainscoting
     4020,                       # Basic flooring
     4520,                       # Basic moulding
     CatalogFurnitureItem(250),  # Cactus Hammoc.
     CatalogFurnitureItem(1960), # Horseshoe wall hanging.
     nextAvailablePole,          # Next Fishing pole
     ),

    ############################# SERIES 5 #############################

    ## NOTE: This is a short catalog (only 5 weeks). The remainder of this
    ##       thirteen week period is provided by Catalog Series 6 (8 weeks).

    # Series 5, week 1 (overall week 53) - Furniture Sale
    Sale(
    CatalogFurnitureItem(210, 0),  # Girly bed
    CatalogFurnitureItem(220, 0),  # Bathtub bed
    CatalogFurnitureItem(1100), # Cabinet Red Wood
    CatalogFurnitureItem(110),  # Chair
    CatalogFurnitureItem(100),  # Chair A
    CatalogFurnitureItem(700),  # Small couch
    CatalogFurnitureItem(710),  # Large couch
    CatalogFurnitureItem(410),  # Girly Fireplace
    CatalogAnimatedFurnitureItem(490), # Girly Fireplace with fire
    CatalogFurnitureItem(1210), # Table
    CatalogFurnitureItem(1200), # Night Stand (end table)
    CatalogFurnitureItem(800),  # Desk
    CatalogFurnitureItem(1110), # Yellow Wood Cabinet
    CatalogFurnitureItem(230),  # Bug Room Bed
    CatalogFurnitureItem(420),  # Round Fireplace
    CatalogAnimatedFurnitureItem(480), # Round Fireplace with fire
    CatalogFurnitureItem(120),  # Desk chair
    CatalogFurnitureItem(1700), # Popcorn cart
    CatalogFurnitureItem(1120), # Bookcase - Tall
    CatalogFurnitureItem(430),  # Bug Room Fireplace
    CatalogAnimatedFurnitureItem(491), # Bug Room Fireplace
    CatalogFurnitureItem(1130), # Bookcase - Low
    CatalogFurnitureItem(130),  # Bug room chair
    CatalogFurnitureItem(300),  # Piano
    CatalogFurnitureItem(1220), # Coffee table
    CatalogFurnitureItem(810),  # Bug Room Desk
    CatalogFurnitureItem(1230), # Coffee table
    CatalogFurnitureItem(310),  # Organ
    CatalogFurnitureItem(1240), # Snorkelers Table
    CatalogFurnitureItem(240),  # Boat bed
    CatalogFurnitureItem(145),  # Lifejacket chair
    CatalogFurnitureItem(1725), # Washing Machine
    CatalogFurnitureItem(140),  # Lobster chair
    CatalogFurnitureItem(950),  # Coral Coat Rack
    CatalogFurnitureItem(1720), # Fountain
    ),

    # Series 5, week 2 (overall week 54) - Clothing Sale
    Sale(
    CatalogClothingItem(116, 0),   # Exclusive boy shirt (yellow hooded sweatshirt)
    CatalogClothingItem(216, 0),   # Exclusive girl shirt (yellow hooded sweatshirt)
    CatalogClothingItem(408, 0),   # Exclusive girl skirt (blue and tan skirt)
    CatalogClothingItem(117, 0),   # Exclusive boy shirt (yellow with palm)
    CatalogClothingItem(217, 0),   # Exclusive girl shirt (yellow with palm)
    CatalogClothingItem(409, 0),   # Exclusive girl shirt (pink and purple skirt)
    CatalogClothingItem(118, 0),   # Exclusive boy shirt (blue with blue and white stripes)
    CatalogClothingItem(218, 0),   # Exclusive girl shirt (blue with 3 yellow stripes)
    CatalogClothingItem(410, 0),   # Exclusive girl shirt (green and yellow with star)
    CatalogClothingItem(119, 0),   # Exclusive boy shirt (orange)
    CatalogClothingItem(219, 0),   # Exclusive girl shirt (pink and beige)
    CatalogClothingItem(120, 0),   # Exclusive boy shirt
    CatalogClothingItem(220, 0),   # Exclusive girl shirt
    CatalogClothingItem(121, 0),   # Exclusive boy shirt
    CatalogClothingItem(221, 0),   # Exclusive girl shirt
    CatalogClothingItem(222, 0),   # Exclusive girl shirt
    CatalogClothingItem(123, 0),   # Exclusive shirt (tie dye boy)
    CatalogClothingItem(224, 0),   # Exclusive shirt (tie dye girl)
    CatalogClothingItem(411, 0),   # Exclusive girl skirt, rainbow
    CatalogClothingItem(311, 0),   # Exclusive shorts (blue with yellow cuff)
    CatalogClothingItem(310, 0),   # Exclusive shorts (orange w/ blue side stripes)
    ),

    # Series 5, week 3 (overall week 55) - Window View Sale
    Sale(
    CatalogWindowItem(40),      # Window view: City
    CatalogWindowItem(70),      # Window view: Tropical Island
    CatalogWindowItem(50),      # Window view: Western
    CatalogWindowItem(60),      # Window view: Underwater
    CatalogWindowItem(80),      # Window view: Starry night
    CatalogWindowItem(100),     # Window view: Snow
    CatalogWindowItem(90),      # Window view: Pool
    CatalogWindowItem(110),     # Window view: Farm
    ),

    # Series 5, week 4 (overall week 56) - Emote Sale
    Sale(
    CatalogEmoteItem(5),        # Shrug
    CatalogEmoteItem(9),        # Applause
    CatalogEmoteItem(13),       # Bow
    CatalogEmoteItem(11),       # Confused
    CatalogEmoteItem(6),        # Victory Dance
    CatalogEmoteItem(8),        # Bored
    CatalogNametagItem(10),
    ),

    # Series 5, week 5 (overall week 57) - Knick-knack Sale
    Sale(
    CatalogFurnitureItem(600),  # Short lamp
    CatalogFurnitureItem(610),  # Tall lamp
    CatalogFurnitureItem(620),  # Lamp A
    CatalogFurnitureItem(630),  # Bug Room Daisy Lamp 1
    CatalogFurnitureItem(640),  # Bug Room Daisy Lamp 2
    CatalogFurnitureItem(650),  # Jellyfish Lamp 1
    CatalogFurnitureItem(660),  # Jellyfish Lamp 2
    CatalogFurnitureItem(900),  # Umbrella Stand
    CatalogFurnitureItem(910),  # Coat Rack
    CatalogFurnitureItem(920),  # Trashcan
    CatalogFurnitureItem(930),  # Bug Room Red Pot
    CatalogFurnitureItem(940),  # Bug Room Yellow Pot
    CatalogFurnitureItem(1000), # Rug square
    CatalogFurnitureItem(1010), # Round Rug A
    CatalogFurnitureItem(1020), # Rug Round B
    CatalogFurnitureItem(1030), # Bug Room Leaf Mat
    CatalogFurnitureItem(1400), # Painting: Cezanne Toon
    CatalogFurnitureItem(1410), # Painting: Flowers
    CatalogFurnitureItem(1420), # Painting: Modern Mickey
    CatalogFurnitureItem(1430), # Painting: Rembrandt Toon
    CatalogFurnitureItem(1440), # Painting: Toon Landscape
    CatalogFurnitureItem(1441), # Painting: Whistler's horse
    CatalogFurnitureItem(1442), # Painting: Degas Toon Star
    CatalogFurnitureItem(1443), # Painting: Magritte Toon Pie
    CatalogFurnitureItem(1500), # Radio A
    CatalogFurnitureItem(1510), # Radio B
    CatalogFurnitureItem(1520), # Radio C
    CatalogFurnitureItem(1530), # Bug Room TV
    CatalogFurnitureItem(1600), # Vase A
    CatalogFurnitureItem(1610), # Vase B
    CatalogFurnitureItem(1620), # Vase B short
    CatalogFurnitureItem(1630), # Vase B tall
    CatalogFurnitureItem(1640), # Vase C short
    CatalogFurnitureItem(1650), # Vase D short
    CatalogFurnitureItem(1660), # Coral Vase
    CatalogFurnitureItem(1661), # Shell Vase
    CatalogFurnitureItem(1710), # Bug Room gLadybug
    CatalogFurnitureItem(1800), # Fish Bowl 1
    CatalogFurnitureItem(1810), # Fish Bowl 2
    CatalogFurnitureItem(1900), # Swordfish Trophy
    CatalogFurnitureItem(1910), # Hammerhead trophy
    ),

    ############################# SERIES 6 #############################

    ## NOTE: This is a short catalog (only 8 weeks). This series makes up the
    ##       difference between the sale catalog (Series 5) and a full catalog.

    # Series 6, week 1 (overall week 58) - Candy Items
    (300,                        # Basic bottoms
     (1, 2020),                  # Basic chat from series 3
     (2, 2030),                  # Basic chat from series 4
     (3, 2040),                  # Basic chat from series 6
     CatalogFurnitureItem(730),  # Twinkie Couch
     nextAvailablePole,          # Next Fishing pole
     ),

    # Series 6, week 2 (overall week 59) - Candy Items
    (100,                        # Basic shirt
     (1, 2020),                  # Basic chat from series 3
     (2, 2030),                  # Basic chat from series 4
     (3, 2040),                  # Basic chat from series 6
     CatalogFurnitureItem(260),  # Ice Cream Bed
     #nextAvailableBank,          # Bank
     ),

    # Series 6, week 3 (overall week 60) - Candy Items
    (300,                        # Basic bottoms
     (1, 2020),                  # Basic chat from series 3
     (2, 2030),                  # Basic chat from series 4
     (3, 2040),                  # Basic chat from series 6
     CatalogFurnitureItem(440),  # Caramel Apple Fireplace
     CatalogAnimatedFurnitureItem(492), # Caramel Apple Fireplace with fire
     nextAvailableCloset,        # Wardrobe
     5000,                       # Pet trick
     ),

    # Series 6, week 4 (overall week 61) - Candy Items
    (100,                        # Basic shirt
     (1, 2020),                  # Basic chat from series 3
     (2, 2030),                  # Basic chat from series 4
     (3, 2040),                  # Basic chat from series 6
     CatalogFurnitureItem(170),  # Cupcake Chair
     CatalogFurnitureItem(1250), # Cookie Table
     ),

    # Series 6, week 5 (overall week 62) - Candy Items
    (300,                        # Basic bottoms
     (1, 2020),                  # Basic chat from series 3
     (2, 2030),                  # Basic chat from series 4
     (3, 2040),                  # Basic chat from series 6
     CatalogFurnitureItem(1140), # Ice Cream Chest
     nextAvailablePole,          # Next Fishing pole
    ),

    # Series 6, week 6 (overall week 63) - Candy Items
    (100,                        # Basic shirt
     (1, 2020),                  # Basic chat from series 3
     (2, 2030),                  # Basic chat from series 4
     (3, 2040),                  # Basic chat from series 6
     CatalogFurnitureItem(2010), # Candy Cake Slide
     CatalogNametagItem(8),
     ),

    # Series 6, week 7 (overall week 64) - Candy Items
    (300,                        # Basic bottoms
     (1, 2020),                  # Basic chat from series 3
     (2, 2030),                  # Basic chat from series 4
     (3, 2040),                  # Basic chat from series 6
     CatalogFurnitureItem(2000), # Candy Swing Set
     5000,                       # Pet trick
     ),

    # Series 6, week 8 (overall week 65) - Candy Items
    (100,                        # Basic shirt
     (1, 2020),                  # Basic chat from series 3
     (2, 2030),                  # Basic chat from series 4
     (3, 2040),                  # Basic chat from series 6
     CatalogFurnitureItem(3000), # Candy Banana Split Shower
     #nextAvailableBank,          # Bank
     ),

    ############################# SERIES 7 #############################

    # Series 7, week 1 (overall week 66) - Color Setable Items
    (300,                        # Basic bottoms
     (1, 2030),                  # Basic chat from series 4
     (2, 2040),                  # Basic chat from series 5
     (3, 2050),                  # Basic chat from series 7
     CatalogClothingItem(131, 0),  # Green shirt w/ yellow buttons
     CatalogClothingItem(225, 0),  # Purple shirt w/ big flower
     nextAvailablePole,          # Next Fishing pole
     ),

    # Series 7, week 2 (overall week 67) - Color Setable Items
    (300,                        # Basic bottoms
     (1, 2030),                  # Basic chat from series 4
     (2, 2040),                  # Basic chat from series 5
     (3, 2050),                  # Basic chat from series 7
     CatalogFurnitureItem(105),  # Desat Chair A
     nextAvailableCloset,        # Wardrobe
     ),

    # Series 7, week 3 (overall week 68) - Color Setable Items
    (300,                        # Basic bottoms
     (1, 2030),                  # Basic chat from series 4
     (2, 2040),                  # Basic chat from series 5
     (3, 2050),                  # Basic chat from series 7
     CatalogFurnitureItem(205),  # Desat Boy's Bed
     ),

    # Series 7, week 4 (overall week 69) - Color Setable Items
    (300,                        # Basic bottoms
     (1, 2030),                  # Basic chat from series 4
     (2, 2040),                  # Basic chat from series 5
     (3, 2050),                  # Basic chat from series 7
     CatalogFurnitureItem(625),  # Desat Lamp A
     ),

    # Series 7, week 5 (overall week 70) - Color Setable Items
    (300,                        # Basic bottoms
     (1, 2030),                  # Basic chat from series 4
     (2, 2040),                  # Basic chat from series 5
     (3, 2050),                  # Basic chat from series 7
     nextAvailablePole,          # Next Fishing pole
     CatalogEmoteItem(12),       # Belly Flop
     CatalogNametagItem(5),
     ),

    # Series 7, week 6 (overall week 71) - Color Setable Items
    (300,                        # Basic bottoms
     (1, 2030),                  # Basic chat from series 4
     (2, 2040),                  # Basic chat from series 5
     (3, 2050),                  # Basic chat from series 7
     CatalogClothingItem(314, 0),  # Green striped shorts
     CatalogClothingItem(414, 0),  # Blue skirt w/ big flower
     #nextAvailableBank,          # Bank
     ),

    # Series 7, week 7 (overall week 72) - Color Setable Items
    (300,                        # Basic bottoms
     (1, 2030),                  # Basic chat from series 4
     (2, 2040),                  # Basic chat from series 5
     (3, 2050),                  # Basic chat from series 7
     CatalogFurnitureItem(715),  # Desat 2-person couch
     nextAvailableCloset,        # Wardrobe
     ),

    # Series 7, week 8 (overall week 73) - Color Setable Items
    (300,                        # Basic bottoms
     (1, 2030),                  # Basic chat from series 4
     (2, 2040),                  # Basic chat from series 5
     (3, 2050),                  # Basic chat from series 7
     CatalogFurnitureItem(1015),  # Desat Round Rug
     CatalogNametagItem(6),
     ),

    # Series 7, week 9 (overall week 74) - Color Setable Items
    (300,                        # Basic bottoms
     (1, 2030),                  # Basic chat from series 4
     (2, 2040),                  # Basic chat from series 5
     (3, 2050),                  # Basic chat from series 7
     CatalogFurnitureItem(1215),  # Desat Radio table
     nextAvailablePole,          # Next Fishing pole
     ),

    # Series 7, week 10 (overall week 75) - Color Setable Items
    (300,                        # Basic bottoms
     (1, 2030),                  # Basic chat from series 4
     (2, 2040),                  # Basic chat from series 5
     (3, 2050),                  # Basic chat from series 7
     CatalogEmoteItem(14),       # Banana Peel
     ),

    # Series 7, week 11 (overall week 76) - Color Setable Items
    (300,                        # Basic bottoms
     (1, 2030),                  # Basic chat from series 4
     (2, 2040),                  # Basic chat from series 5
     (3, 2050),                  # Basic chat from series 7
     CatalogFurnitureItem(1260),  # Desat Bedroom table
     ),

    # Series 7, week 12 (overall week 77) - Color Setable Items
    (300,                        # Basic bottoms
     (1, 2030),                  # Basic chat from series 4
     (2, 2040),                  # Basic chat from series 5
     (3, 2050),                  # Basic chat from series 7
     CatalogFurnitureItem(705),  # Desat 1-person couch
     CatalogNametagItem(3),
     ),

    # Series 7, week 13 (overall week 78) - Color Setable Items
    (300,                        # Basic bottoms
     (1, 2030),                  # Basic chat from series 4
     (2, 2040),                  # Basic chat from series 5
     (3, 2050),                  # Basic chat from series 7
     #nextAvailableBank,          # Bank
     nextAvailablePole,          # Next Fishing pole
     nextAvailableCloset,        # Wardrobe
     ),

    )

assert(len(WeeklySchedule) == ToontownGlobals.CatalogNumWeeks)

class CatalogGenerator:
    """CatalogGenerator

    This class is responsible for constructing a catalog of available
    items for a particular avatar.  It normally exists only on the AI.

    """

    notify = DirectNotifyGlobal.directNotify.newCategory("CatalogGenerator")

    def __init__(self):
        self.__itemLists = {}
        self.__releasedItemLists = {}

    def getReleasedCatalogList(self, weekStart):
        dayNumber = int(weekStart / (24 * 60))
        itemLists = self.__getReleasedItemLists(dayNumber, weekStart)
        return itemLists

    def generateMonthlyCatalog(self, avatar, weekStart):
        # Generates the list of items that should be offered to the
        # given avatar based on the seasonal specials this month.

        # weekStart is the date at which the catalog is considered to
        # have been generated, as minutes elapsed since the epoch.

        # This method is designed for use on the AI, but will function
        # properly on the client, given LocalToon (which is mainly
        # useful for testing).

        # Get the day offset.
        dayNumber = int(weekStart / (24 * 60))
        itemLists = self.__getMonthlyItemLists(dayNumber, weekStart)

        # Now build a list of items for this avatar.

        monthlyCatalog = CatalogItemList.CatalogItemList()

        for list in itemLists:
            saleItem = 0
            if isinstance(list, Sale):
                list = list.args
                saleItem = 1
            for item in list:
                monthlyCatalog += self.__selectItem(avatar, item, [], saleItem = saleItem)
        return monthlyCatalog

    def generateWeeklyCatalog(self, avatar, week, monthlyCatalog):
        # Generates the list of items that should be offered to the
        # given avatar for the current week.  We must have the actual
        # DistributedAvatar object handy so we can query it.

        # This method is designed for use on the AI, but will function
        # properly on the client, given LocalToon (which is mainly
        # useful for testing).

        weeklyCatalog = CatalogItemList.CatalogItemList()

        self.notify.debug("Generating catalog for %s for week %s." % (avatar.doId, week))
        if week >= 1 and week <= len(WeeklySchedule):
            saleItem = 0
            schedule = WeeklySchedule[week - 1]
            if isinstance(schedule, Sale):
                schedule = schedule.args
                saleItem = 1

            for item in schedule:
                weeklyCatalog += self.__selectItem(avatar, item, monthlyCatalog,
                                                   saleItem = saleItem)

            if nextAvailableCloset not in schedule:
                weeklyCatalog += self.__selectItem(avatar, nextAvailableCloset, monthlyCatalog, saleItem = 0)
            weeklyCatalog += self.__selectItem(avatar, get50ItemTrunk, monthlyCatalog, saleItem = 0)

        # Here is an ugly hack for ensuring that everyone gets at
        # least one pet trick offered in their first catalog when pets
        # goes live for the first time.  If it is not yet the end of
        # the month of September 2004 (the month in which pets goes
        # live), and neither the newly-generated catalog nor the
        # avatar's current catalog or back catalog includes a pet
        # trick already, then we will artificially add a random pet
        # trick.
        if time.time() < 1096617600.0:  # 'Fri Oct  1 01:00:00 2004'
            def hasPetTrick(catalog):
                for item in catalog:
                    if isinstance(item, CatalogPetTrickItem):
                        return 1
                return 0

            if not hasPetTrick(weeklyCatalog) and not \
               hasPetTrick(avatar.weeklyCatalog) and not \
               hasPetTrick(avatar.backCatalog):
                self.notify.debug("Artificially adding pet trick to catalog")
                weeklyCatalog += self.__selectItem(avatar, 5000, monthlyCatalog, saleItem = saleItem)

        self.notify.debug("Generated catalog: %s" % (weeklyCatalog))

        return weeklyCatalog

    def generateBackCatalog(self, avatar, week, previousWeek, weeklyCatalog):
        # Generates the list of items that the avatar has seen offered
        # on previous catalogs.
        backCatalog = CatalogItemList.CatalogItemList()
        lastBackCatalog = avatar.backCatalog[:]

        # Add in the items for weeks we may have skipped over, in
        # reverse order.
        thisWeek = min(len(WeeklySchedule), week - 1)
        lastWeek = min(len(WeeklySchedule), previousWeek)
        for week in range(thisWeek, lastWeek, -1):
            self.notify.debug("Adding items from week %s to back catalog" % (week))
            schedule = WeeklySchedule[week - 1]
            if not isinstance(schedule, Sale): # Don't bother with a sale week.
                for item in schedule:
                    for item in self.__selectItem(avatar, item, weeklyCatalog + backCatalog):
                        item.putInBackCatalog(backCatalog, lastBackCatalog)

        # Add the items in our current catalog.
        if previousWeek < week:
            self.notify.debug("Adding current items from week %s to back catalog" % (previousWeek))
            for item in avatar.weeklyCatalog:
                item.putInBackCatalog(backCatalog, lastBackCatalog)

        # Also add in all of the items already on the back catalog.
        backCatalog += lastBackCatalog

        # Remove any repeated items we just generated this week from
        # the newly-generated back catalog.  It's confusing if an item
        # shows up both in the new catalog and also in the back
        # catalog.
        for item in weeklyCatalog:
            while item in backCatalog:
                backCatalog.remove(item)

        return backCatalog

    def __getReleasedItemLists(self, dayNumber, weekStart):
        itemLists = self.__releasedItemLists.get(dayNumber)
        if itemLists != None:
            return itemLists
        else:
            self.__releasedItemLists.clear()

        testDaysAhead = ConfigVariableInt('test-server-holiday-days-ahead', 0).getValue()

        # Hasn't been generated yet today; do so now.
        nowtuple = time.localtime(weekStart * 60 + testDaysAhead * 24 * 60 * 60)
        year = nowtuple[0]
        month = nowtuple[1]
        day = nowtuple[2]

        itemLists = []

        for monthlyItems in MonthlySchedule:
            startMM = monthlyItems[0]
            startDD = monthlyItems[1]
            endMM = monthlyItems[2]
            endDD = monthlyItems[3]

            if len(monthlyItems) == 7:
                startYYYY = monthlyItems[4]
                endYYYY = monthlyItems[5]
                list = monthlyItems[6]
            else:
                startYYYY = 1969
                endYYYY = year
                list = monthlyItems[4]
            pastStart = year > startYYYY or (year == startYYYY and (month > startMM or (month == startMM and day >= startDD)))

            if pastStart:
                itemLists.append(list)

        self.__releasedItemLists[dayNumber] = itemLists
        return itemLists

    def __getMonthlyItemLists(self, dayNumber, weekStart):
        # Returns a list of lists of seasonal items that should be
        # selected from for monthlyCatalogs generated on the indicated
        # day.  Since the answer is always the same for a particular
        # day, we save some time by computing this only once for each
        # different day.

        itemLists = self.__itemLists.get(dayNumber)
        if itemLists != None:
            return itemLists

        testDaysAhead = ConfigVariableInt('test-server-holiday-days-ahead', 0).getValue()

        # Hasn't been generated yet today; do so now.
        nowtuple = time.localtime(weekStart * 60 + testDaysAhead * 24 * 60 * 60)
        year = nowtuple[0]
        month = nowtuple[1]
        day = nowtuple[2]

        self.notify.debug("Generating seasonal itemLists for %s/%s." % (month, day))
        itemLists = []

        for monthlyItems in MonthlySchedule:
            startMM = monthlyItems[0]
            startDD = monthlyItems[1]
            endMM = monthlyItems[2]
            endDD = monthlyItems[3]
            if len(monthlyItems) == 7:
                startYYYY = monthlyItems[4]
                endYYYY = monthlyItems[5]
                list = monthlyItems[6]
            else:
                startYYYY = 1969
                endYYYY = year
                list = monthlyItems[4]
            pastStart = (year >= startYYYY) and (month > startMM) or (month == startMM and day >= startDD)
            beforeEnd = (year <= endYYYY) and (month < endMM) or (month == endMM and day <= endDD)

            # We are within the range if we are pastStart and
            # beforeEnd (the normal case), or (pastStart or
            # beforeEnd) (if end < start, and we're
            # wrapping around at the end of the year).

            if endMM < startMM:
                if (pastStart or beforeEnd):
                    itemLists.append(list)
            else:
                if (pastStart and beforeEnd):
                    itemLists.append(list)

        self.__itemLists[dayNumber] = itemLists
        return itemLists


    def __selectItem(self, avatar, item, duplicateItems, saleItem = 0):
        # Evaluates the item code into a list of CatalogItem objects that
        # are suitable for purchase by the avatar.

        chooseCount = 1

        # If the item is wrapped in a sale wrapper, it's a sale item.
        if isinstance(item, Sale):
            assert(len(item.args) == 1)
            item = item.args[0]
            saleItem = 1

        # If the item is a function, call it.  It should then return
        # an actual item, a list of items, or a (chooseCount, list).
        if callable(item):
            item = item(avatar, duplicateItems)

        if isinstance(item, tuple):
            # Unpack a 2-tuple into a (chooseCount, list).
            chooseCount, item = item

        if isinstance(item, int):
            # If the item is a MetaItem, it's really a list.
            item = MetaItems[item]

        selection = []

        if isinstance(item, CatalogItem.CatalogItem):
            if not item.notOfferedTo(avatar):
                item.saleItem = saleItem
                selection.append(item)

        elif item != None:
            # Choose n of the given list.  That means we should make a
            # copy of the list first.
            list = item[:]
            for i in range(chooseCount):
                if len(list) == 0:
                    return selection
                item = self.__chooseFromList(avatar, list, duplicateItems)
                if item != None:
                    item.saleItem = saleItem
                    selection.append(item)

        return selection

    def __chooseFromList(self, avatar, list, duplicateItems):
        index = random.randrange(len(list))
        item = list[index]
        del list[index]

        # Is this an acceptable item?
        # Make sure you can offer this item to the given avatar,
        # that the avatar hasn't reached his/her purchase limit,
        # and that the item isn't already in the duplicate or
        # backorder list
        while item.notOfferedTo(avatar) or \
              item.reachedPurchaseLimit(avatar) or \
              item in duplicateItems or \
              item in avatar.backCatalog or \
              item in avatar.weeklyCatalog:
            # The current item is unacceptable, see if there is another one
            if len(list) == 0:
                return None
            index = random.randrange(len(list))
            item = list[index]
            del list[index]

        return item

    def outputSchedule(self, filename):
        out = open(Filename(filename).toOsSpecific(), "wb")

        sched = self.generateScheduleDictionary()

        # Now put the items into sorted order, which will collect
        # similar items together for the user's convenience.
        items = list(sched.keys())
        items.sort()

        for item in items:
            weeklist, maybeWeeklist = sched[item]

            color = self.__formatColor(item.getColor())

            # Figure out which series(es) in which the item is
            # offered.
            seriesDict = {}
            self.__determineSeries(seriesDict, weeklist)
            self.__determineSeries(seriesDict, maybeWeeklist)
            seriesList = list(seriesDict.keys())
            seriesList.sort()
            series = str(seriesList)[1:-1]

            week = self.__formatWeeklist(weeklist)
            maybeWeek = self.__formatWeeklist(maybeWeeklist)

            line = '"%s"\t"%s"\t"%s"\t%s\t"%s"\t"%s"\t"%s"\t"%s"\t"%s"' % (
                item.output(store = 0),
                item.getTypeName(),
                item.getDisplayName(),
                item.getBasePrice(),
                item.getFilename(),
                color,
                series,
                week,
                maybeWeek,
                )
            out.write(line + '\n')

        out.close()

    def __formatColor(self, color):
        if color == None:
            return ""
        else:
            return "(%0.2f, %0.2f, %0.2f)" % (color[0], color[1], color[2])

    def __determineSeries(self, seriesDict, weeklist):
        for week in weeklist:
            if isinstance(week, int):
                # If the week is an integer, it's the week number (as
                # opposed to a string, which represents a season).
                series = ((week - 1) / ToontownGlobals.CatalogNumWeeksPerSeries) + 1
                seriesDict[series] = None

    def __formatWeeklist(self, weeklist):
        # Returns a string representing a friendly way to represent
        # the list of weeks.

        str = ''
        for week in weeklist:
            str += ', %s' % (week)
        return str[2:]


    def generateScheduleDictionary(self):
        # Build up a dictionary of item to:
        #  [weeklist, maybeWeeklist]

        # where each weeklist is a list of week numbers and/or season
        # strings.  A season string is of the form "10/01 - 10/31".  The
        # first list is the list of weeks/seasons in which the item is
        # definitely offered to everyone; the second list is the list
        # of weeks/seasons in which the item is just one of a larger
        # pool of items that is offered to everyone (so each player
        # may or may not be offered any one particular item).

        sched = {}

        for index in range(len(WeeklySchedule)):
            week = index + 1

            schedule = WeeklySchedule[index]
            if isinstance(schedule, Sale):
                schedule = schedule.args

            self.__recordSchedule(sched, week, schedule)

        for monthlyItems in MonthlySchedule:
            startMM = monthlyItems[0]
            startDD = monthlyItems[1]
            endMM = monthlyItems[2]
            endDD = monthlyItems[3]
            if len(monthlyItems) == 7:
                list = monthlyItems[6]
            else:
                list = monthlyItems[4]
            string = "%02d/%02d - %02d/%02d" % (startMM, startDD, endMM, endDD)
            self.__recordSchedule(sched, string, list)

        return sched

    def __recordSchedule(self, sched, weekCode, schedule):
        if isinstance(schedule, Sale):
            schedule = schedule.args
        for item in schedule:

            # If the item is a function, we have to handle it as a
            # special case.
            if callable(item):
                if item == nextAvailablePole:
                    item = getAllPoles()

                #elif item == nextAvailableBank:
                #    item = getAllBanks()

                elif item == nextAvailableCloset:
                    item = getAllClosets()

                elif item == get50ItemCloset:
                    item = getMaxClosets()

                elif item == get50ItemTrunk:
                    item = getMaxTrunks()

                else:
                    self.notify.warning("Don't know how to interpret function " % (repr(name)))
                    item = None

            elif isinstance(item, tuple):
                # A tuple is (chooseCount, list).  We don't care about
                # the chooseCount here.
                item = item[1]

            if isinstance(item, int):
                # If the item is a MetaItem, it's really a list.
                item = MetaItems[item]

            if isinstance(item, CatalogItem.CatalogItem):
                # Just one item, definitely offered.
                self.__recordScheduleItem(sched, weekCode, None, item)

            elif item != None:
                # Multiple items, each of which may be offered.
                #if item == MetaItems[3020] or item == MetaItems[3010]:
                #    print("%s: %s" % (weekCode, item))
                for i in item:
                    self.__recordScheduleItem(sched, None, weekCode, i)

    def __recordScheduleItem(self, sched, weekCode, maybeWeekCode, item):
        if item not in sched:
            sched[item] = [[], []]

        #if item == CatalogWallpaperItem(2900) or item == CatalogWallpaperItem(2210):
        #    print("%s,%s: %s" % (item, maybeWeekCode, sched[item]))
        if weekCode != None:
            sched[item][0].append(weekCode)
        if maybeWeekCode != None:
            sched[item][1].append(maybeWeekCode)
