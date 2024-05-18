import socket
import datetime
import os
import pytz
from direct.distributed.DistributedObjectGlobalUD import DistributedObjectGlobalUD
from direct.http.WebRequest import WebRequestDispatcher
from otp.distributed import OtpDoGlobals
from toontown.toonbase import ToontownGlobals
from toontown.uberdog import InGameNewsResponses
from toontown.ai.ToontownAIMsgTypes import WHITELIST_MANAGER_UD_TO_ALL_AI
from toontown.toonbase.ToontownModules import ConfigVariableString

class DistributedWhitelistMgrUD(DistributedObjectGlobalUD):
    """
    Uberdog object that keeps track of the last time the whitelist has been updated
    """
    notify = directNotify.newCategory('DistributedWhitelistMgrUD')
    serverDataFolder = ConfigVariableString('server-data-folder', "").getValue()

    # WARNING this is a global OTP object
    # WhitelistMgrAI is NOT!
    # Hence the use of sendUpdateToDoId when sending back to AI

    setLatestListFailureXML = """
    <setLatestListResponse>
    <success>false</success>
    <error>%s</error>
    </setLatestListResponse>
    \r\n"""

    setLatestListSuccessXML = """
    <setLatestListResponse>
    <success>true</success>
    <info>%s</info>
    </setLatestListResponse>
    \r\n"""

    def __init__(self, air):
        """Construct ourselves, set up web dispatcher."""
        assert self.notify.debugCall()
        DistributedObjectGlobalUD.__init__(self, air)
        self.HTTPListenPort = uber.whitelistMgrHTTPListenPort

        self.webDispatcher = WebRequestDispatcher()
        self.webDispatcher.landingPage.setTitle("WhitelistMgr")
        self.webDispatcher.landingPage.setDescription("Whitelist is update when a new list of the Whitelist is out.")
        self.webDispatcher.registerGETHandler('whitelistMgr', self.whitelistMgr)
        self.webDispatcher.registerGETHandler('whitelistNewList', self.whitelistNewList)
        self.webDispatcher.listenOnPort(self.HTTPListenPort)
        self.webDispatcher.landingPage.addTab("WhitelistMgr","/whitelistMgr")

        self.air.setConnectionName("WhitelistMgr")
        self.air.setConnectionURL("http://%s:%s/" % (socket.gethostbyname(socket.gethostname()),self.HTTPListenPort))

        self.filename = self.getFilename()
        self.latestList = datetime.datetime.now()
        self.latestList = self.loadRecords()

    def getLatestListStr(self):
        self.notify.debugStateCall(self)
        return self.latestList.strftime(self.air.toontownTimeManager.formatStr)

    def getLatestListUtcStr(self):
        self.notify.debugStateCall(self)
        datetimeInUtc = self.latestList.astimezone(pytz.utc)
        result = datetimeInUtc.strftime(self.air.toontownTimeManager.formatStr)
        return result

    def announceGenerate(self):
        """Start accepting http requests."""
        assert self.notify.debugCall()
        DistributedObjectGlobalUD.announceGenerate(self)
        self.b_setLatestList(self.latestList)
        self.webDispatcher.startCheckingIncomingHTTP()

    def whitelistMgr(self, replyTo, **kw):
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

    def whitelistNewList(self, replyTo, **kw):
        try:
            newList = self.air.toontownTimeManager.getCurServerDateTime()
            self.b_setLatestList(newList)
            self.updateRecordFile()
            replyTo.respondXML(self.setLatestListSuccessXML %
                               (self.getLatestListStr()))

            pass
        except Exception as e:
            replyTo.respondXML(self.setLatestListFailureXML  %
                               ("Catastrophic failure setting latest list %s" % str(e)))
            pass

    def getMainMenu(self):
        """Create the main menu with forms for input."""
        header = """<HTML><HEAD><TITLE>Main Menu: Whitelist Mgr</TITLE><link rel="stylesheet" type="text/css" href="/default.css">
        </HEAD>"""

        body = """<BODY><div id="contents"><center><P>"""
        body += """
            Latest List = """
        body += self.getLatestListStr()
        body += """
            <br>
            <form name="myform" action="whitelistNewList">
            <input type="submit" value="New List Released" />
            </form>
            """

        footer = """</tbody></table></P></center></div><div id="footer">Toontown Whitelist</div></BODY></HTML>"""
        help = """<table height = "15%"></table><P><table width = "60%"><caption>Note</caption><tr><th scope=col>- Click on the button when a new list of the whitelist has been released.</th></tr></table></P>"""
        return (header,body,footer,help)


    def updateRecordFile(self):
        """Update current track record in this shard's record file"""
        # notify the leader boards that there has been an update
        try:
            backup = self.filename + '.bu'
            if os.path.exists(self.filename):
                os.rename(self.filename, backup)
            file = open(self.filename, 'w')
            file.seek(0)
            file.write(self.getLatestListStr())
            file.close()
            if os.path.exists(backup):
                os.remove(backup)
        except EnvironmentError:
            self.notify.warning(str(sys.exc_info()[1]))

    def getFilename(self):
        """Compose the track record filename"""
        return "%s.latestlist" % (self.serverDataFolder)

    def getDefaultLatestListTime(self):
        """Hmmm what the heck do we give. Lets use the current time."""
        result = self.air.toontownTimeManager.getCurServerDateTime()
        return result

    def loadRecords(self):
        """Load track record data from default location"""
        try:
            # Try to open the backup file:
            file = open(self.filename + '.bu', 'r')
            # Remove the (assumed) broken file:
            if os.path.exists(self.filename):
                os.remove(self.filename)
        except IOError:
            # OK, there's no backup file, good.
            try:
                # Open the real file:
                file = open(self.filename, 'r')
            except IOError:
                # OK, there's no file.  Grab the default times.
                return self.getDefaultLatestListTime()
        file.seek(0)
        result = self.loadFrom(file)
        file.close()

        return result

    def loadFrom(self, file):
        """Load track record data from specified file"""
        result = self.air.toontownTimeManager.getCurServerDateTime()
        try:
            latestListStr = file.readline()
            result = self.air.toontownTimeManager.convertStrToToontownTime(latestListStr)
        except EOFError:
            pass
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
