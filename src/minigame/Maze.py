"""Maze module: contains the Maze class"""
from .MazeBase import MazeBase

from . import MazeData

class Maze(MazeBase):
    def __init__(self, mapName, mazeData = MazeData.mazeData, cellWidth = MazeData.CELL_WIDTH):
        model = loader.loadModel(mapName)
        mData = mazeData[mapName]

        self.treasurePosList = mData["treasurePosList"]
        self.numTreasures = len(self.treasurePosList)
        MazeBase.__init__(self, model, mData, cellWidth)
