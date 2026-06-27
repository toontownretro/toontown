import direct
from direct.showbase.ShowBase import ShowBase

from otp.sql.DBInterface import DBInterface
from otp.sql.SqlDB import SqlDB, SqlDBConnection, TryAgainLater
from otp.sql import SqlErrors

from toontown.coderedemption import TTCodeRedemptionConsts
from toontown.toonbase.ToontownModules import *
from toontown.toonbase import TTLocalizer

language = TTLocalizer.getLanguage()

showbase = ShowBase(fStartDirect=False, windowType='none')
config = getConfigShowbase()

username = ConfigVariableString("mysql-user").getValue()
password = ConfigVariableString("mysql-passwd").getValue()

if username == "" or password == "":
    print("Username or password not found, check your config.prc!")
    sys.exit(2)
    
class WipeDBConnection(SqlDBConnection):
    def __init__(self, connectInfo, tableLocks={}):
        SqlDBConnection.__init__(self, connectInfo, tableLocks)
        
    def enterConnecting(self):
        if self._lastFailedConnectTime is not None:
            if (globalClock.getRealTime() - self._lastFailedConnectTime) < self.ConnectRetryTimeout:
                raise TryAgainLater(None, '%s:%s' % (self._host, self._port))

        if self._db:
            # No DB initialization required since we're already connected
            self.request(self.Locking)
            return

        try:
            self._db = self.__class__.ConnectFunction(host=self._host, port=self._port, user=self._user, password=self._passwd)
        except SqlErrors.OperationalError as e:
            self.notify.warning(str(e))
            self._lastFailedConnectTime = globalClock.getRealTime()
            raise TryAgainLater(e, '%s:%s' % (self._host, self._port))
        else:
            #self._db.set_character_set('utf8')

            # spammy
            if not self.__class__.LoggedConnectionInfo:
                self.notify.debug("Connected to database=%s at %s:%d." % (self._dbName, self._host, self._port))
                self.__class__.LoggedConnectionInfo = True
            self.request(self.Initializing)
                
    def enterInitializing(self):
        self.request(self.Locking)
        
class WipeDB(SqlDB):
    def __init__(self, host, port, user, passwd, dbname):
        SqlDB.__init__(self, host, port, user, passwd, dbname)
        self.dbname = db
        
        self.db = WipeDBConnection(self)
        
    def setDatabase(self, dbname):
        self.db.destroy()
        self.db._dbName = dbname
        self.dbname = dbname
        self.db.connect()
        
    def commit(self):
        try:
            self.db.commit()
        except Exception as e:
            print("  Failed: %s" % e)
        
    def execute(self):
        try:
            print("Dropping database %s:" % self.dbname)
            cursor = self.db.getCursor()
            cursor.execute("DROP DATABASE %s"% self.dbname)
            print("  Success!")
        except Exception as e:
            print("  Failed: %s" % e)


if language == 'castillian':
    ttDbName = "es_toontownTopDb"
elif language == "japanese":
    ttDbName = "jp_toontownTopDb"
elif language == "german":
    ttDbName = "de_toontownTopDb"
elif language == "french":
    ttDbName = "french_toontownTopDb"
elif language == "portuguese":
    ttDbName = "br_toontownTopDb"
else:
    ttDbName = "toontownTopDb"
    
db = WipeDB("localhost", 3306, username, password, ttDbName)
db.execute()

db.setDatabase(DBInterface.processDBName(TTCodeRedemptionConsts.DefaultDbName))
db.execute()

db.commit()
