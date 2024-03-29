"""BattleBlocker module: contains the BattleBlocker class"""

from toontown.toonbase.ToontownModules import *
from direct.interval.IntervalGlobal import *
from otp.level import BasicEntities
from toontown.toonbase import ToontownGlobals
from direct.directnotify import DirectNotifyGlobal

""" BattleBlocker is a collision sphere that is associated with a battle cell.  If
the collision sphere is entered, it sends a collision message to all suits also
associated with the battle cell.  This will trigger a battle.  Once all the suits in
the battle cell have been defeated, the BattleBlockers message will fall on deaf ears,
and the toon can pass through it without triggering a battle """

# TODO: allow other geometry than a collision sphere

class BattleBlocker(BasicEntities.DistributedNodePathEntity):
    notify = DirectNotifyGlobal.directNotify.newCategory("BattleBlocker")
    def __init__(self, cr):
        BasicEntities.DistributedNodePathEntity.__init__(self, cr)
        self.suitIds = []
        self.battleId = None

    def setActive(self, active):
        self.active = active

    def announceGenerate(self):
        BasicEntities.DistributedNodePathEntity.announceGenerate(self)
        self.initCollisionGeom()

    def disable(self):
        self.ignoreAll()
        self.unloadCollisionGeom()
        BasicEntities.DistributedNodePathEntity.disable(self)

    def destroy(self):
        BasicEntities.DistributedNodePathEntity.destroy(self)

    def setSuits(self, suitIds):
        self.suitIds = suitIds

    def setBattle(self, battleId):
        self.battleId = battleId

    def setBattleFinished(self):
        # this is only called if the Toons won the battle
        assert(self.notify.debug("setBattleFinished, %s" % self.entId))
        # A message is already sent on the AI, so we probably
        # don't need to send one on the client
        #messenger.send("battleBlocker-"+str(self.entId))
        # no need to listen for collision events anymore
        self.ignoreAll()

    def initCollisionGeom(self):
        self.cSphere = CollisionSphere(0,0,0,self.radius)
        self.cSphereNode = CollisionNode("battleBlocker-%s-%s" %
                                         (self.level.getLevelId(), self.entId))
        self.cSphereNode.addSolid(self.cSphere)
        self.cSphereNodePath = self.attachNewNode(self.cSphereNode)
        self.cSphereNode.setCollideMask(ToontownGlobals.WallBitmask)
        self.cSphere.setTangible(0)

        self.enterEvent = "enter" + self.cSphereNode.getName()
        self.accept(self.enterEvent, self.__handleToonEnter)

        """ rather than do this, just use ~cs
        if __dev__:
            from otp.otpbase import OTPGlobals
            self.showCS(OTPGlobals.WallBitmask)
            """

    def unloadCollisionGeom(self):
        if hasattr(self, 'cSphereNodePath'):
            self.ignore(self.enterEvent)
            del self.cSphere
            del self.cSphereNode
            self.cSphereNodePath.removeNode()
            del self.cSphereNodePath

    def __handleToonEnter(self, collEntry):
        self.notify.debug ("__handleToonEnter, %s" % self.entId)
        self.startBattle()


    def startBattle(self):
        if not self.active:
            return

        # don't listen for any more events from the blocker
        # this Toon might not win the battle
        #self.ignoreAll()

        callback = None
        # first check if there is a valid battle going on
        if self.battleId != None and self.battleId in base.cr.doId2do:
            battle = base.cr.doId2do.get(self.battleId)
            if battle:
                self.notify.debug("act like we collided with battle %d" % self.battleId)
                callback = battle.handleBattleBlockerCollision
        elif len(self.suitIds) > 0:
            # a battle has not been created yet, pick the first
            # valid suit to start a battle with
            for suitId in self.suitIds:
                suit = base.cr.doId2do.get(suitId)
                if suit:
                    self.notify.debug("act like we collided with Suit %d ( in state %s )" % (suitId, suit.fsm.getCurrentState().getName()))
                    callback = suit.handleBattleBlockerCollision
                    break

        # the show to explain the local toon getting stopped by this collision sphere
        self.showReaction(callback)


    def showReaction(self, callback=None):
        if not base.localAvatar.wantBattles:
            return

        track = Sequence()
        # add some minimal show
        #track = Sequence(Func(base.cr.playGame.place.setState,'WaitForBattle'),
        #                 ActorInterval(base.localAvatar, animName = 'slip-backward'))
        if callback:
            track.append(Func(callback))
        track.start()

    if __dev__:
        def attribChanged(self, *args):
            self.unloadCollisionGeom()
            self.initCollisionGeom()
