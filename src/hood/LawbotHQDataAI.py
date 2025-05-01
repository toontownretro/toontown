from direct.directnotify import DirectNotifyGlobal
from . import HoodDataAI
from toontown.toonbase import ToontownGlobals
from toontown.coghq import DistributedLawOfficeElevatorExtAI
from toontown.coghq import DistributedCogHQDoorAI
from toontown.building import DistributedDoorAI
from toontown.building import DoorTypes
from toontown.coghq import LobbyManagerAI
from toontown.building import DistributedBossElevatorAI
from toontown.suit import DistributedLawbotBossAI
from toontown.building import DistributedCJElevatorAI
from toontown.building import FADoorCodes
from toontown.building import DistributedBoardingPartyAI
from toontown.toonbase.ToontownModules import ConfigVariableBool

class LawbotHQDataAI(HoodDataAI.HoodDataAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("LawbotHQDataAI")

    def __init__(self, air, zoneId = None):
        self.notify.debug("__init__: zoneId:%s" % zoneId)
        hoodId = ToontownGlobals.LawbotHQ
        if zoneId == None:
            zoneId = hoodId
        HoodDataAI.HoodDataAI.__init__(self, air, zoneId, hoodId)

    def startup(self):
        HoodDataAI.HoodDataAI.startup(self)

        # TODO: define these in a more modular way
        def makeOfficeElevator(index, antiShuffle = 0, minLaff = 0):
            destZone = (
                ToontownGlobals.LawbotStageIntA,
                ToontownGlobals.LawbotStageIntB,
                ToontownGlobals.LawbotStageIntC,
                ToontownGlobals.LawbotStageIntD,)[index]
            elev = DistributedLawOfficeElevatorExtAI.DistributedLawOfficeElevatorExtAI(self.air,
                                                                                       self.air.lawMgr,
                                                                                       destZone, index, antiShuffle = 0, minLaff= minLaff)#antiShufflePOI
            elev.generateWithRequired(ToontownGlobals.LawbotOfficeExt)
            self.addDistObj(elev)
            return elev.doId

        mins = ToontownGlobals.FactoryLaffMinimums[2]
        officeId0 = makeOfficeElevator(0, 0, mins[0])
        officeId1 = makeOfficeElevator(1, 0, mins[1])
        officeId2 = makeOfficeElevator(2, 0, mins[2])
        officeId3 = makeOfficeElevator(3, 0, mins[3])

        # Lobby elevator
        self.lobbyMgr = LobbyManagerAI.LobbyManagerAI(self.air, DistributedLawbotBossAI.DistributedLawbotBossAI)
        self.lobbyMgr.generateWithRequired(ToontownGlobals.LawbotLobby)
        self.addDistObj(self.lobbyMgr)

        self.lobbyElevator = DistributedCJElevatorAI.DistributedCJElevatorAI(self.air, self.lobbyMgr, ToontownGlobals.LawbotLobby, antiShuffle = 1) # antiShufflePOI
        self.lobbyElevator.generateWithRequired(ToontownGlobals.LawbotLobby)
        self.addDistObj(self.lobbyElevator)

        if ConfigVariableBool('want-boarding-groups', 1).getValue():
            self.boardingParty = DistributedBoardingPartyAI.DistributedBoardingPartyAI(self.air, [self.lobbyElevator.doId], 8)
            self.boardingParty.generateWithRequired(ToontownGlobals.LawbotLobby)

        def makeDoor(destinationZone, intDoorIndex, extDoorIndex, lock=0):
            #set up both doors
            intDoor=DistributedCogHQDoorAI.DistributedCogHQDoorAI(
                self.air, 0, DoorTypes.INT_COGHQ,
                self.canonicalHoodId, doorIndex=intDoorIndex, lockValue=lock)
            intDoor.zoneId = destinationZone
            extDoor=DistributedCogHQDoorAI.DistributedCogHQDoorAI(
                self.air, 0, DoorTypes.EXT_COGHQ,
                destinationZone, doorIndex=extDoorIndex, lockValue=lock)

            #point them to each other
            extDoor.setOtherDoor(intDoor)
            intDoor.setOtherDoor(extDoor)

            #generate them
            intDoor.generateWithRequired(destinationZone)
            intDoor.sendUpdate("setDoorIndex", [intDoor.getDoorIndex()])
            self.addDistObj(intDoor)

            extDoor.generateWithRequired(self.canonicalHoodId)
            extDoor.sendUpdate("setDoorIndex", [extDoor.getDoorIndex()])
            self.addDistObj(extDoor)


        # CogHQ Main building -> Lobby doors
        makeDoor(ToontownGlobals.LawbotLobby, 0, 1, FADoorCodes.LB_DISGUISE_INCOMPLETE)
        # Plaza -> Office
        makeDoor(ToontownGlobals.LawbotOfficeExt, 0, 0)

        officeIdList = [officeId0, officeId1, officeId2, officeId3]
        if ConfigVariableBool('want-boarding-parties', 1).getValue():
            self.officeBoardingParty = DistributedBoardingPartyAI.DistributedBoardingPartyAI(self.air, officeIdList, 4)
            self.officeBoardingParty.generateWithRequired(ToontownGlobals.LawbotOfficeExt)

        """
        extDoor1=DistributedCogHQDoorAI.DistributedCogHQDoorAI(
            self.air, 1, DoorTypes.EXT_COGHQ,
            destinationZone, doorIndex=1)
        extDoor2=DistributedCogHQDoorAI.DistributedCogHQDoorAI(
            self.air, 2, DoorTypes.EXT_COGHQ,
            destinationZone, doorIndex=2)
        extDoor3=DistributedCogHQDoorAI.DistributedCogHQDoorAI(
            self.air, 3, DoorTypes.EXT_COGHQ,
            destinationZone, doorIndex=3)
        extDoorList = [extDoor0, extDoor1, extDoor2, extDoor3]

        # Store the lobby door list with the suit planner, so the
        # suits can open the doors as they walk through them.
        for sp in self.suitPlanners:
            if sp.zoneId == ToontownGlobals.LawbotHQ:
                sp.cogHQDoors = extDoorList
        """
