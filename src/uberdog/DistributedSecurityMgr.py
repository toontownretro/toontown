import socket
import datetime
import os
from direct.distributed.DistributedObjectGlobal import DistributedObjectGlobal
from direct.distributed.DistributedObject import DistributedObject
from toontown.toonbase import ToontownGlobals

class DistributedSecurityMgr(DistributedObject):
    """
    Uberdog object that keeps track of the last time the whitelist has been updated
    """
    notify = directNotify.newCategory('SecurityMgr')
    neverDisable = 1

    def __init__(self, cr):
        """Construct ourselves, set up web dispatcher."""
        assert self.notify.debugCall()
        DistributedObject.__init__(self, cr)
        base.cr.whitelistMgr = self

    def delete(self):
        """Delete ourself."""
        DistributedObject.delete(self)
        self.cr.whitelistMgr = None
        return

    def disable(self):
        self.notify.debug("i'm disabling SecurityMgr right now.")
        DistributedObject.disable(self)

    def generate(self):
        # Called when the client loads
        self.notify.debug("BASE: generate")
        DistributedObject.generate(self)

    def updateWhitelist(self):
        messenger.send("updateWhitelist")
        self.notify.info("Updating white list")
