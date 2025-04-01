from direct.fsm.StatePush import FunctionCall
from otp.level.EntityStateVarSet import EntityStateVarSet
from otp.level.LevelSpec import LevelSpec

class CogdoLevelGameBase:

    def getLevelSpec(self):
        return LevelSpec(self.getSpec())

    if __dev__:

        def startHandleEdits(self):
            fcs = []
            # each attribute in the game settings entity can have a handler, e.g.
            # def _handleGameDurationChanged(self, gameDuration): ...
            Consts = self.getConsts()
            for item in list(Consts.__dict__.values()):
                if isinstance(item, EntityStateVarSet):
                    for attribName in item._getAttributeNames():
                        handler = getattr(self, '_handle%sChanged' % attribName, None)
                        if handler:
                            stateVar = getattr(item, attribName)
                            fcs.append(FunctionCall(handler, stateVar))
            self._functionCalls = fcs

        def stopHandleEdits(self):
            if __dev__:
                for fc in self._functionCalls:
                    fc.destroy()
                self._functionCalls = None

        def getEntityTypeReg(self):
            # return an EntityTypeRegistry with information about the
            # entity types that the crane game uses
            from . import CogdoEntityTypes
            from otp.level import EntityTypeRegistry
            typeReg = EntityTypeRegistry.EntityTypeRegistry(CogdoEntityTypes)
            return typeReg
