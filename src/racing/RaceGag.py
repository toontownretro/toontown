from toontown.toonbase.ToontownModules import *
from direct.interval.IntervalGlobal import *
from direct.showbase import DirectObject
from .DroppedGag import *
types=["","Pie","Banana","Anvil"]


class RaceGag(DirectObject.DirectObject):
    def __init__(self,parent,slot, testPos):
        DirectObject.DirectObject.__init__(self)
        self._parent=parent

        self.name='gag-'+str(slot)
        self.geom=DroppedGag(self.name,base.race.qbox)
        self.geom.dropShadow.setScale(.7)
        self.geom.setPos(testPos+Vec3(0,0,-1))
        #qc=CollisionSphere(0,0,0,1)
        qc=CollisionTube(Point3(0,0,-2.5),Point3(0,0,2.5),1)
        self.gagnp=NodePath(CollisionNode(self.name))
        self.gagnp.node().addSolid(qc)
        self.gagnp.reparentTo(self.geom)
        self.gagnp.node().setIntoCollideMask(BitMask32(0x8000))
        self.gagnp.node().setFromCollideMask(BitMask32(0x8000))
        self.slot=slot
        self.type=0
        self.accept("imIn-"+self.name,self.hitGag)
        self.pickupSound=base.loader.loadSfx("phase_6/audio/sfx/KART_getGag.mp3")
        self.fadeout = None

    def delete(self):
        if self.fadeout:
            self.fadeout.finish()
            self.fadeout = None
        self.gagnp.removeNode()
        self.gagnp = None
        self.geom.delete()
        self.geom = None
        del self._parent
        self.ignore("imIn-"+self.name)

    def getType(self):
        return self.type

    def isActive(self):
        if(self.type):
            return True
        else:
            return False

    def genGag(self,spot,type):
        self.type=type
        fadein=self.geom.scaleInterval(1,4)
        self.geom.setScale(0.001)
        #loc=parent.geom.find("**/gag_spot"+str(spot))
        #self.geom.setPos(loc)
        self.geom.reparentTo(self._parent.geom)
        self.gagnp.reparentTo(self.geom)
        fadein.start()


    def hideGeom(self):
        self.geom.detachNode()

    def disableGag(self):
        self.gagnp.reparentTo(hidden)
        self.type=0
        if self.fadeout:
            self.fadeout.finish()
        self.fadeout=Sequence(self.geom.scaleInterval(.2,0),Func(self.hideGeom))
        self.fadeout.start()


    def hitGag(self,cevent):
        if(not self._parent.currGag):
            self.pickupSound.play()
            self._parent.pickupGag(self.slot,self.type)
            #Move the gag into hidden after its faded out.
            self.disableGag()
