from toontown.toonbase.ToontownModules import *
from direct.interval.IntervalGlobal import *
from direct.directnotify import DirectNotifyGlobal
from toontown.toonbase import ToontownGlobals
from otp.otpbase import OTPGlobals
from toontown.cogdominium.DistCogdoCraneObject import DistCogdoCraneObject
from toontown.cogdominium import CogdoCraneGameConsts as GameConsts

class DistCogdoCraneMoneyBag(DistCogdoCraneObject):

    """ This is a safe sitting around in the Cashbot CFO final battle
    room.  It's used as a prop for toons to pick up and throw at the
    CFO's head.  Also, the special safe with self.index == 0
    represents the safe that the CFO uses to put on his own head as a
    safety helmet from time to time. """

    notify = DirectNotifyGlobal.directNotify.newCategory('DistCogdoCraneMoneyBag')
    
    grabPos = (0, 0, GameConsts.Settings.MoneyBagGrabHeight.get())

    # What happens to the crane and its cable when this object is picked up?
    craneFrictionCoef = 0.2
    craneSlideSpeed = 11
    craneRotateSpeed = 16

    # A safe remains under physical control of whichever client
    # last dropped it, even after it stops moving.  This allows
    # goons to push safes out of the way.
    wantsWatchDrift = 0

    def __init__(self, cr):
        DistCogdoCraneObject.__init__(self, cr)
        NodePath.__init__(self, 'object')
        self.index = None
        
        self.flyToMagnetSfx = loader.loadSfx('phase_5/audio/sfx/TL_rake_throw_only.mp3')
        self.hitMagnetSfx = loader.loadSfx('phase_5/audio/sfx/AA_drop_safe.mp3')
        # We want these sfx's to overlap just a smidge for effect.
        self.toMagnetSoundInterval = Parallel(
            SoundInterval(self.flyToMagnetSfx, duration = ToontownGlobals.CashbotBossToMagnetTime, node = self),
            Sequence(Wait(ToontownGlobals.CashbotBossToMagnetTime - 0.02),
                     SoundInterval(self.hitMagnetSfx, duration = 1.0, node = self)))
        self.hitFloorSfx = loader.loadSfx('phase_5/audio/sfx/AA_drop_bigweight_miss.mp3')
        self.hitFloorSoundInterval = SoundInterval(
            self.hitFloorSfx, node = self)

    def announceGenerate(self):
        DistCogdoCraneObject.announceGenerate(self)
        self.name = 'moneyBag-%s' % self.doId
        self.setName(self.name)
        
        self.craneGame.moneyBag.copyTo(self)
        self.shadow = NodePath('notAShadow')
        
        self.collisionNode.setName('moneyBag')
        cs = CollisionSphere(0, 0, 4, 4)
        self.collisionNode.addSolid(cs)
        
        assert(self.index not in self.craneGame.moneyBags)
        self.craneGame.moneyBags[self.index] = self
        
        self.setupPhysics('moneyBag')
        self.resetToInitialPosition()

    def disable(self):
        assert(self.craneGame.moneyBags.get(self.index) == self)
        del self.craneGame.moneyBags[self.index]
        DistCogdoCraneObject.disable(self)

    def hideShadows(self):
        self.shadow.hide()

    def showShadows(self):
        self.shadow.show()

    def getMinImpact(self):
        # This method returns the minimum impact, in feet per second,
        # with which the object should hit the boss before we bother
        # to tell the server.
        if self.craneGame.heldObject:
            return ToontownGlobals.CashbotBossSafeKnockImpact
        else:
            return ToontownGlobals.CashbotBossSafeNewImpact

    def resetToInitialPosition(self):
        posHpr = GameConsts.MoneyBagPosHprs[self.index]
        self.setPosHpr(*posHpr)
        self.physicsObject.setVelocity(0, 0, 0)

    def fellOut(self):
        # The safe fell out of the world.  Reset it back to its
        # original position.
        
        self.deactivatePhysics()
        self.d_requestInitial()

    ##### Messages To/From The Server #####

    def setIndex(self, index):
        self.index = index

    def setObjectState(self, state, avId, craneId):
        if state == 'I':
            self.demand('Initial')
        else:
            DistCogdoCraneObject.setObjectState(self, state, avId, craneId)

    def d_requestInitial(self):
        self.sendUpdate('requestInitial')

    ### FSM States ###

    def enterInitial(self):
        self.resetToInitialPosition()
        self.showShadows()

    def exitInitial(self):
        pass

    if __dev__:

        def _handleMoneyBagGrabHeightChanged(self, height):
            grabPos = DistCogdoCraneMoneyBag.grabPos
            DistCogdoCraneMoneyBag.grabPos = (grabPos[0], grabPos[1], height)
