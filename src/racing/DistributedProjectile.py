
#Okay, so what do we need functionally here?
#1. the ability for this to have distributed movement (created by AI, controlled by AI)
#2. The ability to move onto the curve
#3. The ability to move off the curve to hit a player.
from toontown.toonbase.ToontownModules import *
from direct.distributed.ClockDelta import *
from direct.interval.IntervalGlobal import *
from direct.gui.DirectGui import *
from direct.fsm import FSM
from direct.distributed.DistributedSmoothNode import DistributedSmoothNode
from otp.avatar.ShadowCaster import ShadowCaster

class DistributedProjectile(DistributedSmoothNode, ShadowCaster, NodePath):
    def __init__(self, cr):
        ShadowCaster.__init__(self)
        DistributedSmoothNode.__init__(self, cr)
        NodePath.__init__(self, "Projectile")

    def announceGenerate(self):
        DistributedSmoothNode.announceGenerate(self)
        self.name = self.uniqueName('projectile')
        self.posHprBroadcastName = self.uniqueName('projectileBroadcast')

        geom=loader.loadModel("models/smiley")
        self.geom=geom
        self.geom.reparentTo(self)
        self.startSmooth()

        #self.__enableCollisions()

        ###########################################################
        # Add the kart to the scene
        self.reparentTo(render)

    def generate(self):
        DistributedSmoothNode.generate(self)
        self.name = self.uniqueName('projectile')
        self.posHprBroadcastName = self.uniqueName('projectileBroadcast')

        geom=loader.loadModel("models/smiley")
        self.geom=geom
        self.geom.reparentTo(self)
        self.startSmooth()

        #self.__enableCollisions()

        ###########################################################
        # Add the kart to the scene
        self.reparentTo(render)

    def setAvId(self, avId):
        self.avId=avId

    def delete(self):
        DistributedSmoothNode.delete(self)
