from toontown.toonbase.ToontownModules import *
from direct.interval.IntervalGlobal import *
from .StomperGlobals import *
from direct.distributed import ClockDelta
from direct.showbase.PythonUtil import lerp
import math
from otp.level import DistributedEntity
from direct.directnotify import DirectNotifyGlobal
from toontown.toonbase.ToontownModules import NodePath
from otp.level import BasicEntities
from direct.task import Task
from toontown.toonbase import ToontownGlobals
from toontown.coghq import BattleBlocker
import random
from math import *


def circleX(angle, radius, centerX, centerY):
    x = radius * cos(angle) + centerX
    return x

def circleY(angle, radius, centerX, centerY):
    y = radius * sin(angle) + centerY
    return y

def getCirclePoints(segCount, centerX, centerY, radius, wideX= 1.0, wideY = 1.0):
    returnShape = []
    for seg in range(0, int(segCount)):
        coordX = wideX * (circleX(((pi * 2.0) * float(float(seg) / float(segCount))), radius, centerX, centerY))
        coordY = wideY * (circleY(((pi * 2.0) * float(float(seg) / float(segCount))), radius, centerX, centerY))
        returnShape.append((coordX, coordY, 1))

    coordX =  wideX * (circleX(((pi * 2.0) * float(0 / segCount)), radius, centerX, centerY))
    coordY =  wideY * (circleY(((pi * 2.0) * float(0 / segCount)), radius, centerX, centerY))
    returnShape.append((coordX, coordY, 1))
    return returnShape

class DistributedSecurityCamera(BasicEntities.DistributedNodePathEntity):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedSecurityCamera')

    laserFieldModels = ['phase_9/models/cogHQ/square_stomper',]

    def __init__(self, cr):
        #print("start Init")
        BasicEntities.DistributedNodePathEntity.__init__(self, cr)

        node = hidden.attachNewNode('DistributedNodePathEntity')

        self.trackBeamGN = None
        self.trackFloorGN = None
        self.trackX = 10.0
        self.trackY = -5.0
        self.radius = 5.0
        self.trackShape = []
        self.trackShape = getCirclePoints(7, 0.0, 0.0, self.radius)

        self.trackShapeFloor = []
        self.trackShapeFloor = getCirclePoints(16, 0.0, 0.0, self.radius)
        
        self.light = None
        self.lightFollowPath = None

        self.zFloat = 0.05

        self.projector = Point3(0,0,25)

        self.isToonIn = 0
        self.toonX = 0
        self.toonY = 0

        self.canDamage = 1

        self.accel = 0.5
        self.maxVel = 1.0
        self.vX = 0.0
        self.vY = 0.0
        self.targetX = self.trackX
        self.targetY = self.trackY
        self.target = 0

        self.trackTargetList = [None, None, None, None]

        self.lastTime = 0.0
        self.currentTime = 0.0
        self.delta = 0.0

        self.Norm = {}

        self.Norm['Red'] = 0.2
        self.Norm['Green'] = 0.2
        self.Norm['Blue'] = 0.2
        self.Norm['Alpha'] = 1.0

        self.Alert = {}

        self.Alert['Red']= 1.0
        self.Alert['Green']= 0.0
        self.Alert['Blue'] = 0.0
        self.Alert['Alpha'] = 1.0

        self.attackSound = loader.loadSfx("phase_9/audio/sfx/CHQ_GOON_tractor_beam_alarmed.mp3")
        self.onSound = loader.loadSfx("phase_11/audio/sfx/LB_camera_shutter_2.mp3")

        self.attackTrack = Parallel(SoundInterval(self.attackSound, node=self, volume=.8),
                                    SoundInterval(self.onSound, node=self, volume=.8))

        self.moveStartSound = loader.loadSfx("phase_11/audio/sfx/LB_laser_beam_on_2.mp3")
        self.moveStartTrack = Parallel(SoundInterval(self.moveStartSound, node=self, volume=.4))
        self.moveLoopSound = loader.loadSfx("phase_11/audio/sfx/LB_laser_beam_hum_2.mp3")
        self.moveLoopSound.setLoop()
        self.moveLoopTrack = Parallel(SoundInterval(self.moveLoopSound, node=self, volume=.4))
        self.moveStopSound = loader.loadSfx("phase_11/audio/sfx/LB_laser_beam_off_2.mp3")
        self.moveStopTrack = Parallel(SoundInterval(self.moveStopSound, node=self, volume=.4))

        self.taskName = None
        #print("end Init")


    def generateInit(self):
        self.notify.debug('generateInit')
        BasicEntities.DistributedNodePathEntity.generateInit(self)

    def generate(self):
        #print("start generate")
        self.notify.debug('generate')
        BasicEntities.DistributedNodePathEntity.generate(self)
        #print("end generate")


    def announceGenerate(self):
        #print("start announce generate")
        self.notify.debug('announceGenerate')
        BasicEntities.DistributedNodePathEntity.announceGenerate(self)
        # at this point all the entity attributes have been initialized
        # we can load the model now.

        self.trackBeamNode = self.attachNewNode("tracking Beam Node")
        self.trackBeamGN=GeomNode("tracking Beam")
        self.trackBeamNode.attachNewNode(self.trackBeamGN)
        self.trackBeamNode.setTransparency(TransparencyAttrib.MAlpha)
        self.trackBeamNode.setAttrib(ColorBlendAttrib.make(ColorBlendAttrib.MAdd))
        self.trackBeamNode.setTwoSided(False)
        self.trackBeamNode.setDepthWrite(False)

        self.trackFloorNode = self.attachNewNode("tracking floor Node")
        self.trackFloorGN=GeomNode("tracking Floor")
        self.trackFloorNode.attachNewNode(self.trackFloorGN)
        self.trackFloorNode.setTransparency(TransparencyAttrib.MAlpha)
        self.trackFloorNode.setAttrib(ColorBlendAttrib.make(ColorBlendAttrib.MAdd))
        self.trackFloorNode.setTwoSided(False)
        self.trackFloorNode.setDepthWrite(False)

        if not hasattr(self, "trackTarget1"):
            self.trackTarget1 = None
        else:
            self.trackTargetList[1] = self.trackTarget1
        if not hasattr(self, "trackTarget2"):
            self.trackTarget2 = None
        else:
            self.trackTargetList[2] = self.trackTarget2
        if not hasattr(self, "trackTarget3"):
            self.trackTarget3 = None
        else:
            self.trackTargetList[3] = self.trackTarget3

        self.loadModel()

        self.detectName = (("securityCamera %s") % (self.doId))
        #taskMgr.doMethodLater(0.1, self.__detect, self.detectName)
        #print("end announce generate")

    def initCollisionGeom(self):
        pass #overwritting battle blocker
        #import pdb; pdb.set_trace()

    def sendFail(self):
        #print("Bomb!!!")
        self.battleStart()
        self.sendUpdate('trapFire',[])

    def battleStart(self):
        pass
        #self.startBattle()

    def setTarget(self, targetHash):

        targetCount = targetHash % 3
        sanity = 10
        self.target = None
        while targetCount >= 0 and sanity > 0:
            sanity -= 1
            for index in range(1,4):
                if self.trackTargetList[index]:
                    if targetCount == 0:
                        self.target = self.trackTargetList[index]
                    targetCount -= 1
        #print("setting target %s %s" % (self.target, self.trackTargetList))

    def setTrackTarget1(self, targetId):
        #print("setTrackTarget1")
        self.trackTarget1 = targetId
        self.trackTargetList[1] = targetId

    def setTrackTarget2(self, targetId):
        #print("setTrackTarget2")
        self.trackTarget2 = targetId
        self.trackTargetList[2] = targetId

    def setTrackTarget3(self, targetId):
        #print("setTrackTarget3")
        self.trackTarget3 = targetId
        self.trackTargetList[3] = targetId

    def __detect(self, task):
        #print("detect beat")

        distance = self.getDistance(localAvatar)
        greaterDim = self.gridScaleX
        if self.gridScaleY > self.gridScaleX:
            greaterDim = self.gridScaleY

        if distance < (greaterDim * 1.6):
            if localAvatar.getPos(self)[0] > 0 \
                and localAvatar.getPos(self)[0] < self.gridScaleX \
                and localAvatar.getPos(self)[1] > 0 \
                and localAvatar.getPos(self)[1] < self.gridScaleY:
                self.__toonHit()
            else:
                if self.isToonIn:
                    self.isToonIn = 0
                    #self.genGrid()
                self.isToonIn = 0

        taskMgr.doMethodLater(0.1, self.__detect, self.detectName)
        return Task.done

    def __toonHit(self):
        #print("Toon Hit")

        posX = localAvatar.getPos(self)[0]
        posY = localAvatar.getPos(self)[1]
        tileX = int(posX / (self.gridScaleX / self.gridNumX))
        tileY = int(posY / (self.gridScaleY / self.gridNumY))
        #print("tile %s %s %s" % (tileX, tileY, self.gridData[tileX][tileY]))
        if (self.toonX != tileX or self.toonY != tileY) or (not self.isToonIn):
            self.toonX = tileX
            self.toonY = tileY
            self.isToonIn = 1
            if self.gridData[tileX][tileY] < len(self.gridSymbols):
                tileFunction = self.gridSymbols[self.gridData[tileX][tileY]][0]
                if tileFunction:
                    tileFunction()
            self.sendHit()
            #self.genGrid()
        self.isToonIn = 1

    def sendHit(self):
        self.sendUpdate('hit', [self.toonX, self.toonY])

    def disable(self):
        self.notify.debug('disable')
        if self.moveLoopTrack.isPlaying():
            self.moveLoopTrack.finish()
        if self.attackTrack.isPlaying():
            self.attackTrack.finish()
        if self.moveStartTrack.isPlaying():
            self.moveStartTrack.finish()
        if self.moveStopTrack.isPlaying():
            self.moveStopTrack.finish()
            
        if self.light:
            base.removeDynamicLight(self.light)
            self.light = None
            
        # stop things
        self.ignoreAll()
        taskMgr.remove(self.detectName)

        BasicEntities.DistributedNodePathEntity.disable(self)

    def delete(self):
        self.notify.debug('delete')
        # unload things
        self.unloadModel()
        if self.taskName:
            taskMgr.remove(self.taskName)
        BasicEntities.DistributedNodePathEntity.delete(self)

    def loadModel(self):
        self.rotateNode = self.attachNewNode('rotate')
        self.model = loader.loadModel(self.laserFieldModels[self.modelPath])
        self.model.reparentTo(self.rotateNode)
        self.model.setPos(0,1,0)
        self.taskName = 'securityCameraupdate %s' % self.doId

        taskMgr.add(self.__updateTrack, self.taskName, priority=25)


    def unloadModel(self):
        if self.model:
            self.model.removeNode()
            del self.model
            self.model = None

    def __updateTrack(self, task):
        if self.target and self.level and hasattr(self.level, "entities"):
            thing = self.level.entities.get(self.target, None)
            self.targetX = thing.getPos(self)[0]
            self.targetY = thing.getPos(self)[1]
        else:
            return Task.cont

        self.rotateNode.setPos(self.projector)
        self.rotateNode.lookAt(Point3(self.trackX, self.trackY, 0.0))

        #print("target:%s x:%s y:%s track x:%s y:%s" % (self.target, self.targetX, self.targetY, self.trackX, self.trackY))

        #movement
        dt = globalClock.getDt()
        deccel = 1.0 - 1.0 * (dt * 7.0)
        if (deccel < 0):
            deccel = 0.0

        self.dirX = 0.0
        self.dirY = 0.0
        distX = self.targetX - self.trackX
        distY = self.targetY - self.trackY
        trigDist = math.sqrt(distX * distX + distY * distY)
        totalDist = abs(distX) + abs(distY) # I know this is ignoring trig but it'll work out, trust me
        propX = abs(distX) / (totalDist + 0.01)
        propY = abs(distY) / (totalDist + 0.01)
        #direction
        if self.targetX != self.trackX:
            self.dirX = (distX) / abs(distX)
        if self.targetY != self.trackY:
            self.dirY = (distY) / abs(distY)
        #accel
        if trigDist < ((self.radius * 0.5) + 1.0):
            self.vX = self.vX * deccel
            self.vY = self.vY * deccel
            self.moveStopTrack.start()
            self.moveLoopTrack.finish()
        else:
            if not self.moveLoopTrack.isPlaying():
                self.moveLoopTrack.start()
                self.moveStartTrack.start()
            self.vX += self.dirX * self.accel * propX
            self.vY += self.dirY * self.accel * propY

        #if abs(distX) < ((self.radius * 0.5) + 1.0):#abs(self.vX + 1.0):
        #    #print("dist %s rad %s" % (distX, self.radius))
        #    self.vX = self.vX * deccel# - self.vX * 1.0 * deccel
        #else:
        #    self.vX += self.dirX * self.accel * propX
        #if abs(distY) < ((self.radius * 0.5) + 1.0):#abs(self.vY + 1.0):
        #    #print("dist %s rad %s" % (distY, self.radius))
        #    self.vY = self.vY * deccel# - self.vY * 1.0 * deccel
        #else:
        #    self.vY += self.dirY * self.accel * propY
        #limits
        if self.vX > self.maxVel:
            self.vX = self.maxVel
        if self.vX < -self.maxVel:
            self.vX = -self.maxVel

        if self.vY > self.maxVel:
            self.vY = self.maxVel
        if self.vY < -self.maxVel:
            self.vY = -self.maxVel
        #apply
        self.trackX += self.vX * dt
        self.trackY += self.vY * dt
        #end movement

        self.genTrack()
        dist = self.getDist(base.localAvatar)
        if (dist < self.radius) and self.canDamage:
            self.canDamage = 0
            self.sendUpdate('trapFire',[])
            taskMgr.doMethodLater(2.0, self._resetDam, "reset Damage")
            self.attackTrack.start()
        return Task.cont
        #return Task.done

    def _resetDam(self, task = None):
        self.canDamage = 1

    def getDist(self, thing):
        posTX = thing.getX()
        posTY = thing.getY()
        dx = thing.getPos(self)[0] - self.trackX
        dy = thing.getPos(self)[1] - self.trackY
        return sqrt(dx*dx + dy*dy)


    def genTrack(self):
        beamRed = 0.0
        beamGreen = 0.0
        beamBlue = 0.0
        beamAlpha = 1.0

        origin = {}

        origin['Red'] = 0.2
        origin['Green'] = 0.2
        origin['Blue'] = 0.2
        origin['Alpha'] = 1.0

        if self.canDamage:
            origin = self.Norm
        else:
            origin = self.Alert
            
        dist = self.getDist(base.localAvatar)
        draw = 1.0 / (0.01 + float(pow(dist, 0.4)))

        wideX = 1 # + abs((self.trackX + self.projector[0]) / self.projector[2])
        wideY = 1 # + abs((self.trackY + self.projector[1]) / self.projector[2])
        
        self.trackShape = []
        self.trackShape = getCirclePoints(5 + (draw * 12.0), 0.0, 0.0, self.radius, wideX, wideY)

        self.trackShapeFloor = []
        self.trackShapeFloor = getCirclePoints(5 + (draw * 50.0), 0.0, 0.0, self.radius, wideX, wideY)

        if self.trackBeamGN:
            self.trackBeamGN.removeAllGeoms()
        if self.trackFloorGN:
            self.trackFloorGN.removeAllGeoms()

        gFormat = GeomVertexFormat.getV3cp()
        trackBeamVertexData = GeomVertexData("holds my vertices", gFormat, Geom.UHDynamic)
        trackBeamVertexWriter = GeomVertexWriter(trackBeamVertexData, "vertex")
        trackBeamColorWriter = GeomVertexWriter(trackBeamVertexData, "color")

        trackBeamVertexWriter.addData3f(self.projector[0], self.projector[1], self.projector[2]) #origin
        trackBeamColorWriter.addData4f(origin['Red'], origin['Green'], origin['Blue'], origin['Alpha'])
        
        for vertex in self.trackShape:
            trackBeamVertexWriter.addData3f(self.trackX + vertex[0] , self.trackY + vertex[1] , self.zFloat)
            trackBeamColorWriter.addData4f(beamRed, beamGreen, beamBlue, beamAlpha)
            
        del trackBeamVertexWriter
        del trackBeamColorWriter
        
        self.trackBeamTris = GeomTrifans(Geom.UHStatic) # triangle obejcet

        sizeTrack = len(self.trackShape)
        self.trackBeamTris.addVertex(0)
        for countVertex in range(1, sizeTrack + 1):
            self.trackBeamTris.addVertex(countVertex)
        self.trackBeamTris.addVertex(1)
        self.trackBeamTris.closePrimitive()

        self.trackBeamGeom = Geom(trackBeamVertexData)
        self.trackBeamGeom.addPrimitive(self.trackBeamTris)
        self.trackBeamGN.addGeom(self.trackBeamGeom)
        
        if ConfigVariableBool('want-lighting-effects', True).getValue():
            if not self.light:
                self.lightFollowPath = NodePath("lightPath")
                self.lightFollowPath.reparentTo(self)

                light = qpLight(qpLight.TSpot)
                light.setAttenuation(1, 0, 0)
                light.setCullRadius(256)
                light.setInnerCone(7.8)
                light.setOuterCone(8)
            else:
                light = self.light
            
            light.setPos(self.rotateNode.getPos(base.render))
            light.setHpr(self.rotateNode.getHpr(base.render))
            
            light.setColorSrgb255Scalar(Vec4(origin['Red'] * 255, origin['Green'] * 255, origin['Blue'] * 255, origin['Alpha'] * 38250))

            if not self.light:
                self.light = light
                base.addDynamicLight(self.light, followParent=self.lightFollowPath)

            return

        trackFloorVertexData = GeomVertexData("holds my vertices", gFormat, Geom.UHDynamic)
        trackFloorVertexWriter = GeomVertexWriter(trackFloorVertexData, "vertex")
        trackFloorColorWriter = GeomVertexWriter(trackFloorVertexData, "color")

        #trackFloorVertexWriter.addData3f(self.projector[0] + 4.0, self.projector[1] + 10.0, self.projector[2])
        trackFloorVertexWriter.addData3f(self.trackX, self.trackY, self.zFloat) #center
        trackFloorColorWriter.addData4f(origin['Red'], origin['Green'], origin['Blue'], origin['Alpha'])

        for vertex in self.trackShapeFloor:
            trackFloorVertexWriter.addData3f(self.trackX + vertex[0] , self.trackY + vertex[1] , self.zFloat)
            trackFloorColorWriter.addData4f(origin['Red'], origin['Green'], origin['Blue'], origin['Alpha'])
            
        del trackFloorVertexWriter
        del trackFloorColorWriter

        self.trackFloorTris = GeomTrifans(Geom.UHStatic) # triangle obejcet
                
        sizeTrack = len(self.trackShapeFloor)
        self.trackFloorTris.addVertex(0)
        for countVertex in range(1, sizeTrack + 1):
            self.trackFloorTris.addVertex(countVertex)
        self.trackFloorTris.addVertex(1)
        self.trackFloorTris.closePrimitive()
    
        self.trackFloorGeom = Geom(trackFloorVertexData)
        self.trackFloorGeom.addPrimitive(self.trackFloorTris)
        self.trackFloorGN.addGeom(self.trackFloorGeom)


    def setProjector(self, projPoint):
        #print("settingProjector")
        self.projector = projPoint
        if self.trackBeamGN and self.trackFloorGN:
            self.genTrack()

    def setHideModel(self, flag):
        if flag:
            self.model.stash()
        else:
            self.model.unstash()