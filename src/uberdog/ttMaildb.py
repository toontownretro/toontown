import sys, datetime

from direct.directnotify import DirectNotifyGlobal

from otp.sql.SqlDB import SqlDB, SqlDBConnection, TryAgainLater
from otp.sql import SqlErrors
from otp.switchboard import sbConfig

from toontown.toonbase.ToontownModules import *
from toontown.uberdog import ttSQL

SERVER_GONE_ERROR = SqlErrors.ServerGoneAway
SERVER_LOST = SqlErrors.ServerLost

class TTMailDBConnection(SqlDBConnection):
    notify = directNotify.newCategory('ttMaildb')
    
    WantMailReconnects = ConfigVariableBool('want-tt-mail-db-reconnects', 1).getValue()

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
            if not self.WantMailReconnects:
                self.notify.warning(str(e))
                self.notify.warning("Failed to connect to SQL database=%s at %s:%d.  ttMaildb DB is disabled." % (self._dbName, self._host, self._port))
                self.request(self.Disconnected)
                return

            self.notify.warning(str(e))
            self._lastFailedConnectTime = globalClock.getRealTime()
            raise TryAgainLater(e, '%s:%s' % (self._host, self._port))
        else:
            #self._db.set_character_set('utf8')

            # spammy
            if not self.__class__.LoggedConnectionInfo:
                self.notify.debug("Connected to maildb=%s at %s:%d." % (self._dbName, self._host, self._port))
                self.__class__.LoggedConnectionInfo = True
            self.request(self.Initializing)
            
    def enterInitializing(self):
        cursor = self.getCursor()
        initDb = ConfigVariableBool('want-maildb-init', __dev__).getValue()
        if initDb:
            try:
                cursor.execute("CREATE DATABASE `%s`" % self._dbName)
                if __debug__:
                    self.notify.info("Database '%s' did not exist, created a new one!" % self._dbName)
            except SqlErrors.ProgrammingError as e:
                # self.notify.info('%s' % str(e))
                pass
            except SqlErrors.OperationalError as e:
                self.notify.info('%s' % str(e))
                pass
                
        cursor.execute("USE `%s`" % self._dbName)
        
        if __debug__:
            self.notify.debug("Using database '%s'" % self._dbName)
            
        try:
            cursor.execute("""
            CREATE TABLE ttrecipientmail (
              messageId             BIGINT     NOT NULL AUTO_INCREMENT UNIQUE,
              recipientId           BIGINT     NOT NULL,
              senderId              BIGINT     NOT NULL,
              message               TEXT       NOT NULL,
              lastupdate            TIMESTAMP  NOT NULL
                                     DEFAULT   CURRENT_TIMESTAMP
                                     ON UPDATE CURRENT_TIMESTAMP,
              dateSent		        TIMESTAMP  NOT NULL default CURRENT_TIMESTAMP,
              readFlag					BOOLEAN    DEFAULT FALSE,
              PRIMARY KEY  (messageId),
              INDEX idx_recipientId (recipientId)
            )
            ENGINE=InnoDB
            DEFAULT CHARSET=utf8;

            """)
            if __debug__:
                self.notify.info("Table ttrecipientmail did not exist, created a new one!")
        except SqlErrors.OperationalError as e:
            pass
            
        try:
            cursor = self.getCursor()
            cursor.execute("USE `%s`" % self._dbName)
            self.notify.debug("Using database '%s'" % self._dbName)
        except:
            self.notify.debug("%s database not found, maildb not active." % self._dbName)
        
        self.request(self.Locking)

class ttMaildb(SqlDB):
    """Based on sbMaildb.py in $OTP/src/switchboard."""

    notify = DirectNotifyGlobal.directNotify.newCategory("ttMaildb")

    def __init__(self, host, port, user, passwd, db):
        SqlDB.__init__(self, host, port, user, passwd, db)
        self.dbname = db
        
        self.db = TTMailDBConnection(self)

    def disconnect(self):
        if self.db.isOff():
            return
        self.db.destroy()
        self.db = None

    def getMail(self, recipientId, isRetry=False):
        if self.db.isDisabled():
            self.notify.debug("ttMaildb was disabled when calling getMail.")
            return ()

        try:
            cursor = self.db.getDictCursor()
            cursor.execute("USE `%s`" % self.dbname)
            cursor.execute(ttSQL.getMailSELECT, (recipientId,))
            res = cursor.fetchall()
            #self.notify.debug("Select was successful in ttMaildb, returning %s" % str(res))
            return res

        except SqlErrors.OperationalError as e:
            if isRetry == True:
                self.notify.warning("Error on getMail retry, giving up:\n%s" % str(e))
                return ()
            elif e.errno == SERVER_GONE_ERROR or e.errno == SERVER_LOST:
                self.db.reconnect()
                return self.getMail(recipientId, True)
            else:
                self.notify.warning("Unknown error in getMail, retrying:\n%s" % str(e))
                self.db.reconnect()
                return self.getMail(recipientId, True)
        except Exception as e:
            self.notify.warning("Unknown error in getMail, giving up:\n%s" % str(e))
            return ()

    def putMail(self, recipientId, senderId, message, isRetry=False):
        if self.db.isDisabled():
            self.notify.debug("ttMaildb was disabled when calling putMail.")
            return ()

        try:
            countcursor = self.db.getCursor()
            countcursor.execute("USE `%s`" % self.dbname)
            countcursor.execute(ttSQL.getMailSELECT, (recipientId,))
            if countcursor.rowcount >= sbConfig.mailStoreMessageLimit:
                self.notify.debug("%d's mailbox is full!  Can't fit message from %d." % (recipientId, senderId))
                return

            cursor = self.db.getDictCursor()
            cursor.execute(ttSQL.putMailINSERT, (recipientId, senderId, message))
            self.db.commit()

        except SqlErrors.OperationalError as e:
            if isRetry == True:
                self.notify.warning("Error on putMail retry, giving up:\n%s" % str(e))
                return
            elif e.errno == SERVER_GONE_ERROR or e.errno == SERVER_LOST:
                self.db.reconnect()
                self.putMail(recipientId, senderId, message, True)
            else:
                self.notify.warning("Unknown error in putMail, retrying:\n%s" % str(e))
                self.db.reconnect()
                self.putMail(recipientId, senderId, message, True)
        except Exception as e:
            self.notify.warning("Unknown error in putMail, giving up:\n%s" % str(e))
            return

    def deleteMail(self, accountId, messageId, isRetry=False):
        if self.db.isDisabled():
            self.notify.debug("ttMaildb was disabled when calling deleteMail.")
            return ()

        try:
            cursor = self.db.getDictCursor()
            cursor.execute("USE `%s`" % self.dbname)
            cursor.execute(ttSQL.deleteMailDELETE, (messageId, accountId))

            if cursor.rowcount < 1:
                self.notify.warning("%d tried to delete message %d which didn't exist or wasn't his!" % (accountId, messageId))

            self.db.commit()

        except SqlErrors.OperationalError as e:
            if isRetry == True:
                self.notify.warning("Error in deleteMail retry, giving up:\n%s" % str(e))
                return
            elif e.errno == SERVER_GONE_ERROR or e.errno == SERVER_LOST:
                self.db.reconnect()
                self.deleteMail(accountId, messageId, True)
            else:
                self.notify.warning("Unnown error in deleteMail, retrying:\n%s" % str(e))
                self.db.reconnect()
                self.deleteMail(accountId, messageId, True)
        except Exception as e:
            self.notify.warning("Unknown error in deleteMail, giving up:\n%s" % str(e))
            return

    def dumpMailTable(self):
        cursor = self.db.getDictCursor()
        cursor.execute("USE `%s`" % self.dbname)
        cursor.execute("SELECT * FROM recipientmail")
        return cursor.fetchall()