#-------------------------------------------------------------------------------
# Contact: X (Schell Games)
# Created: X, 2010
#
# Purpose: AI, handles the spawning, collection of barrels, and score setting
#------------------------------------------------------------------------------

import random
#from sets import Set

from direct.directnotify import DirectNotifyGlobal
from direct.distributed import DistributedObjectAI
from direct.showbase import PythonUtil
from direct.task import Timer
from direct.task.Task import Task

from toontown.toonbase import ToontownGlobals

from toontown.cogdominium import CogdoBarrelRoomConsts
from toontown.cogdominium import DistributedCogdoBarrelAI

class CogdoBarrelRoomAI:
    notify = DirectNotifyGlobal.directNotify.newCategory(
        'DistributedCogdoBarrelRoomAI')

    def __init__(self, cogdoInteriorAI):
        self.cogdoInteriorAI = cogdoInteriorAI
        
        # Setup task names
        self.allBarrelsCollectedTask = self.cogdoInteriorAI.taskName('allBarrelsCollectedTask')
        self.collectionDoneEvent = self.cogdoInteriorAI.taskName('barrelCollectionDone')
        
        # Setup a timer for collection
        self.collectTimer = None
        
        # Track toonIds and laff
        self.results = [[], [],]
        
        # Check each player slot
        for i in range(CogdoBarrelRoomConsts.MaxToons):
            
            # If a player exists get their Id
            if i < len(self.cogdoInteriorAI.toons):
                self.results[0].append(self.cogdoInteriorAI.toons[i])
            # If no player exists set the Id to 0
            else:
                self.results[0].append(0)
            
            # Set laff to 0
            self.results[1].append(0)

        # Spawn barrels
        self.spawnedBarrels = []
        self.__spawnBarrels()

    def destroy(self):
        """
        Cleans up the barrel room
        """
        # Stop any collection tasks
        taskMgr.remove(self.allBarrelsCollectedTask)
        
        # Stop the timer
        if self.collectTimer:
            self.collectTimer.stop()
            self.collectTimer = None

        # Remove all barrels
        for barrel in self.spawnedBarrels:
            barrel.requestDelete()

        # Reset the barrel list
        self.spawnedBarrels = []

    def __spawnBarrels(self):
        """
        Sets spawned barrels
        """
        self.spawnedBarrels = []

        def spawnBarrel(index):
            """
            Spawns barrels
            """
            # Create a barrel with a callback to barrelCollected
            barrel = DistributedCogdoBarrelAI.DistributedCogdoBarrelAI(self.cogdoInteriorAI.air, index, self.barrelCollected)
            barrel.generateWithRequired(self.cogdoInteriorAI.zoneId)
            self.spawnedBarrels.append(barrel)

        for i in range(CogdoBarrelRoomConsts.numBarrels()):
            spawnBarrel(i)

    def reset(self):
        """
        Hides all barrels and sets all players score to 0
        """
        # Hide the barrels
        for barrel in self.spawnedBarrels:
            barrel.d_setState(CogdoBarrelRoomConsts.StateHidden)
        
        # Set everyone's score to 0
        for i in range(CogdoBarrelRoomConsts.MaxToons):
            self.results[1][i] = 0

    def activate(self):
        """
        Starts the barrel collection phase
        """
        # Add a timer
        self.collectTimer = Timer.Timer()
        self.collectTimer.startCallback(CogdoBarrelRoomConsts.CollectionTime, self.__endCollectionPhase)
        
        # Make barrels obtainable
        for barrel in self.spawnedBarrels:
            barrel.interactive = True

        # Remove any previous barrel tasks
        taskMgr.remove(self.allBarrelsCollectedTask)
        
        # Add a new to check to see if all barrels were collected
        taskMgr.doMethodLater(CogdoBarrelRoomConsts.AllBarrelsCollectedTime, self.__checkAllBarrelsCollected, self.allBarrelsCollectedTask)

    def __endCollectionPhase(self):
        """
        Stops the barrel collection phase
        """
        messenger.send(self.collectionDoneEvent)

    def deactivate(self):
        """
        Stops the timer and disables barrel collection
        """
        # Stop the timer
        if self.collectTimer:
            self.collectTimer.stop()
            self.collectTimer = None
       
        # Make the barrels unobtainable
        for barrel in self.spawnedBarrels:
            barrel.interactive = False

    def setScore(self, score):
        """
        Sets how many barrels can be collected based on game score
        """
        # Calculates the number of good barrels based on the score
        numGood = int(score * (CogdoBarrelRoomConsts.numBarrels() + 0.5))
        
        # Randomize which barrel gets what state
        random.shuffle(self.spawnedBarrels)
        
        # Give each barrel a specific state
        for i in range(len(self.spawnedBarrels)):
            if i < numGood:
                # Barrel can be collected
                state = CogdoBarrelRoomConsts.StateAvailable
            else:
                # Barrel is crushed and cannot be collected
                state = CogdoBarrelRoomConsts.StateCrushed
            
            # Set the barrels
            self.spawnedBarrels[i].d_setState(state)

    def barrelCollected(self, barrel, avId):
        """
        Detects barrel collection
        """
        # Find the player who collect a barrel
        try:
            
            # If found add the laff they regained to the reward
            playerIndex = self.results[0].index(avId)
            self.results[1][playerIndex] += barrel.laff
        
        # If the avatar Id isn't found, print out a warning
        except ValueError:
            self.notify.warning('barrelCollected: Unrecognized avId %s' % avId)

    def __checkAllBarrelsCollected(self, task):
        """
        Check if all barrels have been collected
        """
        # If enabled it will move to the next phase once all barrels are collected
        if not CogdoBarrelRoomConsts.EndWithAllBarrelsCollected:
            return
        
        # All barrels were collected, move on
        if self.__allBarrelsCollected():
            self.__endCollectionPhase()
        else:
            # There's still barrels left, check later
            return Task.again

    def __toonIdNeedsLaff(self, toonId):
        """
        Checks if a player needs healing
        """
        # Get their Id
        toon = self.cogdoInteriorAI.air.doId2do.get(toonId)
        # Returns true if the toon is not fully healed
        if toon != None:
            return not toon.isToonedUp()

    def __allBarrelsCollected(self):
        """
        Checks if all toons who need healing have collect the barrels
        Returns true if all barrels were collected by them
        """
        # Check for any toon that still needs healing
        toonsNeedingLaff = set([
            toon for toon in self.cogdoInteriorAI.toons if self.__toonIdNeedsLaff(toon)])
        
        # Check if all spawned barrels have been collected by players who need health
        for barrel in self.spawnedBarrels:
            # If there are still players who need health, return false
            if not toonsNeedingLaff.issubset(set(barrel.grabbedBy)):
                return False

        # All barrels have been grabbed by those who need health
        return True

    def __str__(self):
        return str(self.cogdoInteriorAI) + '.CogdoBarrelRoomAI'
