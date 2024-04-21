from direct.directnotify import DirectNotifyGlobal
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer
from direct.gui.DirectGui import *
from toontown.toonbase.ToontownModules import *
from toontown.toontowngui import TTDialog

class ElevatorNotifier:
    """CatalogNotifyDialog:

    Pops up to tell you when you have a new catalog, or a new delivery
    from the catalog.
    """

    notify = DirectNotifyGlobal.directNotify.newCategory("CatalogNotifyDialog")

    def __init__(self):
        self.frame = None
        pass



    def handleButton(self):
        self.__handleButton(1)

    def createFrame(self, message, framePos = None, withStopping = True, ttDialog = False):
        if not framePos:
            framePos = (0.0, 0, 0.78)
        if not ttDialog:
            self.frame = DirectFrame(
                relief = None,
                image = DGG.getDefaultDialogGeom(),
                image_color = ToontownGlobals.GlobalDialogColor,
                image_scale = (1.0, 1.0, 0.40),
                text = message,
                text_wordwrap = 16,
                text_scale = 0.06,
                text_pos = (-0.0, 0.1),
                pos = framePos,
                )
        else:
            self.frame = TTDialog.TTDialog(
                relief = None,
                image = DGG.getDefaultDialogGeom(),
                image_color = ToontownGlobals.GlobalDialogColor,
                image_scale = (1.0, 1.0, 0.40),
                text = message,
                text_wordwrap = 16,
                text_scale = 0.06,
                text_pos = (-0.0, 0.1),
                pos = framePos,
                )

        buttons = loader.loadModel(
            'phase_3/models/gui/dialog_box_buttons_gui')
        self.cancelImageList = (buttons.find('**/CloseBtn_UP'),
                                buttons.find('**/CloseBtn_DN'),
                                buttons.find('**/CloseBtn_Rllvr'))
        self.okImageList = (buttons.find('**/ChtBx_OKBtn_UP'),
                            buttons.find('**/ChtBx_OKBtn_DN'),
                            buttons.find('**/ChtBx_OKBtn_Rllvr'))


        self.doneButton = DirectButton(
            parent = self.frame,
            relief = None,
            image = self.cancelImageList,
            command = self.handleButton,
            pos = (0, 0, -0.14),
            )
        if not withStopping:
            self.doneButton['command'] = self.__handleButtonWithoutStopping
        self.doneButton.show()
        self.frame.show()


    def cleanup(self):
        """cleanup(self):
        Cancels any pending request and removes the panel from the
        screen, unanswered.
        """
        if self.frame:
            self.frame.destroy()
        self.frame = None
        self.nextButton = None
        self.doneButton = None
        self.okImageList = None
        self.cancelImageList = None

    def setOkButton(self):
        self.doneButton['image'] = self.okImageList

    def setCancelButton(self):
        self.doneButton['image'] = self.cancelImageList

    def __handleButton(self, value):
        self.cleanup()
        place = base.cr.playGame.getPlace()
        if place:
            place.setState('walk')

    def showMe(self, message, pos = None, ttDialog = False):
        if self.frame == None:
            place = base.cr.playGame.getPlace()
            if place:
                self.createFrame(message, pos, True, ttDialog)
                place.setState('stopped')

    def showMeWithoutStopping(self, message, pos = None, ttDialog = False):
        """
        Some messages need not have the toon in a stopped state.
        Show the elevator message by keeping them in their previous state itself.
        """
        if self.frame == None:
            self.createFrame(message, pos, False, ttDialog)

    def __handleButtonWithoutStopping(self):
        self.cleanup()

    def isNotifierOpen(self):
        if self.frame:
            return True
        else:
            return False
