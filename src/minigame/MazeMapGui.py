#===============================================================================
# Contact: Ryan Hipple (Schell Games)
# Created: March 2010
#
# Purpose: Class that generates and displays a minimap for a maze.  It also
#          handles masking out and revealing areas as they are discovered.  The
#          minimap has a layer for the maps walls (self.map), a layer for the
#          mask (self.mask), a layer for content under the mask
#          (self.maskedLayer), and a layer for content above the mask
#          (self.visibleLayer).
#===============================================================================

# python imports
import random

# panda imports
from direct.showbase.PythonUtil import Enum
from direct.gui.DirectGui import DirectFrame, DGG
from toontown.toonbase.ToontownModules import Vec2, VBase4F
from toontown.toonbase.ToontownModules import CardMaker, NodePath
from toontown.toonbase.ToontownModules import Texture, PNMImage

#TODO:maze: move this to a config or global location

# Default resolution for the mask.  Should be no lower than 32.
# Larger values decrease performance.
DEFAULT_MASK_RESOLUTION = 32

# Default ratio for the reveal radius.  This is essentially the percentage of
# the map that is revealed with each step.
DEFAULT_RADIUS_RATIO = 0.05 # 0.09

# Resolution for the map image that will be generated based on the map data.
MAP_RESOLUTION = 320

# Defines the function used to clear a portion of the mask
MazeRevealType = Enum((
    "SmoothCircle",
    "HardCircle",
    "Square",
))

MAZE_REVEAL_TYPE = MazeRevealType.SmoothCircle

class MazeMapGui(DirectFrame):

    notify = directNotify.newCategory("MazeMapGui")

    def __init__(self, mazeCollTable, maskResolution = None, radiusRatio = None, bgColor = (0.8, 0.8, 0.8), fgColor = (0.5, 0.5, 0.5, 1.0)):
        """
        Constructor for a MazeMap.  the mazeLayout parameter is a 2d array of
        bools (or ints... maybe more depth will be added with that).
        maskResolution is a value for the resolution of the mask covering the
        map.  It should range from 32 to 256.  radiusRatio is essentially
        the percentage of the map that is revealed with each step.
        """
        DirectFrame.__init__(self,
            relief = None,
            state = DGG.NORMAL,
            sortOrder = DGG.BACKGROUND_SORT_INDEX,
        )

        self.hide()
        self._bgColor = bgColor
        self._fgColor = fgColor
        self._mazeCollTable = mazeCollTable
        self._mazeWidth = len(self._mazeCollTable[0])
        self._mazeHeight = len(self._mazeCollTable)

        # store / set parameters
        #self._mazeLayout = mazeLayout
        self._maskResolution = maskResolution or DEFAULT_MASK_RESOLUTION
        if radiusRatio is None:
            self._radius = self._maskResolution * DEFAULT_RADIUS_RATIO
        else:
            self._radius = self._maskResolution * radiusRatio

        # store false for all maze cells to represent that none of them have
        # been revealed yet.  This can prevent the expensive call to altering
        # the mask if a cell is already revealed
        self._revealedCells = []
        for y in range(self._mazeHeight):
            self._revealedCells.append([])
            for u in range(self._mazeWidth):
                self._revealedCells[y].append(False)

        # create reveal function mappings
        self._revealFunctions = {
            MazeRevealType.SmoothCircle : self._revealSmoothCircle,
            MazeRevealType.HardCircle : self._revealHardCircle,
            MazeRevealType.Square : self._revealSquare,
        }
        self._revealFunction = MAZE_REVEAL_TYPE

        # create the map and the mask
        self.map = self._createMapTextureCard()
        self.map.reparentTo(self)
        self.maskedLayer = self.attachNewNode("maskedLayer")
        self.mask = self._createMaskTextureCard()
        self.mask.reparentTo(self)
        self.visibleLayer = self.attachNewNode("visibleLayer")
        self._laffMeterModel = loader.loadModel("phase_3/models/gui/laff_o_meter")
        self._toon2marker = {}

        #TODO:maze: handle locks and doors
        self._players = []
        self._locks = []
        self._doors = []

    #--- Initialization, Destruction, and Resetting ---#########################

    def _createMapTextureCard(self):
        """
        This will return a NodePath with a card textured with the minimap.  The
        minimap texture is dynamically created from the map data.
        """
        # create and fill empty map image
        mapImage = PNMImage(MAP_RESOLUTION, MAP_RESOLUTION)
        mapImage.fill(*self._bgColor)
        fgColor = VBase4F(*self._fgColor)

        # iterate through the map data and place a block in the map image where appropriate
        for x in range(self._mazeHeight):
            for y in range(self._mazeWidth):
                if self._mazeCollTable[y][x] == 1:
                    ax = float(x)/self._mazeWidth * MAP_RESOLUTION
                    invertedY = self._mazeHeight - 1 - y
                    ay = float(invertedY)/self._mazeHeight * MAP_RESOLUTION

                    #TODO:maze use different blocks for different wall types or items
                    #mapImage.copySubImage(random.choice(blockFiles), int(ax), int(ay), 20, 20, 32, 32)

                    #TODO:maze find the ideal block texture size for the map so we dont
                    #          have to do this strange offset
                    #mapImage.copySubImage(blockFiles[0], int(ax), int(ay), 0, 0, 32, 32)
                    self._drawSquare(mapImage, int(ax), int(ay), 10, fgColor)

        # create a texture from the map image
        mapTexture = Texture("mapTexture")
        mapTexture.setupTexture(Texture.TT2dTexture, self._maskResolution, self._maskResolution, 1, Texture.TUnsignedByte, Texture.FRgba)
        mapTexture.setMinfilter(Texture.FTLinear)
        mapTexture.load(mapImage)
        mapTexture.setWrapU(Texture.WMClamp)
        mapTexture.setWrapV(Texture.WMClamp)

        mapImage.clear()
        del mapImage

        # put the texture on a card and return it
        cm = CardMaker("map_cardMaker")
        cm.setFrame(-1.0,1.0,-1.0,1.0)
        map = self.attachNewNode(cm.generate())
        map.setTexture(mapTexture, 1)
        return map

    def _createMaskTextureCard(self):
        """
        This will return a NodePath with a card textured with the map mask.  It
        also creates several other members that re needed to change the mask.
        """
        # create and fill empty mask image
        self._maskImage = PNMImage(self._maskResolution, self._maskResolution, 4)
        for x in range(self._maskResolution):
            for y in range(self._maskResolution):
                #maskImage.setXel(x,y,mapImage.getRed(x/13,y/10),mapImage.getGreen(x/13,y/10),mapImage.getBlue(x/13,y/10))
                self._maskImage.setXelA(x,y,0,0,0,1)

        # create the texture for the mask
        self.maskTexture = Texture("maskTexture")
        self.maskTexture.setupTexture(Texture.TT2dTexture, self._maskResolution, self._maskResolution, 1, Texture.TUnsignedByte, Texture.FRgba)
        self.maskTexture.setMinfilter(Texture.FTLinear)
        self.maskTexture.setWrapU(Texture.WMClamp)
        self.maskTexture.setWrapV(Texture.WMClamp)

        self.maskTexture.load(self._maskImage)
        base.graphicsEngine.renderFrame()

        # put the mask texture on a card and return it
        cm = CardMaker("mask_cardMaker")
        cm.setFrame(-1.0,1.1,-1.1,1.1)
        mask = self.attachNewNode(cm.generate())
        mask.setTexture(self.maskTexture, 1)
        mask.setTransparency(1)
        return mask

    def _drawSquare(self, image, ulx, uly, size, color):
        """
        Draws a square on the supplied PNMImage starting at (ulx, uly) with a
        size of "size" and a color of "color".
        """
        x = int(ulx)
        while x <= ulx + size:
            y = int(uly)
            while y <= uly + size:
                if x > 0 and y > 0 and x < image.getXSize() and y < image.getYSize():
                    image.setXelA( x, y, color )
                y += 1
            x += 1

    def destroy(self):
        del self._mazeCollTable
        del self._maskResolution
        del self._radius
        del self._revealedCells

        del self._revealFunctions
        del self._revealFunction

        # remove and delete all nodes
        self.map.removeNode()
        del self.map
        self.mask.removeNode()
        del self.mask
        self.maskedLayer.removeNode()
        del self.maskedLayer
        self.visibleLayer.removeNode()
        del self.visibleLayer

        # remove and delete all lists of nodes
        self._maskImage.clear()
        del self._maskImage

        self.maskTexture.clear()
        del self.maskTexture

        self._laffMeterModel.removeNode()
        del self._laffMeterModel

        DirectFrame.destroy(self)

    #--- Reveal shape functions ---#############################################

    def _revealSmoothCircle(self, x, y, center):
        length = (Vec2(x,y)-center).length()
        goalAlpha = max(0.0, (length/float(self._radius)) - 0.5)
        self._maskImage.setXelA(
            x,
            y,
            VBase4F( 0.0, 0.0, 0.0, min(self._maskImage.getAlpha(x,y), goalAlpha*2.0))
        )

    def _revealHardCircle(self, x, y, center):
        length = (Vec2(x,y)-center).length()
        if length <= self._radius:
            self._maskImage.setXelA(x,y,VBase4F(0,0,0,0))

    def _revealSquare(self, x, y, center):
        self._maskImage.setXelA(x,y,VBase4F(0,0,0,0))

    #--- Private Functions ---##################################################

    def _drawHole(self, x, y):
        center = Vec2(x, y)
        ul = center - Vec2(self._radius, self._radius)
        lr = center + Vec2(self._radius, self._radius)
        x = int(ul[0])
        while x <= lr[0]:
            y = int(ul[1])
            while y <= lr[1]:
                if x > 0 and y > 0 and x < self._maskResolution and y < self._maskResolution:
                    self._revealFunctions[self._revealFunction](x, y, center)
                y += 1
            x += 1

        self.maskTexture.load(self._maskImage)
        self.mask.setTexture(self.maskTexture, 1)

    def _createSimpleMarker(self, size, color = (1, 1, 1)):
        halfSize = size * 0.5
        cm = CardMaker("mazemap_simple_marker")
        cm.setFrame(-halfSize, halfSize, -halfSize, halfSize)
        markerNP = self.maskedLayer.attachNewNode(cm.generate())
        markerNP.setColor(*color)
        return markerNP

    def tile2gui(self, x, y):
        y = self._mazeHeight - y
        cellWidth = self._maskResolution / self._mazeWidth
        cellHeight = self._maskResolution / self._mazeHeight
        ax = float(x)/self._mazeWidth * self._maskResolution
        ax += cellWidth
        ay = float(y)/self._mazeHeight * self._maskResolution
        ay += cellHeight
        return ax, ay

    def gui2pos(self, x, y):
        return (x / self._maskResolution * 2.0 - 0.97, 0, y / self._maskResolution * -2.0 + 1.02)

    def _getToonMarker(self, toon):
        hType = toon.style.getType()
        if hType == "rabbit":
            hType = "bunny"
        return self._laffMeterModel.find("**/" + hType + "head")

    #--- Member Functions ---###################################################

    def addToon(self, toon, tX, tY):
        """
        Adds a player to the minimap.  This will add a colored dot to the map
        that represents the player.  The dot location can then be updated
        using the revealCell call.
        --- This is subject to change pending a new player-lock data system. ---
        """
        assert self.notify.debugCall()
        
        marker = NodePath("toon_marker-%i" % toon.doId)
        marker.reparentTo(self)
        self._getToonMarker(toon).copyTo(marker)
        marker.setColor(toon.style.getHeadColor())
        if toon.isLocal():
            marker.setScale(0.07)
        else:
            marker.setScale(0.05)
        marker.flattenStrong()
        marker.setPos(*self.gui2pos(*self.tile2gui(tX, tY)))
        self._toon2marker[toon] = marker

    def removeToon(self, toon):
        if toon not in self._toon2marker:
            return
        self._toon2marker[toon].removeNode()
        del self._toon2marker[toon]

    def updateToon(self, toon, tX, tY):
        if toon not in self._toon2marker:
            return
        x, y = self.tile2gui(tX, tY)
        self._toon2marker[toon].setPos(*self.gui2pos(x, y))
        if tY < 0 or tY >= len(self._revealedCells):
            self.notify.warning("updateToon earlying out:")
            self.notify.warning("(tX, tY): (%s, %s)" % (tX, tY))
            self.notify.warning("len(_revealedCells): %s" % (len(self._revealedCells),))
            if len(self._revealedCells) > 0:
                self.notify.warning("len(_revealedCells[0]): %s" % (len(self._revealedCells[0]),))
            return
        if tX < 0 or tX >= len(self._revealedCells[tY]):
            self.notify.warning("updateToon earlying out:")
            self.notify.warning("(tX, tY): (%s, %s)" % (tX, tY))
            self.notify.warning("len(_revealedCells): %s" % (len(self._revealedCells),))
            if tY < len(self._revealedCells):
                self.notify.warning("len(_revealedCells[tY]): %s" % (len(self._revealedCells[tY]),))
            elif len(self._revealedCells) > 0:
                self.notify.warning("len(_revealedCells[0]): %s" % (len(self._revealedCells[0]),))
            return
        if not self._revealedCells[tY][tX]:
            self._drawHole(x, y)
            self._revealedCells[tY][tX] = True

    def revealCell(self, x, y):
        """
        Clears out the mask around the given cell and stores that the cell has
        been revealed to prevent attempting to edit the mask for the cell again.
        """

        ax, ay = self.tile2gui(x, y)

        if not self._revealedCells[y][x]:
            self._drawHole(ax, ay)
            self._revealedCells[y][x] = True
            
    def revealAll(self):
        """ Clears out all of the mask. """
        for x in range(self._maskResolution):
            for y in range(self._maskResolution):
                self._maskImage.setXelA(x,y,0,0,0,0)
        self.revealCell(0, 0)

    def reset(self):
        """ Turns all of the mask on, covering the entire map. """
        for x in range(self._maskResolution):
            for y in range(self._maskResolution):
                self._maskImage.setXelA(x,y,0,0,0,1)
