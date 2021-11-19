import socket
import datetime
import os
from direct.distributed.DistributedObjectGlobal import DistributedObjectGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI
from otp.distributed import OtpDoGlobals
from toontown.toonbase import ToontownGlobals

ParentClass = DistributedObjectAI
#ParentClass = DistributedObjectGlobal
class DistributedWhitelistMgrAI(ParentClass ):
    """
    Uberdog object that keeps track of the last time the whitelist has been updated
    """
    notify = directNotify.newCategory('DistributedWhitelistMgrAI')


    def __init__(self, cr):
        """Construct ourselves, set up web dispatcher."""
        assert self.notify.debugCall()
        ParentClass.__init__(self, cr)
        self.updateWhitelist = ""

    def generate(self):
        """We have zone info but not required fields, register for the special."""
        self.air.registerForChannel(OtpDoGlobals.OTP_DO_ID_TOONTOWN_WHITELIST_MANAGER)
        ParentClass.generate(self)

    def announceGenerate(self):
        # tell uberdog we are starting up, so we can get info on the currently running public parties
        # do whatever other sanity checks is necessary here
        DistributedObjectAI.announceGenerate(self)
        self.air.sendUpdateToDoId("DistributedWhitelistMgr",
                                  'whitelistMgrAIStartingUp',
                                  OtpDoGlobals.OTP_DO_ID_TOONTOWN_WHITELIST_MANAGER,
                                   [self.doId, self.air.districtId]
                                  )
    def updateWhitelist(self, issueStr):
        """We normally get this once, we could get this when a new list is released while logged in."""
        # we receive this as a utc str
        assert self.notify.debugStateCall(self)
        self.updateWhitelist = ListStr
        pass

    def b_updateWhitelist(self, latestList):
        self.updateWhitelist(latestList)
        self.d_updateWhitelist(latestList)
        
    def d_updateWhitelist(self, latestList):
        self.sendUpdate("updateWhitelist",[self.updateWhitelist()])
        

    def getUpdateWhitelist(self):
        """We normally get this once, we could get this when a new list is released while logged in."""
        assert self.notify.debugStateCall(self)
        return self.updateWhitelist
        pass
    

    def newListUDtoAI(self, listStr):
        """Well the UD is telling us we have a new list, spread it to the clients."""
        self.b_updateWhitelist(listStr)
        
