import socket
import datetime
import os
from direct.distributed.DistributedObjectGlobal import DistributedObjectGlobal
from direct.distributed.DistributedObject import DistributedObject
from toontown.toonbase import ToontownGlobals

class DistributedWhitelistMgr(DistributedObject):
    """
    Uberdog object that keeps track of the last time the whitelist has been updated
    """
    notify = directNotify.newCategory('WhitelistMgr')
    neverDisable = 1

    def __init__(self, cr):
        """Construct ourselves, set up web dispatcher."""
        assert self.notify.debugCall()
        DistributedObject.__init__(self, cr)
        base.cr.whitelistMgr = self

    def delete(self):
        """Delete ourself."""
        DistributedObject.delete(self)
        self.cr.whitelistMgr  = None

    def disable(self):
        self.notify.debug( "i'm disabling WhitelistMgr right now." )
        DistributedObject.disable(self)

    def generate(self):
        # Called when the client loads
        self.notify.debug("BASE: generate")
        DistributedObject.generate(self)

    def updateWhitelist(self):
        """We normally get this once, we could get this when a new whitelist is released while logged in."""
        # the string we get is in utc
        assert self.notify.debugStateCall(self)
        messenger.send('updateWhitelist')
        self.notify.info('Updating white list')
