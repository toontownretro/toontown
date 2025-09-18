#-------------------------------------------------------------------------------
# Contact: X (Schell Games)
# Created: X, 2010
#
# Purpose: Client-side, creates the reward ui showing the player's name and
#          their current and max laff.
#------------------------------------------------------------------------------

from toontown.toonbase.ToontownModules import *

from direct.gui.DirectGui import *

from toontown.toonbase import ToontownGlobals, TTLocalizer

from toontown.cogdominium import CogdoBarrelRoomConsts

class CogdoBarrelRoomRewardPanel(DirectFrame):

    def __init__(self):
        # Create the main frame
        DirectFrame.__init__(
            self,
            relief = None,
            geom = DGG.getDefaultDialogGeom(),
            geom_color = ToontownGlobals.GlobalDialogColor,
            geom_scale = TTLocalizer.RPdirectFrame,
            pos = (0, 0, 0.587)
           )
        self.initialiseoptions(CogdoBarrelRoomRewardPanel)
        
        # Create the title
        self.avNameLabel = DirectLabel(
            parent = self,
            relief = None,
            pos = (0, 0, 0.3),
            # Move to TTLocalizer
            text = "Toon Ups",
            text_scale = 0.08
           )
        
        self.rewardLines = []
        for i in range(CogdoBarrelRoomConsts.MaxToons):
            rewardLine = {}
            
            # Create a sub frame
            rewardLine['frame'] = DirectFrame(
                parent = self,
                relief = None,
                frameSize = (-0.5, 0.5, -0.045, 0.042),
                pos = (0, 0, 0.1 + -0.09 * i)
               )
            
            # Display their name
            rewardLine['name'] = DirectLabel(
                parent = rewardLine['frame'],
                relief = None,
                text = "",
                text_scale = TTLocalizer.RPtrackLabels,
                text_align = TextNode.ALeft,
                pos = (-0.4, 0, 0),
                text_pos = (0, -0.02)
               )
            
            # Display their health
            rewardLine['laff'] = DirectLabel(
                parent = rewardLine['frame'],
                relief = None,
                text = "",
                text_scale = 0.05,
                text_align = TextNode.ARight,
                pos = (0.4, 0, 0),
                text_pos = (0, -0.02)
               )
            self.rewardLines.append(rewardLine)

    def setRewards(self, results):
        """
        Adds player's info the rewards UI
        """
        # Get their Id and laff
        for p in range(len(results[0])):
            doId = results[0][p]
            laff = results[1][p]
            
            # Set the text
            if doId > 0 and doId in base.cr.doId2do:
                toon = base.cr.doId2do[doId]
                self.rewardLines[p]['name'].setProp('text', toon.getName())
                self.rewardLines[p]['laff'].setProp('text', str(laff))
                
                # Make them stand out
                if doId == base.localAvatar.getDoId():
                    self.rewardLines[p]['frame'].setProp('relief', DGG.RIDGE)
                    self.rewardLines[p]['frame'].setProp('borderWidth', (0.01, 0.01))
                    self.rewardLines[p]['frame'].setProp('frameColor', (1, 1, 1, 0.5))
