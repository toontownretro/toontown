from toontown.toonbase.ToontownModules import Quat
from toontown.toonbase.ToontownModules import OdeWorld, OdeSimpleSpace, OdeJointGroup, OdeUtil
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.ClockDelta import globalClockDelta

class MinigamePhysicsWorldBase:
    """Base class for both client and ai versions of minigame physics.

    Should not have any hardcoded info which is specific to a given game.
    """

    notify = DirectNotifyGlobal.directNotify.newCategory("MinigamePhysicsWorldBase")

    def __init__(self, canRender = 0):
        """Create the MinigamePhysicsWorldBase."""
        self.canRender = canRender

        #universal ODE stuff
        self.world = OdeWorld()
        self.space = OdeSimpleSpace()
        self.contactgroup = OdeJointGroup()

        # Items needed to render
        self.bodyList = [] # list of ODE bodies, or ode panda pairs if canRender
        self.geomList = []
        self.massList = []
        self.rayList = []

        self.showContacts = 0
        self.jointMarkers = []
        self.jointMarkerCount = 64

        self.meshDataList = []
        self.geomDataList = []
        self.commonObjectInfoDict = {}

        self.maxColCount = 0

        #items used to keep track on placement between ode and panda
        if self.canRender:
            self.odePandaRelationList = self.bodyList
            self.root = render.attachNewNode("physics root node")
            #self.worldAttach = render.attachNewNode("physics geom attach point")
        else:
            self.root = NodePath("physics root node")

        self.placerNode = self.root.attachNewNode("Placer")
        self.subPlacerNode = self.placerNode.attachNewNode("Placer Sub Node")

        #movable enviromnmental objects that need to be syncronized
        self.commonObjectDict = {}
        self.commonId = 0

        self.worldAttach = self.root.attachNewNode("physics geom attach point")

        self.timingCycleLength = 10.0
        self.timingCycleOffset = 0.0

        self.timingSimTime = 0.0
        self.FPS = 60.0
        self.DTAStep = 1.0 / self.FPS # in seconds, how much to increase per physics step
        self.DTA = 0

        self.useQuickStep = False # child classes can override this
        self.deterministic = True # child classes can override this
        self.numStepsInSimulateTask = 0

    def delete(self):
        """cleanup the MinigamePhysicsWorldBase."""
        self.notify.debug("Max Collision Count was %s" % (self.maxColCount))
        self.stopSim()
        self.commonObjectDict = None

        if self.canRender:
            for pair in self.odePandaRelationList:
                pair[0].remove()
                pair[1].destroy()
            self.odePandaRelationList = None
        else:
            for body in self.bodyList:
                body[1].destroy()
            self.bodyList = None

        for mass in self.massList:
            #mass.destroy()
            mass = None

        for geom in self.geomList:
            geom.destroy()
            geom = None

        for ray in self.rayList:
            ray.destroy()
            ray = None

        self.placerNode.remove()
        self.root.remove()

        for marker in self.jointMarkers:
            marker.remove()
        self.jointMarkers = None

        for data in self.geomDataList:
            data.destroy()

        for data in self.meshDataList:
            data.destroy()


        self.contactgroup.empty()
        self.world.destroy()
        self.space.destroy()
        self.world = None
        self.space = None

    def setupSimulation(self):
        """Meant to be overridden by the child classes.

        Include initializing the surface table, set gravity, etc.
        """
        if self.canRender:
            for count in range(self.jointMarkerCount):
                testMarker = render.attachNewNode("Joint Marker")
                ballmodel = loader.loadModel('phase_3/models/misc/sphere')
                ballmodel.reparentTo(testMarker)
                ballmodel.setScale(0.1)
                testMarker.setPos(0.0,0.0,-100.0)
                self.jointMarkers.append(testMarker)
        pass

    def startSim(self):
        """Start the real time physics simulation."""
        taskMgr.add(self.__simulationTask, "simulation task")

    def stopSim(self):
        """Stop the real time physics simulation."""
        taskMgr.remove("simulation task")

    def __simulationTask(self, task):
        """Simulate the world, multiple steps if needed."""
        self.DTA += globalClock.getDt()
        numSteps = int (self.DTA / self.DTAStep)
        #self.notify.debug('numSteps = %d' % numSteps)
        if numSteps > 10:
            self.notify.warning('phyics steps = %d' % numSteps)

        startTime = globalClock.getRealTime()

        while self.DTA >= self.DTAStep:
            if self.deterministic:
                OdeUtil.randSetSeed(0)
            self.DTA -= self.DTAStep
            self.preStep()
            self.simulate()
            self.postStep()

        if self.canRender:
            self.placeBodies()

        return task.cont

    def preStep(self):
        """Called before one physics steps"""
        pass

    def postStep(self):
        """Called after one physics step."""
        # mark the contact joints
        if self.showContacts and self.canRender:
            for count in range(self.jointMarkerCount):
                pandaNodePathGeom = self.jointMarkers[count]
                if count < self.colCount:
                    pandaNodePathGeom.setPos(self.space.getContactData((count *3) + 0), self.space.getContactData((count *3) + 1), self.space.getContactData((count *3) + 2))
                else:
                    pandaNodePathGeom.setPos(0.0,0.0,-100.0)
        pass


    def simulate(self):
        """Do one physics step."""
        self.colCount = self.space.autoCollide() # Detect collisions and create contact joints
        if self.colCount is None:
            self.colCount = 0
        if self.maxColCount < self.colCount:
            self.maxColCount = self.colCount
            self.notify.debug("New Max Collision Count %s" % (self.maxColCount))
        if self.useQuickStep:
            self.world.quickStep(self.DTAStep) # Simulate
        else:
            self.world.step(self.DTAStep) # Simulate

        #self.notify.debug('self.bodyList = %s' % self.bodyList)
        for bodyPair in self.bodyList:
            self.world.applyDampening(self.DTAStep, bodyPair[1])

        self.contactgroup.empty() # Remove all contact joints
        # self.commonObjectControl()
        self.timingSimTime = self.timingSimTime + self.DTAStep

    def placeBodies(self):
        """Make the nodePaths match up to the physics bodies."""
        for pair in self.odePandaRelationList:
            pandaNodePathGeom = pair[0]
            odeBody = pair[1]
            if pandaNodePathGeom:
                pandaNodePathGeom.setPos(odeBody.getPosition())
                # rotation = (odeBody.getRotation() * (180.0/math.pi))
                pandaNodePathGeom.setQuat(Quat(odeBody.getQuaternion()[0],odeBody.getQuaternion()[1],odeBody.getQuaternion()[2],odeBody.getQuaternion()[3]))


    def getOrderedContacts(self, count):
        """Return the two collide ids of a collision."""
        c0 = self.space.getContactId(count,0 )
        c1 = self.space.getContactId(count,1 )
        if c0 > c1:
            chold = c1
            c1 = c0
            c0 = chold
        return c0, c1
