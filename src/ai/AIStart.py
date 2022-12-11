import builtins

class game:
    name = "toontown"
    process = "ai"
builtins.game = game()

# NOTE: this file is not used in production. See AIServiceStart.py

import time
import os
import sys

print("Initializing...")

from otp.ai.AIBaseGlobal import *
from . import ToontownAIRepository
from direct.showbase import PythonUtil

# Clear the default model extension for AI developers, so they'll know
# when they screw up and omit it.
from toontown.toonbase.ToontownModules import loadPrcFileData
loadPrcFileData("AIStart.py", "default-model-extension")

simbase.mdip = ConfigVariableString("msg-director-ip", "localhost").getValue()

# Now the AI connects directly to the state server instead of the msg director
simbase.mdport = ConfigVariableInt("msg-director-port", 6666).getValue()

simbase.esip = ConfigVariableString("event-server-ip", "localhost").getValue()
simbase.esport = ConfigVariableInt("event-server-port", 4343).getValue()


districtType = 0
serverId = ConfigVariableInt("district-ssid", 20100000).getValue()

for i in range(1, 20+1):
    # always set up for i==1, then take the first district above 1 (if any)
    if i==1 or os.getenv("want_district_%s" % i):
        if i==1:
            postfix = ''
        else:
            postfix = '-%s' % i
        districtNumber = ConfigVariableInt(
            "district-id%s"%postfix,
            200000000 + i*1000000).getValue()
        districtName = ConfigVariableString(
            "district-name%s"%postfix,
            "%sville" % {1: 'Silly',
                         2: 'Second',
                         3: 'Third',
                         4: 'Fourth',
                         5: 'Fifth',
                         6: 'Sixth',
                         7: 'Seventh',
                         8: 'Eighth',
                         9: 'Ninth', }.get(i, str(i))
                         ).getValue()
        districtMinChannel = ConfigVariableInt(
            "district-min-channel%s"%postfix,
            200100000 + i*1000000).getValue()
        districtMaxChannel = ConfigVariableInt(
            "district-max-channel%s"%postfix,
            200149999 + i*1000000).getValue()
        if i != 1:
            break

"""
Setup the log files
We want C++ and Python to both go to the same log so they will be interlaced properly.
"""

# Will make the log directory if it doesn't exist yet.
logDir = os.path.join(os.getcwd(), ConfigVariableString("tt-log-ai-base-dir", "toonlog").getValue())
ltime = time.localtime()

if not os.path.isdir(logDir):
    print(f"didn't find a log dir, making {logDir}")
    os.mkdir(logDir)

# date_hour_sequence.log will be added to the logfile name by RotatingLog():
logfile = os.path.join(logDir, "aidistrict-dev-%02d%02d%02d_%02d%02d%02d.log" % (
    ltime[0] - 2000,    # year
    ltime[1],           # month
    ltime[2],           # day
    ltime[3],           # hour
    ltime[4],           # minute
    ltime[5]            # second
))

# Redirect Python output and err to the same file
class LogAndOutput:
    def __init__(self, orig, log):
        self.orig = orig
        self.log = log
    def write(self, str):
        self.log.write(str)
        self.log.flush()
        self.orig.write(str)
        self.orig.flush()
    def flush(self):
        self.log.flush()
        self.orig.flush()

log = open(logfile, 'a')
logOut = LogAndOutput(sys.__stdout__, log)
logErr = LogAndOutput(sys.__stderr__, log)
sys.stdout = logOut
sys.stderr = logErr

from toontown.toonbase.ToontownModules import *

# Give Panda the same log we use
nout = MultiplexStream()
Notify.ptr().setOstreamPtr(nout, 0)
nout.addFile(Filename(logfile))
nout.addStandardOutput()
nout.addSystemDebug()

print("-"*30, "creating toontown district %s" % districtNumber, "-"*30)

simbase.air = ToontownAIRepository.ToontownAIRepository(
        simbase.mdip,
        simbase.mdport,
        simbase.esip,
        simbase.esport,
        None,
        districtNumber,
        districtName,
        districtType,
        serverId,
        districtMinChannel,
        districtMaxChannel)

# How we let the world know we are not running a service
simbase.aiService = 0

try:
    simbase.air.fsm.request("districtReset")
    run()
except:
    info = PythonUtil.describeException()
    simbase.air.writeServerEvent('ai-exception', districtNumber, info)
    raise
