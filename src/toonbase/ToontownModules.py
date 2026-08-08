# This is a temporary hack so we don't have to fix all the PandaModules imports.

from otp.otpbase.OTPModules import *

# Toontown specific modules
from panda3d.toontown import *

# DirectFrames (sometimes) rely on this
from direct.gui.DirectGuiGlobals import NO_FADE_SORT_INDEX, FOREGROUND_SORT_INDEX, BACKGROUND_SORT_INDEX

# ToonBase.py relies on this
from panda3d.core import Loader as PandaLoader

# RobotToonManager.py relies on this
import direct
