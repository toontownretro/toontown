# This is a temporary hack so we don't have to fix all the PandaModules imports.

from otp.otpbase.OTPModules import *

# Toontown specific modules
from panda3d.toontown import *

# Instead of editing each file to fix issues with modern Panda
# if a file imports this and has issues they should be fixed here

# DirectFrames (sometimes) rely on this
from direct.gui.DirectGuiGlobals import NO_FADE_SORT_INDEX, FOREGROUND_SORT_INDEX, BACKGROUND_SORT_INDEX, FADE_SORT_INDEX

# House editing relies on this
from direct.directtools.DirectGlobals import SKIP_ALL, SKIP_BACKFACE, SKIP_CAMERA, SKIP_UNPICKABLE
from direct.directtools.DirectUtil import CLAMP

# ToonBase.py relies on this
from panda3d.core import Loader as PandaLoader

# RobotToonManager.py relies on this
import direct
