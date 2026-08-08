import os

class ModuleList:
    serverDataFolder = simbase.config.GetString('server-data-folder', "")

    def __init__(self):
        self.moduleWhitelistFilename = self.getWhitelistFilename()
        self.moduleBlacklistFilename = self.getBlacklistFilename()
        self.loadBlacklistFile()
        self.loadWhitelistFile()

    def getWhitelistFilename(self):
        """Compose the track record filename"""
        result = "%s.moduleWhiteList" % (self.serverDataFolder)
        return result

    def getBlacklistFilename(self):
        """Compose the track record filename"""
        result = "%s.moduleBlackList" % (self.serverDataFolder)
        return result

    def loadBlacklistFile(self):
        """Load track record data from default location"""
        try:
            # Try to open the backup file:
            file = open(self.moduleBlacklistFilename + '.bu', 'rb')
            # Remove the (assumed) broken file:
            if os.path.exists(self.moduleBlacklistFilename):
                os.remove(self.moduleBlacklistFilename)
        except IOError:
            # OK, there's no backup file, good.
            try:
                # Open the real file:
                file = open(self.moduleBlacklistFilename, 'rb')
            except IOError:
                # OK, there's no file.  Grab the default times.
                return set()
        file.seek(0)
        moduleFile = self.loadFrom(file)
        file.close()

        result = self.loadFrom(moduleFile)
        self.moduleBlacklist = result

        return result

    def loadWhitelistFile(self):
        """Load track record data from default location"""
        try:
            # Try to open the backup file:
            file = open(self.moduleWhitelistFilename + '.bu', 'rb')
            # Remove the (assumed) broken file:
            if os.path.exists(self.moduleWhitelistFilename):
                os.remove(self.moduleWhitelistFilename)
        except IOError:
            # OK, there's no backup file, good.
            try:
                # Open the real file:
                file = open(self.moduleWhitelistFilename, 'rb')
            except IOError:
                # OK, there's no file.  Grab the default times.
                return set()

        file.seek(0)
        moduleFile = self.loadFrom(file)
        file.close()

        result = self.loadFrom(moduleFile)
        self.moduleWhitelist = result

        return result

    def loadFrom(self, file):
        """Load track record data from specified file"""
        result = set()
        try:
            for module in file:
                module = module.strip()
                if module:
                    result.add(module)
        except EOFError:
            pass
        return result

    def updateWhitelistFile(self):
        """Update current track record in this shard's record file"""
        # notify the leader boards that there has been an update
        try:
            backup = self.getWhitelistFilename() + '.bu'
            if os.path.exists(self.getWhitelistFilename()):
                os.rename(self.getWhitelistFilename(), backup)
            file = open(self.getWhitelistFilename(), 'wb')
            file.seek(0)
            for whiteModule in self.moduleWhitelist:
                file.write(whiteModule + '\n')
            file.close()
            if os.path.exists(backup):
                os.remove(backup)

        except EnvironmentError:
            self.notify.warning(str(sys.exc_info()[1]))

    def updateBlacklistFile(self):
        """Update current track record in this shard's record file"""
        # notify the leader boards that there has been an update
        try:
            backup = self.getBlacklistFilename() + '.bu'
            if os.path.exists(self.getBlacklistFilename()):
                os.rename(self.getBlacklistFilename(), backup)
            file = open(self.getBlacklistFilename(), 'wb')
            file.seek(0)
            for blackModule in self.moduleBlacklist:
                file.write(blackModule + '\n')
            file.close()
            if os.path.exists(backup):
                os.remove(backup)

        except EnvironmentError:
            self.notify.warning(str(sys.exc_info()[1]))
