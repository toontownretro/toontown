from toontown.toonbase.ToontownModules import *
from direct.gui.DirectGui import *
from direct.directnotify import DirectNotifyGlobal
from . import TTDialog
from toontown.toonbase import TTLocalizer
from direct.showbase import PythonUtil
from direct.showbase.DirectObject import DirectObject
from otp.login import LeaveToPayDialog
#from otp.otpbase import OTPLauncherGlobals

"""
d.destroy()
from direct.gui import DirectDialog
buttons = loader.loadModel('phase_3/models/gui/dialog_box_buttons_gui')
guiButton = loader.loadModel("phase_3/models/gui/quit_button")
cancelImageList = (buttons.find('**/CloseBtn_UP'),buttons.find('**/CloseBtn_DN'),buttons.find('**/CloseBtn_Rllvr'))
subscribeImageList = (guiButton.find('**/QuitBtn_DN'),guiButton.find("**/QuitBtn_DN"),guiButton.find("**/QuitBtn_RLVR"),)
buttonImage = [subscribeImageList,cancelImageList]
buttonText = ('Subscribe Now!', 'Cancel')
d = DirectDialog.DirectDialog(buttonImageList=buttonImage,buttonTextList=buttonText)
"""

Pages = {

    # "stringToken" : (localized text,
    #                  image filename,
    #                  image format flag [square = 2, portrait = 1, landscape = 0],
    #                  members only flag,
    #                  )

    'otherHoods' : (TTLocalizer.TeaserOtherHoods,
                    'features-hoods',
                    0,
                    1,
                    ),
    'typeAName' : (TTLocalizer.TeaserTypeAName,
                   'features-typeAName',
                   0,
                   1,
                   ),
    'sixToons'   : (TTLocalizer.TeaserSixToons,
                    'features-sixToons',
                    0,
                    1,
                    ),
    'otherGags'  : (TTLocalizer.TeaserOtherGags,
                    'features-gags',
                    0,
                    1,
                    ),
    'clothing'   : (TTLocalizer.TeaserClothing,
                    'features-clothes',
                    0,
                    0,
                    ),
    'furniture'  : (TTLocalizer.TeaserFurniture,
                    'features-furniture',
                    0,
                    1,
                    ),
    'cogHQ'      : (TTLocalizer.TeaserCogHQ,
                    'features-cogHq',
                    0,
                    1,
                    ),
    'secretChat' : (TTLocalizer.TeaserSecretChat,
                    'features-chat',
                    0,
                    1,
                    ),
    'mailers'    : (TTLocalizer.TeaserCardsAndPosters,
                    'features-mailers',
                    0,
                    1,
                    ),
    'holidays'   : (TTLocalizer.TeaserHolidays,
                    'features-holidays',
                    0,
                    0,
                    ),
    'quests'     : (TTLocalizer.TeaserQuests,
                    'features-quests',
                    0,
                    1,
                    ),
    'emotions'   : (TTLocalizer.TeaserEmotions,
                    'features-catalog',
                    0,
                    1,
                    ),
    'minigames'  : (TTLocalizer.TeaserMinigames,
                    'features-minigames',
                    0,
                    0,
                    ),
    'karting'    : (TTLocalizer.TeaserKarting,
                    'features-karting',
                    0,
                    1,
                    ),
    'kartingAccessories'    : (TTLocalizer.TeaserKartingAccessories,
                               'features-kartingAccessories',
                               0,
                               1,
                               ),
    'gardening'    : (TTLocalizer.TeaserGardening,
                      'features-garden', # Fix
                      0,
                      1,
                      ),
    'bigger'    : (TTLocalizer.TeaserBigger,
                   'features-bigger',
                   1,
                   1,
                   ),
    'rental'    : (TTLocalizer.TeaserRental,
                   'features-rental',
                   0,
                   1,
                   ),
    'tricks'    : (TTLocalizer.TeaserTricks,
                   'features-tricks',
                   0,
                   0,
                   ),
    'species'    : (TTLocalizer.TeaserSpecies,
                    'features-species',
                    1,
                    1,
                    ),
    'golf'       : (TTLocalizer.TeaserGolf,
                    'features-golf',
                    0,
                    1,
                    ),
    'fishing'       : (TTLocalizer.TeaserFishing,
                       'features-fishing',
                       0,
                       1,
                       ),
    'parties'       : (TTLocalizer.TeaserParties,
                       'features-parties',
                       0,
                       1,
                       ),
    }

PageOrder = [
    'sixToons',
    'typeAName',
    'species',
    'otherHoods',
    'otherGags',
    'clothing',
    'furniture',
    'bigger',
    'rental',
    'parties',
    'tricks',
    'cogHQ',
    'secretChat',
    'mailers',
    'holidays',
    'quests',
    'emotions',
    'minigames',
    'karting',
    'kartingAccessories',
    'gardening',
    'golf',
    'fishing',
    ]

class TeaserPanel(DirectObject):
    """Tease trialers with descriptions of what they'll get if they subscribe
    """
    notify = DirectNotifyGlobal.directNotify.newCategory("TeaserPanel")
    
    def __init__(self, pageName, doneFunc=None):
    
        self.doneFunc = doneFunc

        # if we don't have a feature browser, make one
        if not hasattr(self, "browser"):
            self.browser = FeatureBrowser()
            self.browser.load()
            self.browser.setPos(0, 0, -0.65)
            self.browser.reparentTo(hidden)
        
        self.leaveDialog = None
        self.showPage(pageName)

    
    def _TeaserPanel__handleDone(self, choice):
        # clean up the teaser panel and take appropriate action
        self.cleanup()
        self.unload()

        if choice == 1:
            self._TeaserPanel__handlePay()
        else:
            self._TeaserPanel__handleContinue()

    def _TeaserPanel__handleContinue(self):
        # call the user done function
        if self.doneFunc:
            print("calling doneFunc")
            self.doneFunc()
        
    def _TeaserPanel__handlePay(self):
        if base.cr.isWebPlayToken() or __dev__:
            if self.leaveDialog == None:
                self.notify.warning("### making LTP")
                self.leaveDialog = LeaveToPayDialog.LeaveToPayDialog(0, doneFunc=self.doneFunc)
            self.notify.warning("### showing LTP")
            self.leaveDialog.show()
        else:
            self.notify.error("You should not have a TeaserPanel without a PlayToken")

    
    def destroy(self):
        self.cleanup()

    # dialog callback code passes a value    
    def cleanup(self):
        if hasattr(self, 'browser'):
            self.browser.reparentTo(hidden)
            self.browser.ignoreAll()
        if hasattr(self, 'dialog'):
            base.transitions.noTransitions()
            self.dialog.cleanup()
            del self.dialog
        if self.leaveDialog:
            self.leaveDialog.destroy()
            self.leaveDialog = None
        self.ignoreAll()

    def unload(self):
        # there is a chance the gui code might have already deleted this
        if hasattr(self, 'browser'):
            self.browser.destroy()
            del self.browser
    
    def showPage(self, pageName):
        if pageName not in PageOrder:
            self.notify.error("unknown page '%s'" % pageName)

        # map page name to browser index
        self.browser.scrollTo(PageOrder.index(pageName))

        # remove current global dialog if present
        self.cleanup()

        self.dialog = TTDialog.TTDialog(
            parent = aspect2dp,
            text = TTLocalizer.TeaserTop,
            text_wordwrap = 20,
            text_scale = TTLocalizer.TPtop,
            topPad = -0.05,
            midPad = 1.25,
            sidePad = 0.0,
            command = self._TeaserPanel__handleDone,
            fadeScreen = 0.5,
            style = TTDialog.TwoChoice,
            buttonTextList = [TTLocalizer.TeaserSubscribe,
                              TTLocalizer.TeaserContinue,
                              ],
            button_text_scale = TTLocalizer.TPbutton,
            buttonPadSF = 5.5,
            sortOrder = DGG.NO_FADE_SORT_INDEX,
            )

        self.dialog.setPos(0, 0, 0.75)
        self.browser.reparentTo(self.dialog)
        base.transitions.fadeScreen(.5)

        self.accept('arrow_right', self.showNextPage)
        self.accept('arrow_left', self.showPrevPage)
    
    def showNextPage(self):
        self.notify.debug("show next")
        self.browser.scrollBy(1)
    
    def showPrevPage(self):
        self.notify.debug("show prev")
        self.browser.scrollBy(-1)

    def showPay(self):
        # show the pay button
        self.dialog.buttonList[0].show()

    def hidePay(self):
        # hide the pay button
        self.dialog.buttonList[0].hide()
    
    def removed(self):
        # return the removed status of our nodepath object
        if hasattr(self, 'dialog') and self.dialog:
            return self.dialog.removed()
        elif hasattr(self, 'leaveDialog') and self.leaveDialog:
            return self.leaveDialog.removed()
        else:
            return 1


class FeatureBrowser(DirectScrolledList):

    # special methods
    def __init__(self, parent = aspect2dp, **kw):
        """__init__(self)
        FeatureBrowser constructor: create a scrolling list of features
        """

        self._parent = parent

        # make the scrolling pick list for the member features
        gui = loader.loadModelOnce('phase_3/models/gui/scroll_arrows_gui')
        
        optiondefs = (
            ('parent', self._parent,    None),
            ('relief', None,    None),
            # inc and dec are DirectButtons
            ('incButton_image',(
                gui.find("**/FndsLst_ScrollUp"),
                gui.find("**/FndsLst_ScrollDN"),
                gui.find("**/FndsLst_ScrollUp_Rllvr"),
                gui.find("**/FndsLst_ScrollUp"),
                ),    None),
            ('incButton_relief',                       None, None),
            ('incButton_scale',              (2.0, 1.5, 2.5), None),
            ('incButton_pos',                  (0.65, 0, 0.03), None),
            ('incButton_hpr',                      (0, 0, 90), None),
            # Make the disabled button fade out
            ('incButton_image3_color',   Vec4(0.8,0.8,0.8,0.5), None),
            ('decButton_image', (
                gui.find("**/FndsLst_ScrollUp"),
                gui.find("**/FndsLst_ScrollDN"),
                gui.find("**/FndsLst_ScrollUp_Rllvr"),
                gui.find("**/FndsLst_ScrollUp"),
                ),    None),
            ('decButton_relief',                          None, None),
            ('decButton_scale',                  (2.0, 1.5, 2.5), None),
            ('decButton_pos',                      (-0.65, 0, 0.03), None),
            ('decButton_hpr',                      (0, 0, -90), None),
            # Make the disabled button fade out
            ('decButton_image3_color',   Vec4(0.8,0.8,0.8,0.5), None),
            ('numItemsVisible',                              1, None),
            ('items',        [], None),
            ('scrollSpeed',                                  4, None),
            )
        
        gui.removeNode()
        # Merge keyword options with default options
        self.defineoptions(kw, optiondefs)
        # Initialize superclasses
        DirectScrolledList.__init__(self, parent)
        self.initialiseoptions(FeatureBrowser)
    
    def destroy(self):
        DirectScrolledList.destroy(self)
    
    def load(self):
        # load up the images
        guiModel = loader.loadModelOnce("phase_3/models/gui/feature_gui")
        logoModel = loader.loadModelOnce("phase_3/models/gui/members_only_gui")
        
        for page in PageOrder:
            textInfo, imageName, aspect, members = Pages.get(page)
            # UK and AP have no collectable cards
            if base.cr.productName in ['DisneyOnline-UK', 'DisneyOnline-AP']:
                if imageName == "features-mailers":
                    imageName = "features-mailers-UK"
            imageModel = guiModel.find("**/" + imageName)
            # landscape
            if aspect == 0:
                scale = (1.1, 0, 0.85)
                logoPos = (0.44, 0, -0.31)
            # portrait
            elif aspect == 1:
                scale = (0.7, 0, 0.9)
                logoPos = (0.275, 0, -0.335)
            # square
            else:
                scale = (0.8, 0, 0.8)
                logoPos = (0.45, 0, -0.28)
            
            panel = DirectFrame(
                parent = self,
                relief = None,
                image = imageModel,
                image_scale = scale,
                image_pos = (0, 0, 0.05),
                text = textInfo,
                text_scale = TTLocalizer.TPpanel,
                text_pos = (0, -0.55),
                )
            self.addItem(panel)
            
            if members:
                logo = DirectFrame(
                    parent = panel,
                    relief = None,
                    image = logoModel.find('**/MembersOnly'),
                    image_scale = (0.2875, 0, 0.25),
                    image_pos = logoPos,
                    )
                continue
        
        guiModel.removeNode()
        logoModel.removeNode()

