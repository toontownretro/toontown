from toontown.toonbase.ToontownModules import NodePath, BillboardEffect, Vec3, Point3, TextureStage, \
     TransparencyAttrib, DecalEffect, VBase4
from direct.fsm import FSM
from direct.gui.DirectGui import DirectFrame, DGG
from direct.interval.IntervalGlobal import LerpScaleInterval, LerpColorScaleInterval, Parallel,\
     Sequence, Wait


class DinerStatusIndicator(NodePath, FSM.FSM):
    """Client only object that shows the status of one diner."""

    def __init__(self, parent, pos=None, scale =None):
        """Create a new indicator object."""
        NodePath.__init__(self, 'DinerStatusIndicator')
        if parent:
            self.reparentTo(parent)
        if pos:
            self.setPos(pos)
        if scale:
            self.setScale(scale)
        self.loadAssets()
        FSM.FSM.__init__(self,'DinerStatusIndicator')
        self.activeIval = None

    def delete(self):
        """Remove ourself from the world."""
        if self.activeIval:
            self.activeIval.pause()
            self.activeIval = None
        if self.angryIcon:
            self.angryIcon.removeNode()
            self.angryIcon = None
        if self.angryMeter:
            self.angryMeter.removeNode()
            self.angryMeter = None
        if self.hungryIcon:
            self.hungryIcon.removeNode()
            self.hungryIcon = None
        if self.hungryMeter:
            self.hungryMeter.removeNode()
            self.hungryMeter = None
        if self.eatingIcon:
            self.eatingIcon.removeNode()
            self.eatingIcon = None
        if self.eatingMeter:
            self.eatingMeter.removeNode()
            self.eatingMeter = None
        self.removeNode()

    def loadAssets(self):
        """Load all the stuff we need."""
        iconsFile = loader.loadModel('phase_12/models/bossbotHQ/BanquetIcons')
        self.angryIcon, self.angryMeter = self.loadIcon(iconsFile, '**/Anger')
        self.hungryIcon, self.hungryMeter = self.loadIcon(iconsFile, '**/Hunger')
        self.eatingIcon, self.eatingMeter = self.loadIcon(iconsFile, '**/Food')
        # Angry doesn't need a meter
        self.angryMeter.removeNode()
        self.angryMeter = None
        iconsFile.removeNode()

    def loadIcon(self, iconsFile, name):
        """Load and returns one icon and the associated meter."""
        retVal = iconsFile.find(name)
        retVal.setBillboardAxis()
        retVal.reparentTo(self)
        # create a dark copy
        dark = retVal.copyTo(NodePath())
        dark.reparentTo(retVal)
        dark.setColor(0.5,0.5,0.5,1)
        # make it look right when they are both on top of each other
        #retVal.setEffect(DecalEffect.make())
        retVal.setTransparency(TransparencyAttrib.MAlpha, 1)
        # now for the tricky part, move it down and do the texture projection
        ll, ur = dark.getTightBounds()
        center = retVal.attachNewNode('center')
        center.setPos(0, 0, ll[2])
        center.setDepthOffset(1)
        dark.wrtReparentTo(center)
        dark.setTexProjector(TextureStage.getDefault(), center, retVal)
        dark.setDepthOffset(2)
        retVal.stash()
        return retVal, center

    def enterEating(self, timeToFinishFood):
        """Enter the eating state and display the meter interval."""
        self.eatingIcon.unstash()
        self.activeIval = self.createMeterInterval(self.eatingIcon, self.eatingMeter, timeToFinishFood)
        self.activeIval.start()

    def exitEating(self):
        """Exit the eating state, cleanup the meter interval."""
        if self.activeIval:
            self.activeIval.finish()
            self.activeIval = None
        self.eatingIcon.stash()

    def enterHungry(self, timeToFinishFood):
        """Enter the hungry state and display the meter interval."""
        self.hungryIcon.unstash()
        self.activeIval = self.createMeterInterval(self.hungryIcon, self.hungryMeter, timeToFinishFood)
        self.activeIval.start()

    def exitHungry(self):
        """Exit the hungry state, cleanup the meter interval."""
        if self.activeIval:
            self.activeIval.finish()
            self.activeIval = None
        self.hungryIcon.stash()

    def enterAngry(self):
        """Enter the angry state and display the meter interval."""
        self.angryIcon.unstash()

    def exitAngry(self):
        """Exit the angry state, cleanup the meter interval."""
        self.angryIcon.stash()
        if self.activeIval:
            self.activeIval.finish()
            self.activeIval = None

    def enterDead(self):
        """Enter the dead state and display the meter interval."""
        pass

    def exitDead(self):
        """Exit the dead state, cleanup the meter interval."""
        pass

    def enterInactive(self):
        """Enter the dead state and display the meter interval."""
        pass

    def exitInactive(self):
        """Exit the dead state, cleanup the meter interval."""
        pass

    def createMeterInterval(self, icon, meter, time):
        """Create and return the meter interval."""
        ivalDarkness = LerpScaleInterval(meter,time,
                                      scale=Vec3(1, 1, 1),
                                      startScale=Vec3(1, 0.001, 0.001))
        flashingTrack = Sequence()
        flashDuration = 10
        if time > flashDuration:
            flashingTrack.append(Wait(time-flashDuration))
            for i in range(10):
                flashingTrack.append(Parallel(
                    LerpColorScaleInterval(icon, 0.5, VBase4(1, 0, 0, 1)),
                    icon.scaleInterval(0.5, 1.25)
                    ))
                flashingTrack.append(Parallel(
                    LerpColorScaleInterval(icon, 0.5, VBase4(1,1,1,1)),
                    icon.scaleInterval(0.5, 1)
                    ))

        retIval = Parallel(
            ivalDarkness,
            flashingTrack
            )
        return retIval
