from direct.directnotify import DirectNotifyGlobal
from direct.distributed import DistributedObject
from direct.interval.IntervalGlobal import *
from otp.speedchat import SpeedChatGlobals
from toontown.toonbase import TTLocalizer

class DistributedGreenToonEffectMgr(DistributedObject.DistributedObject):
    """GreenToon effect client implementation; make the toon green if
    they say 'It's easy to be green!' to Eugene during the Ides Of March event."""

    notify = DirectNotifyGlobal.directNotify.newCategory(
        'DistributedGreenToonEffectMgr')
    
    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)

        # go ahead and start listening to speedchat
        def phraseSaid(phraseId):
            greenPhrase  = 30450
            if phraseId == greenPhrase :
                self.addGreenToonEffect()
        self.accept(SpeedChatGlobals.SCStaticTextMsgEvent, phraseSaid)

    def announceGenerate(self):
        DistributedObject.DistributedObject.announceGenerate(self)
        DistributedGreenToonEffectMgr.notify.debug('announceGenerate')

    def delete(self):
        # stop listening to speed chat
        self.ignore(SpeedChatGlobals.SCStaticTextMsgEvent)
        DistributedObject.DistributedObject.delete(self)

    # do the event
    def addGreenToonEffect(self):
        DistributedGreenToonEffectMgr.notify.debug('addGreenToonEffect')
        av = base.localAvatar
        self.sendUpdate('addGreenToonEffect', [])
            
        msgTrack = Sequence(
            Func(av.setSystemMessage, 0, TTLocalizer.GreenToonEffectMsg),
            )
        msgTrack.start()
