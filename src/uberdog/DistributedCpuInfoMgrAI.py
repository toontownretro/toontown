import socket
import datetime
import os
from direct.distributed.DistributedObjectGlobal import DistributedObjectGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI
from direct.http.WebRequest import WebRequestDispatcher
from otp.distributed import OtpDoGlobals
from toontown.toonbase import ToontownGlobals

ParentClass = DistributedObjectAI
#ParentClass = DistributedObjectGlobal
class DistributedCpuInfoMgrAI(ParentClass ):
    """
    Uberdog object that keeps track of the last time in game news has been updated
    """
    notify = directNotify.newCategory('DistributedCpuInfoMgrAI')


    def __init__(self, cr):
        """Construct ourselves, set up web dispatcher."""
        assert self.notify.debugCall()
        ParentClass.__init__(self, cr)
        self.latestIssueStr = ""
        self.avId2Fingerprint = {}
        self.accept("avatarEntered", self.handleAvatarEntered) 

    def generate(self):
        """We have zone info but not required fields, register for the special."""
        # IN_GAME_NEWS_MGR_UD_TO_ALL_AI will arrive on this channel
        self.air.registerForChannel(OtpDoGlobals.OTP_DO_ID_TOONTOWN_CPU_INFO_MANAGER)
        ParentClass.generate(self)

    def announceGenerate(self):
        # tell uberdog we are starting up, so we can get info on the currently running public parties
        # do whatever other sanity checks is necessary here
        DistributedObjectAI.announceGenerate(self)
        
    def sendCpuInfoToUd(self, info, fingerprint):
        """Prepare to send the info to the UD, we don't have the DISLid yet.""" 
        requesterId = self.air.getAvatarIdFromSender()
        self.avId2Fingerprint[requesterId] = (info,fingerprint)
         
    def handleAvatarEntered(self, avatar):
        """Send the cpu info to the UD once we get the avatar and the DISL id."""
        if avatar.doId in self.avId2Fingerprint:            
            info, fingerprint = self.avId2Fingerprint.get(avatar.doId)            
            dislId = 0
            if avatar:
                try:
                    dislId = avatar.DISLid
                except:
                    pass
            if dislId:
                self.air.sendUpdateToDoId("DistributedCpuInfoMgr",
                                      'setCpuInfoToUd',
                                      OtpDoGlobals.OTP_DO_ID_TOONTOWN_CPU_INFO_MANAGER,
                                      [avatar.doId, dislId, info[:255],fingerprint[:255]]
                                  )
            else:
                self.notify.warning("avId=%s has dislId=%s" % (avatar.doId, dislId))
            del self.avId2Fingerprint[avatar.doId]
 
