from direct.gui.DirectGui import *
from toontown.toonbase.ToontownModules import *
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer
from toontown.effects import FireworkGlobals
from toontown.effects import Fireworks
from . import FireworksGui

class FireworkItemPanel(DirectFrame):
    def __init__(self, itemName, itemNum, *extraArgs):
        self.gui = extraArgs[0][0]
        self.type = extraArgs[0][1][itemNum]
        self.shootEvent = extraArgs[0][2]
        self._name = FireworkGlobals.Names[self.type]
        DirectFrame.__init__(
            self,
            image = DGG.getDefaultDialogGeom(),
            image_color = (0.75, 0.75, 0.75, 1),
            image_scale = (0.25, 0, 0.25),
            relief=None
            )
        self.initialiseoptions(FireworkItemPanel)
        self.load()

    def load(self):
        # add a picture of the firework.  draw it first so we can
        # draw the quantity on top of it.
        self.picture = DirectButton(
            parent = self,
            image = (
                DGG.getDefaultDialogGeom(),
                DGG.getDefaultDialogGeom(),
                DGG.getDefaultDialogGeom()),
            relief = None,
            command = self.__launchFirework,
            extraArgs = [self.type],
            image_color = (.8,.9,1,1),
            )
        self.picture.setScale(0.2)
        self.picture.setPos(0, 0, 0)
        self.picture.initialiseoptions(self.picture)
        panelWidth = 7
        nameFont = ToontownGlobals.getInterfaceFont()

        # draw the quantity on top
        self.quantityLabel = DirectLabel(
            parent = self.picture,
            relief = None,
            pos = (0,0,0.0),
            scale = 0.45,
            text = self._name,
            text_scale = 0.6,
            text_fg = (0, 0, 0, 1),
            #text_shadow = (0, 0, 0, 1),
            text_pos = (0, -.14, 0),
            text_font = nameFont,
            text_wordwrap = panelWidth,
            )

        #self.__dimSky()

    def unload(self):
        del self.picture
        self.quantityLabel.destroy()
        del self.quantityLabel
        # call parent destructor
        DirectFrame.destroy(self)
        #self.__resetSky()

    def destroy(self):
        # this is only so the DirectGui code cleans us up properly
        self.unload()

    def __launchFirework(self, index):
        messenger.send(self.shootEvent, [index])

    def __dimSky(self):
        self.oldSkyScale = base.cr.playGame.hood.loader.sky.getColorScale()
        base.cr.playGame.hood.loader.sky.setColorScale(.3,.3,.3,1)

    def __resetSky(self):
        base.cr.playGame.hood.loader.sky.setColorScale(self.oldSkyScale)
