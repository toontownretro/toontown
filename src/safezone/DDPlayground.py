
from toontown.toonbase.ToontownModules import *

from . import Playground
from direct.task.Task import Task
import random
from direct.fsm import ClassicFSM, State
from direct.actor import Actor
from toontown.toonbase import ToontownGlobals
from direct.directnotify import DirectNotifyGlobal
from toontown.hood import Place

class DDPlayground(Playground.Playground):
    notify = DirectNotifyGlobal.directNotify.newCategory("DDPlayground")

    def __init__(self, loader, parentFSM, doneEvent):
        assert self.notify.debugStateCall(self)
        Playground.Playground.__init__(self, loader, parentFSM, doneEvent)
        # Underwater stuff
        self.cameraSubmerged = -1
        self.toonSubmerged = -1
        self.activityFsm = ClassicFSM.ClassicFSM(
            'Activity', [
                State.State(
                    'off',
                    self.enterOff,
                    self.exitOff,
                    ['OnBoat']),
                State.State(
                    'OnBoat',
                    self.enterOnBoat,
                    self.exitOnBoat,
                    ['off'])
                ],
            # Initial state
            'off',
            # Final state
            'off',
            )
        self.activityFsm.enterInitialState()

    def load(self):
        assert self.notify.debugStateCall(self)
        Playground.Playground.load(self)

    def unload(self):
        assert self.notify.debugStateCall(self)
        del self.activityFsm
        Playground.Playground.unload(self)

    def enter(self, requestStatus):
        assert self.notify.debugStateCall(self)
        self.nextSeagullTime = 0
        taskMgr.add(self.__seagulls, 'dd-seagulls')
        self.loader.hood.setWhiteFog()
        # donald=self.loader.donald
        # donald.loop("wheel")
        # donald.setZ(3.95)
        # donald.setY(-1.0)
        # donald.reparentTo(base.cr.playGame.hood.loader.boat)
        Playground.Playground.enter(self, requestStatus)

    def exit(self):
        assert self.notify.debugStateCall(self)
        Playground.Playground.exit(self)
        taskMgr.remove('dd-check-toon-underwater')
        taskMgr.remove('dd-check-cam-underwater')
        taskMgr.remove('dd-seagulls')
        # Clean up underwater state
        self.loader.hood.setNoFog()
        # donald=self.loader.donald
        # donald.stop()
        # donald.reparentTo(hidden)

    def enterStart(self):
        assert self.notify.debugStateCall(self)
        self.cameraSubmerged = 0
        self.toonSubmerged = 0
        taskMgr.add(self.__checkToonUnderwater,
                    'dd-check-toon-underwater')
        taskMgr.add(self.__checkCameraUnderwater,
                    'dd-check-cam-underwater')

    def enterDoorOut(self):
        assert self.notify.debugStateCall(self)
        taskMgr.remove('dd-check-toon-underwater')

    def exitDoorOut(self):
        assert self.notify.debugStateCall(self)

    def enterDoorIn(self, requestStatus):
        assert self.notify.debugStateCall(self)
        Playground.Playground.enterDoorIn(self, requestStatus)
        taskMgr.add(self.__checkToonUnderwater,
                    'dd-check-toon-underwater')

    def __checkCameraUnderwater(self, task):
        # spammy: assert self.notify.debugStateCall(self)
        # We need to take into account the height of the local toon
        # if (base.localAvatar.getZ() < -2.3314585):
        # It is more accurate to use the camera because it can
        # move independently of the toon
        if (camera.getZ(render) < 1.0):
            self.__submergeCamera()
        else:
            self.__emergeCamera()
        return Task.cont

    def __checkToonUnderwater(self, task):
        # spammy: assert self.notify.debugStateCall(self)
        # We need to take into account the height of the local toon
        if (base.localAvatar.getZ() < -2.3314585):
            self.__submergeToon()
        else:
            self.__emergeToon()
        return Task.cont

    def __submergeCamera(self):
        if (self.cameraSubmerged == 1):
            return
        assert self.notify.debugStateCall(self)
        self.loader.hood.setUnderwaterFog()
        base.playSfx(self.loader.underwaterSound, looping = 1, volume = 0.8)
        self.loader.seagullSound.stop()
        taskMgr.remove('dd-seagulls')
        self.cameraSubmerged = 1
        self.walkStateData.setSwimSoundAudible(1)

    def __emergeCamera(self):
        if (self.cameraSubmerged == 0):
            return
        assert self.notify.debugStateCall(self)
        self.loader.hood.setWhiteFog()
        self.loader.underwaterSound.stop()
        self.nextSeagullTime = random.random() * 8.0
        taskMgr.add(self.__seagulls, 'dd-seagulls')
        self.cameraSubmerged = 0
        self.walkStateData.setSwimSoundAudible(0)

    def __submergeToon(self):
        if (self.toonSubmerged == 1):
            return
        assert self.notify.debugStateCall(self)
        base.playSfx(self.loader.submergeSound)  # plays a splash sound

        # Make sure you are in walk mode This fixes a bug where you could
        # open your stickerbook over the water and get stuck in swim mode
        # becuase the Place was still in StickerBook state.
        if ConfigVariableBool('disable-flying-glitch', 1).getValue() == 0:
            self.fsm.request('walk')

        # You have to pass in the swim sound effect to swim mode.
        self.walkStateData.fsm.request('swimming', [self.loader.swimSound])
        # Let everyone else see your splash
        pos = base.localAvatar.getPos(render)
        base.localAvatar.d_playSplashEffect(pos[0], pos[1], 1.675)
        self.toonSubmerged = 1

    def __emergeToon(self):
        if (self.toonSubmerged == 0):
            return
        assert self.notify.debugStateCall(self)
        self.walkStateData.fsm.request('walking')
        self.toonSubmerged = 0

    def __seagulls(self, task):
        if (task.time < self.nextSeagullTime):
            return Task.cont
        assert self.notify.debugStateCall(self)
        base.playSfx(self.loader.seagullSound)
        self.nextSeagullTime = task.time + random.random() * 4.0 + 8.0
        return Task.cont

    def enterTeleportIn(self, requestStatus):
        assert self.notify.debugStateCall(self)
        self.toonSubmerged = -1
        taskMgr.remove('dd-check-toon-underwater')
        Playground.Playground.enterTeleportIn(self, requestStatus)

    def teleportInDone(self):
        """
        Override Place.py teleportInDone to check if we are cameraSubmerged.
        If we are cameraSubmerged, we should swim instead of walk
        """
        assert self.notify.debugStateCall(self)
        self.toonSubmerged = -1
        taskMgr.add(self.__checkToonUnderwater,
                    'dd-check-toon-underwater')
        Playground.Playground.teleportInDone(self)

    ##### Off state #####

    def enterOff(self):
        assert self.notify.debugStateCall(self)
        return None

    def exitOff(self):
        assert self.notify.debugStateCall(self)
        return None

    ##### OnBoat state #####

    def enterOnBoat(self):
        assert self.notify.debugStateCall(self)
        base.localAvatar.b_setParent(ToontownGlobals.SPDonaldsBoat)
        base.playSfx(self.loader.waterSound, looping=1)

    def exitOnBoat(self):
        assert self.notify.debugStateCall(self)
        base.localAvatar.b_setParent(ToontownGlobals.SPActors)
        self.loader.waterSound.stop()
