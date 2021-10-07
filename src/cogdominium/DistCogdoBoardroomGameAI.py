from direct.directnotify.DirectNotifyGlobal import directNotify
from toontown.cogdominium.CogdoBoardroomGameBase import CogdoBoardroomGameBase
from toontown.cogdominium.DistCogdoLevelGameAI import DistCogdoLevelGameAI
from toontown.cogdominium import CogdoBoardroomGameConsts as Consts

class DistCogdoBoardroomGameAI(CogdoBoardroomGameBase, DistCogdoLevelGameAI):
    notify = directNotify.newCategory("DistCogdoBoardroomGameAI")

    def __init__(self, air, interior):
        DistCogdoGameAI.__init__(self, air, interior)

    def enterGame(self):
        DistCogdoGameAI.enterGame(self)
        # start the game up. Or wait for a while, that's fun too
        self._gameDoneEvent = taskMgr.doMethodLater(
            Consts.GameDuration.get(), self._gameDoneDL, self.uniqueName('boardroomGameDone'))

    def exitGame(self):
        taskMgr.remove(self._gameDoneEvent)
        self._gameDoneEvent = None

    def _gameDoneDL(self, task):
        self._handleGameFinished()
        return task.done

    def enterFinish(self):
        DistCogdoGameAI.enterFinish(self)
        self._finishDoneEvent = taskMgr.doMethodLater(
            Consts.FinishDuration.get(), self._finishDoneDL, self.uniqueName('boardroomFinishDone'))

    def exitFinish(self):
        taskMgr.remove(self._finishDoneEvent)
        self._finishDoneEvent = None

    def _finishDoneDL(self, task):
        self.announceGameDone()
        return task.done
