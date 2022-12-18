import builtins, time, os, sys, random, inspect

import dearpygui.dearpygui as dpg

from panda3d.core import Loader as PandaLoader

from direct.gui import DirectGuiGlobals
from direct.stdpy import threading
from direct.task import Task
from direct.task.TaskManagerGlobal import *

from toontown.toonbase.ToontownModules import *
from toontown.toonbase import ToontownGlobals

########## Callbacks ##########

global injectText
injectText = ""

def setInjectText(sender, app_data, user_data):
    global injectText
    injectText = str(app_data)
    
def inject(sender, app_data, user_data):
    global injectText
    try:
        exec (injectText, globals())
    except:
        import traceback
        traceback.print_exc()
        
def pseduoMembership(sender, app_data, user_data):
    if not hasattr(base, 'cr') or not base.cr:
        return
    if not hasattr(base, 'localAvatar') or not base.localAvatar:
        return
        
    def null1():
        return 1
        
    def null2(*args, **kwargs):
        return 1
        
    def null3(*args, **kwargs):
        return 2
        
    base.cr.isPaid = null1
    base.cr.allowSecretChat = null1
    base.cr.isParentPasswordSet = null2
    base.localAvatar.getGameAccess = null3
    
    base.localAvatar.setSystemMessage(0, "You now have pseudo-membership! Enjoy doing some extra things you couldn't before!")
    
def skipToontorial(sender, app_data, user_data):
    if not hasattr(base, 'cr') or not base.cr:
        return
    if not hasattr(base, 'localAvatar') or not base.localAvatar:
        return

    mgr = base.cr.doFind("TutorialManager")
    if not mgr:
        return
    
    mgr.d_requestSkipTutorial()
    base.cr.gameFSM.request('closeShard')
    
    base.localAvatar.setSystemMessage(0, "Skipped the Toontorial!")
    
def splashEverybody(sender, app_data, user_data):
    if not hasattr(base, 'cr') or not base.cr:
        return
    if not hasattr(base, 'localAvatar') or not base.localAvatar:
        return
        
    toons = base.cr.doFindAll("DistributedToon")
    for toon in toons:
        base.localAvatar.d_playSplashEffect(toon.getX(), toon.getY(), toon.getZ())
        base.localAvatar.playSplashEffect(toon.getX(), toon.getY(), toon.getZ())
        
    base.localAvatar.setSystemMessage(0, "Splish Splash! Now everybody is wet!")
        
def teleportAnywhere(sender, app_data, user_data):
    if not hasattr(base, 'localAvatar') or not base.localAvatar:
        return
        
    zones = [ToontownGlobals.DonaldsDock, ToontownGlobals.ToontownCentral, ToontownGlobals.TheBrrrgh, ToontownGlobals.MinniesMelodyland,
             ToontownGlobals.DaisyGardens, ToontownGlobals.OutdoorZone, ToontownGlobals.FunnyFarm, ToontownGlobals.GoofySpeedway,
             ToontownGlobals.DonaldsDreamland, ToontownGlobals.BossbotHQ, ToontownGlobals.SellbotHQ, ToontownGlobals.CashbotHQ, ToontownGlobals.LawbotHQ]
    
    base.localAvatar.setZonesVisited(zones)
    base.localAvatar.setHoodsVisited(zones)
    base.localAvatar.setTeleportAccess(zones)
    
    base.localAvatar.setSystemMessage(0, "You can now teleport anywhere!")
    
########## Class ##########
        
class ToontownDebugTools():
    """
    Implements our debug tools for Toontown.
    """

    def __init__(self):
        self.thread = None
        
    def start(self):
        self.thread = threading.Thread(target = self.__openImgui, name="ToontownDebugTools")
        self.thread.start()
        
    def __openImgui(self):
        dpg.create_context()
        dpg.configure_app(manual_callback_management=True)
        dpg.create_viewport(title='Toontown Debug Tools', width=640, height=615)
        dpg.setup_dearpygui()

        with dpg.window(label="Tools"):
            # Add our tab bar.
            with dpg.tab_bar():
                # Add our Injector tab.
                with dpg.tab(label="Injector"):
                    paragraph = """"""

                    dpg.add_input_text(label="", multiline=True, default_value=paragraph, width=610, height=495, callback=setInjectText, tab_input=True)
                    dpg.add_button(label="Inject", width=610, callback=inject)
                # Add a Codes tab.
                # This is full of built-in injector codes.
                with dpg.tab(label="Codes"):
                    # We want a horizontal groups for all of our buttons.
                    
                    # Generic Cheats
                    with dpg.group(horizontal=True):
                        dpg.add_button(label="Pseudo-Membership", callback=pseduoMembership)
                        dpg.add_button(label="Splash Everybody", callback=splashEverybody)
                        dpg.add_button(label="Skip Toontorial", callback=skipToontorial)
                    
                    # Add line seperator.
                    dpg.add_separator(label="Teleport Codes")
                    
                    # Teleport Cheats
                    with dpg.group(horizontal=True):
                        dpg.add_button(label="Teleport Anywhere", callback=teleportAnywhere)

        # Main Loop
        dpg.show_viewport()
        #dpg.start_dearpygui()

        # Handle callbacks
        while dpg.is_dearpygui_running():
            jobs = dpg.get_callback_queue() # retrieves and clears queue
            self.__runCallbacks(jobs)
            dpg.render_dearpygui_frame()
            
        dpg.destroy_context()
        
    def __runCallbacks(self, jobs):
        if jobs is None:
            return
            
        for job in jobs:
            if job[0] is None:
                continue
            
            sig = inspect.signature(job[0])
            args = []
            for arg in range(len(sig.parameters)):
                args.append(job[arg+1])
            #job[0](*args)
            taskMgr.doMethodLater(0, job[0], job[0].__name__ + str(id(job[0])) + str(id(args)), extraArgs=args)