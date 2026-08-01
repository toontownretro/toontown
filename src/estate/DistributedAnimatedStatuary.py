from toontown.toonbase.ToontownModules import NodePath
from direct.directnotify import DirectNotifyGlobal
from toontown.toonbase import ToontownGlobals
from toontown.estate import DistributedStatuary
from toontown.estate import GardenGlobals
from direct.actor import Actor

class DistributedAnimatedStatuary(DistributedStatuary.DistributedStatuary):
    """
    Regular statues and toon statues don't change once planted.
    This class does, initially created for the melting snowman
    """
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedAnimatedStatuary')

    def __init__(self, cr):
        self.notify.debug('constructing DistributedAnimatedStatuary')
        DistributedStatuary.DistributedStatuary.__init__(self, cr)

    def loadModel(self):
        """Load the assets, hide the other parts that don't match our growth level."""
        self.rotateNode = self.plantPath.attachNewNode('rotate')
        self.model = Actor.Actor()
        #import pdb; pdb.set_trace()
        animPath = self.modelPath + self.anims[1]
        self.model.loadModel(self.modelPath + self.anims[0])
        self.model.loadAnims(dict([[self.anims[1], animPath]]))
        colNode = self.model.find('**/+CollisionNode')
        if self.typeIndex == 234:
            colNode.setScale(0.5)
        if not colNode.isEmpty():
            (score, multiplier) = ToontownGlobals.PinballScoring[ToontownGlobals.PinballStatuary]
            if self.pinballScore:
                score = self.pinballScore[0]
                multiplier = self.pinballScore[1]
            scoreNodePath = NodePath("statuary-%d-%d" % (score, multiplier))
            colNode.setName('statuaryCol')
            scoreNodePath.reparentTo(colNode.getParent())
            colNode.reparentTo(scoreNodePath)
        self.model.setScale(self.worldScale)
        self.model.reparentTo(self.rotateNode)
        self.model.loop(self.anims[1])

    def setTypeIndex(self, typeIndex):
        DistributedStatuary.DistributedStatuary.setTypeIndex(self, typeIndex)
        self.anims = GardenGlobals.PlantAttributes[typeIndex]['anims']

    def setupShadow(self):
        if self.typeIndex == 234:
            pass
        else:
            DistributedStatuary.DistributedStatuary.setupShadow()
