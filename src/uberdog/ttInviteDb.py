import sys, datetime

from direct.directnotify import DirectNotifyGlobal

from otp.sql.SqlDB import SqlDB, SqlDBConnection, TryAgainLater
from otp.sql import SqlErrors

from toontown.uberdog import ttSQL
from toontown.parties import PartyGlobals

from toontown.toonbase.ToontownModules import *

SERVER_GONE_ERROR = SqlErrors.ServerGoneAway
SERVER_LOST = SqlErrors.ServerLost

class TTInviteDBConnection(SqlDBConnection):
    notify = directNotify.newCategory('ttInviteDb')
    
    WantInviteReconnects = ConfigVariableBool('want-tt-invite-db-reconnects', 1).getValue()

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
            if not self.WantInviteReconnects:
                self.notify.warning(str(e))
                self.notify.warning("Failed to connect to SQL database=%s at %s:%d.  ttInviteDb DB is disabled." % (self._dbName, self._host, self._port))
                self.request(self.Disconnected)
                return

            self.notify.warning(str(e))
            self._lastFailedConnectTime = globalClock.getRealTime()
            raise TryAgainLater(e, '%s:%s' % (self._host, self._port))
        else:
            #self._db.set_character_set('utf8')

            # spammy
            if not self.__class__.LoggedConnectionInfo:
                self.notify.debug("Connected to invitedb=%s at %s:%d." % (self._dbName, self._host, self._port))
                self.__class__.LoggedConnectionInfo = True
            self.request(self.Initializing)
            
    def enterInitializing(self):
        cursor = self.getCursor()
        initDb = ConfigVariableBool('want-tt-invitedb-init', __dev__).getValue()
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
            # well if we're creating the party table again,
            # might as well create the party status lookup table for the benefit of database reporting
            cursor.execute("Show tables like 'ttInviteStatus';")
            if not cursor.rowcount:
                # we know the ttInviteStatus table doesn't exist, create it again
                cursor.execute("""
                DROP TABLE IF EXISTS ttInviteStatus;
                """)

                cursor.execute("""
                CREATE TABLE ttInviteStatus(
                  statusId      TINYINT NOT NULL,
                  description   VARCHAR(20) NOT NULL,
                  lastupdate    TIMESTAMP  NOT NULL
                                      DEFAULT   CURRENT_TIMESTAMP
                                      ON UPDATE CURRENT_TIMESTAMP,
                  PRIMARY KEY (statusId),
                  UNIQUE INDEX uidx_desc(description)
                )
                ENGINE=Innodb
                DEFAULT CHARSET=utf8;
                """)
                # this ensure that the table values come directly from PartyGlobals.InviteStatus
                for index in range(len(PartyGlobals.InviteStatus)):
                    cursor.execute(\
                        "INSERT INTO ttInviteStatus(statusId, description) VALUES (%d, '%s')" %
                    (index, PartyGlobals.InviteStatus.getString(index)))

            # TODO is it better to do a show tables than to do a try create Table except block?
            cursor.execute("""
            CREATE TABLE ttInvite (
              inviteId           BIGINT     NOT NULL AUTO_INCREMENT,
              partyId            BIGINT     NOT NULL,
              guestId            BIGINT     NOT NULL,
              statusId           TINYINT    NOT NULL DEFAULT 0,
              lastupdate         TIMESTAMP  NOT NULL
                                 DEFAULT   CURRENT_TIMESTAMP
                                 ON UPDATE CURRENT_TIMESTAMP,

              PRIMARY KEY  (inviteId),
              INDEX idx_guestId (guestId),
              INDEX idx_partyId(partyId),
              FOREIGN KEY (partyId) REFERENCES ttParty(partyId) ON DELETE CASCADE
            )
            ENGINE=InnoDB
            DEFAULT CHARSET=utf8;
            """)
            if __debug__:
                self.notify.info("Table ttInvite did not exist, created a new one!")
        except SqlErrors.OperationalError as e:
            #self.notify.warning("Unknown error when creating tables, retrying:\n%s" % str(e))
            pass
            
        try:
            cursor = self.getCursor()
            cursor.execute("USE `%s`" % self._dbName)
            self.notify.debug("Using database '%s'" % self._dbName)
        except:
            self.notify.debug("%s database not found, ttInviteDb not active." % self._dbName)
            
        self.request(self.Locking)

class ttInviteDb(SqlDB):
    """Based on sbMaildb.py in $OTP/src/switchboard."""

    notify = DirectNotifyGlobal.directNotify.newCategory("ttInviteDb")

    def __init__(self, host, port, user, passwd, db):
        SqlDB.__init__(self, host, port, user, passwd, db)
        self.dbname = db
        
        self.db = TTInviteDBConnection(self)

    def disconnect(self):
        if self.db.isOff():
            return
        self.db.destroy()
        self.db = None

    def getInvites(self, avatarId, isRetry=False):
        """
        Returns a tuple, which could be empty.
        """
        if self.db.isDisabled():
            self.notify.debug("ttInviteDb was disabled when calling getInvites.")
            return ()

        try:
            cursor = self.db.getDictCursor()
            cursor.execute("USE `%s`"%self.dbname)
            cursor.execute(ttSQL.getInvitesSELECT,(avatarId,))
            res = cursor.fetchall()
            self.notify.debug("Select was successful in ttInvitedb, returning %s" % str(res))
            return res

        except SqlErrors.OperationalError as e:
            if isRetry == True:
                self.notify.warning("Error on getInvites retry, giving up:\n%s" % str(e))
                return ()
            elif e.errno == SERVER_GONE_ERROR or e.errno == SERVER_LOST:
                self.db.reconnect()
                return self.getInvites(avatarId,True)
            else:
                self.notify.warning("Unknown error in getInvites, retrying:\n%s" % str(e))
                self.db.reconnect()
                return self.getInvites(avatarId,True)
        except Exception as e:
            self.notify.warning("Unknown error in getInvites, giving up:\n%s" % str(e))
            return ()

    def putInvite(self, partyId, inviteeId, isRetry=False):
        if self.db.isDisabled():
            self.notify.debug("ttInviteDb was disabled when calling putInvite.")
            return

        try:
            cursor = self.db.getDictCursor()
            cursor.execute(ttSQL.putInviteINSERT, (partyId, inviteeId))
            self.db.commit()

        except SqlErrors.OperationalError as e:
            if isRetry == True:
                self.notify.warning("Error on putInvite retry, giving up:\n%s" % str(e))
                return
            elif e.errno == SERVER_GONE_ERROR or e.errno == SERVER_LOST:
                self.db.reconnect()
                self.putInvite(partyId, inviteeId, True)
            else:
                self.notify.warning("Unknown error in putInvite, retrying:\n%s" % str(e))
                self.db.reconnect()
                self.putInvite(partyId, inviteeId, True)
        except Exception as e:
            self.notify.warning("Unknown error in putInvite, giving up:\n%s" % str(e))
            return

    def deleteInviteByParty(self, partyId, isRetry=False):
        if self.db.isDisabled():
            self.notify.debug("ttInviteDb was disabled when calling deleteInviteByParty.")
            return

        try:
            cursor = self.db.getDictCursor()
            cursor.execute("USE `%s`"%self.dbname)
            cursor.execute(ttSQL.deleteInviteByPartyDELETE,( partyId))

            if cursor.rowcount < 1:
                self.notify.warning("%d tried to delete party %d which didn't exist or wasn't his!" % (accountId,messageId))

            self.db.commit()

        except SqlErrors.OperationalError as e:
            if isRetry == True:
                self.notify.warning("Error in deleteInviteByParty retry, giving up:\n%s" % str(e))
                return
            elif e.errno == SERVER_GONE_ERROR or e.errno == SERVER_LOST:
                self.db.reconnect()
                self.deleteMail(accountId, messageId, True)
            else:
                self.notify.warning("Unnown error in deleteInviteByParty, retrying:\n%s" % str(e))
                self.db.reconnect()
                self.deleteMail(accountId, messageId, True)
        except Exception as e:
            self.notify.warning("Unknown error in deleteInviteByParty, giving up:\n%s" % str(e))
            return

    def getReplies(self, partyId, isRetry=False):
        if self.db.isDisabled():
            self.notify.debug("ttInviteDb was disabled when calling getReplies.")
            return ()

        try:
            cursor = self.db.getDictCursor()
            cursor.execute("USE `%s`"%self.dbname)
            cursor.execute(ttSQL.getRepliesSELECT,(partyId,))
            res = cursor.fetchall()
            #self.notify.debug("Select was successful in ttInvitedb, returning %s" % str(res))
            return res

        except SqlErrors.OperationalError as e:
            if isRetry == True:
                self.notify.warning("Error on getReplies retry, giving up:\n%s" % str(e))
                return ()
            elif e.errno == SERVER_GONE_ERROR or e.errno == SERVER_LOST:
                self.db.reconnect()
                return self.getReplies(partyId, True)
            else:
                self.notify.warning("Unknown error in getReplies, retrying:\n%s" % str(e))
                self.db.reconnect()
                return self.getReplies(partyId, True)
        except Exception as e:
            self.notify.warning("Unknown error in getReplies, giving up:\n%s" % str(e))
            return ()

    def dumpInviteTable(self):
        cursor = self.db.getDictCursor()
        cursor.execute("USE `%s`"%self.dbname)
        cursor.execute("SELECT * FROM ttInviteDb")
        return cursor.fetchall()

    def getOneInvite(self, inviteKey, isRetry = False):
        if self.db.isDisabled():
            self.notify.debug("ttInviteDb was disabled when calling getOneInvite.")
            return ()

        try:
            cursor = self.db.getDictCursor()
            cursor.execute("USE `%s`"%self.dbname)
            cursor.execute(ttSQL.getOneInviteSELECT,(inviteKey,))
            res = cursor.fetchall()
            #self.notify.debug("Select was successful in ttInvitedb, returning %s" % str(res))
            return res

        except SqlErrors.OperationalError as e:
            if isRetry == True:
                self.notify.warning("Error on getOneInvite retry, giving up:\n%s" % str(e))
                return ()
            elif e.errno == SERVER_GONE_ERROR or e.errno == SERVER_LOST:
                self.db.reconnect()
                return self.getOneInvite(partyId, True)
            else:
                self.notify.warning("Unknown error in getOneInvite, retrying:\n%s" % str(e))
                self.db.reconnect()
                return self.getOneInvite(partyId, True)
        except Exception as e:
            self.notify.warning("Unknown error in getOneInvite, giving up:\n%s" % str(e))
            return ()

    def updateInvite(self, inviteKey, newStatus, isRetry = False):
        if self.db.isDisabled():
            self.notify.debug("ttInviteDb was disabled when calling updateInvite.")
            return ()

        try:
            cursor = self.db.getDictCursor()
            cursor.execute("USE `%s`"%self.dbname)
            cursor.execute(ttSQL.inviteUPDATE,(newStatus, inviteKey))
            self.db.commit()
            res = cursor.fetchall()
            #self.notify.debug("Select was successful in ttInvitedb, returning %s" % str(res))
            return res

        except SqlErrors.OperationalError as e:
            if isRetry == True:
                self.notify.warning("Error on updateInvite retry, giving up:\n%s" % str(e))
                return ()
            elif e.errno == SERVER_GONE_ERROR or e.errno == SERVER_LOST:
                self.db.reconnect()
                return self.updateInvite( newStatus, inviteKey, True)
            else:
                self.notify.warning("Unknown error in updateInvite, retrying:\n%s" % str(e))
                self.db.reconnect()
                return self.updateInvite( newStatus, inviteKey, True)
        except Exception as e:
            self.notify.warning("Unknown error in updateInvite, giving up:\n%s" % str(e))
            return ()

    def getInviteesOfParty(self, inviteKey, isRetry = False):
        if self.db.isDisabled():
            self.notify.debug("ttInviteDb was disabled when calling getInviteesOfParty.")
            return ()

        try:
            cursor = self.db.getDictCursor()
            cursor.execute("USE `%s`"%self.dbname)
            cursor.execute(ttSQL.getInviteesOfPartySELECT,(inviteKey,))
            res = cursor.fetchall()
            #self.notify.debug("Select was successful in ttInvitedb, returning %s" % str(res))
            return res

        except SqlErrors.OperationalError as e:
            if isRetry == True:
                self.notify.warning("Error on getInviteesOfParty retry, giving up:\n%s" % str(e))
                return ()
            elif e.errno == SERVER_GONE_ERROR or e.errno == SERVER_LOST:
                self.db.reconnect()
                return self.getInviteesOfParty(partyId, True)
            else:
                self.notify.warning("Unknown error in getInviteesOfParty, retrying:\n%s" % str(e))
                self.db.reconnect()
                return self.getInviteesOfParty(partyId, True)
        except Exception as e:
            self.notify.warning("Unknown error in getInviteesOfParty, giving up:\n%s" % str(e))
            return ()