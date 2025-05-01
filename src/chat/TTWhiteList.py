import os
import datetime
from toontown.toonbase.ToontownModules import *
from direct.directnotify import DirectNotifyGlobal
from direct.distributed import DistributedObject
from direct.showbase import AppRunnerGlobal
from otp.chat.WhiteList import WhiteList
from toontown.toonbase import TTLocalizer

class TTWhiteList(WhiteList, DistributedObject.DistributedObject):
    RedownloadTaskName = "RedownloadWhitelistTask"
    WhitelistBaseDir = ConfigVariableString("whitelist-base-dir", "").getValue()
    WhitelistStageDir = ConfigVariableString("whitelist-stage-dir", "whitelist").getValue()
    WhitelistOverHttp = ConfigVariableBool("whitelist-over-http", True).getValue()
    WhitelistFileName = ConfigVariableString("whitelist-filename", "twhitelist.dat").getValue()
    def __init__(self):
        self.redownloadingWhitelist = False
        self.startRedownload = datetime.datetime.now()
        self.endRedownload = datetime.datetime.now()
        self.percentDownloaded = 0.0
        self.notify = DirectNotifyGlobal.directNotify.newCategory('TTWhiteList')
        self.whitelistDir = Filename('')
        vfs = VirtualFileSystem.getGlobalPtr()
        filename = Filename('twhitelist.dat')
        searchPath = DSearchPath()
        if AppRunnerGlobal.appRunner:
            # In the web-publish runtime, it will always be here:
            searchPath.appendDirectory(Filename.expandFrom('$TT_3_ROOT/phase_3/etc'))
        else:
            # In other environments, including the dev environment, look here:
            searchPath.appendDirectory(Filename('.'))
            searchPath.appendDirectory(Filename('etc'))
            searchPath.appendDirectory(Filename.fromOsSpecific(os.path.expandvars('$TOONTOWN/src/chat')))
            searchPath.appendDirectory(Filename.fromOsSpecific(os.path.expandvars('toontown/src/chat')))
            searchPath.appendDirectory(Filename.fromOsSpecific(os.path.expandvars('toontown/chat')))
        found = vfs.resolveFilename(filename,searchPath)
        if not found:
            self.notify.info("Couldn't find whitelist data file!")
        data = vfs.readFile(filename, 1)
        lines = data.split(b'\n')
        WhiteList.__init__(self, lines)
        self.redownloadWhitelist()
        self.defaultWord = TTLocalizer.ChatGarblerDefault[0]
        self.accept('updateWhitelist', self.handleNewWhitelist)

    def unload(self):
        self.ignore('updateWhitelist')
        self.removeDownloadingTextTask()

    def redownloadWhitelist(self):
        """Get the new whitelist that came out while he was playing."""
        self.percentDownload = 0.0
        self.notify.info('starting redownloadWhitelist')
        self.startRedownload = datetime.datetime.now()
        self.redownloadingWhitelist = True
        self.addDownloadingTextTask()
        self.whitelistUrl = self.getWhitelistUrl()
        #self.whitelistDir = Filename(self.findWhitelistDir())

        #Filename(self.whitelistDir + '/.').makeDir()
        http = HTTPClient.getGlobalPtr()

        self.url = self.whitelistUrl + self.WhitelistFileName
        self.ch = http.makeChannel(True)

        #localFilename = Filename(self.whitelistDir, 'twhitelist.dat')

        self.ch.getHeader(DocumentSpec(self.url))

        size = self.ch.getFileSize()
        doc = self.ch.getDocumentSpec()
        #localSize = localFilename.getFileSize()
        outOfDate = True

        #if size == localSize:
        #    if doc.hasDate():
        #        date = doc.getDate()
        #        localDate = HTTPDate(localFilename.getTimestamp())
        #        if localDate.compareTo(date) > 0:
        #            outOfDate = False
        #            self.notify.info('Whitelist is up to date')

        taskMgr.remove(self.RedownloadTaskName)

        if outOfDate and self.ch.isValid():
            self.ch.beginGetDocument(doc)
            #self.ch.downloadToFile(localFilename)
            #taskMgr.add(self.downloadWhitelistTask, self.RedownloadTaskName)
        else:
            self.updateWhitelist()

    def getWhitelistUrl(self):
        """Get the appropriate URL to use if we are in test, qa, or live."""
        # First if all else fails, we hard code the live whitelist url
        # Early 2024 cdn.toontown.disney.go.com became unreachable, we need to change it to cdn.toontown.dolimg.com
        # Early 2025 cdn.toontown.dolimg.com became unreachable, we need to change it to cdn.dolimg.com
        result = ConfigVariableString("fallback-whitelist-url", "http://cdn.dolimg.com/toontown/en/").getValue()
        # next check if we have an override, say they want to url to point to a file in their harddisk
        override = ConfigVariableString("whitelist-url", "").getValue()
        if override:
            self.notify.info("got an override url,  using %s for the whitelist" % override)
            result = override
        else:
            try:
                launcherUrl = base.launcher.getValue("GAME_WHITELIST_URL", "")
                if launcherUrl:
                    result = launcherUrl
                    self.notify.info("got GAME_WHITELIST_URL from launcher using %s" % result)
                else:
                    self.notify.info("blank GAME_WHITELIST_URL from launcher, using %s" % result)

            except:
                self.notify.warning("got exception getting GAME_WHITELIST_URL from launcher, using %s" % result)
        return result

    def addDownloadingTextTask(self):
        """Add a simple little task to show whitelist is downloading stuff."""
        self.removeDownloadingTextTask()
        task = taskMgr.doMethodLater(1, self.loadingTextTask, "WhitelistDownloadingTextTask")
        task.startTime = globalClock.getFrameTime()
        self.loadingTextTask(task)

    def removeDownloadingTextTask(self):
        """Add a simple little task to show whitelist is downloading stuff."""
        taskMgr.remove('WhitelistDownloadingTextTask')

    def loadingTextTask(self, task):
        """Change a visual element to indicate we're still downloading."""
        timeIndex = int(globalClock.getFrameTime() - task.startTime) % 3
        timeStrs = (TTLocalizer.NewsPageDownloadingNews0,
                    TTLocalizer.NewsPageDownloadingNews1,
                    TTLocalizer.NewsPageDownloadingNews2)
        textToDisplay = timeStrs[timeIndex] % (int(self.percentDownloaded*100))
        
        return task.again

    def findWhitelistDir(self):
        """Returns the directory string for news content.

        Returns None if it cant find the directory
        """

        if self.WhitelistOverHttp:
            # If we're running whitelist-over-http, we dump the news into a
            # staging directory.
            return self.WhitelistStageDir

        searchPath = DSearchPath()
        if AppRunnerGlobal.appRunner:
            # In the web-publish runtime, it will always be here:
            searchPath.appendDirectory(Filename.expandFrom('$TT_3_5_ROOT/phase_3/etc'))
        else:
            # In the launcher or dev environment, look here:
            basePath = os.path.expandvars('$TTMODELS') or './ttmodels'
            searchPath.appendDirectory(Filename.fromOsSpecific(basePath + '/built/' + self.WhitelistBaseDir))
            searchPath.appendDirectory(Filename(self.WhitelistBaseDir))

        pfile = Filename(self.WhitelistFileName)
        found = vfs.resolveFilename(pfile, searchPath)
        if not found:
            self.notify.warning('findWhitelistDir - no path: %s' % self.WhitelistFileName)
            #self.setErrorMessage(TTLocalizer.NewsPageErrorDownloadingFile % self.WhitelistFileName)
            return None
        self.notify.debug("found whitelist file %s" % pfile)
        realDir = pfile.getDirname()
        return realDir

    def downloadWhitelistTask(self, task):
        """ Continues downloading the URL in self.url and self.filename. """

        if self.ch.run():
            return task.cont

        doc = self.ch.getDocumentSpec()
        date = ''
        if doc.hasDate():
            date = doc.getDate().getString()

        if not self.ch.isValid():
            self.notify.warning("Unable to download %s" % (self.url))
            self.redownloadingWhitelist = False
            return task.done
         # Hey, we're done!
        self.notify.info('Done downloading whitelist file')
        self.updateWhitelist()

        return task.done

    def updateWhitelist(self):
        localFilename = Filename(self.whitelistDir, 'twhitelist.dat')
        if not localFilename.exists():
            return
        data = vfs.readFile(localFilename, 1)
        lines = data.split(b'\n')
        self.words = []
        for line in lines:
            self.words.append(line.strip(b'\n\r').lower())

        self.words.sort()
        self.numWords = len(self.words)
        self.defaultWord = TTLocalizer.ChatGarblerDefault[0]

    def handleNewWhitelist(self):
        """Handle getting this newWhitelist message."""
        self.redownloadWhitelist()
