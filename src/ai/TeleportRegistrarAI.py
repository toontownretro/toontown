# Potential temp

from direct.directnotify import DirectNotifyGlobal

class TeleportRegistrarAI:
    notify = DirectNotifyGlobal.directNotify.newCategory("TeleportRegistrarAI")

    def registerValidTeleport(self, toAvId, available, shardId, hoodId, zoneId, fromAvId):
        """ toAvId 100000016|available 1|shardId 201000000|hoodId 2000|zoneId 2000|fromAvId 100000003 """
        pass
