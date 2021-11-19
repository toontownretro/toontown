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
