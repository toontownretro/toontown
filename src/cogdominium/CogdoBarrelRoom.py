#-------------------------------------------------------------------------------
# Contact: X (Schell Games)
# Created: X, 2010
#
# Purpose: Client-side, handles cutscene creation, barrel collection, reward showing
#------------------------------------------------------------------------------

import random

from toontown.toonbase.ToontownModules import *

from direct.interval.IntervalGlobal import *
from direct.directnotify import DirectNotifyGlobal

from toontown.toonbase import ToontownGlobals, ToontownTimer

from toontown.cogdominium import CogdoBarrelRoomConsts, CogdoBarrelRoomRewardPanel
from toontown.distributed import DelayDelete

class CogdoBarrelRoom:
    notify = DirectNotifyGlobal.directNotify.newCategory(
        'DistributedCogdoBarrelRoom')

    def __init__(self):
        self.timer = None
        
        self.model = None
        self._isLoaded = False
        
        self.dummyElevInNode = None
        self.cogdoBarrelsNode = None
        self.entranceNode = None
        self.nearBattleNode = None
        
        self.rewardUi = None
        self.rewardUiTaskName = 'CogdoBarrelRoom-RewardUI'
        self.rewardCameraTaskName = 'CogdoBarrelRoom-RewardCamera'
        
        self.fog = None
        
        self.defaultFar = None
        
        self.stomperSfx = None

    def destroy(self):
        self.unload()

    def load(self):
        if self._isLoaded:
            return
        
        self.timer = ToontownTimer.ToontownTimer()
        self.timer.stash()
        
        self.model = loader.loadModel(CogdoBarrelRoomConsts.BarrelRoomModel)
        self.model.setPos(*CogdoBarrelRoomConsts.BarrelRoomModelPos)
        self.model.reparentTo(render)
        self.model.stash()
        
        self.dummyElevInNode = self.model.attachNewNode('elevator-in')
        self.dummyElevInNode.hide()
        
        self.entranceNode = self.model.attachNewNode('door-entrance')
        self.entranceNode.setPos(0, -65, 0)
        
        self.nearBattleNode = self.model.attachNewNode('near-battle')
        self.nearBattleNode.setPos(0, -25, 0)
        
        self.rewardUi = CogdoBarrelRoomRewardPanel.CogdoBarrelRoomRewardPanel()
        self.hideRewardUi()
        
        self.stomperSfx = base.loader.loadSfx(CogdoBarrelRoomConsts.StomperSound)
        
        self.fog = Fog('barrel-room-fog')
        self.fog.setColor(CogdoBarrelRoomConsts.BarrelRoomFogColor)
        self.fog.setLinearRange(*CogdoBarrelRoomConsts.BarrelRoomFogLinearRange)
        
        self._isLoaded = True

    def unload(self):
        if self.model:
            self.model.removeNode()
            self.model = None
        
        if self.timer:
            self.timer.destroy()
            self.timer = None
        
        if self.rewardUi:
            self.rewardUi.destroy()
            self.rewardUi = None
        
        if self.fog:
            render.setFogOff()
            del self.fog
        
        taskMgr.remove(self.rewardUiTaskName)
        taskMgr.remove(self.rewardCameraTaskName)
        
        self._isLoaded = False

    def isLoaded(self):
        return self._isLoaded

    def show(self):
        if not self.cogdoBarrelsNode:
            self.cogdoBarrelsNode = render.find('**/@@CogdoBarrels')
            self.cogdoBarrelsNode.reparentTo(self.model)
            self.cogdoBarrelsNode.unstash()
        
        self.defaultFar = base.camLens.getFar()
        base.camLens.setFar(CogdoBarrelRoomConsts.BarrelRoomCameraFar)
        
        self.showBattleAreaLight(True)
        
        render.setFog(self.fog)
        
        self.model.unstash()

    def hide(self):
        self.model.stash()
        render.setFogOff()
        if self.defaultFar is not None:
            base.camLens.setFar(self.defaultFar)
        return

    def activate(self):
        self.notify.info('Activating barrel room: %d sec timer.' % CogdoBarrelRoomConsts.CollectionTime)
        self.timer.unstash()
        self.timer.posAboveShtikerBook()
        self.timer.countdown(CogdoBarrelRoomConsts.CollectionTime)
        base.cr.playGame.getPlace().fsm.request('walk')

    def deactivate(self):
        self.notify.info('Deactivating barrel room.')
        self.timer.stop()
        self.timer.stash()

    def placeToonsAtEntrance(self, toons):
        for i in range(len(toons)):
            toons[i].setPosHpr(self.entranceNode, * CogdoBarrelRoomConsts.BarrelRoomPlayerSpawnPoints[i])

    def placeToonsNearBattle(self, toons):
        for i in range(len(toons)):
            toons[i].setPosHpr(self.nearBattleNode, * CogdoBarrelRoomConsts.BarrelRoomPlayerSpawnPoints[i])

    def showBattleAreaLight(self, visible = True):
        lightConeNode = self.model.find('**/battleCone')
        if lightConeNode != None and not lightConeNode.isEmpty():
            if visible:
                lightConeNode.show()
            else:
                lightConeNode.hide()
        return

    def getIntroInterval(self):
        """
        Creates an intro cutscene interval when entering the barrel room
        The camera pans from right to left and back to right
        """
        avatar = base.localAvatar
        trackName = '__introBarrelRoom-%d' % avatar.doId
        track = Parallel(name = trackName)
        track.append(self.__stomperIntervals())
        track.append(Sequence(
                        # Show the right stompers
                        Func(camera.reparentTo, render),
                        Func(camera.setPosHpr, self.model, -20.0, -87.9, 12.0, -30, 0, 0),
                        Func(base.transitions.irisIn, 0.5),
                        Wait(1.0),
                        # Move the camera to the left
                        LerpHprInterval(camera,
                                        duration = 2.0,
                                        startHpr = Vec3(-30, 0, 0),
                                        hpr = Vec3(0, 0, 0),
                                        blendType = 'easeInOut'),
                        Wait(2.5),
                        # Move the camera back to the right
                        LerpHprInterval(camera,
                                        duration = 3.0,
                                        startHpr = Vec3(0, 0, 0),
                                        hpr = Vec3(-45, 0, 0),
                                        blendType = 'easeInOut'),
                        Wait(2.5),
                        ),
                    )
        track.delayDelete = DelayDelete.DelayDelete(avatar, 'introBarrelRoomTrack')
        track.setDoneEvent(trackName)
        return (track, trackName)

    def __stomperIntervals(self):
        """
        Creates a stomper interval of the stompers being disabled
        during the room cutscene
        """
        # Set the sound
        ivals = [SoundInterval(self.stomperSfx)]
        
        i = 0
        for stomperDef in CogdoBarrelRoomConsts.StomperProps:
            # Find all stompers
            stomperNode = render.find(stomperDef['path'])
            
            if stomperNode:
                # Randomly choose a position between 10 and 20
                maxZ = random.uniform(10, 20)
                
                # Set the minimum by dividing the maxZ by 10
                minZ = maxZ - 10
                
                # If the motion is set to up make it go from bottom to top
                if stomperDef['motion'] == 'up':
                    startZ, destZ = minZ, maxZ
                # Else start from top to bottom
                else:
                    startZ, destZ = maxZ, minZ
                
                # Set their new position
                stomperNode.setPos(Point3(0, 0, startZ))
                
                # Create the animation
                ivals.append(LerpPosInterval(
                                stomperNode,
                                CogdoBarrelRoomConsts.StomperHaltTime,
                                Point3(0, 0, destZ),
                                blendType = 'easeOut',
                                ),
                            )
            
            # Increase the count by 1
            i += 1

        # Return the animation for playing
        return Parallel(*tuple(ivals))

    def __rewardUiTimeout(self, callback):
        """
        Hide the Ui if a timeout happens
        """
        # Hide the Ui
        self.hideRewardUi()
        
        # Do a callback if asked
        if callback is not None:
            callback()

    def __rewardCamera(self):
        """
        Creates a forced view of the main elevator doors
        during the reward cutscene
        """
        trackName = 'cogdoBarrelRoom-RewardCamera'
        track = Sequence(
                    Func(camera.reparentTo, render),
                    Func(camera.setPosHpr, self.model, 0, 0, 11.0, 0, -14, 0),
                    Func(self.showBattleAreaLight, False),
                    name = trackName,
                    )
        return (track, trackName)

    def showRewardUi(self, results, callback = None):
        """
        Displays the reward UI at the end of the barrel room floor
        """
        # Set the camera
        track, trackName = self.__rewardCamera()
        
        # Check if the reward Ui should be shown
        if CogdoBarrelRoomConsts.ShowRewardUI:
            # Make it visible
            self.rewardUi.setRewards(results)
            self.rewardUi.unstash()
        
        # Set the UI to be shown for 5 seconds
        taskMgr.doMethodLater(CogdoBarrelRoomConsts.RewardUiTime,
            self.__rewardUiTimeout, self.rewardUiTaskName, extraArgs = [callback])
        
        return (track, trackName)

    def setRewardResults(self, results):
        """
        Sets the result to the reward UI
        """
        self.rewardUi.setRewards(results)

    def hideRewardUi(self):
        """
        Hides the reward UI
        """
        self.rewardUi.stash()
        taskMgr.remove(self.rewardUiTaskName)
