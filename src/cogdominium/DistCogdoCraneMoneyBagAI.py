from toontown.toonbase.ToontownModules import *
from toontown.toonbase import ToontownGlobals
from otp.otpbase import OTPGlobals
from toontown.cogdominium.DistCogdoCraneObjectAI import DistCogdoCraneObjectAI
from toontown.cogdominium import CogdoCraneGameConsts as GameConsts

class DistCogdoCraneMoneyBagAI(DistCogdoCraneObjectAI):

    """ This is an object that can be picked up an dropped in the
    final battle scene with the Cashbot CFO.  In particular, it's a
    safe or a goon.  """

    # This should be true for objects that will eventually transition
    # from SlidingFloor to Free when they stop moving.
    wantsWatchDrift = 0

    def __init__(self, air, boss, index):
        DistCogdoCraneObjectAI.__init__(self, air, boss)
        self.index = index
        
        self.avoidHelmet = 0
        
        # A sphere so goons will see and avoid us.
        cn = CollisionNode('sphere')
        cs = CollisionSphere(0, 0, 0, 6)
        cn.addSolid(cs)
        self.attachNewNode(cn)

    def resetToInitialPosition(self):
        posHpr = GameConsts.MoneyBagPosHprs[self.index]
        self.setPosHpr(*posHpr)

    ### Messages ###


    def getIndex(self):
        return self.index

    def hitBoss(self, impact):
        avId = self.air.getAvatarIdFromSender()
        
        self.validate(avId, impact <= 1.0,
                      'invalid hitBoss impact %s' % impact)
                      
        if avId not in self.boss.involvedToons:
            return

        if self._state != 'Dropped' and self._state != 'Grabbed':
            return

        if self.avoidHelmet or self == self.boss.heldObject:
            # Ignore the helmet we just knocked off.
            return

        # The client reports successfully striking the boss in the
        # head with this object.
        if self.boss.heldObject == None:
            if self.boss.attackCode == ToontownGlobals.BossCogDizzy:
                # While the boss is dizzy, a safe hitting him in the
                # head does lots of damage.
                damage = int(impact * 50)
                self.boss.recordHit(max(damage, 2))
            else:
                # If he's not dizzy, he grabs the safe and makes a
                # helmet out of it--but only once every five minutes
                # from a particular avatar (to reduce griefing).
                if self.boss.acceptHelmetFrom(avId):
                    self.demand('Grabbed', self.boss.doId, self.boss.doId)
                    self.boss.heldObject = self

        else:
            # It knocks a helmet off his head.
            if impact >= ToontownGlobals.CashbotBossSafeKnockImpact:
                self.boss.heldObject.demand('Dropped', avId, self.boss.doId)
                self.boss.heldObject.avoidHelmet = 1
                self.boss.heldObject = None
                self.avoidHelmet = 1
                self.boss.waitForNextHelmet()

    def requestInitial(self):
        # The client controlling the safe dropped it through the
        # world; reset it to its initial state.
        
        avId = self.air.getAvatarIdFromSender()
        
        if avId == self.avId:
            self.demand('Initial')



    ### FSM States ###
    
    def enterGrabbed(self, avId, craneId):
        DistCogdoCraneObjectAI.enterGrabbed(self, avId, craneId)
        self.avoidHelmet = 0

    def enterInitial(self):
        # The safe is in its initial, resting position.
        
        self.avoidHelmet = 0
        self.resetToInitialPosition()
        
        if self.index == 0:
            # The special "helmet-only" safe goes away completely when
            # it's in Initial mode.
            self.stash()

        self.d_setObjectState('I', 0, 0)

    def exitInitial(self):
        if self.index == 0:
            self.unstash()

    def enterFree(self):
        # The safe is somewhere on the floor, but not under anyone's
        # control.  This can only happen to a safe when the player who
        # was controlling it disconnects during battle.

        DistCogdoCraneObjectAI.enterFree(self)
        self.avoidHelmet = 0
