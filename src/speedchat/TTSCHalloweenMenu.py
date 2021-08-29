"""
TTSCHalloweenMenu.py: contains the TTSCHalloweenMenu class
"""
from direct.showbase import PythonUtil
from otp.speedchat.SCMenu import SCMenu
from otp.speedchat.SCMenuHolder import SCMenuHolder
from otp.speedchat.SCStaticTextTerminal import SCStaticTextTerminal
from otp.otpbase import OTPLocalizer

#this is the structure of the racing menu
HalloweenMenu = [
(OTPLocalizer.HalloweenMenuSections[0], [30250, 30251, 30252]),
]

class TTSCHalloweenMenu(SCMenu):
    """
    Speedchat phrases for Halloween
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
        for section in HalloweenMenu:
            if section[0] == -1:
                #This is not a submenu but a terminal!
                for phrase in section[1]:
                    if phrase not in OTPLocalizer.SpeedChatStaticText:
                        print(('warning: tried to link Halloween phrase %s which does not seem to exist' % phrase))
                        break
                    self.append(SCStaticTextTerminal(phrase))
            else: #this should be a submenu
                menu = SCMenu()
                for phrase in section[1]:
                    if phrase not in OTPLocalizer.SpeedChatStaticText:
                        print(('warning: tried to link Halloween phrase %s which does not seem to exist' % phrase))
                        break
                    menu.append(SCStaticTextTerminal(phrase))

                menuName = str(section[0])
                self.append(SCMenuHolder(menuName, menu))
