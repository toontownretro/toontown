"""
TTSCIdesOfMarchMenu.py: contains the TTSCIdesOfMarchmenu class
"""

from direct.showbase import PythonUtil
from otp.speedchat.SCMenu import SCMenu
from otp.speedchat.SCMenuHolder import SCMenuHolder
from otp.speedchat.SCStaticTextTerminal import SCStaticTextTerminal
from otp.otpbase import OTPLocalizer

IdesOfMarchMenu = [
(OTPLocalizer.IdesOfMarchMenuSections[0], [30450, 30451, 30452]),
]

class TTSCIdesOfMarchMenu(SCMenu):
    """
    Speedchat phrases for Ides Of March
    """
    def __init__(self):
        SCMenu.__init__(self)
        
        self.__messagesChanged()

    def destroy(self):
        SCMenu.destroy(self)

    def clearMenu(self):
        SCMenu.clearMenu(self)

    def __messagesChanged(self):
        # clear out everything from our menu
        self.clearMenu()
        
        # if local toon has not been created, don't panic
        try:
            lt = base.localAvatar
        except:
            return
        for section in IdesOfMarchMenu:
            if section[0] == -1:
                #This is not a submenu but a terminal!
                for phrase in section[1]:
                    if phrase not in OTPLocalizer.SpeedChatStaticText:
                        print(('warning: tried to link IdesOfMarch phrase %s which does not seem to exist' % phrase))
                        break
                    self.append(SCStaticTextTerminal(phrase))
            else: #this should be a submenu
                menu = SCMenu()
                for phrase in section[1]:
                    if phrase not in OTPLocalizer.SpeedChatStaticText:
                        print(('warning: tried to link IdesOfMarch phrase %s which does not seem to exist' % phrase))
                        break
                    menu.append(SCStaticTextTerminal(phrase))

                menuName = str(section[0])
                self.append(SCMenuHolder(menuName, menu))
