
from otp.ai.AIBaseGlobal import *
from toontown.toonbase.ToontownModules import *
from .DistributedNPCToonBaseAI import *

from . import ToonDNA
from direct.task.Task import Task
from toontown.ai import DatabaseObject
from toontown.estate import ClosetGlobals

class DistributedNPCTailorAI(DistributedNPCToonBaseAI):
    freeClothes = ConfigVariableBool('free-clothes', 0).getValue()
    housingEnabled = ConfigVariableBool('want-housing', 1).getValue()
    
    def __init__(self, air, npcId):
        DistributedNPCToonBaseAI.__init__(self, air, npcId)
        self.timedOut = 0
        # Tailors are not in the business of giving out quests
        self.givesQuests = 0
        self.customerDNA = None
        self.customerId = None
        self.customerTops = None
        self.customerBottoms = None

    def getTailor(self):
        return 1

    def delete(self):
        taskMgr.remove(self.uniqueName('clearMovie'))
        self.ignoreAll()
        self.customerDNA = None
        self.customerId = None
        self.customerTops = None
        self.customerBottoms = None
        DistributedNPCToonBaseAI.delete(self)

    def avatarEnter(self):
        avId = self.air.getAvatarIdFromSender()
        # this avatar has come within range
        assert self.notify.debug("avatar enter " + str(avId))

        if (avId not in self.air.doId2do):
            self.notify.warning("Avatar: %s not found" % (avId))
            return

        if (self.isBusy()):
            self.freeAvatar(avId)
            return

        # Store the original customer DNA so we can revert if a disconnect
        # happens
        av = self.air.doId2do[avId]
        self.customerDNA = ToonDNA.ToonDNA()
        self.customerDNA.makeFromNetString(av.getDNAString())
        self.customerTops = ToonDNA.getTops(self.customerDNA.getGender(), tailorId = self.npcId)
        self.customerBottoms = ToonDNA.getBottoms(self.customerDNA.getGender(), tailorId = self.npcId)
        self.customerId = avId
        av.b_setDNAString(self.customerDNA.makeNetString())

        # Handle unexpected exit
        self.acceptOnce(self.air.getAvatarExitEvent(avId),
                        self.__handleUnexpectedExit, extraArgs=[avId])

        flag = NPCToons.PURCHASE_MOVIE_START_BROWSE
        if self.freeClothes:
            flag = NPCToons.PURCHASE_MOVIE_START
            if self.housingEnabled and self.isClosetAlmostFull(av):
                flag = NPCToons.PURCHASE_MOVIE_START_NOROOM
        elif (self.air.questManager.hasTailorClothingTicket(av, self) == 1):
            flag = NPCToons.PURCHASE_MOVIE_START
            if self.housingEnabled and self.isClosetAlmostFull(av):
                flag = NPCToons.PURCHASE_MOVIE_START_NOROOM
        elif(self.air.questManager.hasTailorClothingTicket(av, self) == 2):
            flag = NPCToons.PURCHASE_MOVIE_START
            if self.housingEnabled and self.isClosetAlmostFull(av):
                flag = NPCToons.PURCHASE_MOVIE_START_NOROOM

        self.sendShoppingMovie(avId, flag)
        DistributedNPCToonBaseAI.avatarEnter(self)

    def isClosetAlmostFull(self, av):
        numClothes = len(av.clothesTopsList)/4 + len(av.clothesBottomsList)/2
        if numClothes >= av.maxClothes-1:
            return 1
        return 0

    def sendShoppingMovie(self, avId, flag):
        assert self.notify.debug('sendShoppingMovie()')
        self.busy = avId
        self.sendUpdate("setMovie", [flag,
                        self.npcId, avId,
                        ClockDelta.globalClockDelta.getRealNetworkTime()])

        # Timeout
        taskMgr.doMethodLater(NPCToons.TAILOR_COUNTDOWN_TIME,
                                self.sendTimeoutMovie,
                                self.uniqueName('clearMovie'))

    def rejectAvatar(self, avId):
        self.notify.warning("rejectAvatar: should not be called by a Tailor!")

    def sendTimeoutMovie(self, task):
        assert self.notify.debug('sendTimeoutMovie()')
        # The timeout has expired.  Restore the client back to his
        # original DNA automatically (instead of waiting for the
        # client to request this).

        toon = self.air.doId2do.get(self.customerId)
        # On second thought, we're better off not asserting this.
        #assert(self.busy == self.customerId)
        if (toon != None and self.customerDNA):
            toon.b_setDNAString(self.customerDNA.makeNetString())
            # Hmm, suppose the toon has logged out at the same time?
            # Is it possible to miss this update due to a race
            # condition?

        self.timedOut = 1
        self.sendUpdate("setMovie", [NPCToons.PURCHASE_MOVIE_TIMEOUT,
                        self.npcId, self.busy,
                        ClockDelta.globalClockDelta.getRealNetworkTime()])

        self.sendClearMovie(None)
        return Task.done

    def sendClearMovie(self, task):
        assert self.notify.debug('sendClearMovie()')
        # Ignore unexpected exits on whoever I was busy with
        self.ignore(self.air.getAvatarExitEvent(self.busy))
        self.customerDNA = None
        self.customerId = None
        self.customerTops = None
        self.customerBottoms = None
        self.busy = 0
        self.timedOut = 0
        self.sendUpdate("setMovie", [NPCToons.PURCHASE_MOVIE_CLEAR,
                        self.npcId, 0,
                        ClockDelta.globalClockDelta.getRealNetworkTime()])
        self.sendUpdate("setCustomerDNA", [0,''])
        return Task.done

    def completePurchase(self, avId):
        assert self.notify.debug('completePurchase()')
        self.busy = avId
        # Send a movie to reward the avatar
        self.sendUpdate("setMovie", [NPCToons.PURCHASE_MOVIE_COMPLETE,
                        self.npcId, avId,
                        ClockDelta.globalClockDelta.getRealNetworkTime()])
        self.sendClearMovie(None)

    def setClothesChoices(self, finished, topChoice=-1, bottomChoice=-1):
        assert self.notify.debug('setClothesChoices(): %s' % self.timedOut)
        avId = self.air.getAvatarIdFromSender()

        if avId != self.customerId:
            if self.customerId:
                self.air.writeServerEvent('suspicious', avId, 'DistributedNPCTailorAI.setClothesChoices customer is %s' % (self.customerId))
                self.notify.warning("customerId: %s, but got setClothesChoices for: %s" % (self.customerId, avId))
            else:
                self.air.writeServerEvent('suspicious', avId, 'DistributedNPCTailorAI.setClothesChoices customer is non-existant')
                self.notify.warning("We have no customer, but got setClothesChoices for: %s" % (avId))
            return
            
        if not avId in self.air.doId2do:
            self.notify.warning('No avatar for avId: %d, but got setClothesChoices' % avId)
            return 
        
        # Create the new temp dna.
        dna = ToonDNA.ToonDNA()
        dna.makeFromNetString(self.customerDNA.makeNetString())
        
        # Apply our top choice if we have chosen one.
        if topChoice >= 0:
            if topChoice < len(self.customerTops):
                dna.topTex = self.customerTops[topChoice][0]
                dna.topTexColor = self.customerTops[topChoice][1]
                dna.sleeveTex = self.customerTops[topChoice][2]
                dna.sleeveTexColor = self.customerTops[topChoice][3]
            else:
                self.air.writeServerEvent('suspicious', avId, 'DistributedNPCTailorAI.setClothesChoices got invalid top choice: %d' % (topChoice))
                self.notify.warning('Invalid top choice: %d for avId: %d' % (topChoice, avId))
                return
                
        # Apply our bottom choice if we have chosen one.
        if bottomChoice >= 0:
            if bottomChoice < len(self.customerBottoms):
                dna.botTex = self.customerBottoms[bottomChoice][0]
                dna.botTexColor = self.customerBottoms[bottomChoice][1]
            else:
                self.air.writeServerEvent('suspicious', avId, 'DistributedNPCTailorAI.setClothesChoices got invalid bottom choice: %d' % (bottomChoice))
                self.notify.warning('Invalid bottom choice: %d for avId: %d' % (bottomChoice, avId))
                return
                
        # Make our net string blob.
        blob = dna.makeNetString()

        av = self.air.doId2do[avId]
        if (finished == 2 and which > 0):
            # Make sure client was actually able to purchase
            if (self.air.questManager.removeClothingTicket(av, self) == 1 or self.freeClothes):
                assert self.notify.debug('Successful purchase')
                # No need to set the dna, it should already be set
                av.b_setDNAString(blob)
                
                if topChoice >= 0:
                    if (av.addToClothesTopsList(self.customerDNA.topTex, self.customerDNA.topTexColor, self.customerDNA.sleeveTex, self.customerDNA.sleeveTexColor) == 1):
                        av.b_setClothesTopsList(av.getClothesTopsList())
                    else:
                        self.notify.warning('NPCTailor: setClothesChoices() - unable to save old tops - we exceeded the tops list length')
                if bottomChoice >= 0:
                    if (av.addToClothesBottomsList(self.customerDNA.botTex, self.customerDNA.botTexColor) == 1):
                        av.b_setClothesBottomsList(av.getClothesBottomsList())
                    else:
                        self.notify.warning('NPCTailor: setClothesChoices() - unable to save old bottoms - we exceeded the bottoms list length')

                self.air.writeServerEvent('boughtTailorClothes', avId, "%s|%s|%s|%s" % (self.doId, topChoice, bottomChoice, self.customerDNA.asTuple()))
            else:
                self.air.writeServerEvent('suspicious', avId, 'DistributedNPCTailorAI.setClothesChoices bogus clothing ticket')
                self.notify.warning('NPCTailor: setClothesChoices() - client tried to purchase with bogus clothing ticket!')
                if self.customerDNA:
                    av.b_setDNAString(self.customerDNA.makeNetString())
        elif (finished == 1):
            # Purchase cancelled - make sure DNA gets reset, but don't
            # burn the clothing ticket
            if self.customerDNA:
                av.b_setDNAString(self.customerDNA.makeNetString())
        else:
            # Warning - we are trusting the client to set their DNA here
            # This is a big security hole. Either the client should just send
            # indexes into the clothing choices or the tailor should verify
            #av.b_setDNAString(dna)
            # Don't set the avatars DNA.  Instead, send a message back to the
            # all the clients in this zone telling them them the dna of the localToon
            # so they can set it themselves.
            self.sendUpdate("setCustomerDNA", [avId, blob])

        if (self.timedOut == 1 or finished == 0):
            return
        if (self.busy == avId):
            taskMgr.remove(self.uniqueName('clearMovie'))
            self.completePurchase(avId)
        elif self.busy:
            self.air.writeServerEvent('suspicious', avId, 'DistributedNPCTailorAI.setClothesChoices busy with %s' % (self.busy))
            self.notify.warning('setClothesChoices from unknown avId: %s busy: %s' % (avId, self.busy))

    def __handleUnexpectedExit(self, avId):
        self.notify.warning('avatar:' + str(avId) + ' has exited unexpectedly')

        # Only do customer work with the busy id
        if (self.customerId == avId):
            toon = self.air.doId2do.get(avId)
            if (toon == None):
                toon = DistributedToonAI.DistributedToonAI(self.air)
                toon.doId = avId

            if self.customerDNA:
                toon.b_setDNAString(self.customerDNA.makeNetString())
                # Force a database write since the toon is gone and might
                # have missed the distributed update.
                db = DatabaseObject.DatabaseObject(self.air, avId)
                db.storeObject(toon, ["setDNAString"])
        else:
            self.notify.warning('invalid customer avId: %s, customerId: %s ' % (avId, self.customerId))

        # Only do busy work with the busy id
        # Warning: send the clear movie at the end of this transaction because
        # it clears out all the useful values needed here
        if (self.busy == avId):
            self.sendClearMovie(None)
        else:
            self.notify.warning('not busy with avId: %s, busy: %s ' % (avId, self.busy))
