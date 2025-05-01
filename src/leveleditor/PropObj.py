"""
ToonTown Prop object
"""

from .ToonTownObj import *

class PropObj(ToonTownObj):
    def __init__(self, editor, propType, dna=None, nodePath=None, nameStr=None):
        self.propType = propType
        if nameStr:
            self._name = nameStr
        else:
            self._name = self.propType + '_DNARoot'
        ToonTownObj.__init__(self, editor, dna, nodePath)

    def initDNA(self):
        dnaNode = DNAProp(self._name)
        dnaNode.setCode(self.propType)
        dnaNode.setPos(VBase3(0))
        dnaNode.setHpr(VBase3(0))
        return dnaNode
