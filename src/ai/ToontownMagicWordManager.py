from direct.interval.IntervalGlobal import *
from direct.distributed import PyDatagram
from direct.distributed.MsgTypes import MsgName2Id
from toontown.toonbase.ToontownModules import *
from direct.distributed import DistributedObject
from toontown.toon import DistributedToon
from direct.directnotify import DirectNotifyGlobal
from toontown.town import TownBattleAttackPanel
from toontown.suit import RoguesGallery
from otp.avatar import Avatar
from otp.chat import ChatManager
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import ToontownBattleGlobals
import string
from toontown.toon import Toon
from direct.showbase import PythonUtil
from toontown.suit import DistributedSuitPlanner
from toontown.suit import DistributedBossCog
from otp.otpbase import OTPGlobals
from direct.distributed.ClockDelta import *
from otp.ai import MagicWordManager
from toontown.hood import ZoneUtil
from toontown.battle import Fanfare
from toontown.golf import GolfGlobals
from toontown.distributed import ToontownDistrictStats
from toontown.coderedemption import TTCodeRedemptionConsts
from toontown.rpc import AwardManagerConsts
from toontown.toonbase.ToontownModules import *

if base.wantKarts:
    from toontown.racing.KartDNA import *
    from toontown.racing.KartShopGui import *

if (__debug__):
    import pdb

class ToontownMagicWordManager(MagicWordManager.MagicWordManager):
    notify = DirectNotifyGlobal.directNotify.newCategory("ToontownMagicWordManager")
    neverDisable = 1

    GameAvatarClass = DistributedToon.DistributedToon

    def __init__(self, cr):
        MagicWordManager.MagicWordManager.__init__(self, cr)
        self.rogues = None
        self.ruler = None
        self.dbg_running_fast = 0

    def generate(self):
        MagicWordManager.MagicWordManager.generate(self)
        self.accept("magicWord", self.b_setMagicWord)

    def doLoginMagicWords(self):
        MagicWordManager.MagicWordManager.doLoginMagicWords(self)
        if ConfigVariableBool('want-chat', 0).getValue():
            # Automatically send ~chat if want-chat is true.
            self.d_setMagicWord('~chat', base.localAvatar.doId, 0)
        if (ConfigVariableBool('want-run', 0).getValue() or
            ConfigVariableBool('want-toontown-run', 0).getValue()):
            self.toggleRun()
        if ConfigVariableBool('immortal-mode', 0).getValue():
            self.d_setMagicWord('~immortal', base.localAvatar.doId, 0)
        mintFloor = ConfigVariableInt('mint-floor', -1).getValue()
        if mintFloor != -1:
            self.d_setMagicWord('~mintFloor %s' % mintFloor,
                                base.localAvatar.doId, 0)
        mintId = ConfigVariableInt('mint-id', -1).getValue()
        if mintId != -1:
            self.d_setMagicWord('~mint %s' % mintId,
                                base.localAvatar.doId, 0)
        autoRestock = ConfigVariableInt('auto-restock', -1).getValue()
        if autoRestock != -1:
            self.d_setMagicWord('~autoRestock %s' % autoRestock,
                                base.localAvatar.doId, 0)

        # NOTE: AI respects ~autoRich only for __dev__ and GMs.
        autoRich = ConfigVariableInt('auto-rich', -1).getValue()
        if autoRich != -1:
            self.d_setMagicWord('~autoRich %s' % autoRich,
                                base.localAvatar.doId, 0)

        # NOTE: AI respects ~autoResistanceRestock only for __dev__ and GMs.
        autoResistanceRestock = ConfigVariableInt('auto-resistance-restock', -1).getValue()
        if autoResistanceRestock != -1:
            self.d_setMagicWord('~autoResistanceRestock %s' % autoResistanceRestock,
                                base.localAvatar.doId, 0)

        # NOTE: AI respects ~autoRestockSOS only for __dev__ and GMs.
        autoRestockSOS = ConfigVariableInt('auto-restock-sos', -1).getValue()
        if autoRestockSOS != -1:
            self.d_setMagicWord('~autoRestockSOS %s' % autoRestockSOS,
                                base.localAvatar.doId, 0)

        # NOTE: AI respects ~autoRestockPinkSlips only for __dev__ and GMs.
        autoRestockPinkSlips = ConfigVariableInt('auto-restock-pink-slips', -1).getValue()
        if autoRestockPinkSlips != -1:
            self.d_setMagicWord('~autoRestockPinkSlips %s' % autoRestockPinkSlips,
                                base.localAvatar.doId, 0)

        # NOTE: AI respects ~autoRestockSummons only for __dev__ and GMs.
        autoRestockSummons = ConfigVariableInt('auto-restock-summons', -1).getValue()
        if autoRestockSummons != -1:
            self.d_setMagicWord('~autoRestockSummons %s' % autoRestockSummons,
                                base.localAvatar.doId, 0)

        # NOTE: AI respects ~setPaid only for __dev__ and GMs.
        paidStatus = ConfigVariableString('force-paid-status', 'none').getValue()
        if paidStatus != 'none':
            self.d_setMagicWord('~setPaid %s' % choice(paidStatus == 'paid', 1, 0),
                                localAvatar.doId, 0)
        self.doConfigMagicWords()

    def doConfigMagicWords(self):
        autoMagicWords = ConfigVariableString('auto-magic-words', '').getValue().split('|')
        for command in autoMagicWords:
            if command:
                self.d_setMagicWord(command.strip(), base.localAvatar.doId, 0)

    def disable(self):
        self.ignore("magicWord")
        if self.dbg_running_fast:
            self.toggleRun()
        MagicWordManager.MagicWordManager.disable(self)

    def doMagicWord(self, word, avId, zoneId):
        wordIs = Functor(self.wordIs, word)

        if (MagicWordManager.MagicWordManager.doMagicWord(self, word, avId,
                                                          zoneId) == 1):
            pass
        elif wordIs("~sf"):
            args = word.split()
            name = ''
            if len(args) > 1:
                name = args[1]
            base.cr.useShader(name)
        elif wordIs("~fanfare"):
            go = Fanfare.makeFanfareWithMessageImage(0, base.localAvatar, 1, "You just did a ~fanfare.  Here's a rake.", Vec2(0,0.2), 0.08, base.localAvatar.inventory.buttonLookup(1, 1), Vec3(0,0,0), 4)
            Sequence(go[0],Func(go[1].show),
                     LerpColorScaleInterval(go[1],duration=.5,startColorScale=Vec4(1,1,1,0),colorScale=Vec4(1,1,1,1)),Wait(2),
                     LerpColorScaleInterval(go[1],duration=.5,startColorScale=Vec4(1,1,1,1),colorScale=Vec4(1,1,1,0)),
                     Func(go[1].remove)).start()
            #go[0].start()
            #Fanfare.makeFanfareWithMessageImage(0, base.localAvatar, 1, "This is the message", Vec2(0,0.2), 0.08, base.localAvatar.inventory.buttonLookup(1, 1), Vec3(0,0,0), 4)[0].start()
            #Fanfare.makeFanfare(0, base.localAvatar).start()
        elif wordIs("~endgame"):
            print("Requesting minigame abort...")
            messenger.send("minigameAbort")
        elif wordIs("~wingame"):
            print("Requesting minigame victory...")
            messenger.send("minigameVictory")
        elif wordIs("~walk"):
            try:
                fsm = base.cr.playGame.getPlace().fsm
                fsm.forceTransition('walk')
            except:
                pass
        elif wordIs("~movie"):
            try:
                fsm = base.cr.playGame.getPlace().fsm
                fsm.forceTransition('movie')
            except:
                pass
        elif wordIs("~sit"):
            try:
                base.cr.playGame.getPlace().fsm.request('sit')
            except:
                pass
        elif wordIs("~rogues"):
            suitname = None
            if (len(word)>7):
                suitname=word[7:].split(' ')[1]
            self.rogues = RoguesGallery.RoguesGallery(suitname)
            self.rogues.enter()
            if suitname != None:
                self.rogues.animate()
            self.acceptOnce('mouse1', self.exit_rogues)
            # no longer keep rogues obj around after creation, so we can make a different one

        elif wordIs("~showPaths"):
            for obj in list(self.cr.doId2do.values()):
                if isinstance(obj, DistributedSuitPlanner.DistributedSuitPlanner):
                    obj.showPaths()
            place = base.cr.playGame.getPlace()
            if hasattr(place, "showPaths"):
                place.showPaths()

        elif wordIs("~hidePaths"):
            for obj in list(self.cr.doId2do.values()):
                if isinstance(obj, DistributedSuitPlanner.DistributedSuitPlanner):
                    obj.hidePaths()
            place = base.cr.playGame.getPlace()
            if hasattr(place, "hidePaths"):
                place.hidePaths()
        elif wordIs("~raceForever"):
            base.raceForever=True
        elif wordIs("~listen"):
            base.localAvatar.garbleChat = 0

        elif wordIs("~nochat") or wordIs("~chat") or wordIs("~superchat"):
            base.localAvatar.garbleChat = 1

        elif wordIs("~exec"):
            # Enable execChat.
            ChatManager.ChatManager.execChat = 1

        elif wordIs("~photoshoot"):
            # Empty the world for screenshots of the localToon
            base.cr.playGame.hood.sky.hide()
            base.cr.playGame.getPlace().loader.geom.hide()
            base.win.setClearColor(VBase4(1, 1, 1, 1))
            base.localAvatar.stopLookAroundNow()
            base.localAvatar.stopBlink()
            base.localAvatar.setNameVisible(0)

        elif wordIs("~hideAttack"):
            # Hide the attack panel so we can see around it.
            TownBattleAttackPanel.hideAttackPanel(1)

        elif wordIs("~showAttack"):
            # Reveal the attack panel again.
            TownBattleAttackPanel.hideAttackPanel(0)

        elif wordIs("~collisions_on"):
            base.localAvatar.collisionsOn()

        elif wordIs("~collisions_off"):
            base.localAvatar.collisionsOff()

        elif wordIs('~battle_detect_off'):
            from toontown.suit import DistributedSuit
            DistributedSuit.ALLOW_BATTLE_DETECT = 0

        elif wordIs('~battle_detect_on'):
            from toontown.suit import DistributedSuit
            DistributedSuit.ALLOW_BATTLE_DETECT = 1

        elif wordIs('~battles'):
            base.localAvatar.setWantBattles(
                not base.localAvatar.wantBattles)
            if base.localAvatar.wantBattles:
                response = 'battles ON'
            else:
                response = 'battles OFF'
            self.setMagicWordResponse(response)

        elif wordIs('~skipBattleMovie') or wordIs('~sbm'):
            ToontownBattleGlobals.SkipMovie = not ToontownBattleGlobals.SkipMovie
            if ToontownBattleGlobals.SkipMovie:
                response = "battle movies will be skipped"
            else:
                response = "battle movies will be played"
            self.setMagicWordResponse(response)

        elif wordIs('~addCameraPosition'):
            base.localAvatar.addCameraPosition()

        elif wordIs('~removeCameraPosition'):
            base.localAvatar.removeCameraPosition()

        elif wordIs('~printCameraPosition'):
            base.localAvatar.printCameraPosition(
                base.localAvatar.cameraIndex)

        elif wordIs('~printCameraPositions'):
            base.localAvatar.printCameraPositions()

        elif wordIs('~worldCam') or wordIs('~wc'):
            #print the camera position and hpr in world coordinates
            myCam = render.find('**/camera')
            if not myCam.isEmpty():
                camParent = myCam.getParent()
                myCam.wrtReparentTo(render)
                pos = myCam.getPos()
                hpr = myCam.getHpr()
                response = "(%.2f, %.2f, %.2f,) (%.2f, %.2f, %.2f)" % (pos[0], pos[1], pos[2], hpr[0], hpr[1], hpr[2])
                if not camParent.isEmpty():
                    myCam.wrtReparentTo(camParent)
                self.setMagicWordResponse(response)
                print(response)





        elif wordIs("~sync"):
            # Sync with the AI, like F6, but rather than accumulating
            # sync informatoin, throw away whatever information was
            # there from before.  If a second parameter is supplied,
            # it is a number of seconds of temporary extra skew to
            # apply; the default is 0.

            tm = base.cr.timeManager
            if tm == None:
                response = "No TimeManager."
                self.setMagicWordResponse(response)

            else:
                tm.extraSkew = 0.0
                skew = word[5:].strip()
                if skew != "":
                    tm.extraSkew = float(skew)
                globalClockDelta.clear()
                tm.handleHotkey()

        elif wordIs("~period"):
            # Reset the period timer to expire in the indicated number
            # of seconds, or with no parameter, report the number of
            # seconds remaining.

            timeout = word[7:].strip()
            if timeout != "":
                seconds = int(timeout)
                base.cr.stopPeriodTimer()
                base.cr.resetPeriodTimer(seconds)
                base.cr.startPeriodTimer()

            # Now report the number of seconds remaining.
            if base.cr.periodTimerExpired:
                response = "Period timer has expired."

            elif base.cr.periodTimerStarted:
                elapsed = globalClock.getFrameTime() - base.cr.periodTimerStarted
                secondsRemaining = base.cr.periodTimerSecondsRemaining - elapsed
                response = "Period timer expires in %s seconds." % (int(secondsRemaining))
            else:
                response = "Period timer not set."

            self.setMagicWordResponse(response)

        elif wordIs("~net"):
            # Simulate pulling or restoring the network plug.
            if base.cr.networkPlugPulled():
                base.cr.restoreNetworkPlug()
                base.cr.startHeartbeat()
                response = "Network restored."
            else:
                base.cr.pullNetworkPlug()
                base.cr.stopHeartbeat()
                response = "Network disconnected."
            self.setMagicWordResponse(response)

        elif wordIs("~lag"):
            if not hasattr(base.cr, "magicLag"):
                base.cr.startDelay(0.1,0.35)
                base.cr.magicLag = None
                response = "Simulated Lag On"
            else:
                base.cr.stopDelay()
                del base.cr.magicLag
                response = "Simulated Lag Off"
            self.setMagicWordResponse(response)

        elif wordIs("~endlessquietzone"):
            base.endlessQuietZone = not base.endlessQuietZone
            response = "endless quiet zone %s" % choice(base.endlessQuietZone,
                       'ON', 'OFF')
            self.setMagicWordResponse(response)



        elif wordIs("~cogPageFull"):
            # show all panels on cog page of Shticker book
            base.localAvatar.suitPage.updateAllCogs(3)

        elif wordIs('~mintId'):
            # the AI is going to listen for this also, but let's keep a local
            # copy
            args = word.split()
            postName = 'mintIdOverride'
            if len(args) < 2:
                if bboard.has(postName):
                    bboard.remove(postName)
            else:
                try:
                    id = int(args[1])
                    # make sure it's a valid id
                    foo = ToontownGlobals.MintNumRooms[id]
                except:
                    pass
                else:
                    bboard.post(postName, id)

        elif wordIs('~mintRoom'):
            # the AI is going to listen for this also, but let's keep a local
            # copy
            args = word.split()
            postName = 'mintRoom'
            if len(args) < 2:
                if bboard.has(postName):
                    bboard.remove(postName)
            else:
                try:
                    id = int(args[1])
                except:
                    pass
                else:
                    bboard.post(postName, id)

        elif wordIs('~mintWarp'):
            args=word.split()
            if len(args) < 2:
                self.setMagicWordResponse('Usage: ~mintWarp roomId')
                return
            try:
                roomNum = int(args[1])
            except:
                self.setMagicWordResponse('roomId not found: %s' % args[1])
                return
            if not bboard.has('mint'):
                self.setMagicWordResponse('not in a mint')
                return
            mint = bboard.get('mint')
            if not mint.warpToRoom(roomNum):
                self.setMagicWordResponse(
                    'invalid roomId or roomId not in this mint: %s' % args[1])
                return

        elif wordIs('~mintLayouts'):
            from toontown.coghq import MintLayout
            MintLayout.printAllCashbotInfo()
            self.setMagicWordResponse('logged mint layouts')

        elif wordIs("~edit"):
            if not __dev__:
                self.setMagicWordResponse("client not running in dev mode")
                return

            from otp.level import EditorGlobals
            # Is there a level that has made itself available for editing?
            level = bboard.get(EditorGlobals.EditTargetPostName)
            if level == None:
                self.setMagicWordResponse('no level available for editing')
                return

            from toontown.coghq import DistributedInGameEditor
            EditorGlobals.assertReadyToEdit()
            editUsername = EditorGlobals.getEditUsername()
            # make sure we're not already editing this level
            editors = base.cr.doFindAll('DistributedInGameEditor')
            for e in editors:
                if isinstance(
                    e, DistributedInGameEditor.DistributedInGameEditor):
                    if e.getLevelDoId() == level.doId:
                        if (e.editorIsLocalToon() or
                            e.getEditUsername() == editUsername):
                            self.setMagicWordResponse(
                                "you ('%s') are already editing this level" %
                                editUsername)
                            return
            cmd = "~inGameEdit %s %s" % (level.doId, editUsername)
            # Now send the real magic word with the doId etc. also
            self.b_setMagicWord(cmd)

        elif wordIs('~fshow'):
            from toontown.coghq import DistributedFactory
            factories = base.cr.doFindAll("DistributedFactory")
            factory = None
            for f in factories:
                if isinstance(f, DistributedFactory.DistributedFactory):
                    factory = f
                    break
            if factory is None:
                self.setMagicWordResponse('factory not found')
                return
            factory.setColorZones(not factory.fColorZones)

        elif wordIs('~fzone'):
            args = word.split()
            if len(args) < 2:
                self.setMagicWordResponse('Usage: ~fzone <zoneNum>')
                return
            zoneId = int(args[1])

            from toontown.coghq import DistributedFactory
            factories = base.cr.doFindAll("DistributedFactory")
            factory = None
            for f in factories:
                if isinstance(f, DistributedFactory.DistributedFactory):
                    factory = f
                    break
            if factory is None:
                self.setMagicWordResponse('factory not found')
                return
            factory.warpToZone(zoneId)

        elif wordIs("~undead"):
            # regenerate dead goons
            try:
                goons = base.cr.doFindAll("Goon")
                for goon in goons:
                    goon.undead()
            except:
                self.notify.warning("Error in undead")
        elif wordIs("~resyncGoons"):
            try:
                goons = base.cr.doFindAll("Goon")
                for goon in goons:
                    goon.resync()
            except:
                self.notify.warning("Error in resyncing")
        elif wordIs("~catalog"):
            self.doCatalog(word)

        elif wordIs('~petCam') and base.wantPets:
            if hasattr(base, 'petCamPrevParent'):
                base.cam.reparentTo(base.petCamPrevParent)
                del base.petCamPrevParent
            else:
                petId = base.localAvatar.getPetId()
                pet = self.cr.doId2do.get(petId)
                if pet:
                    if not hasattr(pet, 'camNode'):
                        pet.camNode = pet.attachNewNode('camNode')
                        pet.camNode.setPos(0, 0, 2.5)
                    base.petCamPrevParent = base.cam.getParent()
                    base.cam.reparentTo(pet.camNode)

        elif wordIs('~lockPet') and base.wantPets:
            petId = base.localAvatar.getPetId()
            pet = self.cr.doId2do.get(petId)
            if pet:
                if not pet.isLockedDown():
                    pet.lockPet()

        elif wordIs('~unlockPet') and base.wantPets:
            petId = base.localAvatar.getPetId()
            pet = self.cr.doId2do.get(petId)
            if pet:
                if pet.isLockedDown():
                    pet.unlockPet()

        elif wordIs('~resetPetTutorial') and base.wantPets:
            base.localAvatar.setPetTutorialDone(False)
            response = "Pet Tutorial flag reset"
            self.setMagicWordResponse(response)

        elif wordIs('~bossBattle'):
            self.doBossBattle(word)

        elif wordIs("~RaceChat"):
                #loadup chat phrases
                base.localAvatar.chatMgr.chatInputSpeedChat.addKartRacingMenu()
        elif wordIs('~BuyKart'):
            if base.wantKarts:
                def doShtikerLater(task):
                    base.localAvatar.addKartPage()
                    return 0
                if (base.localAvatar.hasKart()):
                    response = "Returning Kart %s" % (base.localAvatar.getKartBodyType())
                    base.localAvatar.requestKartDNAFieldUpdate(KartDNA.bodyType, InvalidEntry)
                    self.setMagicWordResponse(response)
                else:
                    base.localAvatar.requestKartDNAFieldUpdate(KartDNA.rimsType, getDefaultRim())
                    taskMgr.doMethodLater(1.0, doShtikerLater, "doShtikerLater")

                # NOTE - BE SURE TO CHECK AI VERSION OF THIS AS IT SETS ACCESSSORIES OWNED FOR THE TOONAI.
                response = "Kart %s has been purchased with body and accessory color %s." % (word[9], getDefaultColor())
                base.localAvatar.requestKartDNAFieldUpdate(KartDNA.bodyType, int(word[9]))
                self.setMagicWordResponse(response)
            else:
                self.setMagicWordResponse("Enable wantKarts in Config.prc")
        elif wordIs('~leaveRace'):
            messenger.send('leaveRace')
        elif wordIs('~kartParticles'):
            b = ConfigVariableBool('want-kart-particles', 0)
            b.setValue(not b)
        elif wordIs('~gardenGame'):
            messenger.send("gardenGame")
            response = "You must be on your estate"
            self.setMagicWordResponse(response)

        elif wordIs("~verboseState"):
            # show all panels on cog page of Shticker book
            base.localAvatar.verboseState()

        elif wordIs('~golf'):
            self.doGolf(word)

        elif wordIs('~whiteList'):
            base.localAvatar.chatMgr.chatInputSpeedChat.addWhiteList()

        elif wordIs('~updateWhiteList'):
            self.notify.info('Updating WhiteList')
            base.whiteList.redownloadWhitelist()

        elif wordIs('~noWhiteList'):
            base.localAvatar.chatMgr.chatInputSpeedChat.removeWhiteList()

        elif wordIs("~setPaid"):
            args = word.split()
            if len(args) > 1:
                paid = int(args[1])
                statusString = ConfigVariableString('force-paid-status', 'none').getValue()
                if paid:
                    paid = 1
                    if statusString != 'none':
                        if statusString == 'VELVET':
                            ConfigVariableString('force-paid-status').setValue("FULL")
                        elif statusString == 'unpaid':
                            ConfigVariableString('force-paid-status').setValue("paid")
                    base.cr.setIsPaid(1)
                else:
                    paid = 0
                    if statusString != 'none':
                        if statusString == 'FULL':
                            ConfigVariableString('force-paid-status').setValue("VELVET")
                        elif statusString == 'paid':
                            ConfigVariableString('force-paid-status').setValue("unpaid")
                    base.cr.setIsPaid(0)
            else:
                #self.setMagicWordResponse(senderId, "0 for unpaid 1 for paid")
                return

        # Parties
        elif wordIs("~party"):
            self.doParty(word, avId, zoneId)

        # In Game News
        elif wordIs("~news"):
            self.doNews(word, avId, zoneId)

        # Boarding Party GUI
        elif wordIs('~bgui'):
            if not hasattr(self, 'groupPanel'):
                from toontown.toon import GroupPanel
                self.groupPanel = GroupPanel.GroupPanel(base.localAvatar.boardingParty)
                self.groupPanel.frame.show()
            else:
                self.groupPanel.frame.hide()
                self.groupPanel.cleanup()
                del self.groupPanel

        elif wordIs('~generateOrder'):
            args = word.split()
            if len(args) > 1:
                newOrder = int(args[1])
                if newOrder>=0 and newOrder <=2:
                    datagram = PyDatagram.PyDatagram()
                    datagram.addUint16(MsgName2Id["CLIENT_CHANGE_GENERATE_ORDER"])
                    datagram.addUint32(newOrder)
                    base.cr.send(datagram)
                    response = "changing generate order to %s" % newOrder
                    self.setMagicWordResponse(response)
            else:
                response = "args: 0 default, 1 reversed, 2 shuffled"
                self.setMagicWordResponse(response)


        # Ruler
        elif wordIs('~ruler'):
            response = "Each unit is equal to one foot"
            self.setMagicWordResponse(response)
            if self.ruler:
                self.ruler.detachNode()
                del self.ruler

            self.ruler = loader.loadModel("phase_3/models/props/xyzAxis")
            self.ruler.reparentTo(render)
            self.ruler.setPos(base.localAvatar.getPos())
            self.ruler.place()

        elif wordIs("~toonIdTags"):
            otherToons = base.cr.doFindAllOfType('DistributedToon')
            if otherToons:
                for toon in otherToons[0]:
                    # this forces the nametag font to be the basic font that has numbers
                    toon.setNametagStyle(0)
            messenger.send('nameTagShowAvId', [])
            base.idTags = 1

        elif wordIs('~code'):
            # code redemption
            args = word.split()
            if len(args) > 1:
                code = word[len(args[0])+1:]
                base.codeRedemptionMgr.redeemCode(code, self._handleCodeRedemptionResponse)
                response = 'sending code %s to server...' % code
            else:
                response = '~code <code>'
            self.setMagicWordResponse(response)

    def _handleCodeRedemptionResponse(self, result, awardMgrResult):
        if not result:
            msg = 'code redeemed'
        else:
            if result != TTCodeRedemptionConsts.RedeemErrors.AwardCouldntBeGiven:
                errMsg = TTCodeRedemptionConsts.RedeemErrorStrings[result]
            else:
                errMsg = AwardManagerConsts.GiveAwardErrorStrings[awardMgrResult]
            msg = 'code NOT redeemed (%s)' % (errMsg, )
        base.localAvatar.setChatAbsolute(msg, CFSpeech | CFTimeout)

    def doParty(self,word, av, zoneId):
        args = word.split()
        response = None
        action = None

        if len(args) == 1:
            return

        action = args[1]
        if action == 'plan':
            # We need to know if we're about to plan a party upon entering the
            # teleportIn state of the Party.py fsm. Following the pet tutorial's
            # lead by setting a boolean on the avatar.
            base.localAvatar.aboutToPlanParty = True
            base.localAvatar.creatingNewPartyWithMagicWord = False
        elif action == 'new':
            # Let's tell ourselves we're creating a new party, so we know what
            # to do with the response
            base.localAvatar.aboutToPlanParty = False
            base.localAvatar.creatingNewPartyWithMagicWord = True
        elif action == 'start':
            base.localAvatar.creatingNewPartyWithMagicWord = False
            base.localAvatar.aboutToPlanParty = False
            hoodId = ToontownGlobals.PartyHood
            ToontownDistrictStats.refresh('shardInfoUpdated')
            # We need to find the lowest populated shard and have the party there
            curShardTuples = base.cr.listActiveShards()
            # Tuple is of form : (shardId, name, pop, WelcomeValleyPopulation)
            lowestPop = 100000000000000000
            shardId = None
            for shardInfo in curShardTuples:
                pop = shardInfo[2]
                if pop < lowestPop:
                    lowestPop = pop
                    shardId = shardInfo[0]
            if shardId == base.localAvatar.defaultShard:
                shardId = None
            base.cr.playGame.getPlace().requestLeave({
                "loader": "safeZoneLoader",
                "where": "party",
                "how" : "teleportIn",
                "hoodId" : hoodId,
                "zoneId" : -1,
                "shardId" : shardId,
                "avId" : -1,
            })
        elif action == 'unreleasedClient':
            newVal = base.cr.partyManager.toggleAllowUnreleasedClient()
            response = "Allow Unreleased Client = %s" % newVal
        elif action == 'showdoid':
            newVal = base.cr.partyManager.toggleShowDoid()
            response = "show doid = %s" % newVal
        elif action == 'debugGrid':
            newVal = not ConfigVariableBool('show-debug-party-grid').getValue()
            ConfigVariableBool('show-debug-party-grid').setValue(newVal)
            response = "Grid: %s; re-enter party to see changes." % newVal

        if response is not None:
            self.setMagicWordResponse(response)

    def doCatalog(self, word):
        """Handle the ~catalog magic word: manage catalogs.  Most of
        these are handled by the AI."""

        args = word.split()


        if len(args) == 1:
            # No parameter.  Handled by AI.
            return

        elif args[1] == "reload":
            phone = base.cr.doFind('phone')
            if phone and phone.phoneGui:
                phone.phoneGui.reload()
                response = "Reloaded catalog screen"
            else:
                response = "Phone is not active."

        elif args[1] == "dump":
            if len(args) <= 2:
                response = "Specify output filename."
            else:
                from toontown.catalog import CatalogGenerator
                cg = CatalogGenerator.CatalogGenerator()
                cg.outputSchedule(args[2])
                response = "Catalog schedule written to file %s." % (args[2])

        else:
            # Some other parameter.  Handled by AI.
            return

        self.setMagicWordResponse(response)


    def toggleRun(self):
        if (self.dbg_running_fast):
            self.dbg_running_fast = 0
            OTPGlobals.ToonForwardSpeed = self.save_fwdspeed
            OTPGlobals.ToonReverseSpeed = self.save_revspeed
            OTPGlobals.ToonRotateSpeed =self.save_rotspeed
            base.localAvatar.setWalkSpeedNormal()
        else:
            self.dbg_running_fast = 1
            self.save_fwdspeed = OTPGlobals.ToonForwardSpeed
            self.save_revspeed = OTPGlobals.ToonReverseSpeed
            self.save_rotspeed = OTPGlobals.ToonRotateSpeed
            OTPGlobals.ToonForwardSpeed = 60
            OTPGlobals.ToonReverseSpeed = 30
            OTPGlobals.ToonRotateSpeed = 100
            base.localAvatar.setWalkSpeedNormal()


    def requestTeleport(self, loaderId, whereId, hoodId, zoneId, avId):
        """requestTeleport(self, int hoodId, int zoneId, int avId)

        The AI tells the avatar go somewhere.  This is probably in
        response to a magic word requesting transfer to a zone.
        """
        place = base.cr.playGame.getPlace()
        if loaderId == "":
            loaderId = ZoneUtil.getBranchLoaderName(zoneId)
        if whereId == "":
            whereId = ZoneUtil.getToonWhereName(zoneId)
        if hoodId == 0:
            hoodId = place.loader.hood.id
        if avId == 0:
            avId = -1
        place.fsm.forceTransition('teleportOut',
                                  [{"loader": loaderId,
                                    "where": whereId,
                                    "how": "teleportIn",
                                    "hoodId": hoodId,
                                    "zoneId": zoneId,
                                    "shardId": None,
                                    "avId": avId}])


    def exit_rogues(self):
        self.rogues.exit()
        del self.rogues
        self.rogues = None

    def identifyDistributedObjects(self, name):
        # Find the nearby distributed object or objects (of any type)
        # with the given name.  Returns a list of (name, obj) pairs.

        result = []
        lowerName = name.lower()

        for obj in list(base.cr.doId2do.values()):
            className = obj.__class__.__name__
            try:
                name = obj.getName()
            except:
                name = className

            if name.lower() == lowerName or \
               className.lower() == lowerName or \
               className.lower() == "distributed" + lowerName:
                result.append((name, obj))

        return result

    def getCSBitmask(self, st):
        # Decompose the string into keywords, and return the
        # corresponding collision bitmask, suitable for passing to
        # NodePath.showCS() or hideCS().
        words = st.lower().split()
        if len(words) == 0:
            return None

        invalid = ""

        bitmask = BitMask32.allOff()
        for w in words:
            if w == "wall":
                bitmask |= ToontownGlobals.WallBitmask
            elif w == "floor":
                bitmask |= ToontownGlobals.FloorBitmask
            elif w == "cam":
                bitmask |= ToontownGlobals.CameraBitmask
            elif w == "catch":
                bitmask |= ToontownGlobals.CatchBitmask
            elif w == "ghost":
                bitmask |= ToontownGlobals.GhostBitmask
            elif w == "furniture":
                bitmask |= (ToontownGlobals.FurnitureSideBitmask |
                            ToontownGlobals.FurnitureTopBitmask |
                            ToontownGlobals.FurnitureDragBitmask)
            elif w == "furnitureside":
                bitmask |= ToontownGlobals.FurnitureSideBitmask
            elif w == "furnituretop":
                bitmask |= ToontownGlobals.FurnitureTopBitmask
            elif w == "furnituredrag":
                bitmask |= ToontownGlobals.FurnitureDragBitmask
            elif w == "pie":
                bitmask |= ToontownGlobals.PieBitmask
            else:
                invalid += " " + w

        if invalid:
            self.setMagicWordResponse("Unknown CS keyword(s): %s" % invalid)

        return bitmask

    def getFontByName(self, fontname):
        if fontname == "toon":
            return ToontownGlobals.getToonFont()
        elif fontname == "building":
            return ToontownGlobals.getBuildingNametagFont()
        elif fontname == "minnie":
            return ToontownGlobals.getMinnieFont()
        elif fontname == "suit":
            return ToontownGlobals.getSuitFont()
        else:
            return MagicWordManager.MagicWordManager.getFontByName(self, fontname)

    def doBossBattle(self, word):
        """Handle the ~bossBattle magic word: manage a final boss
        battle."""

        args = word.split()

        # Find the particular Boss Cog that's in the same zone with
        # the avatar.
        bossCog = None
        for distObj in list(self.cr.doId2do.values()):
            if isinstance(distObj, DistributedBossCog.DistributedBossCog):
                bossCog = distObj
                break

        response = None
        if len(args) == 1:
            # No parameter: ignore (handled by AI).
            pass

        elif args[1] == "safe":
            # ~bossBattle safe [flag]: Ignore hits to the toon during the pie
            # scene.  This acts as a toggle.
            if len(args) <= 2:
                flag = not bossCog.localToonIsSafe
            else:
                flag = int(args[2])

            bossCog.localToonIsSafe = flag
            if flag:
                response = "LocalToon is now safe from boss attacks"
            else:
                response = "LocalToon is now vulnerable to boss attacks"

        elif args[1] == "stun":
            # ~bossBattle stun: stun all of the goons in the CFO battle.
            bossCog.stunAllGoons()

        elif args[1] == "destroy":
            # ~bossBattle destroy: destroy all of the goons in the CFO battle.
            bossCog.destroyAllGoons()

        elif args[1] == "avatarEnter":
            # ~bossBattle avatarEnter: run this if you get No Toons error.
            bossCog.d_avatarEnter()
            response = 'called d_avatarEnter'

        if response:
            self.setMagicWordResponse(response)


    def doGolf(self, word):
        """Handle the ~golf magic word for valid client side stuff."""
        args = word.split()
        response = None
        if len(args) == 1:
            # No parameter: ignore (handled by AI).
            pass
        elif args[1] == "debugBarrier":
            golfHole = base.cr.doFind('DistributedGolfHole')
            if golfHole:
                if hasattr(golfHole,'golfBarrier') and not golfHole.golfBarrier.isEmpty():
                    if golfHole.golfBarrier.isHidden():
                        golfHole.golfBarrier.show()
                        response = 'showing golf barrier'
                    else:
                        golfHole.golfBarrier.hide()
                        response = 'hiding golf barrier'
            else:
                response = 'no golf hole'
        elif args[1] == "contact":
            messenger.send("ode toggle contacts")
        elif args[1] == "power":
            if len(args) > 2:
                base.golfPower = args[2]
                response = ('setting power to %s' % (args[2]))
            else:
                base.golfPower = None
                response = 'unsetting power'
        elif args[1] == "heading":
            if len(args) > 2:
                golfHole = base.cr.doFind('DistributedGolfHole')
                if golfHole:
                    golfHole.doMagicWordHeading(args[2])
                    response = ('setting heading to %s' % (args[2]))
            else:
                response = 'need heading parameter'
        elif args[1] == "list":
            response = ""
            for holeId in GolfGlobals.HoleInfo:
                if holeId < 18:
                    response += '%d: %s\n'%(holeId, GolfGlobals.getHoleName(holeId))
        elif args[1] == "list2":
            response = ""
            for holeId in GolfGlobals.HoleInfo:
                if holeId >= 18:
                    response += '%d: %s\n'%(holeId, GolfGlobals.getHoleName(holeId))

        if response:
            self.setMagicWordResponse(response)

    def doNews(self,word, av, zoneId):
        args = word.split()
        response = None
        action = None

        if len(args) == 1:
            return

        action = args[1]
        if action == 'frame':

            NametagGlobals.setMasterArrowsOn(0)
            from toontown.shtiker import InGameNewsFrame
            base.newsFrame = InGameNewsFrame.InGameNewsFrame()
            base.newsFrame.activate()
            response = "putting in game news direct frame up"
        elif action == 'snapshot':
            response = localAvatar.newsPage.doSnapshot()

        if response is not None:
            self.setMagicWordResponse(response)
