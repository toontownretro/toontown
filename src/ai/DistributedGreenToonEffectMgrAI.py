from direct.directnotify import DirectNotifyGlobal
from direct.distributed import DistributedObjectAI
from otp.otpbase import OTPGlobals
import time

class DistributedGreenToonEffectMgrAI(DistributedObjectAI.DistributedObjectAI):
    """GreenToon effect ai implementation. This object sits in zone 5819 ('Green Bean Jeans'
    interior) and will activate the greenToon effect for anyone who says 'It's easy to be green!' to Eugene
    during the Ides Of March event."""

    notify = DirectNotifyGlobal.directNotify.newCategory(
        'DistributedGreenToonEffectMgrAI')
    
    def __init__(self, air, holidayId):
        DistributedObjectAI.DistributedObjectAI.__init__(self, air)

    # do the event
    def addGreenToonEffect(self):
        avId = self.air.getAvatarIdFromSender()
        av = self.air.doId2do.get(avId)
        localTime = time.localtime()
        date = (localTime[0],
                localTime[1],
                localTime[2],
                localTime[6],
                )

        from toontown.ai import HolidayManagerAI
        # This seems horrible to hardcode but still an improvement over hardcoding
        # the duration
        endTime = HolidayManagerAI.HolidayManagerAI.holidays[105].getEndTime(date)
        
        if not av:
            self.notify.warning(
                'Tried to add Green Toon effect to av %s, but they left' % avId)
        else:
            DistributedGreenToonEffectMgrAI.notify.warning(
                'Activating Green Toon effect for av %s' % avId)
            #av.b_setCheesyEffect(OTPGlobals.CEGreenToon, 0, (time.time()/60)+1)
            av.b_setCheesyEffect(OTPGlobals.CEGreenToon, 0, endTime/60)
