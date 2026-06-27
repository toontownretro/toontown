import sys, datetime

from direct.directnotify import DirectNotifyGlobal

from otp.sql.SqlDB import SqlDB, SqlDBConnection, TryAgainLater
from otp.sql import SqlErrors

from toontown.uberdog import ttSQL
from toontown.parties import PartyGlobals
from toontown.parties.PartyGlobals import PartyStatus,InviteTheme

from toontown.toonbase.ToontownModules import *

SERVER_GONE_ERROR = SqlErrors.ServerGoneAway
SERVER_LOST = SqlErrors.ServerLost

class TTPartyDBConnection(SqlDBConnection):
    notify = directNotify.newCategory('ttPartyDb')
    
    WantPartyReconnects = ConfigVariableBool('want-tt-party-db-reconnects', 1).getValue()

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
            if not self.WantPartyReconnects:
                self.notify.warning(str(e))
                self.notify.warning("Failed to connect to SQL database=%s at %s:%d.  ttPartyDb DB is disabled." % (self._dbName, self._host, self._port))
                self.request(self.Disconnected)
                return

            self.notify.warning(str(e))
            self._lastFailedConnectTime = globalClock.getRealTime()
            raise TryAgainLater(e, '%s:%s' % (self._host, self._port))
        else:
            #self._db.set_character_set('utf8')

            # spammy
            if not self.__class__.LoggedConnectionInfo:
                self.notify.debug("Connected to partydb=%s at %s:%d." % (self._dbName, self._host, self._port))
                self.__class__.LoggedConnectionInfo = True
            self.request(self.Initializing)
                
    def enterInitializing(self):
        cursor = self.getCursor()
        initDb = ConfigVariableBool('want-tt-partydb-init', __dev__).getValue()
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
            cursor.execute("Show tables like 'ttPartyStatus';")
            if not cursor.rowcount:
                # we know the ttPartyStatus table doesn't exist, create it again
                cursor.execute("""
                DROP TABLE IF EXISTS ttPartyStatus;
                """)

                cursor.execute("""
                CREATE TABLE ttPartyStatus(
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
                # this ensure that the table values come directly from PartyGlobals.PartyStatus
                for index in range(len(PartyGlobals.PartyStatus)):
                    cursor.execute(\
                        "INSERT INTO ttPartyStatus(statusId, description) VALUES (%d, '%s')" %
                    (index, PartyGlobals.PartyStatus.getString(index)))

            # TODO is it better to do a show tables than to do a try create Table except block?
            cursor.execute("""
            CREATE TABLE ttParty (
              partyId             BIGINT     NOT NULL AUTO_INCREMENT,
              hostId              BIGINT     NOT NULL,
              startTime           TIMESTAMP     NOT NULL  default CURRENT_TIMESTAMP,
              endTime             TIMESTAMP     NOT NULL  default CURRENT_TIMESTAMP,
              isPrivate             BOOLEAN       default False,
              inviteTheme         TINYINT,
              activities           VARBINARY(252),
              decorations         VARBINARY(252),
              statusId              TINYINT default 0,
              creationTime          TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
              lastupdate          TIMESTAMP  NOT NULL
                                  DEFAULT   CURRENT_TIMESTAMP
                                  ON UPDATE CURRENT_TIMESTAMP,

              PRIMARY KEY  (partyId),
              INDEX idx_hostId (hostId),
              INDEX idx_statusId(statusId)
            )
            ENGINE=InnoDB
            DEFAULT CHARSET=utf8;

            """)

            # size calculations
            # partyId  8 bytes
            # hostId   8 bytes
            # startTime 4 bytes
            # endTime   4 bytes
            # isPrivate 1 byte
            # inviteTheme 1 byte
            # activites 252 bytes
            # decorations 252 bytes
            # statys 1 byte
            # creationTime 4 bytes
            # lastupdate 4 bytes
            # TOTAL = 539 bytes
            if __debug__:
                self.notify.info("Table ttParty did not exist, created a new one!")
        except SqlErrors.OperationalError as e:
            pass

        try:
            cursor = self.getCursor()
            cursor.execute("USE `%s`"%self._dbName)
            self.notify.debug("Using database '%s'"%self._dbName)
        except:
            self.notify.debug("%s database not found, ttPartydb not active." % self._dbName)
            
        self.request(self.Locking)

class ttPartyDb(SqlDB):
    """Based on sbMaildb.py in $OTP/src/switchboard."""

    notify = DirectNotifyGlobal.directNotify.newCategory("ttPartyDb")

    def __init__(self, host, port, user, passwd, db):
        SqlDB.__init__(self, host, port, user, passwd, db)
        self.dbname = db
        
        self.db = TTPartyDBConnection(self)
        
    def disconnect(self):
        if self.db.isOff():
            return
        self.db.destroy()
        self.db = None

    def getParty(self, partyId, isRetry=False):
        """
        isRetry indicates whether this attempt is a retry or not.
        """
        if self.db.isDisabled():
            self.notify.debug("ttPartyDb was disabled when calling getParty")
            return ()

        try:
            cursor = self.db.getDictCursor()
            cursor.execute("USE `%s`" % self.dbname)
            cursor.execute(ttSQL.getPartySELECT, (partyId,))
            res = cursor.fetchall()
            self.notify.debug("Select was successful in ttPartyDb, returning %s" % str(res))
            return res
        except SqlErrors.OperationalError as e:
            if isRetry:
                self.notify.warning("Error on getParty retry. Giving up:\n%s" % str(e))
                return ()
            elif e.errno == SERVER_GONE_ERROR or e.errno == SERVER_LOST:
                self.db.reconnect()
                return self.getParty(partyId,True)
            else:
                self.notify.warning("Unknown error in getParty, retrying:\n%s" % str(e))
                self.db.reconnect()
                return self.getParty(partyId,True)
        except Exception as e:
            self.notify.warning("Unknown error in getParty, giving up:\n%s" % str(e))
            return ()

    def putParty(self, hostId, startTime, endTime, isPrivate, inviteTheme, activities, decorations, status, isRetry=False):
        """
        Returns False if the operation failed for any reason.

        isRetry indicates whether this attempt is a retry or not.
        """
        self.notify.debug("putParty( hostId=%s, startTime=%s, endTime=%s, isPrivate=%s, inviteTheme=%s, ... status=%s, isRetry=%s )" %(hostId, startTime, endTime, isPrivate, InviteTheme.getString(inviteTheme), PartyStatus.getString(status), isRetry) )
        if self.db.isDisabled():
            self.notify.warning("ttPartyDb was disabled when calling putParty.")
            return False

        # we need to parse activites and decorations
        activityStr = ""
        for activity in activities:
            for field in activity:
                activityStr += chr(field)

        decorStr = ""
        for decor in decorations:
            for field in decor:
                decorStr += chr(field)

        try:
            countcursor = self.db.getCursor()
            countcursor.execute("USE `%s`" % self.dbname)
            countcursor.execute(ttSQL.getPartyOfHostMatchingStatusSELECT,(hostId,PartyStatus.Pending))
            if countcursor.rowcount >= PartyGlobals.MaxHostedPartiesPerToon:
                self.notify.debug("%d can't host another party, over the limit " %(hostId))
                return False

            cursor = self.db.getDictCursor()

            cursor.execute(ttSQL.putPartyINSERT,
                           (hostId, startTime, endTime, isPrivate, inviteTheme, activityStr, decorStr, status))
            self.db.commit()
        except SqlErrors.OperationalError as e:
            if isRetry:
                self.notify.warning("putParty failed with error '%s' on retry. Giving up." % str(e))
                return False
            elif e.errno == SERVER_GONE_ERROR or e.errno == SERVER_LOST:
                self.db.reconnect()
                return self.putParty(hostId, startTime, endTime, isPrivate, inviteTheme, activityStr, decorStr, status, True)
            else:
                self.notify.warning("putParty failed with error '%s'. Retrying." % str(e))
                self.db.reconnect()
                return self.putParty(hostId, startTime, endTime, isPrivate, inviteTheme, activityStr, decorStr, status, True)
        except Exception as e:
            self.notify.warning("putParty failed with error '%s'. Giving up." % str(e))
            return False

        return True # if we got this far without an exception, we're good

    def deleteParty(self,partyId,isRetry=False):
        """
        isRetry indicates whether this attempt is a retry or not.
        """
        if self.db.isDisabled():
            self.notify.warning("ttPartyDb was disabled when calling deleteParty.")
            return

        try:
            cursor = self.db.getDictCursor()
            cursor.execute("USE `%s`"%self.dbname)
            cursor.execute(ttSQL.deletePartyDELETE,(messageId, partyId))

            if cursor.rowcount < 1:
                self.notify.warning("%d tried to delete party %d which didn't exist or wasn't his!" % (accountId,messageId))

            self.db.commit()

        except SqlErrors.OperationalError as e:
            if isRetry:
                self.notify.warning("Error in deleteParty retry, giving up:\n%s" % str(e))
                return
            elif e.errno == SERVER_GONE_ERROR or e.errno == SERVER_LOST:
                self.db.reconnect()
                self.deleteParty(partyId,True)
            else:
                self.notify.warning("Unnown error in deleteParty, retrying:\n%s" % str(e))
                self.db.reconnect()
                self.deleteParty(partyId,True)
        except Exception as e:
            self.notify.warning("Unknown error in deleteParty, giving up:\n%s" % str(e))
            return

    def dumpPartyTable(self):
        cursor = self.db.getDictCursor()
        cursor.execute("USE `%s`"%self.dbname)
        cursor.execute("SELECT * FROM ttPartyDb")
        return cursor.fetchall()

    def getPartiesAvailableToStart(self, currentTime, isRetry=False):
        """
        Returns a list of tuples of partyId and hostId of all parties allowed to
        start.  A party is allowed to start if its status is Pending and server
        time is past it's start time.
        """
        if self.db.isDisabled():
            self.notify.debug("ttPartyDb was disabled when calling getPartiesAvailableToStart.")
            return ()

        try:
            cursor = self.db.getDictCursor()
            cursor.execute("USE `%s`"%self.dbname)
            cursor.execute(ttSQL.getPartiesAvailableToStart,(currentTime, PartyGlobals.PartyStatus.Pending))
            res = cursor.fetchall()
            # Ok, these parties can start, go ahead and set their status to CanStart
            self._setPartyStatusToCanStart(res)
            return res

        except SqlErrors.OperationalError as e:
            if isRetry:
                self.notify.warning("Error on getPartiesAvailableToStart retry, giving up:\n%s" % str(e))
                return ()
            elif e.errno == SERVER_GONE_ERROR or e.errno == SERVER_LOST:
                self.db.reconnect()
                return self.getPartiesAvailableToStart(currentTime, True)
            else:
                self.notify.warning("Unknown error in getPartiesAvailableToStart, retrying:\n%s" % str(e))
                self.db.reconnect()
                return self.getPartiesAvailableToStart(currentTime,True)
        except Exception as e:
            self.notify.warning("Unknown error in getPartiesAvailableToStart, giving up:\n%s" % str(e))
            return ()

    def _setPartyStatusToCanStart(self, tupleOfResultDictionaries):
        """ Set the status on the following parties to CanStart """
        for resDict in tupleOfResultDictionaries:
            self.changePartyStatus(resDict['partyId'], PartyGlobals.PartyStatus.CanStart)

    def getPartiesOfHost(self, hostId, sortedByStartTime = False, isRetry=False):
        """
        Returns a tuple, which could be empty.

        isRetry indicates whether this attempt is a retry or not.
        """
        if self.db.isDisabled():
            self.notify.debug("ttPartyDb was disabled when calling getPartiesOfHost.")
            return ()

        try:
            cursor = self.db.getDictCursor()
            cursor.execute("USE `%s`"%self.dbname)
            if sortedByStartTime:
                cursor.execute(ttSQL.getPartyOfHostSortedSELECT,(hostId,))
            else:
                cursor.execute(ttSQL.getPartyOfHostSELECT,(hostId,))
            res = cursor.fetchall()
            #self.notify.debug("Select was successful in ttMaildb, returning %s" % str(res))
            return res

        except SqlErrors.OperationalError as e:
            if isRetry:
                self.notify.warning("Error on getPartiesOfHost retry, giving up:\n%s" % str(e))
                return ()
            elif e.errno == SERVER_GONE_ERROR or e.errno == SERVER_LOST:
                self.db.reconnect()
                return self.getPartiesOfHost(hostId, sortedByStartTime, True)
            else:
                self.notify.warning("Unknown error in getPartiesOfHost, retrying:\n%s" % str(e))
                self.db.reconnect()
                return self.getPartiesOfHost(hostId, sortedByStartTime, True)
        except Exception as e:
            self.notify.warning("Unknown error in getPartiesOfHost, giving up:\n%s" % str(e))
            return ()

    def getPartiesOfHostThatCanStart(self, hostId, isRetry=False):
        """
        Returns a tuple, which could be empty.
        isRetry indicates whether this attempt is a retry or not.
        """
        if self.db.isDisabled():
            self.notify.debug("ttPartyDb was disabled when calling getPartiesOfHostThatCanStart.")
            return ()

        try:
            cursor = self.db.getDictCursor()
            cursor.execute("USE `%s`"%self.dbname)
            cursor.execute(ttSQL.getPartyOfHostMatchingStatusSELECT,(hostId,PartyGlobals.PartyStatus.CanStart))
            res = cursor.fetchall()
            return res

        except SqlErrors.OperationalError as e:
            if isRetry:
                self.notify.warning("Error on getPartiesOfHostThatCanStart retry, giving up:\n%s" % str(e))
                return ()
            elif e.errno == SERVER_GONE_ERROR or e.errno == SERVER_LOST:
                self.db.reconnect()
                return self.getPartiesOfHostThatCanStart(hostId, True)
            else:
                self.notify.warning("Unknown error in getPartiesOfHostThatCanStart, retrying:\n%s" % str(e))
                self.db.reconnect()
                return self.getPartiesOfHostThatCanStart(hostId, True)
        except Exception as e:
            self.notify.warning("Unknown error in getPartiesOfHostThatCanStart, giving up:\n%s" % str(e))
            return ()

    def changePrivate(self, partyId, newPrivateStatus, isRetry=False):
        """
        isRetry indicates whether this attempt is a retry or not.
        """
        if self.db.isDisabled():
            self.notify.debug("ttPartyDb was disabled when calling changePrivate.")
            return ()

        try:
            cursor = self.db.getDictCursor()
            cursor.execute("USE `%s`"%self.dbname)
            cursor.execute(ttSQL.partyPrivateUPDATE,( newPrivateStatus, partyId))
            self.db.commit()
            res = cursor.fetchall()
            #self.notify.debug("Select was successful in ttMaildb, returning %s" % str(res))
            return res

        except SqlErrors.OperationalError as e:
            if isRetry:
                self.notify.warning("Error on changePrivate retry, giving up:\n%s" % str(e))
                return ()
            elif e.errno == SERVER_GONE_ERROR or e.errno == SERVER_LOST:
                self.db.reconnect()
                return self.changePrivate(newPrivateStatus, partyId, True)
            else:
                self.notify.warning("Unknown error in changePrivate, retrying:\n%s" % str(e))
                self.db.reconnect()
                return self.changePrivate( newPrivateStatus, partyId, True)
        except Exception as e:
            self.notify.warning("Unknown error in changePrivate, giving up:\n%s" % str(e))
            return ()

    def changePartyStatus(self, partyId, newPartyStatus, isRetry=False):
        """
        isRetry indicates whether this attempt is a retry or not.
        """
        if self.db.isDisabled():
            self.notify.debug("ttPartyDb was disabled when calling changePartyStatus.")
            return ()

        try:
            cursor = self.db.getDictCursor()
            cursor.execute("USE `%s`"%self.dbname)
            cursor.execute(ttSQL.partyStatusUPDATE,( newPartyStatus, partyId))
            self.db.commit()
            res = cursor.fetchall()
            #self.notify.debug("Select was successful in ttMaildb, returning %s" % str(res))
            return res

        except SqlErrors.OperationalError as e:
            if isRetry:
                self.notify.warning("Error on changePartyStatus retry, giving up:\n%s" % str(e))
                return ()
            elif e.errno == SERVER_GONE_ERROR or e.errno == SERVER_LOST:
                self.db.reconnect()
                return self.changePartyStatus(newPartyStatus, partyId, True)
            else:
                self.notify.warning("Unknown error in changePartyStatus, retrying:\n%s" % str(e))
                self.db.reconnect()
                return self.changePartyStatus( newPartyStatus, partyId, True)
        except Exception as e:
            self.notify.warning("Unknown error in changePartyStatus, giving up:\n%s" % str(e))
            return ()

    def convertListToSQLString(self, partyIds):
        """Convert a list of integers to a string sql recognizes."""
        # string version of partyIds is so close to what we need, but it adds the L
        inClause = "("
        for index in range(len(partyIds)):
            inClause += "%d" % partyIds[index]
            if index < len(partyIds) - 1:
                inClause += ","
        inClause += ")"
        return inClause

    def getMultipleParties(self, partyIds, sortByStartTime = False, isRetry=False):
        """
        Return all the partyInfo matching the partyIds list,
        It may return nothing if there are no matches.
        isRetry indicates whether this attempt is a retry or not.
        """
        if self.db.isDisabled():
            self.notify.debug("ttPartyDb was disabled when calling getMultipleParties.")
            return ()

        if not partyIds:
            self.notify.debug("empty list in partyIds for getMultipleParties")
            return()

        try:
            cursor = self.db.getDictCursor()
            cursor.execute("USE `%s`"%self.dbname)
            inClause = self.convertListToSQLString(partyIds)

            if sortByStartTime:
                cursor.execute(ttSQL.getMultiplePartiesSortedSELECT % inClause)
            else:
                cursor.execute(ttSQL.getMultiplePartiesSELECT % inClause)
            res = cursor.fetchall()
            self.notify.debug("Select was successful in getMultipleParties, returning %s" % str(res))
            return res

        except SqlErrors.OperationalError as e:
            if isRetry:
                self.notify.warning("Error on getMultipleParties retry. Giving up:\n%s" % str(e))
                return ()
            elif e.errno == SERVER_GONE_ERROR or e.errno == SERVER_LOST:
                self.db.reconnect()
                return self.getMultipleParties(partyIds, sortByStartTime, True)
            else:
                self.notify.warning("Unknown error in getMultipleParties, retrying:\n%s" % str(e))
                self.db.reconnect()
                return self.getMultipleParties(partyIds,sortByStartTime, True)
        except Exception as e:
            self.notify.warning("Unknown error in getMultipleParties, giving up:\n%s" % str(e))
            return ()
            
    def getPrioritizedParties(self, partyIds, thresholdTime, limit, future, cancelled, isRetry=False):
        """Return parties from the database using the criteria specified in future and cancelled."""
        if self.db.isDisabled():
            self.notify.debug("ttPartyDb was disabled when calling getPrioritizedParties.")
            return ()

        if not partyIds:
            self.notify.debug("empty list in partyIds for getPrioritizedParties.")
            return()

        sqlString = ""
        if future and cancelled:
            sqlString = ttSQL.getCancelledFuturePartiesSELECT
        elif future and not cancelled:
            sqlString = ttSQL.getNonCancelledFuturePartiesSELECT
        elif not future and cancelled:
            sqlString = ttSQL.getCancelledPastPartiesSELECT
        else:
            sqlString = ttSQL.getNonCancelledPastPartiesSELECT

        try:
            cursor = self.db.getDictCursor()
            cursor.execute("USE `%s`"%self.dbname)
            inClause = self.convertListToSQLString(partyIds)

            parameters = (inClause, thresholdTime,  str(limit))
            execStr = sqlString % parameters
            cursor.execute(execStr)

            res = cursor.fetchall()
            self.notify.debug("Select was successful in getPrioritizedParties, returning %s" % str(res))
            return res

        except SqlErrors.OperationalError as e:
            if isRetry:
                self.notify.warning("Error on getPrioritizedParties retry. Giving up:\n%s" % str(e))
                return ()
            elif e.errno == SERVER_GONE_ERROR or e.errno == SERVER_LOST:
                self.db.reconnect()
                return self.getPrioritizedParties( partyIds, thresholdTime, limit, future, cancelled, isRetry=True)
            else:
                self.notify.warning("Unknown error in getPrioritizedParties getCancelledFutureParties, retrying:\n%s" % str(e))
                self.db.reconnect()
                return self.getPrioritizedParties( partyIds, thresholdTime, limit, future, cancelled, isRetry=True)
        except Exception as e:
            self.notify.warning("Unknown error in getPrioritizedParties getCancelledFutureParties, giving up:\n%s" % str(e))
            return ()

    def getHostPrioritizedParties(self, hostId, thresholdTime, limit, future, cancelled, isRetry=False):
        """Return parties from the database using the criteria specified in future and cancelled."""
        if self.db.isDisabled():
            self.notify.debug("ttPartyDb was disabled when calling getHostPrioritizedParties.")
            return ()

        if not hostId:
            self.notify.debug("empty list in hostId for getHostPrioritizedParties")
            return()

        sqlString = ""
        if future and cancelled:
            sqlString = ttSQL.getHostCancelledFuturePartiesSELECT
        elif future and not cancelled:
            sqlString = ttSQL.getHostNonCancelledFuturePartiesSELECT
        elif not future and cancelled:
            sqlString = ttSQL.getHostCancelledPastPartiesSELECT
        else:
            sqlString = ttSQL.getHostNonCancelledPastPartiesSELECT

        try:
            cursor = self.db.getDictCursor()
            cursor.execute("USE `%s`"%self.dbname)
            parameters = (hostId, thresholdTime,  str(limit))
            execStr = sqlString % parameters
            cursor.execute(execStr)

            res = cursor.fetchall()
            self.notify.debug("Select was successful in getHostPrioritizedParties, returning %s" % str(res))
            return res

        except SqlErrors.OperationalError as e:
            if isRetry:
                self.notify.warning("Error on getHostPrioritizedParties retry. Giving up:\n%s" % str(e))
                return ()
            elif e.errno == SERVER_GONE_ERROR or e.errno == SERVER_LOST:
                self.db.reconnect()
                return self.getHostPrioritizedParties( hostId, thresholdTime, limit, future, cancelled, isRetry=True)
            else:
                self.notify.warning("Unknown error in getHostPrioritizedParties getCancelledFutureParties, retrying:\n%s" % str(e))
                self.db.reconnect()
                return self.getHostPrioritizedParties( hostId, thresholdTime, limit, future, cancelled, isRetry=True)
        except Exception as e:
            self.notify.warning("Unknown error in getHostPrioritizedParties getCancelledFutureParties, giving up:\n%s" % str(e))
            return ()

    def forceFinishForStarted(self, thresholdTime, isRetry=False):
        """
        isRetry indicates whether this attempt is a retry or not.
        Returns a list of (partyId,hostId) for the ones that were forced to finished
        """
        if self.db.isDisabled():
            self.notify.debug("ttPartyDb was disabled when calling forceFinishForStarted.")
            return ()

        try:
            cursor = self.db.getDictCursor()
            cursor.execute("USE `%s`"%self.dbname)
            cursor.execute(ttSQL.partyGetPartiesGoingToFinishedSELECT,(thresholdTime,))
            res = cursor.fetchall()
            cursor.execute(ttSQL.partyForceFinishForStartedUPDATE,(thresholdTime,))
            self.db.commit()

            #self.notify.debug("Select was successful in ttMaildb, returning %s" % str(res))
            return res

        except SqlErrors.OperationalError as e:
            if isRetry:
                self.notify.warning("Error on forceFinishForStarted retry, giving up:\n%s" % str(e))
                return ()
            elif e.errno == SERVER_GONE_ERROR or e.errno == SERVER_LOST:
                self.db.reconnect()
                return self.forceFinishForStarted(thresholdTime, True)
            else:
                self.notify.warning("Unknown error in forceFinishForStarted, retrying:\n%s" % str(e))
                self.db.reconnect()
                return self.forceFinishForStarted( thresholdTime, True)
        except Exception as e:
            self.notify.warning("Unknown error in forceFinishForStarted, giving up:\n%s" % str(e))
            return ()

    def forceNeverStartedForCanStart(self, thresholdTime, isRetry=False):
        """
        isRetry indicates whether this attempt is a retry or not.
        """
        if self.db.isDisabled():
            self.notify.debug("ttPartyDb was disabled when calling forceNeverStartedForCanStart.")
            return ()

        try:
            cursor = self.db.getDictCursor()
            cursor.execute("USE `%s`"%self.dbname)
            cursor.execute(ttSQL.partyGetPartiesGoingToNeverStartedSELECT,(thresholdTime,))
            res = cursor.fetchall()
            cursor.execute(ttSQL.partyForceNeverStartedForCanStartUPDATE ,(thresholdTime,))
            self.db.commit()

            #self.notify.debug("Select was successful in ttMaildb, returning %s" % str(res))
            return res

        except SqlErrors.OperationalError as e:
            if isRetry:
                self.notify.warning("Error on forceNeverStartedForCanStart retry, giving up:\n%s" % str(e))
                return ()
            elif e.errno == SERVER_GONE_ERROR or e.errno == SERVER_LOST:
                self.db.reconnect()
                return self.forceNeverStartedForCanStart(thresholdTime, True)
            else:
                self.notify.warning("Unknown error in forceNeverStartedForCanStart, retrying:\n%s" % str(e))
                self.db.reconnect()
                return self.forceNeverStartedForCanStart( thresholdTime, True)
        except Exception as e:
            self.notify.warning("Unknown error in forceNeverStartedForCanStart, giving up:\n%s" % str(e))
            return ()

    def changeMultiplePartiesStatus(self, partyIds, newPartyStatus, isRetry=False):
        """
        isRetry indicates whether this attempt is a retry or not.
        """
        if self.db.isDisabled():
            self.notify.debug("ttPartyDb was disabled when calling changeMultiplePartiesStatus.")
            return ()

        if not partyIds:
            self.notify.debug("empty list in partyIds for changeMultiplePartiesStatus")
            return()

        try:
            cursor = self.db.getDictCursor()
            cursor.execute("USE `%s`"%self.dbname)
            inClause = self.convertListToSQLString(partyIds)
            sqlString = ttSQL.partyMultipleStatusUPDATE
            parameters = ( newPartyStatus, inClause)
            execStr = sqlString % parameters
            cursor.execute(execStr)
            self.db.commit()
            res = cursor.fetchall()
            #self.notify.debug("Select was successful in ttMaildb, returning %s" % str(res))
            return res

        except SqlErrors.OperationalError as e:
            if isRetry:
                self.notify.warning("Error on changeMultiplePartiesStatus retry, giving up:\n%s" % str(e))
                return ()
            elif e.errno == SERVER_GONE_ERROR or e.errno == SERVER_LOST:
                self.db.reconnect()
                return self.changeMultiplePartiesStatus(partyIds, newPartyStatus,  True)
            else:
                self.notify.warning("Unknown error in changeMultiplePartiesStatus, retrying:\n%s" % str(e))
                self.db.reconnect()
                return self.changeMultiplePartiesStatus( partyIds, newPartyStatus,  True)
        except Exception as e:
            self.notify.warning("Unknown error in changeMultiplePartiesStatus, giving up:\n%s" % str(e))
            return ()