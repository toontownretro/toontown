from . import DistributedElevator
from . import DistributedBossElevator
from .ElevatorConstants import *
from direct.directnotify import DirectNotifyGlobal
from toontown.toonbase import TTLocalizer

class DistributedVPElevator(DistributedBossElevator.DistributedBossElevator):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedVPElevator')

    def __init__(self, cr):
        DistributedBossElevator.DistributedBossElevator.__init__(self, cr)
        self.type = ELEVATOR_VP
        self.countdownTime = ElevatorData[self.type]['countdown']

    def setupElevator(self):
        """setupElevator(self)
        Called when the building doId is set at construction time,
        this method sets up the elevator for business.
        """
        self.elevatorModel = loader.loadModel(
            "phase_9/models/cogHQ/cogHQ_elevator")

        # The big cog icon on the top is only visible at the BossRoom.
        icon = self.elevatorModel.find('**/big_frame/')
        icon.hide()
        
        self.leftDoor = self.elevatorModel.find("**/left-door")
        self.rightDoor = self.elevatorModel.find("**/right-door")
        
        geom = base.cr.playGame.hood.loader.geom
        locator = geom.find("**/elevator_locator")
        self.elevatorModel.reparentTo(locator)
        self.elevatorModel.setH(180)
        
        DistributedElevator.DistributedElevator.setupElevator(self)

    def getDestName(self):
        return TTLocalizer.ElevatorSellBotBoss
