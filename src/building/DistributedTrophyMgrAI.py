
from direct.distributed import DistributedObjectAI
from direct.directnotify import DirectNotifyGlobal
from toontown.toonbase import TTLocalizer

class DistributedTrophyMgrAI(DistributedObjectAI.DistributedObjectAI):

    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedTrophyMgrAI')

    def __init__(self, air):
        DistributedObjectAI.DistributedObjectAI.__init__(self, air)
        # Dict of avId : score
        self.trophyDict = {}
        # Dict of avId : name since it is hard to query av names
        self.nameDict = {}
        # How many leaders do we want to keep track of?
        self.maxLeaders = 10
        self.__leaders = []
        self.__leaderScores = []
        self.__leaderAvIds = []
        self.__leaderNames = []
        self.__minLeaderScore = 0

    def getTrophyScore(self, avId):
        # Returns the trophy score for a particular avatar.
        return self.trophyDict.get(avId, 0)

    def requestTrophyScore(self):
        # This message is sent from a client wanting to be told his
        # own trophy score.
        avId = self.air.getAvatarIdFromSender()
        av = self.air.doId2do.get(avId)
        if av:
            av.d_setTrophyScore(self.getTrophyScore(avId))

    def recomputeLeaders(self, avId, score):
        """
        Computes a list of score,avId pairs in sorted order, highest first
        """
        # Make a copy so we can manipulate it
        i = [list(t) for t in list(self.trophyDict.items())]
            
        # Recompute only if the score is greater than the lowest score
        # or if there are less than 10 players in the list
        if ((score > self.__minLeaderScore) or (len(i) < 10)):        
            # Reverse the items so we have score first
            list([r.reverse() for r in i])
            # Sort by score
            i.sort()
            # Reverse that score so highest are first
            i.reverse()
            # Truncate the leaders to the max
            # TODO: what about a tie?
            self.__leaders = i[:self.maxLeaders]
            
            # Keep some side tracking variables as an optimization so we
            # do not need to compute them every time.
            self.__leaderScores = [t[0] for t in self.__leaders]
            self.__minLeaderScore = min(self.__leaderScores)
            self.__leaderAvIds = [t[1] for t in self.__leaders]
            self.__leaderNames = [self.nameDict[avId] for avId in self.__leaderAvIds]
    
            self.notify.debug("recomputed leaders:\n leaderScores: %s\n leaderAvIds: %s\n leaderNames: %s" %
                              (self.__leaderScores, self.__leaderAvIds, self.__leaderNames))
            
            # Yep, it changed (well, most likely changed)
            return True
        
        else:
            return False

    def getLeaderInfo(self):
        return self.__leaderAvIds, self.__leaderNames, self.__leaderScores

    def getScoreFromNumFloors(self, numFloors):
        # Based on the number of floors from this building, compute
        # the trophy score received
        return numFloors

    def addTrophy(self, avId, name, numFloors):
        addedScore = self.getScoreFromNumFloors(numFloors)
        score = self.getTrophyScore(avId) + addedScore
        self.trophyDict[avId] = score
        self.nameDict[avId] = name
        if self.recomputeLeaders(avId, score):
            # Send a message to the DistributedHQInteriorAIs to update
            # their leaderboards
            messenger.send("leaderboardChanged")
        self.notify.debug("addTrophy: %s avId: %s" % (addedScore, avId))
        av = self.air.doId2do.get(avId)
        if av:
            av.d_setTrophyScore(score)
        self.air.writeServerEvent(
            'trophy', avId, "%s|%s" % (score, addedScore))

    def removeTrophy(self, avId, numFloors):
        if avId in self.trophyDict:
            removedScore = self.getScoreFromNumFloors(numFloors)
            score = self.getTrophyScore(avId) - removedScore
            self.trophyDict[avId] = score
            if self.recomputeLeaders(avId, score):
                # Send a message to the DistributedHQInteriorAIs to update
                # their leaderboards
                messenger.send("leaderboardChanged")
            self.notify.debug("removeTrophy: %s avId: %s" % (removedScore, avId))

            # Whisper to the avatar to let them know their precious trophy is gone
            av = self.air.doId2do.get(avId)
            if av:
                av.d_setSystemMessage(0, TTLocalizer.RemoveTrophy)
                av.d_setTrophyScore(self.trophyDict[avId])
            
            if self.trophyDict[avId] <= 0:
                del self.trophyDict[avId]
                del self.nameDict[avId]
                self.notify.debug("removeTrophy avId: %s removed from dict" % avId)
            self.air.writeServerEvent(
                'trophy', avId, "%s|%s" % (score, -removedScore))
        else:
            # This should not happen
            self.notify.warning("Tried to remove a trophy from avId: %s that has no trophies" % avId)

    def getSortedScores(self):
        """
        Returns a list of score,avId pairs in sorted order, highest first
        """
        i = [list(t) for t in list(self.trophyDict.items())]
        list([r.reverse() for r in i])
        i.sort()
        i.reverse()
        return i
