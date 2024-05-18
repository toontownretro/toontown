import urllib
import socket
import datetime
import os
import pytz
from direct.distributed.DistributedObjectGlobalUD import DistributedObjectGlobalUD
from direct.http.WebRequest import WebRequestDispatcher
from otp.distributed import OtpDoGlobals
from toontown.toonbase import ToontownGlobals
from toontown.uberdog import InGameNewsResponses
from toontown.ai.ToontownAIMsgTypes import IN_GAME_NEWS_MANAGER_UD_TO_ALL_AI
from toontown.toon.ModuleListAI import ModuleList


class DistributedSecurityMgrUD(DistributedObjectGlobalUD):
    """
    Uberdog object that keeps track of banned module injections
    """
    notify = directNotify.newCategory('DistributedSecurityMgrUD')

    # WARNING this is a global OTP object
    # InGameNewsMgrAI is NOT!
    # Hence the use of sendUpdateToDoId when sending back to AI

    securityMgrFailureXML = """
    <securityMgrResponse>
    <success>false</success>
    <error>%s</error>
    </securityMgrResponse>
    \r\n"""

    securityMgrAddModuleXML = """
    <securityMgrAddResponse>
    <success>true</success>
    <module>%s</module>
    </securityMgrAddResponse>
    \r\n"""

    securityMgrRemoveModuleXML = """
    <securityMgrRemoveResponse>
    <success>true</success>
    <module>%s</module>
    </securityMgrRemoveResponse>
    \r\n"""



    def __init__(self, air):
        """Construct ourselves, set up web dispatcher."""
        assert self.notify.debugCall()
        DistributedObjectGlobalUD.__init__(self, air)
        self.HTTPListenPort = uber.cpuInfoMgrHTTPListenPort
        
        self.webDispatcher = WebRequestDispatcher()
        self.webDispatcher.landingPage.setTitle("SecurityMgr")
        self.webDispatcher.landingPage.setDescription("SecurityMgr handles banning of dll modules.")
        self.webDispatcher.registerGETHandler('securityMgr', self.securityBanMgr)
        self.webDispatcher.registerGETHandler('securityMgrAddWhitelistModule', self.addWhitelistModule)
        self.webDispatcher.registerGETHandler('securityMgrAddBlacklistModule', self.addBlacklistModule)
        self.webDispatcher.registerGETHandler('securityMgrRemoveWhitelistModule', self.removeWhitelistModule)
        self.webDispatcher.registerGETHandler('securityMgrRemoveBlacklistModule', self.removeBlacklistModule)
        self.webDispatcher.registerGETHandler('securityMgrListWhitelistModules', self.listWhitelistModules)
        self.webDispatcher.registerGETHandler('securityMgrListBlacklistModules', self.listBlacklistModules)
        self.webDispatcher.listenOnPort(self.HTTPListenPort)
        self.webDispatcher.landingPage.addTab("SecurityMgr","/securityMgr")
        
        self.air.setConnectionName("SecurityMgr")
        self.air.setConnectionURL("http://%s:%s/" % (socket.gethostbyname(socket.gethostname()),self.HTTPListenPort))

        self.moduleList = ModuleList()

        self.allowedModules = set()
        self.allowedModules = self.moduleList.loadWhitelistFile()

        self.bannedModules = set()
        self.bannedModules = self.moduleList.loadBlacklistFile()

        self.latestList = datetime.datetime.now()

    def announceGenerate(self):
        """Start accepting http requests."""
        assert self.notify.debugCall()
        DistributedObjectGlobalUD.announceGenerate(self)
        self.webDispatcher.startCheckingIncomingHTTP()

    def securityBanMgr(self, replyTo, **kw):
        """Handle all calls to web requests awardMgr."""
        assert self.notify.debugCall()

        # If no arguments are passed, assume that the main menu should
        # be displayed

        if not kw:
            function = None
            id = None
        else:
            function = "doAward"

        header = body = help = footer = ""
        if not function:
            header,body,footer,help= self.getMainMenu()
        else:
            self.notify.debug("%s" % str(kw))
            header,body,footer,help= self.getMainMenu()
            body = """<BODY><div id="contents"><center><P>got these arguments """
            body += str(kw)

        #self.notify.info("%s" % header + body + help + footer)
        replyTo.respond(header + body + help + footer)


    def getMainMenu(self):
        """Create the main menu with forms for input."""
        header = """<HTML><HEAD><TITLE>Main Menu: Security Mgr</TITLE><link rel="stylesheet" type="text/css" href="/default.css">
        </HEAD>"""

        body = """<BODY><div id="contents"><center><P>"""

        body += """
            <br>
            <form name="addWhitelistModuleForm" action="securityMgrAddWhitelistModule">
            <input type="text" name="whitelistModuleToAdd" value="">
            <input type="submit" value="Add Whitelist Module" />
            </form>
            """

        body += """
            <br>
            <form name="addBlacklistModuleForm" action="securityMgrAddBlacklistModule">
            <input type="text" name="blacklistModuleToAdd" value="">
            <input type="submit" value="Add Blacklist Module" />
            </form>
            """

        body += """
            <br>
            <form name="removeWhitelistModuleForm" action="securityMgrRemoveWhitelistModule">
            <input type="text" name="whitelistModuleToRemove" value="">
            <input type="submit" value="Remove Whitelist Module" />
            </form>
            """

        body += """
            <br>
            <form name="removeBlacklistModuleForm" action="securityMgrRemoveBlacklistModule">
            <input type="text" name="blacklistModuleToRemove" value="">
            <input type="submit" value="Remove Blacklist Module" />
            </form>
            """

        body += """
            <br>
            <form name="listWhitelistModulesForm" action="securityMgrListWhitelistModules">
            <input type="submit" value="List Whitelist Modules" />
            </form>
            """

        body += """
            <br>
            <form name="listBlacklistModulesForm" action="securityMgrListBlacklistModules">
            <input type="submit" value="List Blacklist Modules" />
            </form>
            """

        footer = """</tbody></table></P></center></div><div id="footer">Security Mgr</div></BODY></HTML>"""
        help = """<table height = "15%"></table><P><table width = "60%"><caption>Note</caption><tr><th scope=col>- Use add to add ONE module that's allowed or banned. Use remove to take ONE module out. And use list to see them all.</th></tr></table></P>"""
        return (header,body,footer,help)

    def getDefaultLatestListTime(self):
        """Hmmm what the heck do we give. Lets use the current time."""
        result = self.air.toontownTimeManager.getCurServerDateTime()
        return result

    def updateWhitelist(self, listStr):
        self.notify.debugStateCall(self)


    def setLatestList(self, latestList):
        self.latestList = latestList

    def b_setLatestList(self, latestList):
        self.setLatestList(latestList)
        self.d_setLatestList(latestList)

    def d_setLatestList(self, latestList):
        self.sendUpdateToAllAis('newListUDtoAI', [ self.getLatestListUtcStr()])

    def sendUpdateToAllAis(self, message, args):
        dg = self.dclass.aiFormatUpdateMsgType(
                message, self.doId, self.doId, self.air.ourChannel, WHITELIST_MANAGER_UD_TO_ALL_AI, args)
        self.air.send(dg)

    def whitelistMgrAIStartingUp(self,  doId,  shardId):
        """Tell the new AI that just started up what the latest list is."""
        self.air.sendUpdateToDoId(
                "DistributedWhitelistMgr",
                'newListUDtoAI',
                doId ,
                [self.getLatestListStr()]
            )

    def addWhitelistModule(self, replyTo, **kw):
        """Add a new module to be allowed."""
        try:
            module = urllib.parse.unquote(kw['whitelistModuleToAdd'])
            self.allowedModules.add(module)
            self.moduleList.updateWhitelistFile()
            header,body,footer,help= self.getMainMenu()
            replyTo.respondXML(self.securityMgrAddModuleXML %
                               ("%s" % module))

        except Exception as e:
            replyTo.respondXML(self.securityMgrFailureXML %
                               ("Catastrophic failure add module %s" % str(e)))
            self.notify.warning("Got exception %s" % str(e))

    def addBlacklistModule(self, replyTo, **kw):
        """Add a new module to auto ban."""
        try:
            module = urllib.parse.unquote(kw['blacklistModuleToAdd'])
            self.bannedModules.add(module)
            self.moduleList.updateBlacklistFile()
            header,body,footer,help= self.getMainMenu()
            replyTo.respondXML(self.securityMgrAddModuleXML %
                               ("%s" % module))

        except Exception as e:
            replyTo.respondXML(self.securityMgrFailureXML %
                               ("Catastrophic failure add module %s" % str(e)))
            self.notify.warning("Got exception %s" % str(e))
    
    def removeWhitelistModule(self, replyTo, **kw):
        """Remove a module to auto ban."""
        try:
            module = urllib.parse.unquote(kw['whitelistModuleToRemove'])
            if module in self.allowedModules:
                self.allowedModules.remove(module)
                self.moduleList.updateWhitelistFile()
                header,body,footer,help= self.getMainMenu()
                replyTo.respondXML(self.securityMgrRemoveModuleXML %
                                   ("%s" % module))
            else:
                replyTo.respondXML(self.securityMgrFailureXML % ("%s not an allowed module" % module))
        except Exception as e:
            replyTo.respondXML(self.securityMgrFailureXML %
                               ("Catastrophic failure add module %s" % str(e)))
            self.notify.warning("Got exception %s" % str(e))  
    
    def removeBlacklistModule(self, replyTo, **kw):
        """Remove a module to auto ban."""
        try:
            module = urllib.parse.unquote(kw['blacklistModuleToRemove'])
            if module in self.bannedModules:
                self.bannedModules.remove(module)
                self.moduleList.updateBlacklistFile()
                header,body,footer,help= self.getMainMenu()
                replyTo.respondXML(self.securityMgrRemoveModuleXML %
                                   ("%s" % module))
            else:
                replyTo.respondXML(self.securityMgrFailureXML % ("%s not a banned module" % module))
        except Exception as e:
            replyTo.respondXML(self.securityMgrFailureXML %
                               ("Catastrophic failure add module %s" % str(e)))
            self.notify.warning("Got exception %s" % str(e))  
    
    def listWhitelistModules(self, replyTo, **kw):
        """List all allowed modules."""
        try:
            header,body,footer,help= self.getMainMenu()
            body = """<BODY><div id="contents"><center><P>"""
            body += """<h4>Allowed Modules:</h4>
            <table border="1">
            """
            for module in self.allowedModules:
                body += "<tr><td>" + str(module) +  "</td>"+"</tr>\n"
            body += """
            </table>
            """
            replyTo.respond(header +body+ help+footer)
        except Exception as e:
            replyTo.respondXML(self.securityMgrFailureXML % ("Catastrophic failure listing modules %s" % str(e)))
            self.notify.warning("Got exception %s" % str(e))

    def listBlacklistModules(self, replyTo, **kw):
        """List all banned modules."""
        try:
            header,body,footer,help= self.getMainMenu()
            body = """<BODY><div id="contents"><center><P>"""
            body += """<h4>Banned Modules:</h4>
            <table border="1">
            """
            for module in self.bannedModules:
                body += "<tr><td>" + str(module) +  "</td>"+"</tr>\n"
            body += """
            </table>
            """
            replyTo.respond(header +body+ help+footer)
        except Exception as e:
            replyTo.respondXML(self.securityMgrFailureXML % ("Catastrophic failure listing modules %s" % str(e)))
            self.notify.warning("Got exception %s" % str(e))
