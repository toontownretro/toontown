import os
import shutil
import datetime
from toontown.toonbase.ToontownModules import *
from direct.directnotify import DirectNotifyGlobal
from direct.distributed import DistributedObject
from direct.showbase import AppRunnerGlobal
from toontown.toonbase import TTLocalizer

class StreetSign(DistributedObject.DistributedObject):
    RedownloadTaskName = "RedownloadStreetSign"
    StreetSignFileName = ConfigVariableString("street-sign-filename", "texture.jpg").getValue()
    StreetSignBaseDir = ConfigVariableString("street-sign-base-dir", "sign").getValue()
    # Early 2024 cdn.toontown.disney.go.com became unreachable, we need to change it to cdn.toontown.dolimg.com
    # Early 2025 cdn.toontown.dolimg.com became unreachable, we need to change it to cdn.dolimg.com
    StreetSignUrl = ConfigVariableString("street-sign-url", "http://cdn.dolimg.com/toontown/en/street-signs/img/").getValue()
    notify = DirectNotifyGlobal.directNotify.newCategory("StreetSign")

    def __init__(self):
        self.downloadingStreetSign = False
        self.percentDownloaded = 0.0
        self.startDownload = datetime.datetime.now()
        self.endDownload = datetime.datetime.now()
        self.notify.info('Street sign url is %s' % self.StreetSignUrl)
        self.redownloadStreetSign()

    def replaceTexture(self):
        searchPath = DSearchPath()
        searchPath.appendDirectory(self.directory)

    def redownloadStreetSign(self):
        """Get the new sign that came out while he was playing."""

        # I know it's info, it's important enough I feel to appear in the logs
        self.precentDownload = 0.0
        self.startRedownload = datetime.datetime.now()
        self.downloadingStreetSign = True

        # Ensure self.StreetSignBaseDir exists and is a directory.
        Filename(self.StreetSignBaseDir + '/.').makeDir()
        
        http = HTTPClient.getGlobalPtr()
        self.url = self.StreetSignUrl + self.StreetSignFileName
        self.ch = http.makeChannel(True)
        localFilename = Filename(self.StreetSignBaseDir, self.StreetSignFileName)
        self.ch.getHeader(DocumentSpec(self.url))
        size = self.ch.getFileSize()
        doc = self.ch.getDocumentSpec()
        localSize = localFilename.getFileSize()
        outOfDate = True
        
        if size == localSize:
        
            if doc.hasDate():
                date = doc.getDate()
                localDate = HTTPDate(localFilename.getTimestamp())
                
                if localDate.compareTo(date) > 0:
                    outOfDate = False
                    self.notify.info('Street Sign is up to date')
                    
        if outOfDate and self.ch.isValid():
            self.ch.beginGetDocument(doc)
            self.ch.downloadToFile(localFilename)
            taskMgr.add(self.downloadStreetSignTask, self.RedownloadTaskName)

    def downloadStreetSignTask(self, task):
        """ Continues downloading the URL in self.url and self.filename. """

        if self.ch.run():
            return task.cont

        doc = self.ch.getDocumentSpec()
        date = ''
        if doc.hasDate():
            date = doc.getDate().getString()
            
        if not self.ch.isValid():
            self.redownloadingStreetSign = False
            return task.done

        # Successfully downloaded.
        self.notify.info("Down downloading street sign")
        return task.done
