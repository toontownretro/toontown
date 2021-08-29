"""
TTSCLawbotNerfMenu.py: contains the TTSCLawbotNerfMenu class
"""

from direct.showbase import PythonUtil
from otp.speedchat.SCMenu import SCMenu
from otp.speedchat.SCMenuHolder import SCMenuHolder
from otp.speedchat.SCStaticTextTerminal import SCStaticTextTerminal
from otp.otpbase import OTPLocalizer

#this is the structure of the racing menu
LawbotNerfMenu = [
    (OTPLocalizer.LawbotNerfMenuSections[0],
        [30460, 30461, 30462, 30463, 30464, 30465, 30466]),
    (OTPLocalizer.LawbotNerfMenuSections[1],
        [30467, 30468, 30469, 30470, 30471, 30472, 30473, 30474]),            # GROUPING
    (OTPLocalizer.LawbotNerfMenuSections[2],
        [30475, 30476, 30477, 30478, 30479, 30480, 30481, 30482, 30483, 30484, 30485]),            # Lawbot COURTHOUSE/CJ
    ]

class TTSCLawbotNerfMenu(SCMenu):
    """
    Speedchat phrases for Lawbot Nerf
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
        for section in LawbotNerfMenu:
            if section[0] == -1:
                #This is not a submenu but a terminal!
                for phrase in section[1]:
                    if phrase not in OTPLocalizer.SpeedChatStaticText:
                        print(('warning: tried to link Lawbot Nerf phrase %s which does not seem to exist' % phrase))
                        break
                    self.append(SCStaticTextTerminal(phrase))
            else: #this should be a submenu
                menu = SCMenu()
                for phrase in section[1]:
                    if phrase not in OTPLocalizer.SpeedChatStaticText:
                        print(('warning: tried to link Lawbot Nerf phrase %s which does not seem to exist' % phrase))
                        break
                    menu.append(SCStaticTextTerminal(phrase))

                menuName = str(section[0])
                self.append(SCMenuHolder(menuName, menu))
