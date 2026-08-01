"""Maze module: contains the Maze class"""
from .MazeBase import MazeBase
from . import MazeData

# world space:
#
# +Y is up the screen
# +X is to the right
#
# tile space:
# +Y is up the screen
# +X is to the right

class Maze(MazeBase):
    def __init__(self, mapName, mazeData = MazeData.mazeData, cellWidth = MazeData.CELL_WIDTH):
        model = loader.loadModel(mapName)
        # get maze dimensions, boolean collision array
        mData = mazeData[mapName]
        self.treasurePosList = mData["treasurePosList"]
        self.numTreasures = len(self.treasurePosList)
        MazeBase.__init__(self, model, mData, cellWidth)
