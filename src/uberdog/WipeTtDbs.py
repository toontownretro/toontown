import MySQLdb
import direct
from toontown.toonbase.ToontownModules import *
from direct.showbase.ShowBase import ShowBase
from toontown.toonbase import TTLocalizer

language = TTLocalizer.getLanguage()

showbase = ShowBase(fStartDirect=False, windowType='none')
config = getConfigShowbase()

from otp.uberdog.DBInterface import DBInterface
from toontown.coderedemption import TTCodeRedemptionConsts

username = ConfigVariableString("mysql-user").getValue()
password = ConfigVariableString("mysql-passwd").getValue()

if username == "" or password == "":
    print("Username or password not found, check your config.prc!")
    sys.exit(2)


db = MySQLdb.connect(host="localhost",
                     port=3306,
                     user=username,
                     passwd=password)

print("Connected to MySQL at localhost.")

cursor = db.cursor()

def dropdb(dbname):
    try:
        print("Dropping database %s:" % dbname)
        cursor.execute("DROP DATABASE %s"%dbname)
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


dropdb(ttDbName)
dropdb(DBInterface.processDBName(TTCodeRedemptionConsts.DefaultDbName))
db.commit()
