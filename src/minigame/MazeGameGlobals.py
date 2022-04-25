# MazeGameGlobals.py: contains maze game stuff
# used by both AI and client

from direct.showbase import RandomNumGen
from toontown.toonbase.ToontownModules import *

def getMazeName(gameDoId, numPlayers, mazeNames):
    try:
        return forcedMaze
    except:
        names = mazeNames[numPlayers-1]
        return names[RandomNumGen.randHash(gameDoId) % len(names)]

ENDLESS_GAME = ConfigVariableBool('endless-maze-game', 0).getValue()

GAME_DURATION = 60.
SHOWSCORES_DURATION = 2.

# each suit will be updated every N tics, where N can vary from suit to suit
SUIT_TIC_FREQ = int(256)
WALK_SAME_DIRECTION_PROB = 4
WALK_TURN_AROUND_PROB = 30
SUIT_START_POSITIONS = (
    (0.25, 0.25),
    (0.75, 0.75),
    (0.25, 0.75),
    (0.75, 0.25),
    (0.2, 0.5),
    (0.8, 0.5),
    (0.5, 0.2),
    (0.5, 0.8),
    (0.33, 0.),
    (0.66, 0.),
    (0.33, 1.),
    (0.66, 1.),
    (0., 0.33),
    (0., 0.66),
    (1., 0.33),
    (1., 0.66),
    )

#forcedMaze = 'phase_4/models/minigames/maze_2player'
