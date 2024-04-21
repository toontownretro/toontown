"""
Suit module: contains Suit class
Example creation:

from toontown.suit import Suit
s = Suit.Suit()
from toontown.suit import SuitDNA
d = SuitDNA.SuitDNA()
d.newSuit('tbc')
s.setDNA(d)
s.loop('neutral')
s.reparentTo(render)
s.setPos(base.localAvatar, 0,0,0)

s.delete()
del s
"""

"""
Suit Types & Tracks

BossBot (Corporate): 'c'
 Flunky:          f
 PencilPusher:    p
 YesMan:          ym
 MicroManager:    mm
 DownSizer:       ds
 HeadHunter:      hh
 CorporateRaider: cr
 BigCheese:       bc

LawBot (Legal): 'l'
 BottomFeeder:    bf
 BloodSucker:     b
 DoubleTalker:    dt
 AmbulanceChaser: ac
 BackStabber:     bs
 SpinDoctor:      sd
 LegalEagle:      le
 BigWig:          bw

CashBot (Money): 'm'
 ShortChange:     sc
 PennyPincher:    pp
 TightWad:        tw
 BeanCounter:     bc
 NumberCruncher:  nc
 MoneyBags:       mb
 LoanShark:       ls
 RobberBaron:     rb

SellBot (Sales): 's'
 ColdCaller:      cc
 Telemarketer:    tm
 NameDropper:     nd
 GladHander:      gh
 Mover&Shaker:    ms
 TwoFaced:        tf
 TheMingler:      m
 Mr.Hollywood:    mh
"""

import os, string
from direct.actor import Actor
from direct.directnotify import DirectNotifyGlobal
from direct.showbase import AppRunnerGlobal
from direct.task.Task import Task
from otp.avatar import Avatar, ShadowCaster
from toontown.battle import BattleProps, SuitBattleGlobals
from toontown.suit import SuitDNA
from toontown.toonbase import ToontownGlobals, TTLocalizer
from toontown.toonbase.ToontownModules import *
from toontown.toonbase.ToontownModules import VirtualFileMountHTTP, VirtualFileSystem, Filename, DSearchPath

aSize = 6.06
bSize = 5.29
cSize = 4.14

SuitDialogArray = []
SkelSuitDialogArray = []

# list of anims for all suit parts

AllSuits = (
    ("walk", "walk"),
    ("run", "walk"),
    )

AllSuitsMinigame = (
    ("victory", "victory"),
    ("flail", "flailing"),
    ("tug-o-war", "tug-o-war"),
    ("slip-backward", "slip-backward"),
    ("slip-forward", "slip-forward"),
    )

AllSuitsTutorialBattle = (
    ("lose", "lose"),
    ("pie-small-react", "pie-small"),
    ("squirt-small-react", "squirt-small"),
    )

AllSuitsBattle = (
    ("drop-react", "anvil-drop"),
    ("flatten", "drop"),
    ("sidestep-left", "sidestep-left"),
    ("sidestep-right", "sidestep-right"),
    ("squirt-large-react", "squirt-large"),
    ("landing", "landing"),
    ("reach", "walknreach"),
    ("rake-react", "rake"),
    ("hypnotized", "hypnotize"),
    ("soak", "soak"),
    )

SuitsCEOBattle = (
    ("sit", "sit"),
    ("sit-eat-in", "sit-eat-in"),
    ("sit-eat-loop", "sit-eat-loop"),
    ("sit-eat-out", "sit-eat-out"),
    ("sit-angry", "sit-angry"),
    ("sit-hungry-left", "leftsit-hungry"),
    ("sit-hungry-right", "rightsit-hungry"),
    ("sit-lose", "sit-lose"),
    ("tray-walk", "tray-walk"),
    ("tray-neutral", "tray-neutral"),
    ("sit-lose", "sit-lose"),
    )

# corp anims per type
# Flunky (C) Corp 1
f = (
    # pass on carbon copy for now
    ("throw-paper", "throw-paper", 3.5),
    ("phone", "phone", 3.5),
    ("shredder", "shredder", 3.5),
    )
# PencilPusher (B) Corp 2
p = (
    ("pencil-sharpener", "pencil-sharpener", 5),
    ("pen-squirt", "pen-squirt", 5),
    ("hold-eraser", "hold-eraser", 5),
    ("finger-wag", "finger-wag", 5),
    ("hold-pencil", "hold-pencil", 5),
    )
# YesMan (A) Corp 3
ym = (
    ("throw-paper", "throw-paper", 5),
    # pass on ditto
    ("golf-club-swing", "golf-club-swing", 5),
    ("magic3", "magic3", 5),
    ("rubber-stamp", "rubber-stamp", 5),
    ("smile", "smile", 5),
    )
# MicroManager (C) Corp 4
mm = (
    ("speak", "speak", 5),
    ("effort", "effort", 5),
    ("magic1", "magic1", 5),
    ("pen-squirt", "fountain-pen", 5),
    ("finger-wag", "finger-wag", 5),
    )

# Downsizer (B) Corp 5
ds = (
    ("magic1", "magic1", 5), # just as default for now
    ("magic2", "magic2", 5),
    ("throw-paper", "throw-paper", 5),
    ("magic3", "magic3", 5),
    )

# Head Hunter (A) Corp 6
hh = (
    ("pen-squirt", "fountain-pen", 7),
    ("glower", "glower", 5),
    ("throw-paper", "throw-paper", 5),
    ("magic1", "magic1", 5),
    ("roll-o-dex", "roll-o-dex", 5),
    )

# Corporate Raider (C) Corp 7
cr = (
    ("pickpocket", "pickpocket", 5), # just as default for now
    ("throw-paper", "throw-paper", 3.5),
    ("glower", "glower", 5),
    )

# The Big Cheese (A) Corp 8
tbc = (
    ("cigar-smoke", "cigar-smoke", 8),
    ("glower", "glower", 5),
    ("song-and-dance", "song-and-dance", 8),
    ("golf-club-swing", "golf-club-swing", 5),
    )

# sales anims per type
# ColdCaller (C) Sales 1
cc = (
    ("speak", "speak", 5),
    ("glower", "glower", 5),
    ("phone", "phone", 3.5),
    ("finger-wag", "finger-wag", 5), # place holder for speak animation, won't need it
    )
# TeleMarketer (B) Sales 2
tm = (
    ("speak", "speak", 5),
    ("throw-paper", "throw-paper", 5),
    ("pickpocket", "pickpocket", 5),
    ("roll-o-dex", "roll-o-dex", 5),
    ("finger-wag", "finger-wag", 5), # place holder for speak animation, won't need it
    )
# NameDropper (A) Sales 3
nd = (
    ("pickpocket", "pickpocket", 5),
    ("roll-o-dex", "roll-o-dex", 5),
    ("magic3", "magic3", 5),
    ("smile", "smile", 5),
    )
# GladHander (C) Sales 4
gh = (
    ("speak", "speak", 5),
    ("pen-squirt", "fountain-pen", 5),
    # TODO:
    # Neither of these are right...
    # They should be all talk attacks...
    # But until we have the talk animations,
    # these will stay...
    ("rubber-stamp", "rubber-stamp", 5),
    )

# Mover & Shaker (B) Sales 5
ms = (
    ("effort", "effort", 5),
    ("throw-paper", "throw-paper", 5),
    ("stomp", "stomp", 5),
    ("quick-jump", "jump", 6),
    )

# Two-Face (A) Sales 6
tf = (
    ("phone", "phone", 5),
    ("smile", "smile", 5),
    ("throw-object", "throw-object", 5),
    ("glower", "glower", 5),
    )

# The Mingler (A) Sales 7
m = (
    ("speak", "speak", 5),
    ("magic2", "magic2", 5),
    ("magic1", "magic1", 5),
    ("golf-club-swing", "golf-club-swing", 5),
    )

# Mr. Hollywood (A) Sales 8
mh = (
    ("magic1", "magic1", 5),
    ("smile", "smile", 5),
    ("golf-club-swing", "golf-club-swing", 5),
    ("song-and-dance", "song-and-dance", 5),
    )

# money anims per type
# ShortChange (C) Cash 1
sc = (
    ("throw-paper", "throw-paper", 3.5),
    ("watercooler", "watercooler", 5),
    ("pickpocket", "pickpocket", 5),
    )
# PennyPincher (A) Cash 2
pp = (
    ("throw-paper", "throw-paper", 5),
    ("glower", "glower", 5),
    ("finger-wag", "fingerwag", 5),
    )

# TightWad (C) Cash 3
tw = (
    ("throw-paper", "throw-paper", 3.5),
    ("glower", "glower", 5),
    ("magic2", "magic2", 5),
    ("finger-wag", "finger-wag", 5),
    )
# BeanCounter (B) Cash 4
bc = (
    ("phone", "phone", 5),
    ("hold-pencil", "hold-pencil", 5),
    )

# Number Cruncher (A) Cash 5
nc = (
    ("phone", "phone", 5),
    ("throw-object", "throw-object", 5),
    )

# Money Bags (C) Cash 6
mb = (
    ("magic1", "magic1", 5),
    ("throw-paper", "throw-paper", 3.5),
    )

# Loan Shark (B) Cash 7
ls = (
    ("throw-paper", "throw-paper", 5),
    ("throw-object", "throw-object", 5),
    ("hold-pencil", "hold-pencil", 5),
    )

# Robber Baron (A) Cash 8
rb = (
    ("glower", "glower", 5),
    ("magic1", "magic1", 5),
    ("golf-club-swing", "golf-club-swing", 5),
    )

# legal anims per type
# BottomFeeder (C) Law 1
bf = (
    ("pickpocket", "pickpocket", 5),
    ("rubber-stamp", "rubber-stamp", 5),
    ("shredder", "shredder", 3.5),
    ("watercooler", "watercooler", 5),
    ("throw-paper", "throw-paper", 3.5),    #added for lawbot boss battle
    )
# BloodSucker (B) Law 2
b = (
    ("effort", "effort", 5),
    ("throw-paper", "throw-paper", 5),
    ("throw-object", "throw-object", 5),
    ("magic1", "magic1", 5), # also used as place holder for liquidate (glower anim)
    )
# DoubleTalker (A) Law 3
dt = (
    # TODO:
    # Neither of these are right...
    # They should be all talk attacks...
    # But until we have the talk animations,
    # these will stay...
    ("rubber-stamp", "rubber-stamp", 5),
    ("throw-paper", "throw-paper", 5),
    ("speak", "speak", 5),
    ("finger-wag", "fingerwag", 5), # place holder for speak animation, won't need it
    ("throw-paper", "throw-paper", 5),    #added for lawbot boss battle
    )

# AmbulanceChaser (B) Law 4
ac = (
    ("throw-object", "throw-object", 5),
    ("roll-o-dex", "roll-o-dex", 5),
    ("stomp", "stomp", 5),
    ("phone", "phone", 5),
    ("throw-paper", "throw-paper", 5),    #added for lawbot boss battle
    )

# Back Stabber (A) Law 5
bs = (
    ("magic1", "magic1", 5),
    ("throw-paper", "throw-paper", 5),
    ("finger-wag", "fingerwag", 5),
    )

# Spin Doctor (B) Law 6
sd = (
    ("magic2", "magic2", 5),
    ("quick-jump", "jump", 6),
    ("stomp", "stomp", 5),
    ("magic3", "magic3", 5),
    ("hold-pencil", "hold-pencil", 5),
    ("throw-paper", "throw-paper", 5),    #added for lawbot boss battle
    )

# Legal Eagle (A) Law 7
le = (
    ("speak", "speak", 5),
    ("throw-object", "throw-object", 5),
    ("glower", "glower", 5),
    ("throw-paper", "throw-paper", 5),     #added for lawbot boss battle
    )

# Big Wig (A) Law 8
bw = (
    ("finger-wag", "fingerwag", 5), # just as default for now
    ("cigar-smoke", "cigar-smoke", 8),
    ("gavel", "gavel", 8), # incomplete?
    ("magic1", "magic1", 5),
    ("throw-object", "throw-object", 5),
    ("throw-paper", "throw-paper", 5),     #added for lawbot boss battle
    )

if not ConfigVariableBool('want-new-cogs', 0).getValue():
    ModelDict = {
     "a": ("/models/char/suitA-", 4),
     "b": ("/models/char/suitB-", 4),
     "c": ("/models/char/suitC-", 3.5),
     }

    TutorialModelDict = {
     "a": ("/models/char/suitA-", 4),
     "b": ("/models/char/suitB-", 4),
     "c": ("/models/char/suitC-", 3.5),
     }
else:
    ModelDict = {
     "a": ("/models/char/tt_a_ene_cga_", 4),
     "b": ("/models/char/tt_a_ene_cgb_", 4),
     "c": ("/models/char/tt_a_ene_cgc_", 3.5),
     }

    TutorialModelDict = {
     "a": ("/models/char/tt_a_ene_cga_", 4),
     "b": ("/models/char/tt_a_ene_cgb_", 4),
     "c": ("/models/char/tt_a_ene_cgc_", 3.5),
     }

HeadModelDict = {
    "a": ("/models/char/suitA-", 4),
    "b": ("/models/char/suitB-", 4),
    "c": ("/models/char/suitC-", 3.5),
    }
    
PreloadedModelPaths = {}

# We store all of the attributes for how a suit is 
# constructed here. This is for a easier time managing the data.
# And because it's cleaner then a damn else if statement would be.
SuitAttributes = {
    # Format: Suit Scale, Hand Color, Head Color, Suit Heads, Suit Head Texture, Suit Height
    
    # Corporate Department
    
    # Flunky
    "f": (4.0 / cSize, SuitDNA.corpPolyColor, None, ("flunky",  "glasses",), None, 4.88),
    # Pencil Pusher
    "p": (3.35 / bSize, SuitDNA.corpPolyColor, None, ("pencilpusher",), None, 5.00),
    # Yes Man
    "ym": (4.125 / aSize, SuitDNA.corpPolyColor, None, ("yesman",), None, 5.28),
    # Micromanager
    "mm": (2.5 / cSize, SuitDNA.corpPolyColor, None, ("micromanager",), None, 3.25),
    # Downsizer - DEFAULT
    "ds": (4.5 / bSize, SuitDNA.corpPolyColor, None, ("beancounter",), None, 6.08),
    # Head Hunter
    "hh": (6.5 / aSize, SuitDNA.corpPolyColor, None, ("headhunter",), None, 7.45),
    # Corporate Raider
    "cr": (6.75 / cSize, VBase4(0.85, 0.55, 0.55, 1.0), None, ("flunky",), "corporate-raider.txo", 8.23),
    # The Big Cheese
    "tbc": (7.0 / aSize, VBase4(0.75, 0.95, 0.75, 1.0), None, ("bigcheese",), None, 9.34),
    
    # Legal Department
    
    # Bottom Feeder
    "bf": (4.0 / cSize, SuitDNA.legalPolyColor, None, ("tightwad",), "bottom-feeder.txo", 4.81),
    # Blood Sucker
    "b": (4.375 / bSize, VBase4(0.95, 0.95, 1.0, 1.0), None, ("movershaker",), "blood-sucker.txo", 6.17),
    # Double Talker
    "dt": (4.25 / aSize, SuitDNA.legalPolyColor, None, ("twoface",), "double-talker.txo", 5.63),
    # Ambulance Chaser
    "ac": (4.35 / bSize, SuitDNA.legalPolyColor, None, ("ambulancechaser",), None, 6.39),
    # Back Stabber
    "bs": (4.5 / aSize, SuitDNA.legalPolyColor, None, ("backstabber",), None, 6.71),
    # Spin Doctor
    "sd": (5.65 / bSize, VBase4(0.5, 0.8, 0.75, 1.0), None, ("telemarketer",), "spin-doctor.txo", 7.90),
    # Legal Eagle
    "le": (7.125 / aSize, VBase4(0.25, 0.25, 0.5, 1.0), None, ("legaleagle",), None, 8.27),
    # Bigwig
    "bw": (7.0 / aSize, SuitDNA.legalPolyColor, None, ("bigwig",), None, 8.69),
    
    # Money Department
    
    # Short Change
    "sc": (3.6 / cSize, SuitDNA.moneyPolyColor, None, ("coldcaller",), None, 4.77),
    # Penny Pincher
    "pp": (3.55 / aSize, VBase4(1.0, 0.5, 0.6, 1.0), None, ("pennypincher",), None, 5.26),
    # Tightwad
    "tw": (4.5 / cSize, SuitDNA.moneyPolyColor, None, ("tightwad",), None, 5.41),
    # Bean Counter
    "bc": (4.4 / bSize, SuitDNA.moneyPolyColor, None, ("beancounter",), None, 5.95),
    # Number Cruncher
    "nc": (5.25 / aSize, SuitDNA.moneyPolyColor, None, ("numbercruncher",), None, 7.22),
    # Money Bags
    "mb": (5.3 / cSize, SuitDNA.moneyPolyColor, None, ("moneybags",), None, 6.97),
    # Loan Shark
    "ls": (6.5 / bSize, VBase4(0.5, 0.85, 0.75, 1.0), None, ("loanshark",), None, 8.58),
    # Robber Baron
    "rb": (7.0 / aSize, SuitDNA.moneyPolyColor, None, ("yesman",), "robber-baron.txo", 8.95),
    
    # Sales Department
    
    # Cold Caller
    "cc": (3.5 / cSize, VBase4(0.55, 0.65, 1.0, 1.0), VBase4(0.25, 0.35, 1.0, 1.0), ("coldcaller",), None, 4.63),
    # Telemarketer
    "tm": (3.75 / bSize, SuitDNA.salesPolyColor, None, ("telemarketer",), None, 5.24),
    # Name Dropper
    "nd": (4.35 / aSize, SuitDNA.salesPolyColor, None, ("numbercruncher",), "name-dropper.txo", 5.98),
    # Glad Hander
    "gh": (4.75 / cSize, SuitDNA.salesPolyColor, None, ("gladhander",), None, 6.40),
    # Mover & Shaker
    "ms": (4.75 / bSize, SuitDNA.salesPolyColor, None, ("movershaker",), None, 6.70),
    # Two-Face
    "tf": (5.25 / aSize, SuitDNA.salesPolyColor, None, ("twoface",), None, 6.95),
    # The Mingler
    "m": (5.75 / aSize, SuitDNA.salesPolyColor, None, ("twoface",), "mingler.txo", 7.61),
    # Mr. Hollywood
    "mh": (7.0 / aSize, SuitDNA.salesPolyColor, None, ("yesman",), None, 8.95),
}

def loadTutorialSuit():
    """
    Preload the tutorial suit (Flunky)
    """
    loader.loadModel("phase_3.5/models/char/suitC-mod").node()
    loadDialog(1)

def loadSuits(level):
    """loadSuits(int)
    Preload all suit anims and models for given suit level.
    """
    loadSuitModelsAndAnims(level, flag = 1)
    loadDialog(level)

def unloadSuits(level):
    """unloadSuits(int)
    Unload all suit anims and models for given suit level.
    """
    loadSuitModelsAndAnims(level, flag = 0)
    unloadDialog(level)

def loadSuitModelsAndAnims(level, flag = 0):
    """
    Load (flag = 1) or unload (flag = 0) all suit anims and
    models for given suit level.
    """
    # print("print loading level %d suits..." % level)

    for key in list(ModelDict.keys()):
        # load/unload the models
        # All the mods are in 3.5 now, except the suita and B headsd which are in 4
        model, phase = ModelDict[key]
        if ConfigVariableBool('want-new-cogs', 0).getValue():
            headModel, headPhase = HeadModelDict[key]
        else:
            headModel, headPhase = ModelDict[key]
        if flag:
            if ConfigVariableBool('want-new-cogs', 0).getValue():
                filepath = "phase_3.5" + model + "zero"
                if cogExists(model + "zero.bam"):
                    loader.loadModel(filepath).node()
            else:
                filepath = "phase_3.5" + model + "mod"
                PreloadedModelPaths[filepath] = loader.loadModel("phase_3.5" + model + "mod")
            filepath = "phase_" + str(headPhase) + headModel + "heads"
            PreloadedModelPaths[filepath] = loader.loadModel(filepath)
        else:
            if ConfigVariableBool('want-new-cogs', 0).getValue():
                filepath = "phase_3.5" + model + "zero"
                if cogExists(model + "zero.bam"):
                    loader.unloadModel(filepath)
            else:
                filepath = "phase_3.5" + model + "mod"
                if filepath in PreloadedModelPaths:
                    del PreloadedModelPaths[filepath]
                loader.unloadModel(filepath)
            filepath = "phase_" + str(headPhase) + headModel + "heads"
            if filepath in PreloadedModelPaths:
                del PreloadedModelPaths[filepath]
            loader.unloadModel(filepath)


def cogExists(filePrefix):
    searchPath = DSearchPath()
    if AppRunnerGlobal.appRunner:
        # In the web-publish runtime, it will always be here:
        searchPath.appendDirectory(Filename.expandFrom('$TT_3_5_ROOT/phase_3.5'))
    else:
        # In other environments, including the dev environment, look here:
        basePath = os.path.expandvars("$TTMODELS") or "./ttmodels"
        searchPath.appendDirectory(Filename.fromOsSpecific(basePath + "/built/phase_3.5"))
    filePrefix = filePrefix.strip("/")
    pfile = Filename(filePrefix)
    found = vfs.resolveFilename(pfile, searchPath)
    if not found:
        return False
    return True


def loadSuitAnims(suit, flag = 1):
    """loadSuitAnims(string, int):
    Load or unload (flag = 1 or 0) the special anims for the given suit.
    Expects strings as in SuitDNA.suitHeadTypes.
    """
    # make sure its a valid name
    if (suit in SuitDNA.suitHeadTypes):
        # map the name to an animList
        try:
            animList = eval(suit)
        except NameError:
            # no suit specific anims defined
            animList = ()
    else:
        print("Invalid suit name: ", suit)
        return -1

    # process the animList
    for anim in animList:
        phase = "phase_" + str(anim[2])
        filePrefix = ModelDict[bodyType][0]
        animName = filePrefix + anim[1]
        if flag:
            loader.loadModel(animName).node()
        else:
            loader.unloadModel(animName)


def loadDialog(level):
    # use the new dialog
    global SuitDialogArray
    if len(SuitDialogArray) > 0:
        return

    loadPath = "phase_3.5/audio/dial/"
    SuitDialogFiles = [ "COG_VO_grunt",
                        "COG_VO_murmur",
                        "COG_VO_statement",
                        "COG_VO_question"
                        ]

    # load the audio files and store into the dialogue array
    for file in SuitDialogFiles:
        SuitDialogArray.append(base.loader.loadSfx(loadPath + file + ".mp3"))
    SuitDialogArray.append(SuitDialogArray[2])
    SuitDialogArray.append(SuitDialogArray[2])

def loadSkelDialog():
    # use the new dialog
    global SkelSuitDialogArray
    if len(SkelSuitDialogArray) > 0:
        return

    grunt = loader.loadSfx('phase_5/audio/sfx/Skel_COG_VO_grunt.mp3')
    murmur = loader.loadSfx('phase_5/audio/sfx/Skel_COG_VO_murmur.mp3')
    statement = loader.loadSfx('phase_5/audio/sfx/Skel_COG_VO_statement.mp3')
    question = loader.loadSfx('phase_5/audio/sfx/Skel_COG_VO_question.mp3')
    SkelSuitDialogArray = [grunt, murmur, statement, question, statement, statement]

def unloadDialog(level):
    global SuitDialogArray
    SuitDialogArray = []

def unloadSkelDialog():
    global SkelSuitDialogArray
    SkelSuitDialogArray = []

def attachSuitHead(node, suitName):
    """ gets a suit head whose scale and vertical pos has been
    normalized to all the suit heads
    NOTE:  calling class is responsible for cleaning this up!
    (eg. self.head = None)
    """
    suitIndex = SuitDNA.suitHeadTypes.index(suitName)
    suitDNA = SuitDNA.SuitDNA()
    suitDNA.newSuit(suitName)
    suit = Suit()
    suit.setDNA(suitDNA)
    headParts = suit.getHeadParts()
    head = node.attachNewNode('head')
    for part in headParts:
        copyPart = part.copyTo(head)
        # turn on depth write and test.
        copyPart.setDepthTest(1)
        copyPart.setDepthWrite(1)
    suit.delete()
    suit = None
    p1 = Point3()
    p2 = Point3()
    head.calcTightBounds(p1, p2)
    d = p2 - p1
    biggest = max(d[0], d[2])
    # make them ramp up slightly in size as we go down the row
    column = (suitIndex % SuitDNA.suitsPerDept)
    s = (0.2 + (column / 100.0)) / biggest
    # also make them move down slightly as we go across
    pos = -0.14 + ((SuitDNA.suitsPerDept - column - 1) / 135.0)
    head.setPosHprScale(0, 0, pos,
                        180, 0, 0,
                        s, s, s)
    return head

class Suit(Avatar.Avatar):
    """Suit class:"""
    
    notify = DirectNotifyGlobal.directNotify.newCategory('Suit')

    healthColors = (Vec4(0, 1, 0, 1),
                    Vec4(1, 1, 0, 1),
                    Vec4(1, 0.5, 0, 1),
                    Vec4(1, 0, 0, 1),
                    Vec4(0.3, 0.3, 0.3, 1))
    healthGlowColors = (Vec4(0.25, 1, 0.25, 0.5),
                    Vec4(1, 1, 0.25, 0.5),
                    Vec4(1, 0.5, 0.25, 0.5),
                    Vec4(1, 0.25, 0.25, 0.5),
                    Vec4(0.3, 0.3, 0.3, 0))
    medallionColors = {
        # Corporate
        'c' : Vec4(0.863, 0.776, 0.769, 1.000),
        # Sales
        's' : Vec4(0.843, 0.745, 0.745, 1.000),
        # Legal
        'l' : Vec4(0.749, 0.776, 0.824, 1.000),
        # Marketing
        'm' : Vec4(0.749, 0.769, 0.749, 1.000),
        }

    def __init__(self):
        try:
            self.Suit_initialized
            return
        except:
            self.Suit_initialized = 1

        Avatar.Avatar.__init__(self)
        self.setFont(ToontownGlobals.getSuitFont())
        self.setPlayerType(NametagGroup.CCSuit)

        # Suits are now pickable
        self.setPickable(1)

        self.leftHand = None
        self.rightHand = None
        self.shadowJoint = None
        self.nametagJoint = None
        self.headParts = []
        self.healthBar = None
        self.healthCondition = 0
        self.isDisguised = 0
        self.isWaiter = 0

    def delete(self):
        try:
            self.Suit_deleted
            return
        except:
            self.Suit_deleted = 1
            
        if self.leftHand:
            self.leftHand.removeNode()
            self.leftHand = None
        if self.rightHand:
            self.rightHand.removeNode()
            self.rightHand = None
        if self.shadowJoint:
            self.shadowJoint.removeNode()
            self.shadowJoint = None
        if self.nametagJoint:
            self.nametagJoint.removeNode()
            self.nametagJoint = None
        for part in self.headParts:
            part.removeNode()
        self.headParts = []
        self.removeHealthBar()
        Avatar.Avatar.delete(self)

    def setHeight(self, height):
        Avatar.Avatar.setHeight(self, height)

        # Put our name tag higher, since it has three lines...
        self.nametag3d.setPos(0, 0, height + 1.0)

    def getRadius(self):
        # Suits have a fatter collision volume than toons.
        return 2

    def setDNAString(self, dnaString):
        self.dna = SuitDNA.SuitDNA()
        self.dna.makeFromNetString(dnaString)
        self.setDNA(self.dna)

    def setDNA(self, dna):
        if self.style:
            return

        # store the DNA
        self.style = dna

        self.generateSuit()

        # this no longer works in the Avatar init!
        # I moved it here for lack of a better place
        # make the drop shadow
        self.initializeDropShadow()
        self.initializeNametag3d()

    def generateSuit(self):
        """
        Create a suit from dna (an array of strings)
        """

        dna = self.style
        self.headParts = []

        # most heads do not need different poly color or texture
        self.headColor = None
        self.headTexture = None

        # For suit death animation
        self.loseActor = None

        # Have we become a skelecog?
        self.isSkeleton = 0

        # Suit heights have been determined empirically; see
        # RoguesGallery.py or the magic word ~rogues.
        
        self.scale, self.handColor, self.headColor, heads, self.headTexture, height = SuitAttributes[dna.name]
        self.generateBody()
        for head in heads:
            self.generateHead(head)
        self.setHeight(height)

        self.setName(SuitBattleGlobals.SuitAttributes[dna.name]['name'])
        self.getGeomNode().setScale(self.scale)
        self.generateHealthBar()
        self.generateCorporateMedallion()

    def generateBody(self):
        """
        Load the appropriate suit body and anims
        """
        # get the anims
        animDict = self.generateAnimDict()

        # NOTE: It is always phase 3.5 because the models are there
        # while everything else is in phase 5.
        filePrefix, bodyPhase = ModelDict[self.style.body]
        if ConfigVariableBool('want-new-cogs', 0).getValue():
            if cogExists(filePrefix + "zero.bam"):
                self.loadModel("phase_3.5" + filePrefix + "zero")
            else:
                self.loadModel("phase_3.5" + filePrefix + "mod")
        else:
            filepath = "phase_3.5" + filePrefix + "mod"
            if filepath in PreloadedModelPaths:
                self.loadModel(PreloadedModelPaths[filepath])
            else:
                self.loadModel(filepath)
        self.loadAnims(animDict)
        self.setSuitClothes()

    def generateAnimDict(self):
        # compile a dictionary of all anims for this suit in the format
        # { "animName" : "animFilePath", ... }
        animDict = {}

        filePrefix, bodyPhase = ModelDict[self.style.body]

        # load all shared anims
        for anim in AllSuits:
            # a=4, b=4, c=3.5
            animDict[anim[0]] = "phase_" + str(bodyPhase) + filePrefix + anim[1]
        for anim in AllSuitsMinigame:
            # a=4, b=4, c=4
            animDict[anim[0]] = "phase_4" + filePrefix + anim[1]
        for anim in AllSuitsTutorialBattle:
            # a = 4, b = 4, c = 3.5
            filePrefix, bodyPhase = TutorialModelDict[self.style.body]
            animDict[anim[0]] = "phase_" + str(bodyPhase) + filePrefix + anim[1]
        for anim in AllSuitsBattle:
            # a=5, b=5, c=5
            animDict[anim[0]] = "phase_5" + filePrefix + anim[1]

        if not ConfigVariableBool('want-new-cogs', 0).getValue():
            if self.style.body == 'a':
                animDict['neutral'] = 'phase_4/models/char/suitA-neutral'
                # add the CEO battle specific anims
                for anim in SuitsCEOBattle:
                    animDict[anim[0]] = "phase_12/models/char/suitA-" + anim[1]
            elif self.style.body == 'b':
                animDict['neutral'] = 'phase_4/models/char/suitB-neutral'
                # add the CEO battle specific anims
                for anim in SuitsCEOBattle:
                    animDict[anim[0]] = "phase_12/models/char/suitB-" + anim[1]
            elif self.style.body == 'c':
                animDict['neutral'] = 'phase_3.5/models/char/suitC-neutral'
                # add the CEO battle specific anims
                for anim in SuitsCEOBattle:
                    animDict[anim[0]] = "phase_12/models/char/suitC-" + anim[1]

        # load the suit specific anims
        try:
            animList = eval(self.style.name)
        except NameError:
            # no suit specific anims defined
            animList = ()

        for anim in animList:
            phase = "phase_" + str(anim[2])
            animDict[anim[0]] = phase + filePrefix + anim[1]

        return animDict

    def initializeBodyCollisions(self, collIdStr):
        Avatar.Avatar.initializeBodyCollisions(self, collIdStr)

        if not self.ghostMode:
            self.collNode.setCollideMask(self.collNode.getIntoCollideMask() | ToontownGlobals.PieBitmask)

    def setSuitClothes(self, modelRoot=None):
        """
        Set the appropriate textures for this suit dept.
        """
        # default to setting textures on ourselves
        if not modelRoot:
            modelRoot = self

        dept = self.style.dept
        phase = 3.5

        def __doItTheOldWay__():
            # set the clothes textures for the suit dept
            torsoTex = loader.loadTexture("phase_%s/maps/%s_blazer.txo" % (phase, dept))
            torsoTex.setMinfilter(Texture.FTLinearMipmapLinear)
            torsoTex.setMagfilter(Texture.FTLinear)
            legTex = loader.loadTexture("phase_%s/maps/%s_leg.txo" % (phase, dept))
            legTex.setMinfilter(Texture.FTLinearMipmapLinear)
            legTex.setMagfilter(Texture.FTLinear)
            armTex = loader.loadTexture("phase_%s/maps/%s_sleeve.txo" % (phase, dept))
            armTex.setMinfilter(Texture.FTLinearMipmapLinear)
            armTex.setMagfilter(Texture.FTLinear)

            modelRoot.find("**/torso").setTexture(torsoTex, 1)
            modelRoot.find("**/arms").setTexture(armTex, 1)
            modelRoot.find("**/legs").setTexture(legTex, 1)

            # set hand color
            modelRoot.find("**/hands").setColor(self.handColor)

            # find the useful nulls
            self.leftHand = self.find("**/joint*Lhold")
            self.rightHand = self.find("**/joint*Rhold")
            self.shadowJoint = self.find("**/joint*shadow")
            self.nametagJoint = self.find("**/joint*nameTag")
            
        if modelRoot.find("**/body").isEmpty():
            __doItTheOldWay__()
            return

        if dept == 'c':
            texType = 'bossbot'
        elif dept == 'm':
            texType = 'cashbot'
        elif dept == 'l':
            texType = 'lawbot'
        elif dept == 's':
            texType = 'sellbot'

        # set the clothes textures for the suit dept
        filepath = "phase_3.5/maps/tt_t_ene_" + texType + '.txo'
        if cogExists("/maps/tt_t_ene_" + texType + '.txo'):
            bodyTex = loader.loadTexture(filepath)
            modelRoot.find("**/body").setTexture(bodyTex, 1)
        # find the useful nulls
        if not self.find("**/def_joint_left_hold").isEmpty():
            self.leftHand = self.find("**/def_joint_left_hold")
            self.rightHand = self.find("**/def_joint_right_hold")
            self.shadowJoint = self.find("**/def_shadow")
            self.nametagJoint = self.find("**/def_nameTag")
        else:
            self.leftHand = self.find("**/joint*Lhold")
            self.rightHand = self.find("**/joint*Rhold")
            self.shadowJoint = self.find("**/joint*shadow")
            self.nametagJoint = self.find("**/joint*nameTag")


    def makeWaiter(self, modelRoot=None):
        """
        Set the appropriate textures for a bosscog battle waiter
        """
        # default to setting textures on ourselves
        if not modelRoot:
            modelRoot = self
            
        def __doItTheOldWay__():
            # set the clothes textures for a waiter
            torsoTex = loader.loadTexture("phase_3.5/maps/waiter_m_blazer.txo")
            torsoTex.setMinfilter(Texture.FTLinearMipmapLinear)
            torsoTex.setMagfilter(Texture.FTLinear)
            legTex = loader.loadTexture("phase_3.5/maps/waiter_m_leg.txo")
            legTex.setMinfilter(Texture.FTLinearMipmapLinear)
            legTex.setMagfilter(Texture.FTLinear)
            armTex = loader.loadTexture("phase_3.5/maps/waiter_m_sleeve.txo")
            armTex.setMinfilter(Texture.FTLinearMipmapLinear)
            armTex.setMagfilter(Texture.FTLinear)

            modelRoot.find("**/torso").setTexture(torsoTex, 1)
            modelRoot.find("**/arms").setTexture(armTex, 1)
            modelRoot.find("**/legs").setTexture(legTex, 1)

            # set hand color
            modelRoot.find("**/hands").setColor(self.handColor)
            
        self.isWaiter = 1
            
        if modelRoot.find("**/body").isEmpty():
            __doItTheOldWay__()
            return

        filepath = "phase_3.5/maps/tt_t_ene_waiter.txo"
        if cogExists("/maps/tt_t_ene_waiter.txo"):
            bodyTex = loader.loadTexture(filepath)
            modelRoot.find("**/body").setTexture(bodyTex, 1)


    def makeRentalSuit(self, suitType, modelRoot = None):
        if not modelRoot:
            modelRoot = self.getGeomNode()

        def __doItTheOldWay__():
            if suitType == 's':
                torsoTex = loader.loadTexture("phase_3.5/maps/tt_t_ene_sellbotRental_blazer.txo")
                legTex = loader.loadTexture("phase_3.5/maps/tt_t_ene_sellbotRental_leg.txo")
                armTex = loader.loadTexture("phase_3.5/maps/tt_t_ene_sellbotRental_sleeve.txo")
                handTex = loader.loadTexture("phase_3.5/maps/tt_t_ene_sellbotRental_hand.txo")
#            elif suitType == 'l':
#                torsoTex = loader.loadTexture("phase_3.5/maps/tt_t_ene_lawbotRental_blazer.txo")
#                legTex = loader.loadTexture("phase_3.5/maps/tt_t_ene_lawbotRental_leg.txo")
#                armTex = loader.loadTexture("phase_3.5/maps/tt_t_ene_lawbotRental_sleeve.txo")
#                handTex = loader.loadTexture("phase_3.5/maps/tt_t_ene_lawbotRental_hand.txo")
            else:
                self.notify.warning("No rental suit for cog type %s" % suitType)
                return
            modelRoot.find("**/torso").setTexture(torsoTex, 1)
            modelRoot.find("**/arms").setTexture(armTex, 1)
            modelRoot.find("**/legs").setTexture(legTex, 1)
            modelRoot.find("**/hands").setTexture(handTex, 1)
            
        self.isRental = 1
        
        if modelRoot.find("**/body").isEmpty():
            __doItTheOldWay__()
            return
         
        if suitType == 's':
            filepath = "phase_3.5/maps/tt_t_ene_sellbotRental.txo"
#        elif suitType == 'l':
#            filepath = "phase_3.5/maps/tt_t_ene_lawbotRental.txo"
        else:
            self.notify.warning("No rental suit for cog type %s" % suitType)
            return
            
        if cogExists(filepath):
            bodyTex = loader.loadTexture(filepath)
            modelRoot.find("**/body").setTexture(bodyTex, 1)


    def generateHead(self, headType):
        """generateHead(self, string)
        Manipulate the head model to display only the appropriate head
        """
        
        # load the multi-head models
        if ConfigVariableBool('want-new-cogs', 0).getValue():
            filePrefix, phase = HeadModelDict[self.style.body]
        else:
            filePrefix, phase = ModelDict[self.style.body]
        
        filepath = "phase_" + str(phase) + filePrefix + "heads"
        # If for some reason the head is empty, IE: Flunky Glasses. 
        # We can't use the preloaded model path.
        if filepath in PreloadedModelPaths and not PreloadedModelPaths[filepath].isEmpty():
            headModel = PreloadedModelPaths[filepath]
        else:
            headModel = loader.loadModel(filepath)

        # search for the appropriate parts
        headReferences = headModel.findAllMatches("**/" + headType)
        for i in range(0, headReferences.getNumPaths()):
            if ConfigVariableBool('want-new-cogs', 0).getValue():
                headPart = self.instance(headReferences.getPath(i), "modelRoot",
                                         "to_head")
                if not headPart:
                    headPart = self.instance(headReferences.getPath(i), "modelRoot",
                                             "joint*head")
            else:
                headPart = self.instance(headReferences.getPath(i), "modelRoot",
                                         "joint*head")
            # set head texture if necessary
            if self.headTexture:
                headTex = loader.loadTexture("phase_" + str(phase) + "/maps/" +
                                             self.headTexture)
                headTex.setMinfilter(Texture.FTLinearMipmapLinear)
                headTex.setMagfilter(Texture.FTLinear)
                headPart.setTexture(headTex, 1)

            # set head color if necessary
            if self.headColor:
                headPart.setColor(self.headColor)
                
            self.headParts.append(headPart)

        # Now remove the extra instance that was created in the
        # loadModelOnce call; we don't need it anymore now that we've
        # copied everything out.
        headModel.removeNode()

    def generateCorporateTie(self, modelPath=None):
        if not modelPath:
            modelPath = self
        dept = self.style.dept
        tie = modelPath.find('**/tie')
        if tie.isEmpty():
            self.notify.warning('skelecog has no tie model!!!')
            return
        #print('### loading %s tie' % (dept))
        if dept == 'c':
            tieTex = loader.loadTexture("phase_5/maps/cog_robot_tie_boss.txo")
        elif dept == 's':
            tieTex = loader.loadTexture("phase_5/maps/cog_robot_tie_sales.txo")
        elif dept == 'l':
            tieTex = loader.loadTexture("phase_5/maps/cog_robot_tie_legal.txo")
        elif dept == 'm':
            tieTex = loader.loadTexture("phase_5/maps/cog_robot_tie_money.txo")
        tieTex.setMinfilter(Texture.FTLinearMipmapLinear)
        tieTex.setMagfilter(Texture.FTLinear)
        tie.setTexture(tieTex, 1)

    def generateCorporateMedallion(self):
        icons = loader.loadModel('phase_3/models/gui/cog_icons')
        dept = self.style.dept
        if ConfigVariableBool('want-new-cogs', 0).getValue():
            chestNull = self.find('**/def_joint_attachMeter')
            if chestNull.isEmpty():
                chestNull = self.find('**/joint*attachMeter')
        else:
            chestNull = self.find('**/joint*attachMeter')
        if dept == 'c':
            self.corpMedallion = icons.find('**/CorpIcon').copyTo(chestNull)
        elif dept == 's':
            self.corpMedallion = icons.find('**/SalesIcon').copyTo(chestNull)
        elif dept == 'l':
            self.corpMedallion = icons.find('**/LegalIcon').copyTo(chestNull)
        elif dept == 'm':
            self.corpMedallion = icons.find('**/MoneyIcon').copyTo(chestNull)
        self.corpMedallion.setPosHprScale(0.02, 0.05, 0.04,
                                          180.00, 0.00, 0.00,
                                          0.51, 0.51, 0.51)
        self.corpMedallion.setColor(self.medallionColors[dept])
        icons.removeNode()

    def generateHealthBar(self):
        """
        Create a health meter for the suit and put it on his chest
        """
        self.removeHealthBar()

        # Create health button for the suit
        model = loader.loadModel('phase_3.5/models/gui/matching_game_gui')
        button = model.find('**/minnieCircle')
        button.setScale(3.0)
        button.setH(180.0)
        button.setColor(self.healthColors[0])
        if ConfigVariableBool('want-new-cogs', 0).getValue():
            chestNull = self.find('**/def_joint_attachMeter')
            if chestNull.isEmpty():
                chestNull = self.find('**/joint*attachMeter')
        else:
            chestNull = self.find('**/joint*attachMeter')
        button.reparentTo(chestNull)
        self.healthBar = button
        glow = BattleProps.globalPropPool.getProp('glow')
        glow.reparentTo(self.healthBar)
        glow.setScale(0.28)
        glow.setPos(-0.005, 0.01, 0.015)
        glow.setColor(self.healthGlowColors[0])
        button.flattenLight()

        self.healthBarGlow = glow
        self.healthBar.hide()
        self.healthCondition = 0

    def reseatHealthBarForSkele(self):
        self.healthBar.setPos(0.0, 0.1, 0.0)

    def updateHealthBar(self, hp, forceUpdate=0):
        if (hp > self.currHP):
            hp = self.currHP
        self.currHP -= hp

        health = float(self.currHP) / float(self.maxHP)
        if (health > 0.95):
            condition = 0
        elif (health > 0.7):
            condition = 1
        elif (health > 0.3):
            condition = 2
        elif (health > 0.05):
            condition = 3
        elif (health > 0.0):
            # This should be blinking red
            condition = 4
        else:
            # This should be blinking red even faster
            condition = 5

        if (self.healthCondition != condition) or forceUpdate:
            if (condition == 4):
                blinkTask = Task.loop(Task(self.__blinkRed),
                                      Task.pause(0.75),
                                      Task(self.__blinkGray),
                                      Task.pause(0.1))
                taskMgr.add(blinkTask, self.uniqueName('blink-task'))
            elif (condition == 5):
                if (self.healthCondition == 4):
                    taskMgr.remove(self.uniqueName('blink-task'))
                blinkTask = Task.loop(Task(self.__blinkRed),
                                      Task.pause(0.25),
                                      Task(self.__blinkGray),
                                      Task.pause(0.1))
                taskMgr.add(blinkTask, self.uniqueName('blink-task'))
            else:
                self.healthBar.setColor(self.healthColors[condition], 1)
                self.healthBarGlow.setColor(self.healthGlowColors[condition], 1)
            self.healthCondition = condition

    def __blinkRed(self, task):
        self.healthBar.setColor(self.healthColors[3], 1)
        self.healthBarGlow.setColor(self.healthGlowColors[3], 1)
        if (self.healthCondition == 5):
            self.healthBar.setScale(1.17)
        return Task.done

    def __blinkGray(self, task):
        if not self.healthBar:
            return
        self.healthBar.setColor(self.healthColors[4], 1)
        self.healthBarGlow.setColor(self.healthGlowColors[4], 1)
        if (self.healthCondition == 5):
            self.healthBar.setScale(1.0)
        return Task.done

    def removeHealthBar(self):
        if self.healthBar:
            self.healthBar.removeNode()
            self.healthBar = None
        if (self.healthCondition == 4 or self.healthCondition == 5):
            taskMgr.remove(self.uniqueName('blink-task'))
        self.healthCondition = 0

    # the lose actor is seperate cog geometry intended for explosions only
    def getLoseActor(self):
        """
        Return the lose geometry and anim for this type of suit
        as an actor. If we are a skelecog, get that lose actor instead
        """
        if ConfigVariableBool('want-new-cogs', 0).getValue():
            if self.find("**/body"):
                return self
        if (self.loseActor == None):
            if not self.isSkeleton:
                # standard cog
                filePrefix, phase = TutorialModelDict[self.style.body]
                loseModel = "phase_" + str(phase) + filePrefix + "lose-mod"
                loseAnim = "phase_" + str(phase) + filePrefix + "lose"

                # make the actor
                self.loseActor = Actor.Actor(loseModel, {"lose":loseAnim})

                # copy the current head to the lose actor
                loseNeck = self.loseActor.find("**/joint*head")
                for part in self.headParts:
                    part.instanceTo(loseNeck)

                # put the appropriate textures on the suit
                if self.isWaiter:
                    self.makeWaiter(self.loseActor)
                else:
                    self.setSuitClothes(self.loseActor)
            else:
                # skelecog
                loseModel = "phase_5/models/char/cog" + self.style.body.upper() + "_robot-lose-mod"
                filePrefix, phase = TutorialModelDict[self.style.body]
                loseAnim = "phase_" + str(phase) + filePrefix + "lose"

                # make the actor
                self.loseActor = Actor.Actor(loseModel, {"lose":loseAnim})

                # set the appropriate tie texture
                self.generateCorporateTie(self.loseActor)

        # set the scale on the lose actor
        self.loseActor.setScale(self.scale)

        # put lose actor where actor is
        self.loseActor.setPos(self.getPos())
        self.loseActor.setHpr(self.getHpr())

        # put a shadow under the lose actor
        if ShadowCaster.globalDropShadowFlag:
            shadowJoint = self.loseActor.find("**/joint*shadow")
            dropShadow = loader.loadModel("phase_3/models/props/drop_shadow")
            dropShadow.setScale(0.45)
            dropShadow.setColor(0.0, 0.0, 0.0, 0.5)
            dropShadow.reparentTo(shadowJoint)

        return(self.loseActor)

    def cleanupLoseActor(self):
        self.notify.debug('cleanupLoseActor()')
        if (self.loseActor != None):
            self.notify.debug('cleanupLoseActor() - got one')
            self.loseActor.cleanup()
        self.loseActor = None

    # the load seperate cog geometry for cogs that become cog skeletons
    def makeSkeleton(self):
        """
        Convert to skeleton geometry.
        """
        model = "phase_5/models/char/cog" + self.style.body.upper() + "_robot-zero"
        anims = self.generateAnimDict()

        # remember the current anim
        anim = self.getCurrentAnim()

        # grab the drop shadow
        dropShadow = self.dropShadow
        if not dropShadow.isEmpty():
            dropShadow.reparentTo(hidden)

        # remove the old geometry
        self.removePart("modelRoot")

        # load the skeleton geometry
        self.loadModel(model)
        self.loadAnims(anims)

        # set the scale on the skeleton actor (plus a little extra to make it look right)
        self.getGeomNode().setScale(self.scale * 1.0173)
        self.generateHealthBar()
        self.generateCorporateMedallion()
        # set the appropriate tie texture
        self.generateCorporateTie()
        self.setHeight(self.height)


        # some of the geometry needs to be backfaced and billboarded
        parts = self.findAllMatches('**/pPlane*')
        for partNum in range(0, parts.getNumPaths()):
            #print('found billboarded part!')
            bb = parts.getPath(partNum)
            bb.setTwoSided(1)

        # redo the nametag and drop shadow
        self.setName(TTLocalizer.Skeleton)
        nameInfo = TTLocalizer.SuitBaseNameWithLevel % {"name":  self._name,
                                                        "dept":  self.getStyleDept(),
                                                        "level": self.getActualLevel(),}
        self.setDisplayName( nameInfo )

        # re-find the useful nulls
        self.leftHand = self.find("**/joint*Lhold")
        self.rightHand = self.find("**/joint*Rhold")
        self.shadowJoint = self.find("**/joint*shadow")
        self.nametagJoint = self.find("**/joint*nameTag")

        if not dropShadow.isEmpty():
            dropShadow.setScale(0.75)
            if not self.shadowJoint.isEmpty():
                dropShadow.reparentTo(self.shadowJoint)

        # start the animation again
        self.loop(anim)

        # set the flag
        self.isSkeleton = 1

    # getters and setters
    def getHeadParts(self):
        """
        Return the list of stored head parts
        """
        return self.headParts

    def getRightHand(self):
        """
        Return the null in the right hand
        """
        return self.rightHand

    def getLeftHand(self):
        """
        Return the null in the left hand
        """
        return self.leftHand

    def getShadowJoint(self):
        """
        Return the node for attaching the shadow
        """
        return self.shadowJoint

    def getNametagJoints(self):
        """
        Return the CharacterJoint that animates the nametag, in a list.
        """
        joints = []
        bundle = self.getPartBundle("modelRoot")
        attach = bundle.findAttachment("joint_nameTag")
        if attach >= 0:
            joints.append((attach, bundle))
        return joints

    def getDialogueArray(self):
        if self.isSkeleton:
            loadSkelDialog()
            return SkelSuitDialogArray
        return SuitDialogArray
