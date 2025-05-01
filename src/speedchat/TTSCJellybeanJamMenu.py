"""
TTSCJellybeanJamMenu.py: contains the TTSCJellybeanJamMenu class
"""

from direct.showbase import PythonUtil
from otp.speedchat.SCMenu import SCMenu
from otp.speedchat.SCMenuHolder import SCMenuHolder
from otp.speedchat.SCStaticTextTerminal import SCStaticTextTerminal
from otp.otpbase import OTPLocalizer

#this is the structure of the racing menu
JellybeanJamMenu = [
    (OTPLocalizer.JellybeanJamMenuSections[0],            # GET JELLYBEANS
        [30180, 30181, 30182, 30183, 30184, 30185]),
    (OTPLocalizer.JellybeanJamMenuSections[1],            # SPEND JELLYBEANS
        [30186, 30187, 30188, 30189, 30190]),
    #(OTPLocalizer.JellybeanJamMenuSections[2],            # JELLYBEAN PARTIES
    #    [30191, 30192, 30193, 30194]),
    ]
   
JellybeanJamPhases = PythonUtil.Enum('TROLLEY, FISHING, PARTIES')
PhaseSpecifPhrases = [30180, 30181, 30182]

class TTSCJellybeanJamMenu(SCMenu):    
    """
    Speedchat phrases for Jellybean Jam
    """
    def __init__(self, phase):
        SCMenu.__init__(self)
        
        if phase in JellybeanJamPhases:
            self.__messagesChanged(phase)
        else:
            print(('warning: tried to add Jellybean Jam phase %s which does not seem to exist' % phase))

    def destroy(self):
        SCMenu.destroy(self)

    def clearMenu(self):
        SCMenu.clearMenu(self)

    def __messagesChanged(self, phase):
        # clear out everything from our menu
        self.clearMenu()
        
        # if local toon has not been created, don't panic
        try:
            lt = base.localAvatar
        except:
            return
        for section in JellybeanJamMenu:
            if section[0] == -1:
                #This is not a submenu but a terminal!
                for phrase in section[1]:
                    if phrase not in OTPLocalizer.SpeedChatStaticText:
                        print(('warning: tried to link Jellybean Jam phrase %s which does not seem to exist' % phrase))
                        break
                    self.append(SCStaticTextTerminal(phrase))
            else: #this should be a submenu
                menu = SCMenu()
                for phrase in section[1]:
                    if phrase not in OTPLocalizer.SpeedChatStaticText:
                        print(('warning: tried to link Jellybean Jam phrase %s which does not seem to exist' % phrase))
                        break
                    menu.append(SCStaticTextTerminal(phrase))

                menuName = str(section[0])
                self.append(SCMenuHolder(menuName, menu))
