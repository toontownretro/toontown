from direct.fsm.StatePush import StateVar
from otp.level.EntityStateVarSet import EntityStateVarSet
from toontown.cogdominium.CogdoEntityTypes import CogdoBoardroomGameSettings

# constants that can be modified by the IGE (~edit)
Settings = EntityStateVarSet(CogdoBoardroomGameSettings)
GameDuration = StateVar(60.0)
FinishDuration = StateVar(10.0)
