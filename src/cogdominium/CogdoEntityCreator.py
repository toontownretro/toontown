from otp.level import EntityCreator
from toontown.cogdominium import CogdoCraneGameConsts
from toontown.cogdominium.CogdoLevelMgr import CogdoLevelMgr
from toontown.cogdominium import CogdoBoardroomGameConsts
from toontown.cogdominium import CogdoCraneGameConsts

class CogdoEntityCreator(EntityCreator.EntityCreator):
    def __init__(self, level):
        EntityCreator.EntityCreator.__init__(self, level)

        # create short aliases for EntityCreator create funcs
        nothing = EntityCreator.nothing
        nonlocalEnt = EntityCreator.nonlocalEnt

        self.privRegisterTypes({
            'levelMgr': CogdoLevelMgr,
            'cogdoBoardroomGameSettings': Functor(self._createCogdoSettings, CogdoBoardroomGameConsts.Settings),
            'cogdoCraneGameSettings': Functor(self._createCogdoSettings, CogdoCraneGameConsts.Settings),
            'cogdoCraneCogSettings': Functor(self._createCogdoSettings, CogdoCraneGameConsts.CogSettings),
            })

    def _createCogdoSettings(self, ent, level, entId):
        #CogdoCraneGameConsts.Settings.initializeEntity(level, entId)
        #return CogdoCraneGameConsts.Settings
        ent.initializeEntity(level, entId)
        return ent
