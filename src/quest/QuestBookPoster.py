from .QuestPoster import *
from direct.directnotify import DirectNotifyGlobal

IMAGE_SCALE_LARGE = 0.15
IMAGE_SCALE_SMALL = 0.1
POSTER_WIDTH = 0.7
TEXT_SCALE = TTLocalizer.QPtextScale * 0.7
TEXT_WORDWRAP = TTLocalizer.QPtextWordwrap * 0.8

class QuestBookPoster(QuestPoster):
    notify = DirectNotifyGlobal.directNotify.newCategory("QuestPoster")
    
    colors = {
        'white' : (1, 1, 1, 1),
        'blue' : (0.45, 0.45, 0.8, 1),
        'lightBlue' : (0.42, 0.671, 1.0, 1.0),
        'green' : (0.45, 0.8, 0.45, 1),
        'lightGreen' : (0.784, 1, 0.863, 1),
        'red' : (0.8, 0.45, 0.45, 1),
        'rewardRed' : (0.8, 0.3, 0.3, 1),
        'brightRed' : (1.0, 0.16, 0.16, 1.0),
        'brown' : (0.52, 0.42, 0.22, 1),
        }
    normalTextColor = (0.3, 0.25, 0.2, 1)
    
    confirmDeleteButtonEvent = "confirmDeleteButtonEvent"

    def __init__(self, parent = aspect2d, **kw):
        # NOTE: Quest card has about +/- 0.35 units of usable space (0.7 units total)
        # Need to calc width of quest info string width = font.calcWidth(string)
        # text scale is equal to 0.7/width
        # wordwrap should be set to width + pad (0.05)
        # For text at scale 0.045, max width = 15.55, set wordwrap to 15.5
        # Load gui images
        bookModel = loader.loadModel("phase_3.5/models/gui/stickerbook_gui")
        questCard = bookModel.find("**/questCard")
        # Define options
        optiondefs = (
            ('relief',        None,             None),
            ('reverse',       0,                None),
            ('mapIndex',      0,                None),
            ('image',         questCard,        None),
            ('image_scale',   (0.8, 1.0, 0.58), None),
            # So we get enter and exit events
            ('state',          DGG.NORMAL,           None),
            )
        # Merge keyword options with default options
        self.defineoptions(kw, optiondefs)
        # Initialize superclass
        QuestPoster.__init__(self, relief=None)
        # Initialize instance
        self.initialiseoptions(QuestBookPoster)
        # Initialize
        self._deleteCallback = None

        # Single frame to hold everything on the quest poster
        self.questFrame = DirectFrame(parent=self, relief=None)

        gui = loader.loadModel("phase_4/models/parties/schtickerbookHostingGUI")
        
        icon = gui.find("**/startPartyButton_inactive")
        iconNP = aspect2d.attachNewNode("iconNP")
        icon.reparentTo(iconNP)
        icon.setX((-12.0792 + 0.2) / 30.48)
        icon.setZ((-9.7404 + 1) / 30.48)
        
        self.mapIndex = DirectLabel(
            parent = self.questFrame,
            relief = None,
            text = "%s" % self["mapIndex"],
            text_fg = (1, 1, 1, 1),
            text_scale = 0.035,
            text_align = TextNode.ACenter,
            image = iconNP,
            image_scale = 0.3,
            image_color = (1, 0, 0, 1),
            pos = (-0.3, 0, 0.15),
            )
        
        self.mapIndex.hide()
        iconNP.removeNode()
        gui.removeNode()
        bookModel.removeNode()
        
        self.reverseBG(self['reverse'])
        
        self.laffMeter = None

    def reverseBG(self, reverse=0):
        # reverse the poster image (for right-hand page in shticker
        # book, for example)
        try:
            self.initImageScale
        except AttributeError:
            self.initImageScale = self['image_scale']
            if reverse:
                self.initImageScale.setX(-abs(self.initImageScale[0]))
                self.questFrame.setX(0.015)
            else:
                self.initImageScale.setX(abs(self.initImageScale[0]))
            self['image_scale'] = self.initImageScale
