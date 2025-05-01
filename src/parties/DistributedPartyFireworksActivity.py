#-------------------------------------------------------------------------------
# Contact: Rob Gordon
# Created: Oct 2008
#
# Purpose: Client-side fireworks for a parties.
#
#-------------------------------------------------------------------------------

# Panda imports
from toontown.toonbase.ToontownModules import Vec3
from toontown.toonbase.ToontownModules import OmniBoundingVolume
from toontown.toonbase.ToontownModules import AlphaTestAttrib
from toontown.toonbase.ToontownModules import RenderAttrib
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import *
from direct.distributed.ClockDelta import globalClockDelta

# Toontown imports
from toontown.effects.FireworkShowMixin import FireworkShowMixin
from toontown.effects.RocketExplosion import RocketExplosion
from toontown.toonbase import TTLocalizer

# Party imports
from .PartyGlobals import FireworkShows
from .PartyGlobals import ActivityIds
from .PartyGlobals import ActivityTypes
from .PartyGlobals import FireworksStartedEvent
from .PartyGlobals import FireworksFinishedEvent
from .PartyGlobals import FireworksPostLaunchDelay
from .PartyGlobals import RocketSoundDelay
from .PartyGlobals import RocketDirectionDelay
from .DistributedPartyActivity import DistributedPartyActivity
from .activityFSMs import FireworksActivityFSM

from . import PartyGlobals

class DistributedPartyFireworksActivity(DistributedPartyActivity, FireworkShowMixin):

    notify = directNotify.newCategory("DistributedPartyFireworksActivity")

    def __init__(self, cr):
        """
        cr: instance of ClientRepository
        """
        DistributedPartyFireworksActivity.notify.debug("__init__")
        DistributedPartyActivity.__init__(self, cr, ActivityIds.PartyFireworks, ActivityTypes.HostInitiated, wantLever=True)
        FireworkShowMixin.__init__(self, restorePlaygroundMusic=True, startDelay=FireworksPostLaunchDelay)

    def setEventId(self, eventId):
        DistributedPartyFireworksActivity.notify.debug("setEventId( %s )" % FireworkShows.getString(eventId) )
        self.eventId = eventId

    def setShowStyle(self, showStyle):
        DistributedPartyFireworksActivity.notify.debug("setShowStyle( %d )" % showStyle)
        self.showStyle = showStyle

    def load(self):
        """
        Load the necessary assets
        """
        DistributedPartyFireworksActivity.notify.debug("load")
        DistributedPartyActivity.load(self)

        self.eventId = PartyGlobals.FireworkShows.Summer

        # load the rocket platform and place it in party space
        self.launchPadModel = loader.loadModel('phase_13/models/parties/launchPad')
        # Compensate for pivot of fireworks model and center it in 2x4 space
        self.launchPadModel.setH(90.0)
        self.launchPadModel.setPos(0.0, -18.0, 0.0)
        # reparent to root
        self.launchPadModel.reparentTo( self.root )
        # special case the depth testing on the railings to prevent
        # transparency oddness
        railingsCollection = self.launchPadModel.findAllMatches("**/launchPad_mesh/*railing*")
        for i in range( railingsCollection.getNumPaths() ):
            railingsCollection[i].setAttrib(AlphaTestAttrib.make(RenderAttrib.MGreater, 0.75))

        # place the lever on the platform
        leverLocator = self.launchPadModel.find("**/RocketLever_locator")
        self.lever.setPosHpr(Vec3.zero(), Vec3.zero())
        self.lever.reparentTo(leverLocator)
        self.toonPullingLeverInterval = None

        # place the activity sign
        self.sign.reparentTo( self.launchPadModel.find("**/launchPad_sign_locator") )

        # load the rocket with animation and place it on the platform
        self.rocketActor = Actor(
            'phase_13/models/parties/rocket_model',
            {'launch':'phase_13/models/parties/rocket_launch'},
        )

        rocketLocator = self.launchPadModel.find("**/rocket_locator")
        self.rocketActor.reparentTo(rocketLocator)
        # ensure the rocket is never culled
        self.rocketActor.node().setBounds( OmniBoundingVolume() )
        self.rocketActor.node().setFinal( True )

        effectsLocator = self.rocketActor.find("**/joint1")
        self.rocketExplosionEffect  = RocketExplosion(effectsLocator, rocketLocator)

        self.rocketParticleSeq = None

        self.launchSound = base.loader.loadSfx("phase_13/audio/sfx/rocket_launch.mp3")

        # create state machine and set initial state
        self.activityFSM = FireworksActivityFSM( self )
        self.activityFSM.request("Idle")

    def unload(self):
        DistributedPartyFireworksActivity.notify.debug("unload")
        taskMgr.remove( self.taskName( "delayedStartShow" ) )
        if self.rocketParticleSeq:
            self.rocketParticleSeq.pause()
            self.rocketParticleSeq = None
        self.launchPadModel.removeNode()
        del self.launchPadModel
        del self.toonPullingLeverInterval
        self.rocketActor.delete()
        self.rocketExplosionEffect.destroy()
        self.activityFSM.request("Disabled")
        del self.rocketActor
        del self.launchSound
        del self.activityFSM
        del self.eventId
        del self.showStyle
        DistributedPartyActivity.unload(self)

    def _leverPulled(self, collEntry):
        DistributedPartyFireworksActivity.notify.debug("_leverPulled")
        hostPulledLever = DistributedPartyActivity._leverPulled(self, collEntry)
        if self.activityFSM.getCurrentOrNextState() == "Active":
            self.showMessage(TTLocalizer.PartyFireworksAlreadyActive)
        elif self.activityFSM.getCurrentOrNextState() == "Disabled":
            self.showMessage(TTLocalizer.PartyFireworksAlreadyDone)
        elif self.activityFSM.getCurrentOrNextState() == "Idle":
            if hostPulledLever:
                base.cr.playGame.getPlace().fsm.request("activity") # prevent toon from moving
                self.toonPullingLeverInterval = self.getToonPullingLeverInterval(base.localAvatar)
                self.toonPullingLeverInterval.append(Func(self.d_toonJoinRequest))
                self.toonPullingLeverInterval.append(Func(base.cr.playGame.getPlace().fsm.request, 'walk'))
                self.toonPullingLeverInterval.start()
            else:
                self.showMessage(TTLocalizer.PartyOnlyHostLeverPull)

    # FSM utility methods
    def setState(self, newState, timestamp):
        DistributedPartyFireworksActivity.notify.debug( "setState( newState=%s, ... )" % newState )
        DistributedPartyActivity.setState( self, newState, timestamp )
        # pass additional parameters only to those states that need it
        if newState == "Active":
            self.activityFSM.request( newState, timestamp )
        else:
            self.activityFSM.request( newState )

    # FSM transition methods
    def startIdle(self):
        DistributedPartyFireworksActivity.notify.debug("startIdle")

    def finishIdle(self):
        DistributedPartyFireworksActivity.notify.debug("finishIdle")

    def startActive(self, showStartTimestamp):
        DistributedPartyFireworksActivity.notify.debug("startActive")
        messenger.send( FireworksStartedEvent )
        # if too much time has passed since the show started, don't bother
        # playing the rocket animation, just hide it
        timeSinceStart = globalClockDelta.localElapsedTime(showStartTimestamp)
        if timeSinceStart > self.rocketActor.getDuration("launch"):
            self.rocketActor.hide()
            self.startShow(self.eventId, self.showStyle, showStartTimestamp)
        else:
            self.rocketActor.play( "launch" )
            self.rocketParticleSeq = Sequence(Wait(RocketSoundDelay), \
                                                        Func(base.playSfx,self.launchSound), \
                                                        Func(self.rocketExplosionEffect.start), \
                                                        Wait(RocketDirectionDelay), \
                                                        LerpHprInterval(self.rocketActor, 4.0, Vec3(0, 0, -60)), \
                                                        Func(self.rocketExplosionEffect.end), \
                                                        Func(self.rocketActor.hide))
            self.rocketParticleSeq.start()

            # give rocket animation some time to play out before starting the show
            taskMgr.doMethodLater(
                FireworksPostLaunchDelay,
                self.startShow,
                self.taskName( "delayedStartShow" ),
                extraArgs=[self.eventId, self.showStyle, showStartTimestamp, self.root],
            )

    def finishActive(self):
        self.rocketParticleSeq = None
        DistributedPartyFireworksActivity.notify.debug("finishActive")
        messenger.send( FireworksFinishedEvent )
        taskMgr.remove( self.taskName( "delayedStartShow" ) )
        FireworkShowMixin.disable(self) # stop the fireworks show

    def startDisabled(self):
        DistributedPartyFireworksActivity.notify.debug("startDisabled")
        if not self.rocketActor.isEmpty():
            self.rocketActor.hide() # so late comers won't see the rocket

    def finishDisabled(self):
        DistributedPartyFireworksActivity.notify.debug("finishDisabled")

    def handleToonDisabled(self, toonId):
        """
        A toon dropped unexpectedly from the game. Handle it!
        """
        self.notify.warning("handleToonDisabled no implementation yet" )
