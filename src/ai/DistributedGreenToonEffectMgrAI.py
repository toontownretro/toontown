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
    
    def __init__(self, air):
        DistributedObjectAI.DistributedObjectAI.__init__(self, air)

    # do the event
    def addGreenToonEffect(self):
        avId = self.air.getAvatarIdFromSender()
        av = self.air.doId2do.get(avId)

        from toontown.ai import HolidayManagerAI
        endTime = HolidayManagerAI.HolidayManagerAI.holidays[self.holidayId].getEndTime(date)
        startTime = HolidayManagerAI.HolidayManagerAI.holidays[self.holidayId].getStartTime(date)
        
        if endTime < startTime:
            end = time.localtime(endTime)
            start = time.localtime(startTime)
            
        newDate = HolidayManagerAI.HolidayManagerAI.holidays[self.holidayId].adjustDate(date)
        endTime = HolidayManagerAI.HolidayManagerAI.holidays[self.holidayId].getEndTime(newDate)   

        if not av:
            DistributedGreenToonEffectMgrAI.notify.warning(
                'Tried to add Green Toon effect to av %s, but they left' % avId)
        else:
            DistributedGreenToonEffectMgrAI.notify.warning(
                'Activating Green Toon effect for av %s' % avId)
            av.b_setCheesyEffect(OTPGlobals.CESnowMan, 0, endTime/60)
            
