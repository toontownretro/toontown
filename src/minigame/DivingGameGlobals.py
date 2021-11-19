# MazeGameGlobals.py: contains maze game stuff
# used by both AI and client

from toontown.toonbase import ToontownGlobals
from toontown.toonbase.ToontownModules import *

ENDLESS_GAME = ConfigVariableBool('endless-maze-game', 0).getValue()
NUM_SPAWNERS = 6
GAME_DURATION = 60.

CollideMask = ToontownGlobals.CatchGameBitmask
