#-------------------------------------------------------------------------------
# Contact: X (Schell Games)
# Created: X, 2010
#
# Purpose: Client-side, creates a cutscene for the laff reward prior to the penthouse battle
#------------------------------------------------------------------------------

from toontown.toonbase.ToontownModules import NodePath, Point3, PlaneNode, TextNode

from direct.interval.IntervalGlobal import *
from direct.showbase.ShowBase import Plane
from direct.directnotify import DirectNotifyGlobal
from direct.showbase.RandomNumGen import RandomNumGen
from direct.interval.MetaInterval import Sequence, Parallel
from direct.interval.FunctionInterval import Func, Wait
from direct.gui.DirectGui import *

from toontown.toonbase.ToontownGlobals import *
from toontown.toonbase import TTLocalizer
from toontown.suit import Suit, SuitDNA
from toontown.toon import Toon, ToonHead, ToonDNA

from .CogdoUtil import CogdoGameMovie
from . import CogdoUtil

class CogdoElevatorMovie(CogdoGameMovie):
    notify = DirectNotifyGlobal.directNotify.newCategory(
        "CogdoElevatorMovie")
    
    # How many seconds pass before the elevator doors open
    elevatorDuration = 5

    def __init__(self):
        CogdoGameMovie.__init__(self)
        
        # Dummy for cutscene
        self._toonDialogueSfx = None
        self.toonHead = None
        self.frame = None

    def displayLine(self, text):
        """
        
        """
        self.notify.debug('displayLine')
        
        # Set the dialog text
        self._dialogueLabel.node().setText(text)
        
        # Parent the toon head to the ui
        self.toonHead.reparentTo(aspect2d)
        
        # Play the dialog sound
        self._toonDialogueSfx.play()
        
        # Render the toon head in front of the ui
        self.toonHead.setClipPlane(self.clipPlane)

    def makeSuit(self, suitType):
        """
        Creates a suit to be used as a cog disguise
        """
        self.notify.debug('makeSuit()')
        
        # Create the suit
        suit = Suit.Suit()
        dna = SuitDNA.SuitDNA()
        dna.newSuit(suitType)
        suit.setStyle(dna)
        
        # Set the suit to be disguised
        suit.isDisguised = 1
        
        # Generate the suit
        suit.generateSuit()
        
        # Adjust its scale and position
        suit.setScale(1, 1, 2)
        suit.setPos(0, 0, -4.4)
        
        # Attach the suit body to the toon head
        suit.reparentTo(self.toonHead)
        
        # Hide the suit's head
        for part in suit.getHeadParts():
            part.hide()
        
        # Set the animation to neutral
        suit.loop('neutral')

    def load(self):
        """
        Creates the cutscene Ui
        """
        self.notify.debug('load()')
        
        CogdoGameMovie.load(self)
        
        # Load the flythru model and find the background and chat bubble 
        backgroundGui = loader.loadModel('phase_5/models/cogdominium/tt_m_gui_csa_flyThru')
        self.bg = backgroundGui.find('**/background')
        self.chatBubble = backgroundGui.find('**/chatBubble')
        
        # Resize the chat bubble
        self.chatBubble.setScale(6.5, 6.5, 7.3)
        self.chatBubble.setPos(0.32, 0, -0.78)
        
        # Resize the background
        self.bg.setScale(5.2)
        self.bg.setPos(0.14, 0, -0.6667)
        self.bg.reparentTo(aspect2d)
        
        # Parent the chat bubble to the ui
        self.chatBubble.reparentTo(aspect2d)
        
        # Create the frame
        self.frame = DirectFrame(
                        geom = self.bg,
                        relief = None,
                        pos = (0.2, 0, -0.6667),
                        )
        
        # Parent the background to it
        self.bg.wrtReparentTo(self.frame)
        
        # Create room title
        self.gameTitleText = DirectLabel(
                                parent = self.frame,
                                text = TTLocalizer.CogdoExecutiveSuiteTitle,
                                scale = TTLocalizer.MRPgameTitleText * 0.8,
                                text_align = TextNode.ACenter,
                                text_font = getSignFont(),
                                text_fg = (1.0, 0.33, 0.33, 1.0),
                                pos = TTLocalizer.MRgameTitleTextPos,
                                relief = None,
                                )
        
        # Parent the title to the frame
        self.chatBubble.wrtReparentTo(self.frame)
        
        # Hide the frame
        self.frame.hide()
        
        # Remove the background Ui
        backgroundGui.removeNode()
        
        # Create the cutscene toon
        self.toonDNA = ToonDNA.ToonDNA()
        self.toonDNA.newToonFromProperties("dss" ,"ss" ,"m" ,"m" ,2 ,0 ,2 ,2 ,1 ,8 ,1 ,8 , 1 ,14 ,)
        self.toonHead = Toon.Toon()
        self.toonHead.setDNA(self.toonDNA)
        
        # Set the disguise to Short Change
        self.makeSuit('sc')
        
        self.toonHead.getGeomNode().setDepthWrite(1)
        self.toonHead.getGeomNode().setDepthTest(1)
        
        # Set the animation to neutral
        self.toonHead.loop('neutral')
        
        # Adjust the position
        self.toonHead.setPosHprScale(-0.73, 0, -1.27, 180, 0, 0, 0.18, 0.18, 0.18)
        
        # Hide the head
        self.toonHead.reparentTo(hidden)
        
        # Start the blink task
        self.toonHead.startBlink()
        
        # Create a plane for the toon head
        self.clipPlane = self.toonHead.attachNewNode(PlaneNode('clip'))
        self.clipPlane.node().setPlane(Plane(0, 0, 1, 0))
        self.clipPlane.setPos(0, 0, 2.45)
        
        # Load the dialog sound
        self._toonDialogueSfx = loader.loadSfx('phase_3.5/audio/dial/AV_dog_long.mp3')
        
        # Create a node for the camera
        self._camHelperNode = NodePath('CamHelperNode')
        self._camHelperNode.reparentTo(render)
        
        # Set the dialog text
        dialogue = TTLocalizer.CogdoElevatorRewardLaff

        def start():
            """
            Starts the cutscene UI
            """
            # Show the UI
            self.frame.show()
            
            # Disable border cells during the cutscene
            base.setCellsAvailable(base.bottomCells + base.leftCells + base.rightCells, 0)

        def end():
            """
            Stops the cutscene UI
            """
            # Hide the dialog
            self._dialogueLabel.reparentTo(hidden)
            
            # Hide the toon head
            self.toonHead.reparentTo(hidden)
            
            # Hide the frame
            self.frame.hide()
            
            # Re-enable border cells
            base.setCellsAvailable(base.bottomCells + base.leftCells + base.rightCells, 1)
            
            # Stop the clock task
            self._stopUpdateTask()

        # Play the cutscene
        self._ival = Sequence(
                        Func(start),
                        Func(self.displayLine, dialogue),
                        Wait(self.elevatorDuration),
                        Func(end),
                        )
        
        # Start the clock task
        self._startUpdateTask()

    def _updateTask(self, task):
        """
        Starts a task to base movement on how much time elapsed
        """
        dt = globalClock.getDt()
        return task.cont

    def unload(self):
        """
        Unload the cutscene
        """
        # Remove the frame
        self.frame.destroy()
        del self.frame

        # Remove the background
        self.bg.removeNode()
        del self.bg

        # Remove the chat bubbles
        self.chatBubble.removeNode()
        del self.chatBubble

        # Stop the blink task and remove the head
        self.toonHead.stopBlink()
        self.toonHead.stop()
        self.toonHead.removeNode()
        self.toonHead.delete()
        del self.toonHead

        # Unload the movie
        CogdoGameMovie.unload(self)
