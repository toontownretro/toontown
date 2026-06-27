"""
Start the Toontown UberDog (Uber Distributed Object Globals server).
"""

import builtins
from direct.task.Task import Task

class game:
    name = "uberDog"
    process = "server"
builtins.game = game()

import time
import os
import sys

if os.getenv('TTMODELS'):
    from toontown.toonbase.ToontownModules import getModelPath, Filename
    # In the publish environment, TTMODELS won't be on the model
    # path by default, so we always add it there.  In the dev
    # environment, it'll be on the model path already, but it
    # doesn't hurt to add it again.
    getModelPath().appendDirectory(Filename.expandFrom("$TTMODELS/built"))

from direct.showbase.PythonUtil import *
from otp.uberdog.UberDogGlobal import *
from toontown.coderedemption import TTCodeRedemptionConsts
from toontown.uberdog.ToontownUberDog import ToontownUberDog
from toontown.uberdog import PartiesUdConfig

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
logfile = os.path.join(logDir, "uberdog-dev-%02d%02d%02d_%02d%02d%02d.log" % (
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

from toontown.toonbase.ToontownModules import Filename, MultiplexStream, Notify

# Give Panda the same log we use
nout = MultiplexStream()
Notify.ptr().setOstreamPtr(nout, 0)
nout.addFile(Filename(logfile))
nout.addStandardOutput()
nout.addSystemDebug()

print("Initializing the Toontown UberDog (Uber Distributed Object Globals server)...")

uber.mdip = ConfigVariableString("msg-director-ip", "localhost").getValue()
uber.mdport = ConfigVariableInt("msg-director-port", 6666).getValue()

uber.esip = ConfigVariableString("event-server-ip", "localhost").getValue()
uber.esport = ConfigVariableInt("event-server-port", 4343).getValue()

stateServerId = ConfigVariableInt("state-server-id", 20100000).getValue()

uber.objectNames = set(os.getenv("uberdog_objects", "").split())

minChannel = ConfigVariableInt("uberdog-min-channel", 200400000).getValue()
maxChannel = ConfigVariableInt("uberdog-max-channel", 200449999).getValue()

uber.sbNSHost = ConfigVariableString("sb-host","").getValue()
uber.sbNSPort = ConfigVariableInt("sb-port",6053).getValue()
uber.sbListenPort = 6060
uber.clHost = "localhost"
uber.clPort = 9090
uber.allowUnfilteredChat = ConfigVariableInt("allow-unfiltered-chat",0).getValue()
uber.bwDictPath = ""

uber.RATManagerHTTPListenPort = ConfigVariableInt("rat-port",8080).getValue()
uber.awardManagerHTTPListenPort = ConfigVariableInt("award-port",8888).getValue()
uber.inGameNewsMgrHTTPListenPort = ConfigVariableInt("in-game-news-port",8889).getValue()
uber.whitelistMgrHTTPListenPort = ConfigVariableInt("whitelist-port",8890).getValue()
uber.mysqlhost = ConfigVariableString("mysql-host", PartiesUdConfig.ttDbHost).getValue()


uber.codeRedemptionMgrHTTPListenPort = ConfigVariableInt('code-redemption-port', 8998).getValue()
uber.crDbName = ConfigVariableString("tt-code-db-name", TTCodeRedemptionConsts.DefaultDbName).getValue()

uber.cpuInfoMgrHTTPListenPort = ConfigVariableInt("security_ban_mgr_port",8892).getValue()
uber.securityMgrHTTPListenPort = ConfigVariableInt("security_port",8893).getValue()

uber.air = ToontownUberDog(
        uber.mdip, uber.mdport,
        uber.esip, uber.esport,
        None,
        stateServerId,
        minChannel,
        maxChannel)

# How we let the world know we are not running a service
uber.aiService = 0

uber.wantEmbeddedOtpServer = ConfigVariableInt(
    "toontown-uberdog-want-embedded-otp-server", 0).getValue()
if uber.wantEmbeddedOtpServer:
    otpServerPath = ConfigVariableString(
        "toontown-uberdog-otp-server-path", "c:/toonsrv").getValue()
    sys.path.append(otpServerPath)

    import otp_server_py
    if not otp_server_py.serverInit(otpServerPath):
       sys.exit(1)

    def ServerYield(task):
        otp_server_py.serverLoop()
        return Task.cont

    uber.taskMgr.add(ServerYield, 'serverYield')
    __builtins__["otpServer"] = otp_server_py


try:
    run()
except:
    info = describeException()
    #uber.air.writeServerEvent('uberdog-exception', districtNumber, info)
    raise
