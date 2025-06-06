from toontown.toonbase.ToontownModules import Point3
from direct.directnotify import DirectNotifyGlobal
from . import HoodDataAI
from toontown.toonbase import ToontownGlobals
from toontown.coghq import DistributedCogHQDoorAI
from toontown.building import DistributedDoorAI
from toontown.building import DoorTypes
from toontown.coghq import LobbyManagerAI
from toontown.building import DistributedBossElevatorAI
from toontown.suit import DistributedBossbotBossAI
from toontown.building import DistributedBBElevatorAI
from toontown.building import DistributedBoardingPartyAI
from toontown.building import FADoorCodes
from toontown.coghq import DistributedCogKartAI
from toontown.toonbase.ToontownModules import ConfigVariableBool

class BossbotHQDataAI(HoodDataAI.HoodDataAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("BossbotHQDataAI")

    def __init__(self, air, zoneId = None):
        """Create BossbotHQDataAI."""
        self.notify.debug("__init__: zoneId:%s" % zoneId)
        hoodId = ToontownGlobals.BossbotHQ
        if zoneId == None:
            zoneId = hoodId
        HoodDataAI.HoodDataAI.__init__(self, air, zoneId, hoodId)
        self.cogKarts = []

    def startup(self):
        """Start the BossbotHQ zone."""
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

        # Lobby elevator
        self.lobbyMgr = LobbyManagerAI.LobbyManagerAI(self.air, DistributedBossbotBossAI.DistributedBossbotBossAI)
        self.lobbyMgr.generateWithRequired(ToontownGlobals.BossbotLobby)
        self.addDistObj(self.lobbyMgr)

        self.lobbyElevator = DistributedBBElevatorAI.DistributedBBElevatorAI(self.air, self.lobbyMgr, ToontownGlobals.BossbotLobby, antiShuffle = 1) # antiShufflePOI
        self.lobbyElevator.generateWithRequired(ToontownGlobals.BossbotLobby)
        self.addDistObj(self.lobbyElevator)

        if ConfigVariableBool('want-boarding-groups', 1).getValue():
            self.boardingParty = DistributedBoardingPartyAI.DistributedBoardingPartyAI(self.air, [self.lobbyElevator.doId], 8)
            self.boardingParty.generateWithRequired(ToontownGlobals.BossbotLobby)
        #self.addDistObj(self.boardingParty)



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
        makeDoor(ToontownGlobals.BossbotLobby, 0, 0, FADoorCodes.BB_DISGUISE_INCOMPLETE)
        # Plaza -> Office
        #makeDoor(ToontownGlobals.LawbotOfficeExt, 0, 0)

        kartIdList = self.createCogKarts()
        if ConfigVariableBool('want-boarding-groups', 1).getValue():
            self.courseBoardingParty = DistributedBoardingPartyAI.DistributedBoardingPartyAI(self.air, kartIdList, 4)
            self.courseBoardingParty.generateWithRequired(self.zoneId)

    def createCogKarts(self):
        """Create the AI Cog karts."""
        posList = ( (154.762, 37.169, 0), (141.403, -81.887,0), (-48.44, 15.308,0) )
        hprList = ( (110.815, 0, 0), (61.231, 0,0), (-105.481,0,0) )
        mins = ToontownGlobals.FactoryLaffMinimums[3]
        kartIdList = []
        for cogCourse in range(len(posList)):
            pos = posList[cogCourse]
            hpr = hprList[cogCourse]
            cogKart = DistributedCogKartAI.DistributedCogKartAI(self.air, cogCourse,
                                                                pos[0], pos[1], pos[2],
                                                                hpr[0], hpr[1], hpr[2],
                                                                self.air.countryClubMgr, minLaff=mins[cogCourse])
            cogKart.generateWithRequired(self.zoneId)
            self.cogKarts.append(cogKart)
            kartIdList.append(cogKart.doId)
        return kartIdList
