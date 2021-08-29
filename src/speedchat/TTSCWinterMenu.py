"""
TTSCWinterMenu.py: contains the TTSCWinterMenu class
"""

from direct.showbase import PythonUtil
from otp.speedchat.SCMenu import SCMenu
from otp.speedchat.SCMenuHolder import SCMenuHolder
from otp.speedchat.SCStaticTextTerminal import SCStaticTextTerminal
from toontown.speedchat.TTSCIndexedTerminal import TTSCIndexedTerminal
from otp.otpbase import OTPLocalizer

#this is the structure of the racing menu
WinterMenu = [
    (OTPLocalizer.WinterMenuSections[0],
        {30200: 30220, 30201: 30221, 30202: 30222, 30203: 30223, 30204: 30224, 30205: 30225}),            # CAROLING
    (OTPLocalizer.WinterMenuSections[1],
        [30275, 30276, 30277]),
    ]

class TTSCWinterMenu(SCMenu):
    """
    Speedchat phrases for Winter
    """
    def __init__(self, carol):
        SCMenu.__init__(self)
        
        self.__messagesChanged(carol)

    def destroy(self):
        SCMenu.destroy(self)

    def clearMenu(self):
        SCMenu.clearMenu(self)

    def __messagesChanged(self, carol):
        # clear out everything from our menu
        self.clearMenu()
        # if local toon has not been created, don't panic
        try:
            lt = base.localAvatar
        except:
            return
        winterMenu = []
        if carol:
            winterMenu.append(WinterMenu[0])
        winterMenu.append(WinterMenu[1])
        for section in winterMenu:
            if section[0] == -1:
                #This is not a submenu but a terminal!
                for phrase in section[1]:
                    if phrase not in OTPLocalizer.SpeedChatStaticText:
                        print(('warning: tried to link Winter phrase %s which does not seem to exist' % phrase))
                        break
                    self.append(SCStaticTextTerminal(phrase))
            else: #this should be a submenu
                menu = SCMenu()
                for phrase in section[1].keys():
                    blatherTxt = section[1][phrase]
                    if blatherTxt not in OTPLocalizer.SpeedChatStaticText:
                        print(('warning: tried to link Winter phrase %s which does not seem to exist' % phrase))
                        break
                    menu.append(TTSCIndexedTerminal(OTPLocalizer.SpeedChatStaticText.get(phrase, None), blatherTxt))

                menuName = str(section[0])
                self.append(SCMenuHolder(menuName, menu))
