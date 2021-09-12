import string
from toontown.toonbase.TTLocalizer_german_Property import *

# To make sure the language checker is working
# DO NOT TRANSLATE THIS
ExtraKeySanityCheck = "Ignore me"

InterfaceFont = 'phase_3/models/fonts/ImpressBT.ttf'
ToonFont = 'phase_3/models/fonts/ImpressBT.ttf'
SuitFont = 'phase_3/models/fonts/vtRemingtonPortable.ttf'
SignFont = 'phase_3/models/fonts/MickeyFont'
MinnieFont = 'phase_3/models/fonts/MinnieFont'
BuildingNametagFont = 'phase_3/models/fonts/MickeyFont'
BuildingNametagShadow = None

# common names
Mickey = "Micky"
Minnie = "Minnie"
Donald = "Donald"
Daisy  = "Daisy"
Goofy  = "Goofy"
Pluto  = "Pluto"
Flippy = "Flippy"

# common locations
lTheBrrrgh = 'Das Brrr'
lDaisyGardens = 'Daisys Gärten'
lDonaldsDock = "Donalds Dock"
lDonaldsDreamland = "Donalds Traumland"
lMinniesMelodyland = "Minnies Melodienland"
lToontownCentral = 'Toontown Mitte'
lToonHQ = 'Toontown-\nZentrale'

# common strings
lCancel = 'Abbrechen'
lClose = 'Schließen'
lOK = 'OK'
lNext = 'Weiter'
lNo = 'Nein'
lQuit = 'Beenden'
lYes = 'Ja'

lHQOfficerF = 'Mitarbeiter der Zentrale'
lHQOfficerM = 'Mitarbeiter der Zentrale'

MickeyMouse = "Micky Maus"

AIStartDefaultDistrict = "Maushöhe"

Cog  = "Bot"
Cogs = "Bots"
ACog = "ein Bot"
TheCogs = "den Bots"
Skeleton = "Skeletobot"
SkeletonP = "Skeletobots"
ASkeleton = "ein Skeletobot"
Foreman = "Vorarbeiter"
ForemanP = "Vorarbeiter"
AForeman = "ein Vorarbeiter"
CogVP = "Bot-VP "
CogVPs = "Bot-VPs"
ACogVP = "ein Bot-VP"

# Quests.py
TheFish = "der Fisch"
AFish = "ein Fisch"
Level = "Level "
QuestsCompleteString = "Beendet "
QuestsNotChosenString = "Nicht ausgewählt"
Period = "."

QuestInLocationString = " %(inPhrase)s %(location)s"

# _avName_ gets replaced with the avatar (player's) name
# _toNpcName_ gets replaced with the npc's name we are being sent to
# _where_ gets replaced with a description of where to find the npc, with a leading \a
QuestsDefaultGreeting = ("Hallo, _avName_!",
                         "Hi, _avName_!",
                         "Na du, _avName_!",
                         "Wie steht's, _avName_!",
                         "Willkommen, _avName_!",
                         "Tag, _avName_!",
                         "Wie geht's, _avName_?",
                         "Guten Tag _avName_!",
                         )
QuestsDefaultIncomplete = ("Wie geht's mit der Aufgabe voran, _avName_?",
                           "Sieht aus, als müsstest du an dieser Aufgabe noch etwas arbeiten!",
                           "Weiter so, _avName_!",
                           "Bleib weiter an dieser Aufgabe dran. Ich weiß, du schaffst das!",
                           "Versuch weiter, diese Aufgabe zu lösen, wir zählen auf dich!",
                           "Arbeite weiter an dieser Toon-Aufgabe!",
                           )
QuestsDefaultIncompleteProgress = ("Du bist zum richtigen Ort gekommen, aber du musst erst noch deine Toon-Aufgabe lösen!",
                                   "Komm wieder her, wenn du mit deiner Toon-Aufgabe fertig bist.",
                                   "Komm wieder, wenn du mit deiner Toon-Aufgabe fertig bist.",
                                   )
QuestsDefaultIncompleteWrongNPC = ("Gut gelöst, diese Toon-Aufgabe. Du solltest mal _toNpcName_ besuchen._where_",
                                   "Sieht aus, als wärst du gleich mit deiner Toon-Aufgabe fertig. Besuch mal _toNpcName_._where_.",
                                   "Besuche _toNpcName_ um deine Toon-Aufgabe zu lösen._where_",
                                   )
QuestsDefaultComplete = ("Gute Arbeit! Hier deine Belohnung ...",
                         "Gut gemacht, _avName_! Nimm das hier als Belohnung ...",
                         "Spitzenleistung, _avName_! Hier deine Belohnung ...",
                         )
QuestsDefaultLeaving = ("Tschüss!",
                        "Auf Wiedersehen!",
                        "Mach's gut, _avName_.",
                        "Bis bald, _avName_!",
                        "Viel Glück!",
                        "Viel Spaß in Toontown!",
                        "Bis demnächst!",
                        )
QuestsDefaultReject = ("Hallo!",
                       "Kann ich helfen?",
                       "Wie geht's?",
                       "Na du!",
                       "Hab grad zu tun, _avName_.",
                       "Ja?",
                       "Tag, _avName_!",
                       "Willkommen, _avName_!",
                       "Hi, _avName_! Wie steht's?",
                       # Game Hints
                       "Weißt du schon, dass du mit F8 dein Sticker-Buch öffnen kannst? ",
                       "Du kannst dich mit deinem Stadtplan wieder zum Spielplatz teleportieren!",
                       "Du kannst mit anderen Spielern Freundschaft schließen, indem du sie anklickst.",
                       "Du kannst mehr über einen " + Cog + " erfahren, indem du ihn anklickst.",
                       "Sammle Schätze auf den Spielplätzen, um dein Lach-O-Meter zu füllen.",
                       Cog +"-Gebäude sind gefährlich! Geh nicht alleine rein!",
                       "Wenn du einen Kampf verlierst, nehmen dir die " + Cogs + " alle Gags ab.",
                       "Fahr mit dem Toon-Express zum Spielplatz, verdiene beim Spielen Jellybeans, um Gags zu kaufen.!",
                       "Du kannst noch mehr Lach-Punkte gewinnen, indem du Toon-Aufgaben löst.",
                       "Für jede gelöste Toon-Aufgabe erhältst du eine Belohnung.",
                       "Einige Belohnungen helfen dir, mehr Gags mit dir zu führen.",
                       "Wenn du einen Kampf gewinnst, bekommst du für jeden vertriebenen " + Cog +  " eine Gutschrift für erledigte Toon-Aufgaben.",
                       "Wenn du ein "+ Cog +  "-Gebäude zurückeroberst, geh wieder hinein und schau nach, was der Besitzer dir als spezielles Dankeschön hinterlassen hat!",
                       "Mit der Taste 'Bild Hoch' kannst du nach oben schauen!",
                       "Mit der Tab-Taste kannst du verschiedene Ansichten deiner Umgebung sehen!",
                       "Um geheimen Freunden zu zeigen, was du gerade denkst, gib vor deinem Gedanken ein '.' ein.",
                       " Wenn ein" + Cog + " angeschlagen ist, fällt es ihm schwerer, herunterfallenden Gegenständen auszuweichen.. ",
                       "Jede Art von "+ Cog +  "-Gebäude hat ein eigenes Aussehen.",
                       "Wenn du "+ Cogs +  " auf den höheren Stockwerken eines Gebäudes besiegst, bringt dir das höhere Geschicklichkeitspunkte ein.",
                       )
QuestsDefaultTierNotDone = ("Hallo, _avName_! Du musst erst deine derzeitigen Toon-Aufgaben lösen, bevor du eine neue bekommst.",
                            "Hallo! Du musst erst die Toon-Aufgaben lösen, an denen du gerade arbeitest, um eine neue zu bekommen.",
                            "Hi, _avName_! Bevor ich dir eine neue Toon-Aufgabe geben kann, musst du erst die lösen, die du schon hast.",
                            )
# The default string gets replaced with the quest getstring
QuestsDefaultQuest = None
QuestsDefaultVisitQuestDialog = ("Ich habe gehört, _toNpcName_ sucht dich._where_",
                                 "Schau mal bei _toNpcName_ rein, wenn du kannst._where_",
                                 "Besuche mal _toNpcName_ , wenn du das nächste Mal in der Nähe bist._where_",
                                 "Schau mal bei Gelegenheit bei _toNpcName_._where_ vorbei",
                                 "_toNpcName_ wird dir deine nächste Toon-Aufgabe geben._where_",
                                 )
# Quest dialog
QuestsLocationArticle = ""
def getLocalNum(num):
	if (num <=9):
		return str(num) + ""
	else:
		return str(num)
QuestsItemNameAndNum = "%(num)s %(name)s"

QuestsCogQuestProgress = "%(progress)s von %(numCogs)s vertrieben"
QuestsCogQuestHeadline = "GESUCHT"
QuestsCogQuestSCStringS = "Ich muss %(cogName)s%(cogLoc)s erledigen."
QuestsCogQuestSCStringP = "Ich muss ein paar %(cogName)s%(cogLoc)s vertreiben."
QuestsCogQuestDefeat = "%s vertreiben"
QuestsCogQuestDefeatDesc = "%(numCogs)s %(cogName)s"

QuestsCogNewbieQuestObjective = "Hilf einem neuen Toon %s zu vertreiben"
QuestsCogNewbieQuestCaption = "Hilf einem neuen Toon %d Lach oder weniger"
QuestsCogNewbieQuestAux = "Vertreiben"
QuestsNewbieQuestHeadline = "LEHRLING"

QuestsCogTrackQuestProgress = "%(progress)s von %(numCogs)s vertrieben"
QuestsCogTrackQuestHeadline = "GESUCHT"
QuestsCogTrackQuestSCStringS = "Ich muss %(cogText)s%(cogLoc)s vertreiben."
QuestsCogTrackQuestSCStringP = "Ich muss ein paar %(cogText)s%(cogLoc)s vertreiben."
QuestsCogTrackQuestDefeat = "%s vertreiben"
QuestsCogTrackDefeatDesc = "%(numCogs)s %(trackName)s"

QuestsCogLevelQuestProgress = "%(progress)s von %(numCogs)s vertrieben"
QuestsCogLevelQuestHeadline = "GESUCHT"
QuestsCogLevelQuestDefeat = "%s vertreiben"
QuestsCogLevelQuestDesc = "ein Level %(level)s+ %(name)s"
QuestsCogLevelQuestDescC = "%(count)s Level %(level)s+ %(name)s"
QuestsCogLevelQuestDescI = "ein Level %(level)s+ %(name)s "
QuestsCogLevelQuestSCString = "Ich muss %(objective)s%(location)s vertreiben."

QuestsBuildingQuestFloorNumbers = ('', '> zwei', '> drei', '> vier', '> fünf')
QuestsBuildingQuestBuilding = "Gebäude"
QuestsBuildingQuestBuildings = "Gebäude"
QuestsBuildingQuestHeadline = "ERLEDIGEN"
QuestsBuildingQuestProgressString = "%(progress)s von %(num)s erledigt"
QuestsBuildingQuestString = "%s erledigen"
QuestsBuildingQuestSCString = "Ich muss %(objective)s%(location)s erledigen."

QuestsBuildingQuestDesc = "ein %(type)s -Gebäude"
QuestsBuildingQuestDescF = "ein %(floors)s-stöckiges %(type)s-Gebäude"
QuestsBuildingQuestDescC = "%(count)s %(type)s Gebäude"
QuestsBuildingQuestDescCF = "%(count)s %(floors)s-stöckige %(type)s Gebäude"
QuestsBuildingQuestDescI = "einige %(type)s -Gebäude"
QuestsBuildingQuestDescIF = "einige %(floors)s-stöckige %(type)s-Gebäude"

QuestFactoryQuestFactory = "Fabrik"
QuestsFactoryQuestFactories = "Fabriken"
QuestsFactoryQuestHeadline = "ERLEDIGEN"
QuestsFactoryQuestProgressString = "%(progress)s von %(num)s erledigt"
QuestsFactoryQuestString = "%s erledigen"
QuestsFactoryQuestSCString = "Ich muss %(objective)s%(location)s erledigen."

QuestsFactoryQuestDesc = "eine %(type)s -Fabrik"
QuestsFactoryQuestDescC = "%(count)s %(type)s -Fabriken"
QuestsFactoryQuestDescI = "einige %(type)s-Fabriken"

QuestsRescueQuestProgress = "%(progress)s von %(numToons)s gerettet"
QuestsRescueQuestHeadline = "RETTEN"
QuestsRescueQuestSCStringS = "Ich muss einen Toon%(toonLoc)s retten."
QuestsRescueQuestSCStringP = "Ich muss ein paar Toons%(toonLoc)s retten."
QuestsRescueQuestRescue = "%s retten"
QuestsRescueQuestRescueDesc = "%(numToons)s Toons"
QuestsRescueQuestToonS = "ein Toon"
QuestsRescueQuestToonP = "Toons"
QuestsRescueQuestAux = "Retten:"

QuestsRescueNewbieQuestObjective = "Hilf einem neuen Toon beim Retten von %s"

QuestCogPartQuestCogPart = "Bot-Anzugteil"
QuestsCogPartQuestFactories = "Fabriken"
QuestsCogPartQuestHeadline = "ZURÜCKHOLEN"
QuestsCogPartQuestProgressString = "%(progress)s von %(num)s zurückgeholt"
QuestsCogPartQuestString = "%s zurückholen"
QuestsCogPartQuestSCString = "Ich muss %(objective)s%(location)s zurückholen."
QuestsCogPartQuestAux = "Zurückholen:"

QuestsCogPartQuestDesc = "ein Bot-Anzugteil"
QuestsCogPartQuestDescC = "%(count)s Bot-Anzugteile"
QuestsCogPartQuestDescI = "einige Bot-Anzugteile"

QuestsCogPartNewbieQuestObjective = 'Hilf einem neuen Toon beim Zurückholen von %s'

QuestsDeliverGagQuestProgress = "%(progress)s von %(numGags)s abgeliefert"
QuestsDeliverGagQuestHeadline = "ABLIEFERN"
QuestsDeliverGagQuestToSCStringS = "Ich muss %(gagName)s abliefern."
QuestsDeliverGagQuestToSCStringP = "Ich muss ein paar %(gagName)s abliefern."
QuestsDeliverGagQuestSCString = "Ich muss etwas abliefern."
QuestsDeliverGagQuestString = "%s abliefern"
QuestsDeliverGagQuestStringLong = "%s an _toNpcName_ abliefern."
QuestsDeliverGagQuestInstructions = "Du kannst diesen Gag im Gag-Shop kaufen, wenn du dir den Zugang verdient hast."

QuestsDeliverItemQuestProgress = ""
QuestsDeliverItemQuestHeadline = "ABLIEFERN"
QuestsDeliverItemQuestSCString = "Ich muss %(article)s%(itemName)s abliefern."
QuestsDeliverItemQuestString = "%s abliefern"
QuestsDeliverItemQuestStringLong = "%s an _toNpcName_ abliefern."

QuestsVisitQuestProgress = ""
QuestsVisitQuestHeadline = "BESUCHEN"
QuestsVisitQuestStringShort = "Besuchen"
QuestsVisitQuestStringLong = "_toNpcName_ besuchen"
QuestsVisitQuestSeeSCString = "Ich muss %s besuchen."

QuestsRecoverItemQuestProgress = "%(progress)s von %(numItems)s zurückgeholt"
QuestsRecoverItemQuestHeadline = "ZURÜCKHOLEN"
QuestsRecoverItemQuestSeeHQSCString = "Ich muss einen Mitarbeiter in der Toontown-Zentrale aufsuchen"
QuestsRecoverItemQuestReturnToHQSCString = "Ich muss %s zu einem Mitarbeiter in Toontown-Zentrale zurückgeben."
QuestsRecoverItemQuestReturnToSCString = "Ich muss %(npcName)s %(item)s zurückgeben."
QuestsRecoverItemQuestGoToHQSCString = "Ich muss zur Toontown-Zentrale gehen."
QuestsRecoverItemQuestGoToPlaygroundSCString = "Ich muss zum %s -Spielplatz."
QuestsRecoverItemQuestGoToStreetSCString = "Ich muss %(to)s %(street)s in %(hood)s gehen."
QuestsRecoverItemQuestVisitBuildingSCString = "Ich muss %s%s besuchen."
QuestsRecoverItemQuestWhereIsBuildingSCString = "Wo ist %s%s?"
QuestsRecoverItemQuestRecoverFromSCString = "Ich muss %(item)s von %(holder)s%(loc)s abholen."
QuestsRecoverItemQuestString = "%(item)s von %(holder)s abholen."
QuestsRecoverItemQuestHolderString = "%(level)s %(holder)d+ %(cogs)s"

QuestsTrackChoiceQuestHeadline = "WÄHLEN"
QuestsTrackChoiceQuestSCString = "Ich muss zwischen %(trackA)s und %(trackB)s wählen."
QuestsTrackChoiceQuestMaybeSCString = "Vielleicht sollte ich %s wählen."
QuestsTrackChoiceQuestString = "Wähle zwischen %(trackA)s und %(trackB)s"

QuestsFriendQuestHeadline = "FREUND"
QuestsFriendQuestSCString = "Ich muss einen Freund gewinnen."
QuestsFriendQuestString = "Einen Freund gewinnen"

QuestsFriendNewbieQuestString = "Gewinne %d Freunde %d Lach oder weniger "
QuestsFriendNewbieQuestProgress = "%(progress)s von %(numFriends)s gewonnen"
QuestsFriendNewbieQuestObjective = "Mit %d neuen Toons anfreunden"

QuestsTrolleyQuestHeadline = "TOON-EXPRESS"
QuestsTrolleyQuestSCString = "Ich muss mit dem Toon-Express fahren."
QuestsTrolleyQuestString = "Mit dem Toon-Express fahren."
QuestsTrolleyQuestStringShort = "Toon-Express fahren"

QuestsMinigameNewbieQuestString = "%d Minigames"
QuestsMinigameNewbieQuestProgress = "%(progress)s von %(numMinigames)s gespielt"
QuestsMinigameNewbieQuestObjective = "%d Minigames mit neuen Toons gespielt"
QuestsMinigameNewbieQuestSCString = "Ich muss mit neuen Toons Minigames spielen."
QuestsMinigameNewbieQuestCaption = "Hilf einem neuen Toon mit %d Lach oder weniger"
QuestsMinigameNewbieQuestAux = "Spielen:"

QuestsMaxHpReward = "Deine Lachstärke hat sich um %s erhöht."
QuestsMaxHpRewardPoster = "Belohnung: %s Punkt mehr Lachstärke"

QuestsMoneyRewardSingular = "Du bekommst 1 Jelly Bean."
QuestsMoneyRewardPlural = "Du bekommst %s Jelly Beans."
QuestsMoneyRewardPosterSingular = "Belohnung: 1 Jelly Bean"
QuestsMoneyRewardPosterPlural = "Belohnung: %s Jelly Beans"

QuestsMaxMoneyRewardSingular = "Du kannst jetzt 1 Jelly Bean mit dir führen."
QuestsMaxMoneyRewardPlural = "Du kannst jetzt %s Jelly Beans mit dir führen."
QuestsMaxMoneyRewardPosterSingular = "Belohnung: 1 Jelly Bean mit dir führen."
QuestsMaxMoneyRewardPosterPlural = "Belohnung: %s Jelly Beans mit dir führen."

QuestsMaxGagCarryReward = "Du bekommst %(name)s. Du kannst jetzt %(num)s Gags mit dir führen."
QuestsMaxGagCarryRewardPoster = "Belohnung: %(name)s (%(num)s)"

QuestsMaxQuestCarryReward = "Du kannst jetzt %s Toon-Aufgaben bekommen."
QuestsMaxQuestCarryRewardPoster = "Belohnung: %s Toon-Aufgaben mit dir führen."

QuestsTeleportReward = "Du hast jetzt Teleport-Zugang zu %s."
QuestsTeleportRewardPoster = "Belohnung: Teleport-Zugang zu %s"

QuestsTrackTrainingReward = "Du kannst jetzt für \"%s\" Gags trainieren."
QuestsTrackTrainingRewardPoster = "Belohnung: Ein Gag-Training"

QuestsTrackProgressReward = "Du hast jetzt Bild %(frameNum)s der %(trackName)s Ablauf-Animation."
QuestsTrackProgressRewardPoster = "Belohnung: \"%(trackName)s\" Ablauf-Animationsbild %(frameNum)s"

QuestsTrackCompleteReward = "Du darfst jetzt \"%s\" Gags mit dir führen und benutzen."
QuestsTrackCompleteRewardPoster = "Belohnung: %s -Ablauf-Abschlusstraining"

QuestsClothingTicketReward = "Du darfst deine Kleidung wechseln"
QuestsClothingTicketRewardPoster = "Belohnung: Eine Kleidermarke"

QuestsCheesyEffectRewardPoster = "Belohnung: %s"

# Quest location dialog text
QuestsStreetLocationThisPlayground = "auf diesem Spielplatz"
QuestsStreetLocationThisStreet = "in dieser Straße"
QuestsStreetLocationNamedPlayground = "auf dem Spielplatz %s "
QuestsStreetLocationNamedStreet = "auf %(toStreetName)s in %(toHoodName)s"
QuestsLocationString = "%(string)s%(location)s"
QuestsLocationBuilding = "%s's Gebäude heißt"
QuestsLocationBuildingVerb = "und das ist"
QuestsLocationParagraph = "\a%(building)s \"%(buildingName)s\"...\a...%(buildingVerb)s %(street)s."
QuestsGenericFinishSCString = "Ich muss eine Toon-Aufgabe lösen."

# MaxGagCarryReward names
QuestsMediumPouch = "einen mittelgroßer Beutel"
QuestsLargePouch = "einen großer Beutel"
QuestsSmallBag = "eine kleine Tasche"
QuestsMediumBag = "eine mittelgroße Tasche"
QuestsLargeBag = "eine große Tasche"
QuestsSmallBackpack = "ein kleiner Rucksack"
QuestsMediumBackpack = "ein mittelgroßer Rucksack"
QuestsLargeBackpack = "ein großer Rucksack"
QuestsItemDict = {
    1 : ["Brille", "Brillen", "eine "],
    2 : ["Schlüssel", "Schlüssel", "einen "],
    3 : ["Tafel", "Tafeln", "eine "],
    4 : ["Buch", "Bücher", "ein "],
    5 : ["Lutscher", "Lutscher", "einen "],
    6 : ["Kreide", "Kreiden", "eine "],
    7 : ["Rezept", "Rezepte", "ein "],
    8 : ["Notiz", "Notizen", "eine "],
    9 : ["Rechenmaschine", "Rechenmaschinen", "eine "],
    10 : ["Clownautoreifen", "Clownautoreifen", "einen"],
    11 : ["Luftpumpe ", "Luftpumpen", "eine "],
    12 : ["Tintenfischtinte", "Tintenfischtinten", "irgendeine "],
    13 : ["Paket", "Pakete", "ein "],
    14 : ["Goldfischquittung", "Goldfischquittungen", "eine "],
    15 : ["Goldfisch", "Goldfische", "einen "],
    16 : ["Öl", "Öle", "etwas "],
    17 : ["Fett", "Fette", "etwas "],
    18 : ["Wasser", "Wasser", "etwas "],
    19 : ["Getriebebericht", "Getriebeberichte", "einen "],
    20 : ["Schwamm", "Schwämme", "einen "],

    # This is meant to be delivered to NPCTailors to complete
    # ClothingReward quests
    1000 : ["Kleidermarke", "Kleidermarken", "eine "],

    # Donald's Dock quest items
    2001 : ["Schlauch", "Schläuche", "einen "],
    2002 : ["Monokelrezept", "Monokelrezepte", "ein "],
    2003 : ["Brillengestell", "Brillengestelle", "irgendein "],
    2004 : ["Monokel", "Monokel", "einen "],
    2005 : ["große weiße Perücke", "große weiße Perücken", "eine "],
    2006 : ["Ballastbündel", "Ballastbündel", "ein "],
    2007 : ["Bot-Zahnrad", "Bot-Zahnräder", "ein "],
    2008 : ["Seekarte", "Seekarten", "eine "],
    2009 : ["verschmutzten Webeleinstek", "verschmutzte Webeleinsteke", "einen "],
    2010 : ["sauberen Webeleinstek", "saubere Webeleinsteke", "einen "],
    2011 : ["Uhrfeder", "Uhrfedern", "eine "],
    2012 : ["Gegengewicht", "Gegengewichte", "ein "],

    # Minnie's Melodienland quest items
    4001 : ["Tinas Inventarliste", "Tinas Inventarlisten", ""],
    4002 : ["Yukis Inventarliste", "Yukis Inventarlisten", ""],
    4003 : ["Inventarlistenformular", "Inventarlistenformulare", "ein "],
    4004 : ["Fifis Inventarliste", "Fifis Inventarlisten", ""],
    4005 : ["Holzmichels Ticket", "Holzmichels Tickets", ""],
    4006 : ["Tabithas Ticket", "Tabithas Tickets", ""],
    4007 : ["Grizzlys Ticket", "Grizzlys Tickets", ""],
    4008 : ["Matte Kastagnette", "Matte Kastagnetten", "eine "],
    4009 : ["Blaue Tintenfischtinte", "Blaue Tintenfischtinte", "irgendeine "],
    4010 : ["glänzende Kastagnette", "glänzende Kastagnetten", "eine "],
    4011 : ["Leos Reim", "Leos Reime", ""],

    # Daisy's Garden quest items
    5001 : ["Seidenkrawatte", "Seidenkrawatten", "eine "],
    5002 : ["Nadelstreifenanzug", "Nadelstreifenanzüge", "einen "],
    5003 : ["Schere", "Scheren", "eine "],
    5004 : ["Postkarte", "Postkarten", "eine "],
    5005 : ["Stift", "Stifte", "einen "],
    5006 : ["Tintenfass", "Tintenfässer", "ein "],
    5007 : ["Schreibblock", "Schreibblöcke", "einen "],
    5008 : ["verschließbare Kassette", "verschließbare Kassetten", "eine "],
    5009 : ["Tüte mit Vogelfutter", "Tüten mit Vogelfutter", "eine "],
    5010 : ["Kettenradzahn", "Kettenradzähne", "einen "],
    5011 : ["Salat", "Salate", "einen "],
    5012 : ["Schlüssel zu Daisys Gärten", "Schlüssel zu Daisys Gärten", "einen "],
    5013 : ["Blaupause des Schachermat-Hauptquartiers", "Blaupausen des Schachermat-Hauptquartiers", "irgendeine "],
    5014 : ["Memo des Schachermat-Hauptquartier", "Memo des Schachermat-Hauptquartiers", "ein "],
    5015 : ["Memo des Schachermat-Hauptquartier", "Memo des Schachermat-Hauptquartiers", "ein "],
    5016 : ["Memo des Schachermat-Hauptquartier", "Memo des Schachermat-Hauptquartiers", "ein "],
    5017 : ["Memo des Schachermat-Hauptquartier", "Memo des Schachermat-Hauptquartiers", "ein "],

    # The Brrrgh quests
    3001 : ["Fußball", "Fußbälle", "einen "],
    3002 : ["Rodelschlitten", "Rodelschlitten", "einen "],
    3003 : ["Eiswürfel", "Eiswürfel", "einen "],
    3004 : ["Liebesbrief", "Liebesbriefe", "einen "],
    3005 : ["Wiener Würstchen", "Wiener Würstchen", "ein "],
    3006 : ["Verlobungsring", "Verlobungsringe", "einen "],
    3007 : ["Stein des Weisen", "Steine des Weisen", "einen "],
    3008 : ["Beruhigungstrank", "Beruhigungstrank", "einen "],
    3009 : ["kaputten Zahn", "kaputte Zähne", "einen "],
    3010 : ["Goldzahn", "Goldzähne", "einen "],
    3011 : ["Kiefernzapfenbrot", "Kiefernzapfenbrote", "einen "],
    3012 : ["Krümelkäse", "Krümelkäse", "irgendeinen "],
    3013 : ["einfachen Löffel", "einfache Löffel", "einen "],
    3014 : ["sprechende Kröte", "sprechende Kröten", "eine "],
    3015 : ["Eistüte", "Eistüten", "eine "],
    3016 : ["Perückenpuder", "Perückenpuder", "irgendein "],
    3017 : ["Quietschentchen", "Quietschentchen", "ein "],
    3018 : ["Fellwürfel", "Fellwürfel", "irgendeinen "],
    3019 : ["Mikrofon", "Mikrofone", "ein "],
    3020 : ["elektrisches Keyboard", "elektrische Keyboards", "ein "],
    3021 : ["Plateauschuhe", "Plateauschuhe", "etwas "],
    3022 : ["Kaviar", "Kaviar", "etwas "],
    3023 : ["Make-up-Puder", "Make-up-Puder", "irgendein "],
    }
QuestsHQOfficerFillin = "Mitarbeiter in der Zentrale"
QuestsHQWhereFillin = ""
QuestsHQBuildingNameFillin = "Toontown-Zentrale"
QuestsHQLocationNameFillin = "In einer beliebigen Gegend"

QuestsTailorFillin = "Schneider"
QuestsTailorWhereFillin = ""
QuestsTailorBuildingNameFillin = "Bekleidungsgeschäft"
QuestsTailorLocationNameFillin = "In einer beliebigen Gegend"
QuestsTailorQuestSCString = "Ich muss zu einem Schneider."

QuestMovieQuestChoiceCancel = "Komm später wieder, wenn du eine neue Toon-Aufgabe brauchst! Tschüss!"
QuestMovieTrackChoiceCancel = "Komm wieder, wenn du dich entscheiden kannst! Tschüss!"
QuestMovieQuestChoice = "Wähle eine Toon-Aufgabe."
QuestMovieTrackChoice = "Bereit zum Wählen? Wähle einen Ablauf oder komm später wieder."

# Constants used in Quests.py, globally defined here
GREETING = 0
QUEST = 1
INCOMPLETE = 2
INCOMPLETE_PROGRESS = 3
INCOMPLETE_WRONG_NPC = 4
COMPLETE = 5
LEAVING = 6

TheBrrrghTrackQuestDict = {
    GREETING : "",
    QUEST : "Jetzt bist du fertig.\aZiehe nun in die Welt und wandere umher, bis du weißt, welchen Ablauf du wählen möchtest.\aWähle klug, denn dies ist dein letzter Track.\aWenn du dir sicher bist, kehre zu mir zurück.",
    INCOMPLETE_PROGRESS : "Wähle mit Verstand.",
    INCOMPLETE_WRONG_NPC : "Wähle mit Verstand.",
    COMPLETE : "Sehr kluge Entscheidung!",
    LEAVING : "Viel Glück! Komm wieder zu mir, wenn du deine neue Fähigkeit beherrschst.",
    }

QuestDialog_3225 = {
    QUEST : "Oh, danke, dass du gekommen bist, _avName_!\aDie Bots in dieser Gegend haben mein Lieferanten verschreckt.\aIch habe niemanden, der diesen Salat an _toNpcName_ausliefert!\aKannst du das für mich tun? Hab vielen Dank!_where_"
    }

QuestDialog_2910 = {
    QUEST : "Schon wieder da?\aDas mit der Feder hast du gut gemacht.\aDer letzte Gegenstand ist ein Gegengewicht.\aSchau mal bei _toNpcName_ vorbei und bring alles mit, was du kriegen kannst._where_"
    }

QuestDialogDict = {
    160 : {GREETING : "",
           QUEST : "OK, jetzt bist du wohl für etwas Interessanteres bereit.\aWenn du 3 Chefomaten vertreiben kannst, bekommst du von mir ein kleines Extra.",
           INCOMPLETE_PROGRESS : "Die "+ Cogs +  " sind draußen auf der Straße, durch die Tunnel.",
           INCOMPLETE_WRONG_NPC : "Tolle Leistung, dein Sieg über die Chefomaten. Geh jetzt zur Toontown-Zentrale, um deine Belohnung abzuholen.",
           COMPLETE : QuestsDefaultComplete,
           LEAVING : QuestsDefaultLeaving,
           },
    161 : {GREETING : "",
           QUEST : "OK, jetzt bist du wohl bereit für etwas Interessanteres.\aKomm wieder her, wenn du 3 Rechtomaten vertrieben hast - dann hab ich ein kleines Geschenk für dich.",
           INCOMPLETE_PROGRESS : "Die "+ Cogs +  " sind draußen auf der Straße, durch die Tunnel.",
           INCOMPLETE_WRONG_NPC : "Tolle Leistung, dein Sieg über die Rechtomaten. Geh jetzt zur Toontown-Zentrale, um deine Belohnung abzuholen!",
           COMPLETE : QuestsDefaultComplete,
           LEAVING : QuestsDefaultLeaving,
           },
 162 : {GREETING : "",
           QUEST : "OK, jetzt bist du wohl bereit für etwas Interessanteres.\aBesiege 3 Monetomaten und komm wieder her, um deine Prämie einzufordern.",
           INCOMPLETE_PROGRESS : "Die "+ Cogs +  " sind draußen auf der Straße, durch die Tunnel.",
           INCOMPLETE_WRONG_NPC : "Tolle Leistung, dein Sieg über die Monetomaten. Geh jetzt zu eine Toontown-Zentrale, um deine Belohnung abzuholen!",
           COMPLETE : QuestsDefaultComplete,
           LEAVING : QuestsDefaultLeaving,
           },
 163 : {GREETING : "",
           QUEST : "OK, jetzt bist du wohl bereit für etwas Interessanteres.\aKomm wieder her, wenn du 3 Schachermaten vertrieben hast, und du bekommst eine Belohnung und eine neue Aufgabe.",
           INCOMPLETE_PROGRESS : "Die "+ Cogs +  " sind draußen auf der Straße, durch die Tunnel.",
           INCOMPLETE_WRONG_NPC : "Tolle Leistung, dein Sieg über die Schachermaten. Geh jetzt zur Toontown-Zentrale, um deine Belohnung abzuholen!",
           COMPLETE : QuestsDefaultComplete,
           LEAVING : QuestsDefaultLeaving,
           },

    164 : {QUEST : "Du siehst aus, als könntest du ein paar neue Gags gebrauchen.\aGeh mal zu Flippy, der kann dir vielleicht aushelfen._where_" },
    165 : {QUEST : "Hallo!\aSieht aus, als müsstest du deine Gags mal in der Praxis trainieren.\aJedes Mal, wenn du einem Bot einen deiner Gags um die Ohren haust, wächst deine Erfahrung.\aWenn du genug Erfahrung hast, kannst du dann einen noch besseren Gag einsetzen.\aGeh deine Gags üben und vertreibe dabei 4 Bots."},
    166 : {QUEST : "Toll, wie du diese Bots vertrieben hast!\aWeißt du, es gibt vier Arten von Bots.\aRechtomaten, Monetomaten, Schachermaten und Chefomaten.\aDu kannst sie an ihrer Färbung und ihren Namensschildern erkennen.\aGeh mal los und besiege zur Übung 4 Chefomaten."},
    167 : {QUEST : "Toll, wie du diese Bots vertrieben hast!\aWeißt du, es gibt vier Arten von Bots.\a Rechtomaten, Monetomaten, Schachermaten und Chefomaten.\aDu kannst sie an ihrer Färbung und ihren Namensschildern erkennen.\aGeh mal los und besiege zur Übung 4 Rechtomaten."},
    168 : {QUEST : "Toll, wie du diese Bots vertrieben hast!\aWeißt du, es gibt vier Arten von Bots.\a Rechtomaten, Monetomaten, Schachermaten und Chefomaten.\aDu kannst sie an ihrer Färbung und ihren Namensschildern erkennen.\aGeh mal los und besiege zur Übung 4 Schachermaten."},
    169 : {QUEST : "Toll, wie du diese Bots vertrieben hast!\aWeißt du, es gibt vier Arten von Bots.\a Rechtomaten, Monetomaten, Schachermaten und Chefomaten.\aDu kannst sie an ihrer Färbung und ihren Namensschildern erkennen.\aGeh mal los und besiege zur Übung 4 Monetomaten."},
    170 : {QUEST : "Toll, jetzt kennst du den Unterschied zwischen den 4 Bot-Arten.\aIch glaube, du kannst jetzt für deinen dritten Gag-Ablauf trainieren.\aSprich mal mit _toNpcName_, bevor du deinen nächsten Gag-Ablauf wählst - er kann dich fachkundig beraten._where_" },
    171 : {QUEST : "Toll, jetzt kennst du den Unterschied zwischen den 4 Bot-Arten.\aIch glaube, du kannst jetzt für deinen dritten Gag-Ablauf trainieren.\aSprich mal mit _toNpcName_, bevor du deinen nächsten Gag-Ablauf wählst - er kann dich fachkundig beraten._where_" },
    172 : {QUEST : "Toll, jetzt kennst du den Unterschied zwischen den 4 Bot-Arten.\aIch glaube, du kannst jetzt für deinen dritten Gag-Ablauf trainieren.\aSprich mal mit _toNpcName_, bevor du deinen nächsten Gag-Ablauf wählst - sie kann dich fachkundig beraten._where_" },

    175 : {GREETING : "",
           QUEST : "Wusstest du schon, dass du dein eigenes Toon-Haus besitzt?\aKlarabella Kuh betreibt einen Katalog, aus dem du per Telefon Möbel zum Einrichten deines Hauses bestellen kannst.\aDu kannst aber auch Schnell-Chat-Sprüche, Kleidung und andere lustige Dinge kaufen.\aIch sage Klarabella, dass sie dir sofort deinen ersten Katalog schicken soll.\aJede Woche erhältst du einen Katalog mit neuen Gegenständen!\aGeh in dein Haus und rufe von dort aus Klarabella an.",
           INCOMPLETE_PROGRESS : "Geh nach Hause und rufe von dort Klarabella an.",
           COMPLETE : "Es macht dir bestimmt Spaß, bei Klarabella etwas zu bestellen!\aIch habe gerade mein Haus neu eingerichtet. Es sieht toontastisch aus!\aLöse weiterhin Toon-Aufgaben, um noch mehr Belohnungen zu bekommen!",
           LEAVING : QuestsDefaultLeaving,
           },

    400 : {GREETING : "",
           QUEST : "Werfen und Spritzen ist toll, aber du wirst noch mehr Gags brauchen, wenn du gegen höhere Bots kämpfen willst.\aWenn du dich mit anderen Toons gegen die Bots zusammenschließt, dann könnt ihr die Angriffe kombinieren und dadurch noch mehr Schaden anrichten.\aProbiert verschiedene Gag-Kombinationen aus, um herauszufinden, was am besten funktioniert.\aWähle für deinen nächsten Ablauf zwischen Volldröhnen und Aufheitern.\aVolldröhnen ist etwas Besonders, weil alle Bots beschädigt werden, wenn es trifft.\aMit Aufheitern kannst du andere Toons im Kampf heilen.\aWenn du für deine Entscheidung bereit bist, komm wieder her und wähle.",
           INCOMPLETE_PROGRESS : "Schon wieder hier? Okay, bist du zum Auswählen bereit?",
           INCOMPLETE_WRONG_NPC : "Denke gut nach, ehe du wählst.",
           COMPLETE : "Gute Wahl. Bevor du nun diese Gags einsetzen kannst, musst du dafür trainieren.\aDazu musst du eine Reihe von Toon-Aufgaben lösen.\aBei jeder Aufgabe erhältst du ein Bild deines Gag-Ablaufs.\aWenn du alle 15 sammelst, kannst du die Aufgabe für das Gag-Abschlusstraining erhalten, bei der du alle deine neuen Gags einsetzen kannst.\aDeine Fortschritte kannst du im Sticker-Buch sehen.",
           LEAVING : QuestsDefaultLeaving,
           },
    1039 : { QUEST : "Besuche _toNpcName_, wenn du dich leichter durch die Stadt bewegen willst._where_" },
    1040 : { QUEST : "Besuche _toNpcName_, wenn du dich leichter durch die Stadt bewegen willst._where_" },
    1041 : { QUEST : "Hi! Was führt dich hierher?\aAlle benutzen ihr tragbares Loch, um sich durch die Stadt zu bewegen.\aAlso, du kannst dich mit der Freunde-Liste zu deinen Freunden teleportieren oder auch mit dem Stadtplan im Sticker-Buch in jede andere Gegend.\aNatürlich musst du dir das erst verdienen!\aHör mal, ich kann deinen Teleport-Zugang zu Toontown Mitte einschalten, wenn du einem Freund von mir hilfst.\aAnscheinend machen die Bots drüben in der Hohlgasse Ärger. Geh mal zu _toNpcName_._where_" },
    1042 : { QUEST : "Hi! Was führt dich hierher?\aAlle benutzen ihr tragbares Loch, um sich durch die Stadt zu bewegen.\aAlso, du kannst dich mit der Freunde-Liste zu deinen Freunden teleportieren oder auch mit dem Stadtplan im Sticker-Buch in jede andere Gegend.\aNatürlich musst du dir das erst verdienen!\aHör mal, ich kann deinen Teleport-Zugang zu Toontown Mitte einschalten, wenn du einem Freund von mir hilfst.\aAnscheinend machen die Bots drüben in der Hohlgasse Ärger. Geh mal zu _toNpcName_._where_" },
    1043 : { QUEST : "Hi! Was führt dich hierher?\aAlle benutzen ihr tragbares Loch, um sich durch die Stadt zu bewegen.\aAlso, du kannst dich mit der Freunde-Liste zu deinen Freunden teleportieren oder auch mit dem Stadtplan im Sticker-Buch in jede andere Gegend.\aNatürlich musst du dir das erst verdienen!\aHör mal, ich kann deinen Teleport-Zugang zu Toontown Mitte einschalten, wenn du einem Freund von mir hilfst.\aAnscheinend machen die Bots drüben in der Hohlgasse Ärger. Geh mal zu _toNpcName_._where_" },
    1044 : { QUEST : "Oh, danke, dass du vorbeikommst. Ich brauche wirklich Hilfe.\aWie du sehen kannst, habe ich keine Kunden.\aMein geheimes Rezeptbuch ist weg und keiner kommt mehr in mein Restaurant.\aIch habe es zuletzt kurz bevor diese Bots mein Gebäude übernahmen gesehen.\aKannst du mir helfen und vier meiner berühmten Rezepte zurückholen?",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Hattest du schon Glück mit meinen Rezepten?" },
    1045 : { QUEST : "Herzlichen Dank!\aBald werde ich die gesamte Sammlung zurückhaben und mein Restaurant wieder aufmachen.\aOh, ich habe hier eine Nachricht für dich - irgendwas über Teleport-Zugang?\aDa steht - danke, dass du meinem Freund geholfen hast, gib das hier jetzt in Toontown-Zentrale ab.\aAlso wirklich vielen Dank - Tschüss!",
             LEAVING : "",
             COMPLETE : "Ach ja, es heißt hier, dass du den netten Leute in der Hohlgasse einen großen Dienst erwiesen hast.\aDa steht, dass du einen Teleport-Zugang nach Toontown Mitte brauchst.\aAlso, du kannst das als erledigt betrachten.\aDu kannst dich jetzt von fast überall aus Toontown zum Spielplatz zurück teleportieren.\aSchlag einfach deinen Stadtplan auf und klicke auf Toontown Mitte." },
    1046 : { QUEST : "Die Monetomaten belästigen die ganze Zeit die Spielgeld-Bausparkasse.\aSchau mal dort vorbei und sieh zu, ob du irgendetwas tun kannst._where_" },
    1047 : { QUEST : "Monetomaten haben sich immer wieder in die Bank geschlichen und unsere Maschinen gestohlen.\aBitte hole 5 Rechenmaschinen von den Monetomaten zurück.\aDamit du nicht immer hin und zurück rennen musst, bring sie einfach alle auf einmal zurück.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Suchst du immer noch Rechenmaschinen?" },
    1048 : { QUEST : "Wow! Danke, dass du unsere Rechenmaschinen gefunden hast.\aHm ... Die sehen ein bißchen beschädigt aus.\aSag mal, könntest du sie rüber zu _toNpcName_ bringen, in ihren Laden \"Kitzelmaschinen\" hier in der Straße?\aVielleicht bekommt sie die wieder hin.",
             LEAVING : "", },
    1049 : { QUEST : "Was ist denn das? Kaputte Rechenmaschinen? \aMonetomaten, sagst du?\aNaja, woll'n mal nachsehen...\aTja, Getriebe rausgenommen, aber ich hab diese Teile nicht mehr ...\aWeißt du, was gehen könnte - ein paar Bot-Zahnräder, große, von größeren Bots ...\aBot-Zahnräder von Level 3 müssten gehen. Ich brauch 2 für jede Maschine, also insgesamt 10.\aBring sie alle auf einmal her, dann mach ich die Dinger klar!",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Denk dran, ich brauch 10 Zahnräder, um die Maschinen zu reparieren." },
    1053 : { QUEST : "Ah ja, das dürfte jetzt klappen.\aAlles fertig, und das kostenlos.\aNimm sie wieder mit zu Spielgeld und sag ihnen `nen schönen Gruß von mir.",
             LEAVING : "",
             COMPLETE : "Rechenmaschinen alle repariert?\aGut gemacht. Ich bin sicher, dass ich hier irgendwo was habe, womit ich dich belohnen kann ... " },
    1054 : { QUEST : "_toNpcName_ braucht Hilfe bei seinen Clownautos._where_" },
    1055 : { QUEST : "Mannomann! Kann die Reifen zu diesem komischen Clownauto nicht finden!\aMeinste, du könntest mir mal helfen?\aDussel-Bob hat sie wohl in den Teich auf'm Spielplatz von Toontown Mitte geschmissen.\aWenn du dich da auf so'n Dock stellst, kannst du die Reifen vielleicht für mich rausfischen.",
             GREETING : "Huhu!",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Hast du Probleme, alle 4 Reifen rauszufischen?" },
    1056 : { QUEST : "Fan-kuchen-tastisch! Jetzt krieg ich dieses olle Clownauto wieder ins Rollen!\aHey, ich dachte, ich hätte hier mal `ne Luftpumpe gehabt, um diese Reifen aufzupumpen ...\aVielleicht hat _toNpcName_ sie sich ausgeliehen?\aKönntest du mal hingehen und sie für mich zurückholen?_where_",
             LEAVING : "" },
    1057 : { QUEST : "Tag.\aEine Reifenpumpe, sagst du?\aIch hab `ne Idee - du hilfst mir, ein paar von diesen höheren Bots von der Straße zu räumen ...\aUnd ich geb dir die Reifenpumpe.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Besser geht's nicht?" },
    1058 : { QUEST : "Gute Arbeit - ich wusste, dass du das schaffst.\aHier ist die Pumpe. Ich bin sicher, _toNpcName_ wird sich freuen, sie wieder zurück zu bekommen.",
             LEAVING : "",
             GREETING : "",
             COMPLETE : "Jippieh! Jetzt kann's losgehen!\aÜbrigens vielen Dank für deine Hilfe.\aHier, nimm das." },
    1059 : { QUEST : "_toNpcName_ gehen die Vorräte aus. Vielleicht kannst du ihm mal helfen?_where_" },
    1060 : { QUEST : "Danke, dass du vorbeikommst!\aDiese Bots haben meine Tinte gestohlen, jetzt geht sie mir fast aus.\aKönntest du für mich etwas Tintenfischtinte aus dem Teich fischen?\aStell dich zum Fischen einfach auf ein Dock am Teich.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Hast du ein Problem beim Fischen?" },
    1061 : { QUEST : "Große Klasse - danke für die Tinte!\aWeißt du was, wenn du vielleicht ein paar von diesen Griffelschiebern aus dem Weg räumen könntest ...\aDann würde mir die Tinte nicht wieder so schnell ausgehen.\aFür deine Belohnung musst du 6 Griffelschieber in Toontown Mitte besiegen.",
             LEAVING : "",
             COMPLETE : "Danke! Ich möchte dich für deine Hilfe belohnen.",
             INCOMPLETE_PROGRESS : "Ich hab grad noch ein paar Griffelschieber gesehen." },
    1062 : { QUEST : "Große Klasse - danke für die Tinte!\aWeißt du was, wenn du vielleicht ein paar von diesen Blutsaugern aus dem Weg räumen könntest ...\aDann würde mir die Tinte nicht wieder so schnell ausgehen.\aFür deine Belohnung musst du 6 Blutsauger in Toontown Mitte besiegen.",
             LEAVING : "",
             COMPLETE : "Danke! Ich möchte dich für deine Hilfe belohnen.",
             INCOMPLETE_PROGRESS : "Ich hab grad noch ein paar Blutsauger gesehen. " },
    900 : { QUEST : "Ich habe gehört, _toNpcName_ braucht Hilfe mit einem Paket._where_" },
    1063 : { QUEST : "Hi - danke, dass du rein gekommen bist. Ein Bot hat mir ein sehr wichtiges Paket direkt unter der Nase weg gestohlen.\aBitte sieh doch mal zu, ob du es zurückholen kannst. Ich glaube, es war einer von Level 3 ...\aAlso erledige Bots von Level 3, bis du mein Paket findest.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Kein Erfolg bei der Suche nach meinem Paket, was?" },
    1067 : { QUEST : "Na, da ist es ja!\aHey, die Adresse ist verschmiert ...\aIch kann nur noch entziffern, dass es für einen Dr. ist - der Rest ist unleserlich.\aVielleicht ist es für _toNpcName_? Könntest du es zu ihm bringen?_where_",
             LEAVING : "" },
    1068 : { QUEST : "Ich erwarte kein Paket. Vielleicht ist es für Dr. B. Geistert?\aMein Assistent geht sowieso heute rüber, da lasse ich ihn das für dich klären.\aWärst du vielleicht so nett, ein paar von den Bots in meiner Straße zu verjagen?\aVertreibe 10 Bots in Toontown Mitte.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Mein Assistent ist noch nicht zurück." },
    1069 : { QUEST : "Dr. B. Geistert sagt, er erwarte auch kein Paket.\aLeider hat ein Monetomat es meinem Assistenten auf dem Rückweg weggenommen.\aKönntest du versuchen, es zurückzubekommen?",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Kein Erfolg bei der Suche nach dem Paket, was?" },
    1070 : { QUEST : "Dr. B. Geistert sagt, er erwarte auch kein Paket.\aLeider hat ein Schachermat es meinem Assistenten auf dem Rückweg weggenommen.\aTut mir leid, aber du wirst diesen Schachermaten finden und das Paket zurückholen müssen.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Kein Erfolg bei der Suche nach dem Paket, was?" },
    1071 : { QUEST : "Dr. B. Geistert sagt, er erwarte auch kein Paket.\aLeider hat ein Chefomat es meinem Assistenten auf dem Rückweg weggenommen.\aKönntest du versuchen, es zurückzubekommen?",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Kein Erfolg bei der Suche nach dem Paket, was?" },
    1072 : { QUEST : "Großartig - du hast es wieder!\aVielleicht solltest du es mal bei _toNpcName_ versuchen, es könnte für ihn sein._where_",
             LEAVING : "" },
    1073 : { QUEST : "Oh, danke, dass du mir meine Pakete bringst.\aWarte mal, ich habe zwei erwartet. Könntest du mal bei _toNpcName_ nachprüfen, ob er vielleicht das andere hat?",
             INCOMPLETE : "Hast du mein anderes Paket finden können?",
             LEAVING : "" },
    1074 : { QUEST : "Er hat gesagt, dass es noch ein Paket gab? Vielleicht haben das auch die Bot gestohlen.\aErledige Bots, bis du das zweite Paket findest.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Kein Erfolg bei der Suche nach dem anderen Paket, was?" },
    1075 : { QUEST : "Offenbar gab es nun doch ein zweites Paket!\aBringe es schnell rüber zu _toNpcName_ und sage ihm, es täte mir Leid.",
             COMPLETE : "Hey, da ist ja mein Paket!\aDa du anscheinend ein sehr hilfsbereiter Toon bist, wirst du das hier brauchen können.",
             LEAVING : "" },
    1076 : { QUEST : "Drüben beim 14-Karat-Goldfisch hat es Ärger gegeben.\a_toNpcName_ könnte wahrscheinlich Hilfe gebrauchen._where_" },
    1077 : { QUEST : "Danke, dass du gekommen bist - die Bots haben alle meine Goldfische gestohlen.\aIch vermute, die Bots möchten sie verkaufen, um schnell Kohle zu machen.\aDiese 5 Fische waren so viele Jahre lang meine einzige Gesellschaft in diesem winzigen Laden ...\aWenn du sie für mich zurückholen könntest, wäre ich dir wirklich sehr dankbar.\aIch bin sicher, dass einer der Bots meine Fische hat.\aVerjage Bots, bis du meine Goldfische findest.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Bitte bring mir meine Goldfische wieder." },
    1078 : { QUEST : "Oh, du hast meine Fische!\aHä? Was ist das - eine Quittung?\aSeufz, naja, am Ende handelt es sich ja um Bots.\aIch werd aus dieser Quittung einfach nicht schlau. Könntest du sie mal zu _toNpcName_ bringen, vielleicht kann er sie lesen?_where_",
             INCOMPLETE : "Was hat _toNpcName_ zu der Quittung gesagt?",
             LEAVING : "" },
    1079 : { QUEST : "Mmh, lass mich mal diese Quittung sehen.\a...Ah ja, hier steht, dass 1 Goldfisch an einen gewissen Kriecher verkauft wurde.\aDie anderen 4 Fische werden aber anscheinend nicht erwähnt.\aVielleicht solltest du versuchen, diesen Kriecher zu finden.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Ich glaube nicht, dass es noch etwas gibt, womit ich dir helfen kann.\aWarum versuchst du nicht, diesen Goldfisch zu finden?" },
    1092 : { QUEST : "Mmh, lass mich mal diese Quittung sehen.\a...Ah ja, hier steht, dass 1 Goldfisch an einen gewissen Keinmünz verkauft wurde.\aDie anderen 4 Fische werden aber anscheinend nicht erwähnt.\aVielleicht solltest du versuchen, diesen Keinmünz zu finden.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Ich glaube nicht, dass es noch etwas gibt, womit ich dir helfen kann.\aWarum versuchst du nicht, diesen Goldfisch zu finden?" },
    1080 : { QUEST : "Oh, dem Himmel sei Dank! Du hast Oscar gefunden - er ist mein Liebling.\aWas sagst du, Oscar? Aha ... wirklich? ... da sind sie?\aOscar sagt, die anderen 4 sind in den Teich auf dem Spielplatz entwischt.\aKönntest du sie für mich einfangen?\aFische sie einfach aus dem Teich.",
             LEAVING : "",
             COMPLETE : "Ach, ich bin ja sooo froh! Wieder vereint zu sein mit meinen kleinen Freunden!\aDafür verdienst du eine hübsche Belohnung!",
             INCOMPLETE_PROGRESS : "Hast du Probleme, diese Fische zu finden?" },
    1081 : { QUEST : "_toNpcName_ scheint festzusitzen. Sie könnte bestimmt eine helfende Hand gebrauchen._where_" },
    1082 : { QUEST : "Ich hab Kleber verkleckert und jetzt steck ich fest - ei, der Daus!\aIch würd alles drum geben, käm ich hier raus.\aIch hab `ne Idee, vielleicht hilfst du mir'n Stück.\aSchlag ein paar Schachermaten und komm mit Öl zurück.",
             LEAVING : "",
             GREETING : "",
             INCOMPLETE_PROGRESS : "Kannst du mir helfen, mich zu entkleben?" },
    1083 : { QUEST : "Öl war schon gut, doch komm ich nicht los.\aWas würde noch helfen, was mach ich denn bloß?\aIch hab `ne Idee, wärst du wohl so nett.\aSchlag ein paar Rechtomaten und bringe mir Fett.",
             LEAVING : "",
             GREETING : "",
             INCOMPLETE_PROGRESS : "Kannst du mir helfen, mich zu entkleben?" },
    1084 : { QUEST : "Nö, keine Chance - nichts hat sich bewegt.\aIch hab das Fett auf die Moneten gelegt.\aApropos Moneten, wir machen es nasser.\aSchlag ein paar Monetomaten und bringe mir Wasser.",
             LEAVING : "",
             GREETING : "",
             COMPLETE : "Hurra, ich bin frei von diesem Leim!\aZur Belohnung wird dies Geschenk jetzt dein,\aDu kannst länger lachen beim Kampfe, und dann ...\aOh nein! Ich kleb ja schon wieder an!",
             INCOMPLETE_PROGRESS : "Kannst du mir helfen, mich zu entkleben?" },
    1085 : { QUEST : "_toNpcName_ führt Forschungen über die Bots durch.\aWenn du helfen willst, geh hin und sprich mal mit ihm._where_" },
    1086 : { QUEST : "Das ist richtig, ich führe eine Studie zu den Bots durch.\aIch möchte wissen, was sie in Gang setzt.\aEs würde mir auf jeden Fall helfen, wenn du ein paar Bot-Zahnräder sammeln könntest.\aAchte darauf, dass sie mindestens von Bots des Level 2 sind, damit sie für die Untersuchung groß genug sind.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Kannst du nicht genügend Zahnräder auftreiben?" },
    1089 : { QUEST : "Okay, da wollen wir mal sehen. Das sind ja hervorragende Exemplare!\aMmm...\aOkay, hier ist mein Bericht. Bringe ihn gleich zur Toontown-Zentrale.",
             INCOMPLETE : "Hast du meinen Bericht in Toontown-Zentrale gebracht?",
             COMPLETE : "Gute Arbeit, _avName_, wir übernehmen jetzt.",
             LEAVING : "" },
    1090 : { QUEST : "_toNpcName_ hat nützliche Informationen für dich._where_" },
    1091 : { QUEST : "Ich habe gehört, dass die Toontown-Zentrale an einer Art Bot-Radar arbeitet.\aDamit sieht man, wo sich die Bots aufhalten, so dass man sie leichter finden kann.\aDie Bot-Seite in deinem Sticker-Buch ist der Schlüssel dazu.\aWenn du genügend Bots bezwingst, kannst du ihre Signale empfangen und verfolgen, wo sie sind.\aBesiege weiterhin Bots, dann bist du dafür bereit.",
             COMPLETE : "Gute Arbeit! Das hier kannst du wahrscheinlich brauchen ...",
             LEAVING : "" },
    401 : {GREETING : "",
           QUEST : "Jetzt kannst du den nächsten Gag-Ablauf auswählen, den du lernen möchtest.\aNimm dir Zeit für die Entscheidung und komm zurück, wenn du bereit bist zu wählen.",
           INCOMPLETE_PROGRESS : "Denke gut nach, ehe du wählst.",
           INCOMPLETE_WRONG_NPC : "Denke gut nach, ehe du wählst.",
           COMPLETE : "Eine kluge Entscheidung ...",
           LEAVING : QuestsDefaultLeaving,
           },
    2201 : { QUEST : "Diese hinterlistigen Bots haben wieder zugeschlagen.\a_toNpcName_ hat einen weiteren verschwundenen Gegenstand gemeldet. Schau mal dort vorbei, ob du das regeln kannst._where_" },
    2202 : { QUEST : "Hi, _avName_. Gott sei Dank bist du hier. Ein gemeiner Pfennigfuchser kam grad hier rein und machte sich mit einem Schlauch davon.\aIch habe den Verdacht, dass sie den für ihre üblen Zwecke verwenden wollen.\aBitte versuche ihn zu finden und bring den Schlauch zurück.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Hast du meinen Schlauch schon gefunden?",
             COMPLETE : "Du hast meinen Schlauch gefunden! Du BIST gut! Hier, deine Belohnung ...",
             },
    2203 : { QUEST : "Die Bots verursachen drüben in der Bank das totale Chaos.\aSuche Käpt'n Karl auf und schau mal, was du tun kannst._where_" },
    2204 : { QUEST : "Willkommen an Bord, Kamerad!\aMist! Diese Halunken von Bots haben mein Monokel zerschmissen und ich kann so mein Kleingeld nicht sortieren. \aSei eine nette Landratte und bring dieses Rezept zu Dr. Queequeg und hol mir ein neues._where_",
             GREETING : "",
             LEAVING : "",
             },
    2205 : { QUEST : "Was ist das?\aAch, ich würde das Rezept ja gern einlösen, aber die Bots haben mein Lager geplündert.\aWenn du mir das Brillengestell von einem Kriecher bringst, kann ich vielleicht helfen.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Tut mir Leid. Kein Kriechergestell, kein Monokel.",
             },
    2206: { QUEST : "Ausgezeichnet!\aEinen Moment ...\aDein Rezept ist hiermit eingelöst. Bitte nimm dieses Monokel gleich mit zu Käpt'n Karl._where_",
            GREETING : "",
            LEAVING : "",
            COMPLETE : "Fest!\aDa verdienst du dir ja tatsächlich deine Seefestigkeit.\aHier hast du.",
            },
    2207 : { QUEST : "Bernikel-Barbara hat einen Bot in ihrem Laden!\aDu solltest mal rübergehen, und zwar pronto._where_" },
    2208 : { QUEST : "Menschenskind! Du hast ihn genau verpasst, Schätzchen.\aEs war ein Heimtücker hier. Er nahm meine große weiße Perücke mit.\aEr sagte, sie sei für seinen Chef, und irgendwas von 'Präzedenzfall.'\aWenn du sie zurückbringen könntest, wäre ich dir ewig dankbar.",
             LEAVING : "",
             GREETING : "",
             INCOMPLETE_PROGRESS : "Hast du ihn immer noch nicht gefunden?\aEr ist groß und hat einen Eierkopf.",
             COMPLETE : "Gefunden!?!?\aDu bist ein echter Schatz!\aDu hast dir das hier mehr als verdient ...",
             },
    2209 : { QUEST : "Melville bereitet sich auf eine wichtige Reise vor.\aGeh hin und sieh mal, wie du ihm helfen kannst._where_"},
    2210 : { QUEST : "Ich kann deine Hilfe brauchen.\aDie Toon-Zentrale hat mich gebeten, eine Reise zu machen und herauszufinden, woher die Bots kommen.\aIch brauch ein paar Sachen für mein Schiff, aber ich habe nicht viele Jelly Beans.\aGeh mal zu Alice und hol etwas Ballast. Du wirst ihr einen Gefallen tun müssen, damit du ihn bekommst._where_",
             GREETING : "Wie geht's, wie steht's, _avName_",
             LEAVING : "",
             },
    2211 : { QUEST : "Melville will also Ballast?\aEr schuldet mir noch was für das letzte Bündel.\aIch geb's dir aber, wenn du fünf Mikromanager aus meiner Straße entfernen kannst.",
             INCOMPLETE_PROGRESS : "Nein, Dummchen! Ich sagte FÜNF Mikromanager ...",
             GREETING : "Was kann ich für dich tun?",
             LEAVING : "",
             },
    2212 : { QUEST : "Abgemacht ist abgemacht.\aHier ist dein Ballast für diesen Geizhals Melville._where_",
             GREETING : "Na, wer kommt denn da ...",
             LEAVING : "",
             },
    2213 : { QUEST : "Hervorragende Arbeit. Ich wusste, dass sie vernünftig sein wird.\aAls nächstes brauche ich eine Seekarte von Art.\aIch glaube, mit meinem Kredit sieht es dort auch nicht so günstig aus. Du wirst wohl was mit ihm aushandeln müssen._where_",
             GREETING : "",
             LEAVING : "",
             },
    2214 : { QUEST : "Ja, ich habe die Seekarte, die Melville braucht.\aUnd wenn du bereit bist, dafür zu arbeiten, bekommst du sie auch.\aIch versuche gerade, ein Astrolabium zu bauen, um mich an den Sternen zu orientieren.\aIch könnte dafür drei Bot-Zahnräder gebrauchen.\aKomm wieder, wenn du sie hast.",
             INCOMPLETE_PROGRESS: "Wie steht's mit den Bot-Zahnrädern?",
             GREETING : "Willkommen!",
             LEAVING : "Viel Glück!",
             },
    2215 : { QUEST : "Oha! Diese Zahnräder sind wirklich gut geeignet.\aHier ist die Karte. Gib sie Melville mit freundlichen Grüßen._where_",
             GREETING : "",
             LEAVING : "",
             COMPLETE : "Nun, damit hätten wir's. Ich bin fertig zum Ablegen!\aWenn du nicht so grün wärst, würde ich dich mitnehmen. Nimm stattdessen das hier.",
             },
    901 : { QUEST : "Wenn du meinst du kannst das - Ahab könnte drüben bei sich ein bisschen Unterstützung gebrauchen ..._where_",
            },
    2902 : { QUEST : "Bist du der Neue?\aGut, gut. Vielleicht kannst du mir helfen.\aIch baue gerade eine riesige fabelhafte Seekrabbe, um die Bots zu verwirren.\aIch könnte allerdings noch einen Webeleinstek brauchen. Geh mal bitte zu Gert und bring einen mit._where_",
             },
    2903 : { QUEST : "Tagchen!\aJa, ich habe von der Riesenkrabbe gehört, an der Ahab arbeitet.\aDer beste Webeleinstek, den ich habe, ist aber ein wenig angeschmuddelt.\aSei so nett und lass ihn erst reinigen, bevor du ihn dort abgibst._where_",
             LEAVING : "Danke!"
             },
    2904 : { QUEST : "Du musst der sein, den Gert geschickt hat.\aIch denke, ich kann das schnell reinigen.\aEinen Moment ...\aBitte schön. So gut wie neu!\aSag Ahab schönen Gruß von mir._where_",
             },
    2905 : { QUEST : "Ah, das ist ja genau, was ich suche.\aDa du einmal hier bist, ich brauche auch noch eine sehr große Uhrfeder.\aSpazier doch mal rüber zu Hook und frag ihn, ob er eine hat._where_",
             },
    2906 : { QUEST : "Eine große Sprungfeder, was?\aTut mir leid, aber die größte Feder, die ich habe, ist immer noch ziemlich klein.\aVielleicht könnte ich eine aus Spritzpistolenabzugsfedern zusammenbauen.\aBring mir drei von diesen Gagdingern, und ich seh zu, was ich tun kann.",
             },
    2907 : { QUEST : "Na, woll'n mal schauen ...\aToll. Einfach toll.\aManchmal bin ich von mir selbst überrascht.\aBitteschön: Eine große Sprungfeder für Ahab!_where_",
             LEAVING : "Bon Voyage!",
             },
     2911 : { QUEST : "Ich würde ja gern was für die gute Sache tun, _avName_.\aAber ich fürchte, die Straßen sind nicht mehr sicher.\aWarum bezwingst du nicht ein paar Monetomaten-Bots, dann reden wir drüber.",
             INCOMPLETE_PROGRESS : "Ich glaube immer noch, du musst die Straßen sicherer machen.",
             },
    2916 : { QUEST : "Ja, ich habe ein Gewicht, das Ahab haben kann.\aAber ich denke, es wäre sicherer, wenn du erst ein paar Schachermaten vertreibst.",
             INCOMPLETE_PROGRESS : "Noch nicht. Erledige erst noch ein paar Schachermaten.",
             },
    2921 : { QUEST : "Hmmm, ich denke, ich könnte ein Gewicht abgeben.\aIch hätte aber ein besseres Gefühl dabei, wenn hier nicht so viele Chefomaten herumschleichen würden.\aBezwinge sechs und komm dann wieder zu mir.",
             INCOMPLETE_PROGRESS : "Ich glaube nicht, dass es schon sicher ist ... ",
             },
    2925 : { QUEST : "Fertig?\aNa, ich denke, jetzt ist es sicher genug.\aHier ist das Gegengewicht für Ahab._where_"
             },
    2926 : {QUEST : "Nun, das ist alles.\aWoll'n mal sehen, ob es jetzt geht.\aHmmm, noch ein kleines Problem.\aIch habe keinen Strom, weil das Bot-Gebäude meine Solarzellen blockiert.\aKannst du es für mich zurückerobern?",
            INCOMPLETE_PROGRESS : "Immer noch kein Strom. Was ist mit dem Gebäude?",
            COMPLETE : "Super! Du bist ja ein echter Bot-Zerstörer! Hier, nimm das als Belohnung ...",
            },
    3200 : { QUEST : "Ich hab grad einen Anruf von _toNpcName_ bekommen.\aEr hat einen schweren Tag. Vielleicht kannst du ihm helfen!\aGeh mal hin und schau, was er braucht._where_" },
    3201 : { QUEST : "Oh, danke, dass du gekommen bist!\aIch brauche jemanden, der diese neue Seidenkrawatte zu _toNpcName_ bringt.\aKönntest du das für mich tun?_where_" },
    3203 : { QUEST : "Oh, das muss die Krawatte sein, die ich bestellt habe! Danke!\aSie passt zu einem Nadelstreifenanzug, den ich gerade fertiggestellt habe, da drüben.\aHe, was ist denn mit dem Anzug passiert?\aOch nein! Die Bots müssen meinen neuen Anzug gestohlen haben!\aJage Bots, bis du meinen Anzug findest, und bring ihn zu mir zurück.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Hast du meinen Anzug schon gefunden? Ich bin sicher, dass die Bots ihn geholt haben!",
             COMPLETE : "Hurra! Du hast meinen neuen Anzug gefunden!\aSiehste, ich hab dir doch gesagt, dass die Bots ihn haben! Hier ist deine Belohnung ... ",
             },

    3204 : { QUEST : "_toNpcName_ hat grad angerufen, um einen Diebstahl zu melden.\aGeh doch mal rüber und schau, ob du die Sache wieder in Ordnung bringen kannst?_where_" },
    3205 : { QUEST : "Hallo, _avName_! Willst du mir helfen?\aIch habe gerade einen Blutsauger aus meinem Laden gejagt. Hui, das war vielleicht gruselig!\aAber jetzt kann ich meine Schere nirgends finden! Ich bin sicher, der Blutsauger hat sie genommen.\aFinde den Blutsauger und erobere mir meine Schere zurück.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Suchst du noch nach meiner Schere?",
             COMPLETE : "Meine Schere! Hab vielen Dank! Hier ist deine Belohnung ... ",
             },

    3206 : { QUEST : "Es klingt, als hätte _toNpcName_ gerade ein Problem mit ein paar Bots.\aSchau mal nach, ob du ihm helfen kannst._where_" },
    3207 : { QUEST : "Hi, _avName_! Danke für's Herkommen!\aEin paar Dummschwätzer sind grad bei mir eingebrochen und haben einen Stapel Postkarten von meiner Theke geklaut.\aBitte geh los und jag alle Dummschwätzer meine Postkarten zurück bekomme!",
             INCOMPLETE_PROGRESS : "Das sind noch nicht alle Postkarten! Such weiter!",
             COMPLETE : "Oh, danke! Jetzt kann ich die Post pünktlich ausliefern! Hier ist deine Belohnung ... ",
             },

    3208 : { QUEST : "Wir bekommen in letzter Zeit Beschwerden von den Anwohnern über diese ganzen Aufschwatzer.\aSieh mal zu, ob du 10 Aufschwatzer vertreiben kannst, um deinen Mit-Toons in Daisys Gärten zu helfen." },
    3209 : { QUEST : "Danke, dass du dich um diese Aufschwatzer gekümmert hast!\aJetzt sind aber die Telemarketer außer Kontrolle geraten.\aErledige 10 Telemarketer in Daisys Gärten und komm wieder her, um deine Belohnung abzuholen." },

    3247 : { QUEST : "Wir bekommen in letzter Zeit Beschwerden von den Anwohnern über diese ganzen Blutsauger.\aSieh mal zu, ob du 20 Blutsauger vertreiben kannst, um deinen Mit-Toons in Daisys Gärten zu helfen." },


    3210 : { QUEST : "Oh nein, der Spritzblume in der Ahornstraße sind gerade die Blumen ausgegangen!\aBring ihnen zehn von deinen eigenen Spritzblumen hin, um ihnen zu helfen.\aDu musst aber erst 10 Spritzblumen in deinem Lager haben.",
             LEAVING: "",
             INCOMPLETE_PROGRESS : "Ich brauche 10 Spritzblumen. Du hast nicht genug!" },
    3211 : { QUEST : "Oh, vielen Dank! Diese Spritzblumen sind unsere Rettung.\aAber ich fürchte mich vor den Bots da draußen.\aKannst du mir helfen und ein paar von den Bots vertreiben?\aKomm wieder zu mir, wenn du 20 Bots in dieser Straße erledigt hast.",
             INCOMPLETE_PROGRESS : "Es sind da draußen immer noch Bots übrig! Mach weiter!",
             COMPLETE : "Oh, vielen Dank! Das ist eine große Hilfe. Deine Belohnung ist ...",
             },

    3212 : { QUEST : "_toNpcName_ hat etwas verloren und braucht Hilfe bei der Suche.\aGeh mal hin und schau, was du tun kannst._where_" },
    3213 : { QUEST : "Hi, _avName_. Kannst du mir helfen?\aIch habe anscheinend meinen Stift verlegt. Möglicherweise haben ihn die Bots weggenommen.\aVertreibe Bots, bis du meinen gestohlenen Stift wiederfindest.",
             INCOMPLETE_PROGRESS : "Hast du meinen Stift schon gefunden?" },
    3214 : { QUEST : "Ja, das ist mein Stift! Vielen Dank!\aAls du weg warst, habe ich aber gemerkt, dass auch mein Tintenfass fehlt.\aVertreibe Bots, um mein Tintenfass zu finden.",
             INCOMPLETE_PROGRESS : "Ich suche immer noch nach meinem Tintenfass!" },
    3215 : { QUEST : "Großartig! Jetzt habe ich meinen Stift und mein Tintenfass wieder.\aAber weißt du was?\aJetzt ist mein Schreibblock weg! Sie müssen ihn auch gestohlen haben!\aSuche die Bots, um meinen gestohlenen Schreibblock zu finden, und dann bringe ihn zu mir zurück und hole dir deine Belohnung ab.",
             INCOMPLETE_PROGRESS : "Irgendetwas Neues vom Schreibblock? " },
    3216 : { QUEST : "Das ist mein Schreibblock! Hurra! Deine Belohnung ist ...\aHe! Wo ist sie denn hin?\aIch hatte deine Belohnung direkt hier in meiner verschließbaren Kassette. Aber die Kassette ist weg!\aDas ist doch nicht zu glauben! Diese Bots haben deine Belohnung gestohlen!\aJage die Bots und hole meine Kassette zurück.\aWenn du sie mir zurückbringst, gebe ich dir deine Belohnung.",
             INCOMPLETE_PROGRESS : "Such weiter nach dieser Kassette! Da ist deine Belohnung drin!",
             COMPLETE : "Na endlich! Ich hatte deine neue Gagtasche in der Kassette. Hier ist sie ...",
             },

    3217 : { QUEST : "Wir haben ein paar Studien zur Schachermat-Mechanik durchgeführt.\aWir müssen uns einige Teile noch näher ansehen.\aBring uns einen Kettenradzahn von einem Wichtigtuer.\aDu kannst dir eins holen, wenn der Bot explodiert." },
    3218 : { QUEST : "Gute Arbeit! Wir brauchen jetzt zum Vergleich einen Zahn von einem Glückshändchen.\aDiese Zähne sind schwerer zu holen, aber lass dich nicht entmutigen." },
    3219 : { QUEST : "Großartig! Jetzt brauchen wir nur noch einen Zahn.\aDiesmal brauchen wir einen von einem Aufbauscher.\aDu musst möglicherweise in ein paar Schachermat-Gebäude hineinschauen, um diese Bots zu finden.\aWenn du einen Zahn hast, bring ihn her und hol dir deine Belohnung ab." },

    3244 : { QUEST : "Wir haben ein paar Studien zur Rechtomat-Mechanik durchgeführt.\aWir müssen uns einige Teile noch näher ansehen.\aBring uns einen Kettenradzahn von einem Unfallabzocker.\aDu kannst dir eins holen, wenn der Bot explodiert." },
    3245 : { QUEST : "Gute Arbeit! Wir brauchen jetzt zum Vergleich einen Zahn von einem Heimtücker.\aDiese Zähne sind schwerer zu holen, aber lass dich nicht entmutigen." },
    3246 : { QUEST : "Großartig! Jetzt brauchen wir nur noch einen Zahn.\aDiesmal brauchen wir einen von einem Schönredner.\aWenn du einen hast, bring ihn her und hol dir deine Belohnung ab." },

    3220 : { QUEST : "Ich habe gerade gehört, dass _toNpcName_ überall nach dir gefragt hat.\aWarum gehst du nicht mal hin und fragst, was sie will?_where_" },
    3221 : { QUEST : "Hi, _avName_! Da bist du ja!\aIch habe gehört, dass du ein ziemlicher Experte für Spritzattacken sein sollst.\aIch brauche jemanden, der allen Toons in Daisys Gärten mal ein gutes Beispiel gibt.\aSetz deine Spritzattacken ein, um ein paar Bots zu vertreiben.\aErmutige auch deine Freunde, mit zu spritzen.\aWenn du 20 Bots vertreiben hast, komm wieder her und hol dir deine Belohnung ab!" },

    3222 : { QUEST : "Es ist höchste Zeit, deine Toonhaftigkeit unter Beweis zu stellen.\aWenn du erfolgreich eine Reihe von Bot-Gebäuden zurückholst, erwirbst du dir das Recht, drei Aufgaben zu tragen.\aErobere zunächst zwei beliebige Bot-Gebäude.\aDu darfst deine Freunde um Hilfe bitten."},
    3223 : { QUEST : "Das mit den Gebäuden hast du gut gemacht!\aErobere nun zwei weitere Gebäude.\aDiese Gebäude müssen mindestens zwei Stockwerke hoch sein." },
    3224 : { QUEST : "Fantastisch!\aJetzt brauchst du nur noch zwei weitere Gebäude erkämpfen.\aDiese Gebäude müssen mindestens drei Stockwerke hoch sein.\aWenn du fertig bist, komm zurück und hol dir deine Belohnung ab!",
             COMPLETE : "Du hast es geschafft, _avName_!\aDu hast deine überaus große Toonhaftigkeit bewiesen.",
             GREETING : "",
             },

    3225 : { QUEST : "_toNpcName_ sagt, dass sie Hilfe braucht.\aGeh doch mal hin und frag, wie du ihr helfen kannst?_where_" },
    3235 : { QUEST : "Oh, das ist der Salat, den ich bestellt habe!\aDanke, dass du ihn mir bringst.\aDiese Bots haben wohl _toNpcName_s eigentliches Lieferanten wieder mal vergrault.\aTu uns doch einen Gefallen und verjage ein paar von den Bots da draußen.\aBezwinge 10 Bots in Daisys Gärten und melde dich dann wieder bei _toNpcName_.",
             INCOMPLETE_PROGRESS : "Du bist noch dabei, Bots für mich zu vertreiben?\aDas ist großartig! Mach so weiter!",
             COMPLETE : "Oh, vielen Dank, dass du diese Bots vertrieben hast!\aJetzt kann ich vielleicht meinen normalen Lieferplan einhalten.\aDeine Belohnung ist ... ",
             INCOMPLETE_WRONG_NPC : "Geh mal zu _toNpcName_ und berichte von den Bots, die du vertrieben hast._where_" },

    3236 : { QUEST : "Es gibt viel zu viele Rechtomaten da draußen.\aDu kannst deinen Teil zur Rettung beitragen!\aErobere 3 Rechtomaten-Gebäude." },
    3237 : { QUEST : "Das mit den Rechtomaten-Gebäuden hast du gut gemacht!\aJetzt gibt es aber zu viele Schachermaten!\aErobere 3 Schachermaten-Gebäude, dann komm zurück und hol dir deine Belohnung ab." },

    3238 : { QUEST : "Oh nein! Ein 'Einmischer'-Bot hat den Schlüssel zu Daisys Gärten gestohlen!\aVersuche doch, ihn zurückzuholen.\aDenk dran, den Einmischer kann man nur in Schachermaten-Gebäuden finden." },
    3239 : { QUEST : "Du hast zwar einen Schlüssel gefunden, aber es ist nicht der richtige!\aWir brauchen den Schlüssel zu Daisys Gärten.\aSuche weiter! Ein \"Einmischer\"-Bot hat ihn noch!" },

    3242 : { QUEST : "Oh nein! Ein Prozessgeier-Bot hat den Schlüssel zu Daisys Gärten gestohlen!\aVersuche mal, ihn zurückzuholen.\aDenk daran, Prozessgeier kann man nur in Rechtomaten-Gebäuden finden. " },
    3243 : { QUEST : "Du hast zwar einen Schlüssel gefunden, aber es ist nicht der richtige!\aWir brauchen den Schlüssel zu Daisys Gärten.\aSuche weiter! Ein Prozessgeier-Bot hat ihn noch!" },

    3240 : { QUEST : "Ich habe grad von _toNpcName_ gehört, dass ein Prozessgeier eine Tüte Vogelfutter gestohlen hat.\aVertreibe Prozessgeier, bis du Volkers Vogelfutter zurückgeholt hast, und bringe es ihm dann.\aProzessgeier findet man nur in Rechtomaten-Gebäuden._where_",
             COMPLETE : "Oh, vielen Dank, dass du mein Vogelfutter gefunden hast!\aDeine Belohnung ist ... ",
             INCOMPLETE_WRONG_NPC : "Das mit dem Vogelfutter hast du gut gemacht!\aBring es jetzt zu _toNpcName_._where_",
             },

    3241 : { QUEST : "Ein paar von den Bot-Gebäuden da draußen werden höher, als uns lieb ist.\aSieh mal zu, ob du ein paar von den höchsten Gebäuden erobern kannst.\aErobere 5 Gebäude mit drei oder mehr Stockwerken und komm´dann wieder, um dir deine Belohnung abzuholen.",
             },

    3250 : { QUEST : "Detektivin Lima drüben in der Eichenstraße hat Meldungen über ein Schachermat-Hauptquartier erhalten.\aSpring mal rüber und hilf ihr bei den Untersuchungen.",
             },
    3251 : { QUEST : "Hier geht etwas Seltsames vor.\aEs gibt hier so viele Schachermaten!\aIch habe gehört, dass sie eine eigene Toontown-Zentrale am Ende dieser Straße eingerichtet haben.\aGeh mal die Straße runter und schau, ob du was rauskriegen kannst.\aFinde Schachermaten-Bots in ihrem Hauptquartier, besiege 5 und melde dich zurück.",
             },
    3252 : { QUEST : "OK, spuck's aus.\aWas sagst du da?\aSchachermaten-Hauptquartier?? Ach du Schreck!!! Es muss was passieren.\aWir müssen Richterin McIntosh Bescheid geben - sie wird wissen, was zu tun ist.\aGeh sofort los und erzähle ihr, was du herausgefunden hast. Du findest sie weiter die Straße runter.",
            },
    3253 : { QUEST : "Ja, kann ich helfen? Ich bin sehr beschäftigt.\aWas? Bot-Zentrale?\aWas? Unsinn. Das könnte nie passieren.\aDu musst dich irren. Völlig absurd.\aWas? Widersprich mir nicht.\aNa gut, dann bring mir Beweise.\aWenn Schachermaten wirklich dieses Bot-Zentrale bauen, dann trägt jeder Bot dort Blaupausen mit sich herum.\aBots lieben Papierkram, weißt du?\aJage Schachermaten, bis du Blaupausen findest.\aBring sie her, dann glaube ich dir vielleicht.",
            },
    3254 : { QUEST : "Du schon wieder, was? Blaupausen? Du hast sie?\aLass mich mal sehen! Hmmm... Eine Fabrik?\aDort bauen sie wohl die Schachermaten ... Und was ist das?\aJa, genau wie ich vermutete. Ich hab's ja immer gewusst.\aSie bauen ein Schachermaten-Bot-Hauptquartier.\aDas ist nicht gut. Muss telefonieren. Sehr viel zu tun. Auf Wiedersehen!\aWas? Ach ja, nimm diese Blaupausen mit zu Detektivin Lima.\aSie kann mehr damit anfangen.",
             COMPLETE : "Was hat Richterin McIntosh gesagt?\aWir hatten Recht? Oh nein. Lass mal diese Blaupausen sehen.\aHmmm... Sieht aus, als würden die Schachermaten eine Fabrik mit Maschinen zur Herstellung von Bots bauen.\aKlingt sehr gefährlich. Halte dich raus, bis du mehr Lach-Punkte hast.\aWenn du mehr Lach-Punkte hast, müssen wir noch viel mehr über das Schachermaten-Hauptquartier rauskriegen.\aBisher aber gut gemacht, hier ist deine Belohnung.",
            },


    3255 : { QUEST : "_toNpcName_ untersucht das Schachermaten-Hauptquartier.\aSchau mal, ob du helfen kannst._where_" },
    3256 : { QUEST : "_toNpcName_ untersucht das Schachermaten-Hauptquartier.\aSchau mal, ob du helfen kannst._where_" },
    3257 : { QUEST : "_toNpcName_ untersucht das Schachermaten-Hauptquartier.\aSchau mal, ob du helfen kannst._where_" },
    3258 : { QUEST : "Es gibt verschiedenste Vermutungen darüber, was die Bots in ihrem neuen Hauptquartier vorhaben.\aIch möchte, dass du direkt von ihnen ein paar Informationen holst.\aWenn wir vier interne Memos von Schachermaten aus ihrem Hauptquartiers bekommen können, dann werden wir klarer sehen.\aBringe dein erstes Memo zu mir, damit wir mehr erfahren.",
             },
    3259 : { QUEST : "Großartig! Lass mal sehen, was in dem Memo steht ... \a\"An alle Schachermaten:\aIch sitze in meinem Büro oben im Schachermat Tower und befördere Bots.\aWer genügend Verdienste gesammelt hat, steige in den Fahrstuhl in der Lobby und komme zu mir.\aDie Ferien sind vorbei - nun wieder an die Arbeit!\aUnterschrift: Schachermat VP\"\aAha ... das wird Flippy interessieren. Ich lasse es ihm sofort zukommen.\aBitte hole jetzt dein zweites Memo und bring es her.",
             },
    3260 : { QUEST : "Ach, gut, dass du zurückkommst. Mal sehen, was du gefunden hast ...\a\"An alle Schachermaten:\aSchachermat Towers hat ein neues Sicherheitssystem installiert, um die Toons fern zu halten.\aWenn Toons in Schachermat Towers aufgegriffen werden, werden sie zum Verhör festgehalten.\aAlles weitere kann in der Lobby bei einem Aperitif besprochen werden.\aUnterschrift: Einmischer\"\aSehr interessant ... Ich gebe diese Information sofort weiter.\aBitte bringe ein drittes Memo her.",
             },
    3261 : { QUEST : "Ausgezeichnete Arbeit, _avName_! Was steht da drin?\a\'An alle Schachermaten:\aToons haben einen Weg gefunden, um in Schachermat Towers einzudringen.\aIch werde Sie heute Abend beim Essen anrufen und Ihnen die Einzelheiten mitteilen.\aUnterschrift:Telemarketer'\aHmmm... ich frage mich, wie Toons da einbrechen ...\aBitte bring noch ein Memo, dann wissen wir erstmal genug, denke ich.",
             COMPLETE : "Ich wusste, dass du es schaffen würdest! OK, in dem Memo heißt es ...\a\"An alle Schachermaten:\aIch war gestern mit Mr. Hollywood beim Lunch.\aEr berichtete, dass der VP zur Zeit sehr beschäftigt ist.\aEr macht nur Termine mit Bots, die eine Beförderung verdienen.\aNoch was vergessen: Glückshändchen spielt am Sonntag mit mir Golf.\aUnterschrift: Wichtigtuer\"\aAlso ... _avName_, das war sehr hilfreich.\aHier ist deine Belohnung.",
             },

    3262 : { QUEST : "_toNpcName_ hat neue Informationen über die Fabrik des Schachermaten-Hauptquartier.\aGeh mal hin und schau, was er hat._where_" },
    3263 : { GREETING : "Hi Sportsfreund!",
             QUEST : "Ich bin Trainer Bemoost, aber du kannst Trainer B. zu mir sagen.\aVon mir stammen die Flechten in Hauen und Flechten, aber auch das Hauen, wenn du weißt, was ich meine.\aHör mal, die Schachermaten haben eine riesige Fabrik fertiggestellt, die 24 Stunden am Tag Schachermaten ausspuckt.\aHol mal ein paar Toon-Sportsfreunde zusammen und hau denen eins drauf!\aIhr müsst im Schachermaten-Hauptquartier nach dem Tunnel zur Fabrik Ausschau halten, und dann den Fabrikfahrstuhl nehmen.\aAchtet darauf, dass ihr volle Gags, volle Lach-Punkte und ein paar starke Toons als Führer habt.\aBesiegt den Vorarbeiter in der Fabrik, um das Vorankommen der Schachermaten aufzuhalten.\aKlingt wie `ne schweißtreibende Angelegenheit, wenn du weißt, was ich meine.",
             LEAVING : "Mach's gut, Sportsfreund!",
             COMPLETE : "He Sportsfreund, gute Arbeit da in der Fabrik!\aSieht aus, als hättest du da ein  Bot-Anzugteil gefunden.\aDer muss wohl bei ihrer Bot-Herstellung übrig geblieben sein.\aDer kann noch gute Dienste leisten. Wenn du mal zu viel Zeit hast, sammle mehr von denen.\aWenn du einen ganzen Bot-Anzug zusammen hast, kann der vielleicht noch zu irgend etwas gut sein ...",
             },

        4001 : {GREETING : "",
            QUEST : "Du kannst jetzt den nächsten Gag-Alauf wählen, den du erlernen möchtest.\aNimm dir Zeit für die Entscheidung und komm zurück, wenn du bereit zum Wählen bist.",
            INCOMPLETE_PROGRESS : "Denke gut nach, ehe du wählst.",
            INCOMPLETE_WRONG_NPC : "Denke gut nach, ehe du wählst.",
            COMPLETE : "Eine kluge Entscheidung ...",
            LEAVING : QuestsDefaultLeaving,
            },

    4002 : {GREETING : "",
            QUEST : "Du kannst jetzt den nächsten Gag-Ablauf wählen, den du erlernen möchtest.\aNimm dir Zeit für die Entscheidung und komm zurück, wenn du bereit zum Wählen bist.",
            INCOMPLETE_PROGRESS : "Denke gut nach, ehe  du wählst.",
            INCOMPLETE_WRONG_NPC : "Denke gut nach, ehe du wählst.",
            COMPLETE : "Eine kluge Entscheidung ...",
            LEAVING : QuestsDefaultLeaving,
            },
    4200 : { QUEST : "Ich wette, Tom könnte bei seinen Forschungen etwas Hilfe gebrauchen._where_",
             },
    4201 : { GREETING: "Wie geht's, wie steht's?",
             QUEST : "Ich bin sehr besorgt über eine Flut von Instrumentendiebstählen.\aIch mache gerade eine Umfrage bei meinen Händlerkollegen.\aVielleicht kann ich ein Muster erkennen, das mir beim Knacken dieses Falls hilft.\aGeh mal rüber zu Tina und frag sie nach einer Konzertina-Inventarliste._where_",
             },
    4202 : { QUEST : "Ja, ich habe heute früh mit Tom gesprochen.\aIch hab die Inventarliste hier.\aBring sie ihm gleich rüber, ja?_where_"
             },
    4203 : { QUEST : "Großartig! Eine weniger ...\aJetzt spring mal rüber und hole die von Yuki._where_",
             },
    4204 : { QUEST : "Oh! Die Inventarliste!\aHab ich ja völlig vergessen.\aIch wette, ich hab sie fertig, bis du 10 Bots vertrieben hast.\aKomm danach wieder rein, und ich verspreche dir, dass ich dann fertig bin.",
             INCOMPLETE_PROGRESS : "31, 32... MI-st!\aWegen dir hab ich mich verzählt!",
             GREETING : "",
             },
    4205 : { QUEST : "Ah, da bist du ja.\aDanke, dass du mir etwas Zeit gegeben hast.\aNimm das hier mit zu Tom und grüß ihn schön von mir._where_",
             },
    4206 : { QUEST : "Hmmm, sehr interessant.\aJetzt kommen wir doch langsam voran.\aOK, die letzte Inventarliste ist die von Fifi._where_",
             },
    4207 : { QUEST : "Inventarliste?\aWie soll ich denn eine Inventarliste schreiben, wenn ich kein Formular habe?\aGeh mal zu Quint und frag ihn, ob er eins für mich hat._where_",
             INCOMPLETE_PROGRESS : "Schon was Neues in Sachen Formular?",
             },
    4208 : { QUEST : "Nu, klar `abe isch Inventarformular!\aAber du musse bezahlen, weisstu?\aIsch mach dir Vorschlag. Isch tausche Formular für ganze Sahnetorte.",
             GREETING : "Hey, was' los, man!",
             LEAVING : "Hey, cool, man.",
             INCOMPLETE_PROGRESS : "Ein Stücke reiche nischt.\aIsch 'abe sehr hungrig, man. Isch brauche GANZES Torte!",
             },
    4209 : { GREETING : "",
             QUEST : "Mmmm...\aDas ist serrr gutt!\aHier deine Formular für Fifi._where_",
             },
    4210 : { GREETING : "",
             QUEST : "Danke. Das ist eine große Hilfe.\aWolln mal sehen ...Fiedeln: 2\aSchon fertig! Bitteschön!",
             COMPLETE : "Gute Arbeit, _avName_.\aIch bin sicher, dass ich diesen Diebstählen jetzt auf den Grund komme.\aKümmer du dich doch um das hier!",
             },

    4211 : { QUEST : "Sag mal, Dr. Unsauber ruft alle fünf Minuten an. Kannst du mal hingehen und nachsehen, was er für ein Problem hat?_where_",
             },
    4212 : { QUEST : "Ui! Ich bin froh, dass die Toontown-Zentrale endlich jemanden geschickt hat.\aIch habe seit Tagen keine Kundschaft mehr.\aEs sind diese nervigen Erbsenzähler überall.\aIch glaube, die bringen unseren Einwohnern eine schlechte Mundhygiene bei.\aVertreibe zehn von ihnen, dann wollen wir doch mal sehen, ob das Geschäft wieder läuft.",
             INCOMPLETE_PROGRESS : "Immer noch keine Kundschaft. Aber mach weiter!",
             },
    4213 : { QUEST : "Vielleicht waren es ja am Ende gar nicht die Erbsenzähler.\aVielleicht sind es die Monetomaten überhaupt.\aNimm dir mal zwanzig von ihnen vor, und dann kommt hoffentlich mal jemand wenigstens zur Kontrolle rein.",
             INCOMPLETE_PROGRESS : "Ich weiß, zwanzig sind eine ganze Menge. Aber ich bin sicher, dass es sich mit Zins und Zinseszins auszahlen wird.",
             },
    4214 : { GREETING : "",
             LEAVING : "",
             QUEST : "Ich verstehe das einfach nicht!\aImmer noch kein EINZIGER Patient!\aVielleicht müssen wir das Übel an der Wurzel anpacken.\aVersuche, ein Monetomaten-Bot-Gebäude zu erobern.\aDas dürfte funktionieren.",
             INCOMPLETE_PROGRESS : "Ach, bitte! Nur ein ganz kleines Gebäude ...",
             COMPLETE : "Immer noch kein Mensch hier.\aAber wenn ich es mir recht überlege ...\aIch hatte ja auch keine Kundschaft, bevor die Bots hier eingedrungen sind!\aIch bin dir für deine Hilfe wirklich dankbar.\aDas hier dürfte dir ein bisschen weiterhelfen."
             },

    4215 : { QUEST : "Anna braucht dringend HIlfe.\aGeh doch mal rüber und schau, was du tun kannst._where_",
             },
    4216 : { QUEST : "Danke, dass du so schnell gekommen bist!\aEs scheint so, als hätten sich die Bots mit ein paar Kreuzfahrttickets meiner Kunden davongemacht.\aYuki sagt, sie hätte ein Glückshändchen gesehen, der hier rauskam und in seinen Glückshändchen lauter Tickets hatte.\aSchau doch mal, ob du Holzmichels Fahrkarte für Alaska zurückholen kannst.",
             INCOMPLETE_PROGRESS : "Diese Glückshändchen können ja inzwischen sonstwo sein ...",
             },
    4217 : { QUEST : "Oh, großartig! Du hast es gefunden!\aJetzt sei so nett und flitz schnell zum Michel rüber, ja?_where_",
             },
    4218 : { QUEST : "Großer Goglmohsch!\aAlaska, ich komme!\aIch halte diese teuflischen Bots nicht mehr aus.\aDu, ich glaube, Anna braucht dich nochmal._where_",
             },
    4219 : { QUEST : "Jawoll, erraten.\aIch brauch dich, um diese vermaledeiten Glückshändchen nochmal zu filzen - wegen Tabithas Ticket zum Jazzfest.\aDu weißt ja jetzt, wie's geht ... ",
               INCOMPLETE_PROGRESS : "Irgendwo ist da noch mehr ... ",
             },
    4220 : { QUEST : "Süß!\aKönntest du das auch noch bei ihm abgeben? _where_",
             },
    4221 : { GREETING : "",
             LEAVING : "Bleib cool ...",
             QUEST : "Cool, Daddy!\aJetzt bin ich wieder voll dabei, _avName_.\aBevor du abhaust, solltest du nochmal bei Anna Banana reinschauen ..._where_",
             },
    4222 : { QUEST : "Das ist das letzte Mal, Ehrenwort!\aJetzt suchst du nach Grizzlys Ticket für den großen Gesangswettbewerb.",
             INCOMPLETE_PROGRESS : "Ach, komm schon, _avName_.\aGrizzly zählt auf dich.",
             },
    4223 : { QUEST : "Das dürfte ein Lächeln auf Grizzlys Gesicht zaubern._where_",
             },
    4224 : { GREETING : "",
             LEAVING : "",
             QUEST : "Hallo, Hallo, HALLO!\aKlasse!\aIch weiß, dass die Jungs und ich dieses Jahr groß abräumen werden.\aAnna sagt, du sollst vorbeikommen und deine Belohnung holen._where_\aWiedersehen, Wiedersehn, WIEDER-WIEDERSEHN!",
             COMPLETE : "Danke für deine große Hilfe, _avName_.\aDu bist wirklich ein Gewinn für Toontown.\aApropos Gewinn ...",
             },

    902 : { QUEST : "Geh mal zu Leo.\aEr braucht jemanden, der für ihn eine Nachricht überbringt._where_",
            },
    4903 : { QUEST : "Alter!\aMeine Kastagnetten sehen ganz matt aus und ich habe heute einen großen Auftritt.\aBring sie zu Carlos, der kann sie vielleicht aufpolieren._where_",
             },
    4904 : { QUEST : "Ja, isch glaubä isch kann dissä polieren.\aAbbär isch brauchä das blauä Tintä aus Tintänfischä.",
             GREETING : "Hola!",
             LEAVING : "Adios!",
             INCOMPLETE_PROGRESS : "Du kannst Tintänfischä findän, wo Angälstäg ist.",
             },
    4905 : { QUEST : "Ja! Dass gutt!\aNun ich brauchä biesschen Zeit für Polierän dissä.\aDu kannst gehän ein Einstockgebäudä übärnähmän, während isch arbeitä, gutt? ",
             GREETING : "Hola!",
             LEAVING : "Adios!",
             INCOMPLETE_PROGRESS : "Eino Momento ...",
             },
    4906 : { QUEST : "Särr gutt!\aHier sind Kastagnättän für Läo._where_",
             },
    4907 : { GREETING : "",
             QUEST : "Cool, Alter!\aDie sehen echt kastanig aus!\aJetzt musst du mal noch bei Hedy den Text von 'Beat nun ist Weihnachtszeit' für mich holen._where_",
             },
    4908 : { QUEST: "Tag!\aHmmm, ich hab das Lied grad nicht zur Hand.\aWenn du mir einen Moment Zeit gibst, notiere ich es aus dem Gedächtnis.\aDu könntest doch mal losgehen und ein zweistöckiges Gebäude eroberst, während ich schreibe!",
             },
    4909 : { QUEST : "Tut mir Leid.\aMein Gedächtnis lässt ein bisschen zu wünschen übrig.\aWenn du noch ein dreistöckiges Gebäude zurück eroberst, bin ich bestimmt fertig, wenn du zurückkommst ...",
             },
    4910 : { QUEST : "Fertig!\aTut mir Leid, dass es so lange gedauert hat.\aNimm das hier mit zu Leo._where_",
             GREETING : "",
             COMPLETE : "Klasse, Alter!\aMein Konzert wird dermaßen rocken, dass es alle umhaut!\aApropos umhauen, hiermit kannst du ein paar Bots umhauen ... "
             },
    5247 : { QUEST : "Diese Gegend ist schon ziemlich heftig ...\aVielleicht magst du ein paar neue Tricks lernen.\a_toNpcName_ hat mir alles Notwendige beigebracht; vielleicht kann er dir auch helfen._where_" },
    5248 : { GREETING : "Ahh, ja.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Du scheinst ein Problem mit meiner Anweisung zu haben?",
             QUEST : "Ahh, also willkommen, neuer Lehrling.\aIch weiß alles, was man über die Sache mit den Torten wissen muss.\aBevor wir aber mit deinem Training anfangen, ist eine kleine Demonstration vonnöten.\aGehe hinaus und erledige zehn von den größten Bots." },
    5249 : { GREETING: "Mmmmm.",
             QUEST : "Ausgezeichnet!\aNun beweise noch deine Fähigkeiten als Angler.\aIch habe gestern drei Fellwürfel in den Teich geworfen.\aFisch sie raus und bring sie mir. ",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Anscheinend stellst du dich mit Rute und Rolle nicht ganz so geschickt an." },
    5250 : { GREETING : "",
             LEAVING : "",
             QUEST : "Aha! Diese Würfel werden sich am Rückspiegel meines Ochsenkarrens gut machen!\aJetzt zeige mir doch noch, dass du deine Feinde unterscheiden kannst.\aKomm wieder her, wenn du zwei der größten Rechtomaten-Gebäude zurückgeholt hast.",
             INCOMPLETE_PROGRESS : "Gibt's Probleme mit den Gebäuden?", },
    5258 : { GREETING : "",
             LEAVING : "",
             QUEST : "Aha! Diese Würfel werden sich am Rückspiegel meines Ochsenkarrens gut machen!\aJetzt zeige mir doch noch, dass du deine Feinde unterscheiden kannst.\aKomm wieder her, wenn du zwei der größten Chefomaten-Gebäude zurückgeholt hast.",
             INCOMPLETE_PROGRESS : "Gibt's Probleme mit den Gebäuden?", },
    5259 : { GREETING : "",
             LEAVING : "",
             QUEST : "Aha! Diese Würfel werden sich am Rückspiegel meines Ochsenkarrens gut machen!\aJetzt zeige mir doch noch, dass du deine Feinde unterscheiden kannst.\aKomm wieder her, wenn du zwei der größten Monetomaten-Gebäude zurückgeholt hast.",
             INCOMPLETE_PROGRESS : "Gibt's Probleme mit den Gebäuden?", },
    5260 : { GREETING : "",
             LEAVING : "",
             QUEST : "Aha! Diese Würfel werden sich am Rückspiegel meines Ochsenkarrens gut machen!\aJetzt zeige mir doch noch, dass du deine Feinde unterscheiden kannst.\aKomm wieder her, wenn du zwei der größten Schachermaten-Gebäude zurückgeholt hast.",
             INCOMPLETE_PROGRESS : "Gibt's Probleme mit den Gebäuden?", },
    5200 : { QUEST : "Diese hinterlistigen Bots haben wieder zugeschlagen.\a_toNpcName_ hat noch einen verschwundenen Gegenstand gemeldet. Schau mal dort vorbei, ob du das regeln kannst._where_" },
    5201 : { GREETING: "",
             QUEST : "Hi, _avName_. Ich schätze, ich sollte dir für dein Kommen danken.\aEin paar von diesen Köpfchenjägern kamen hier rein und stahlen meinen Fußball.\aDer Anführer meinte zu mir, ich müsste ein paar Abstriche machen, und dann riss er ihn mir einfach aus der Hand!\aKannst du meinen Ball zurückholen?",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Na schon irgendein Erfolg bei der Suche nach meinem Fußball?",
             COMPLETE : "Jippieh! Du hast ihn gefunden! Hier, nimm deine Belohnung ...",
             },
    5261 : { GREETING: "",
             QUEST : "Hi, _avName_. Ich schätze, ich sollte dir für dein Kommen danken.\aEin paar von diesen Falschgesichtern kamen hier rein und stahlen meinen Fußball.\aDer Anführer meinte zu mir, ich müsste ein paar Abstriche machen, und dann riss er ihn mir einfach aus der Hand!\aKannst du meinen Ball zurückholen?",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Na schon irgendein Erfolg bei der Suche nach meinem Fußball?",
             COMPLETE : "Jippieh! Du hast ihn gefunden! Hier, nimm deine Belohnung ...",
             },
    5262 : { GREETING: "",
             QUEST : "Hi, _avName_. Ich schätze, ich sollte dir für dein Kommen danken.\aEin paar von diesen Geldsäcken kamen hier rein und stahlen meinen Fußball.\aDer Anführer meinte zu mir, ich müsste ein paar Abstriche machen, und dann riss er ihn mir einfach aus der Hand!\aKannst du meinen Ball zurückholen?",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Na schon irgendein Erfolg bei der Suche nach meinem Fußball?",
             COMPLETE : "Jippieh! Du hast ihn gefunden! Hier, nimm deine Belohnung ...",
             },
    5263 : { GREETING: "",
             QUEST : "Hi, _avName_. Ich schätze, ich sollte dir für dein Kommen danken.\aEin paar von diesen Schönrednern kamen hier rein und stahlen meinen Fußball.\aDer Anführer meinte zu mir, ich müsste ein paar Abstriche machen, und dann riss er ihn mir einfach aus der Hand!\aKannst du meinen Ball zurückholen?",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Na schon irgendein Erfolg bei der Suche nach meinem Fußball?",
             COMPLETE : "Jippieh! Du hast ihn gefunden! Hier, nimm deine Belohnung ...",
             },
    5202 : { QUEST : "Einige der härtesten Bots, die wir bisher kennengelernt haben, sind in Das Brrr eingefallen.\aDu solltest hier wahrscheinlich lieber ein paar mehr Gags bei dir tragen.\aIch habe gehört, dass _toNpcName_ vielleicht eine große Tasche hat, die du dafür verwenden kannst._where_" },
    5203 : { GREETING: "Hä? Bist du von meiner Schlittenmannschaft?",
             QUEST : "Was ist los? Du willst eine Tasche?\aIch hatte hier irgendwo eine ... vielleicht ist sie in meinem Schlitten?\aNur ... ich hab meinen Schlitten seit dem großen Rennen nicht mehr gesehen!\aVielleicht hat ihn einer von diesen Bots mitgenommen?",
             LEAVING : "Hast du meinen Schlitten gesehen?",
             INCOMPLETE_PROGRESS : "Wer bist du nochmal? Tut mir Leid, ich bin noch etwas wirr im Kopf von dem Zusammenstoß." },
    5204 : { GREETING : "",
             LEAVING : "",
             QUEST : "Ist das mein Schlitten? Ich seh hier keine Tasche.\aIch glaube, Huckelberry Schlitzauge war in der Mannschaft ... vielleicht hat er sie?_where_" },
    5205 : { GREETING : "Ooooh, mein Kopf!",
             LEAVING : "",
             QUEST : "Hä? Schorsch wer? Eine Tasche?\aOh, vielleicht war er in unserer Schlittenmannschaft?\aMein Kopf tut so weh, dass ich nicht klar denken kann..\aKönntest du aus dem zugefrorenen Teich ein paar Eiswürfel für meinen Kopf fischen?",
             INCOMPLETE_PROGRESS : "Auuu, mein Kopf bringt mich noch um! Hast du Eis?", },
    5206 : { GREETING : "",
             LEAVING : "",
             QUEST : "Ahhh, das ist schon viel besser!\aDu suchst also nach Schorschs Tasche, hm?\aIch glaube, die ist nach dem Zusammenstoß auf Halbaffen-Sams Kopf gelandet._where_" },
    5207 : { GREETING : "Iiiiiip!",
             LEAVING : "",
             QUEST : "Was Tasche? Wer Hockelberry?\aIch Angst vor Gebäude! Du hauen Gebäude, ich geben dir Tasche!",
             INCOMPLETE_PROGRESS : "Mehr Gebäude! Ich noch Angst!",
             COMPLETE : "Ooooh! Ich haben dich gern!" },
    5208 : { GREETING : "",
             LEAVING : "Iiiiik!",
             QUEST : "Ooooh! Ich haben dich gern!\aGehen zu Schiklinik. Tasche dort." },
    5209 : { GREETING : "Alter!",
             LEAVING : "Bis später!",
             QUEST : "Mann, dieser Halbaffen-Sam ist vielleicht verrückt!\aWenn du nur halb so verrückt bist wie Sam, geb ich dir die Tasche, Mann.\aHau mal paar Bots für deine Tasche in die Tasche, Mann! Na los!",
             INCOMPLETE_PROGRESS : "Bist du sicher, dass das extrem genug war? Hau noch ein paar Bots in die Tasche.",
             COMPLETE : "He, du bist ja ganz schön verrückt! Das war vielleicht ein Haufen Bots, die du da eingetütet hast!\aHier ist deine Tasche!" },

    5210 : { QUEST : "_toNpcName_ ist heimlich in jemanden aus der Nachbarschaft verliebt.\aWenn du ihr hilfst, bekommst du vielleicht eine hübsche Belohnung._where_" },
    5211 : { GREETING: "Huu-huuu.",
             QUEST : "Ich hab die ganze letzte Nacht einen Brief an den Burschen, den ich liebe, geschrieben.\aDoch bevor ich ihn hinbringen konnte, kam einer dieser hässlichen Bots mit Schnabel und nahm ihn weg.\aKannst du ihn für mich zurückholen?",
             LEAVING : "Huu-huuu.",
             INCOMPLETE_PROGRESS : "Bitte finde meinen Brief." },

    5264 : { GREETING: "Huu-huuu.",
             QUEST : "Ich hab die ganze letzte Nacht einen Brief an den Burschen, den ich liebe, geschrieben.\aDoch bevor ich ihn hinbringen konnte, kam einer dieser hässlichen Bots mit Flosse und nahm ihn weg.\aKannst du ihn für mich zurückholen?",
             LEAVING : "Huu-huuu.",
             INCOMPLETE_PROGRESS : "Bitte finde meinen Brief." },
    5265 : { GREETING: "Huu-huuu",
             QUEST : "Ich hab die ganze letzte Nacht einen Brief an den Burschen, den ich liebe, geschrieben.\aDoch bevor ich ihn hinbringen konnte, kam einer dieser hässlichen Einmischer-Bots und nahm ihn weg.\aKannst du ihn für mich zurückholen?",
             LEAVING : "Huu-huuu.",
             INCOMPLETE_PROGRESS : "Bitte finde meinen Brief." },
    5266 : { GREETING: "Huu-huuu.",
             QUEST : "Ich hab die ganze letzte Nacht einen Brief an den Burschen, den ich liebe, geschrieben.\aDoch bevor ich ihn hinbringen konnte, kam einer dieser hässlichen Unternehmensräuber mit Schnabel und nahm ihn weg.\aKannst du ihn für mich zurückholen?",
             LEAVING : "Huu-huuu.",
             INCOMPLETE_PROGRESS : "Bitte finde meinen Brief." },
    5212 : { QUEST : "Oh, danke, dass du meinen Brief gefunden hast!\aBitte, bitte, bitte, könntest du ihn zum hübschesten Burschen der Gegend bringen?",
             GREETING : "",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Du hast meinen Brief noch nicht abgegeben, oder?",
             },
    5213 : { GREETING : "Entzückend, natürlich.",
             QUEST : "Ich hab jetzt keinen Nerv für deinen Brief.\aMir hat jemand all meine Hündchen weggenommen!\aWenn du sie zurückbringst, können wir nochmal drüber reden.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Meine armen kleinen Hündchen!" },
    5214 : { GREETING : "",
             LEAVING : "Tudelu!",
             QUEST : "Danke, dass du meine kleinen Schönen zurückgebracht hast.\aDann wollen wir uns mal deinen Brief ansehen ... \a Mmmm, es scheint, als hätte ich noch eine heimliche Verehrerin.\aDa ist wohl ein Besuch bei meinem lieben Freund Karl angesagt.\aIch bin sicher, du wirst ihn unheimlich mögen._where_" },
    5215 : { GREETING : "Hehe ...",
             LEAVING : "Komm wieder, jaja.",
             INCOMPLETE_PROGRESS : "Da sind immer noch ein paar Große unterwegs. Komm zu uns zurück, wenn die weg sind.",
             QUEST : "Wer hat dich zu uns geschickt? Wir mögen Schnautzies nicht besonders, nein, nein ...\aAber wir tun Bots noch weniger mögen ...\aTu du die Großen vertreiben und wir helfen dir, ja, ja." },
    5216 : { QUEST : "Wir haben dir ja gesagt, dass wir dir helfen tun.\aAlso tu diesen Ring zu dem Mädel bringen.",
             GREETING : "",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Du tust diesen Ring immer noch haben???",
             COMPLETE : "Oh Liiiiebling!!! Danke!!!\aOh, und ich habe auch etwas Besonderes für dich.",
             },
    5217 : { QUEST : "Es klingt, als könnte _toNpcName_ Hilfe gebrauchen._where_" },
    5218 : { GREETING : "",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Ich bin sicher, dass da irgendwo noch mehr Einmischer unterwegs sind.",
             QUEST : "Hilfe!!! Hilfe!!! Ich kann nicht mehr!\aDiese Einmischer machen mich wahnsinnig!!!" },
    5219 : { GREETING : "",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Das können nicht alle gewesen sein. Ich habe gerade einen gesehen!!!",
             QUEST : "Oh, danke, aber jetzt sind es die Unternehmensräuber!!!\aDu musst mir helfen!!!" },
    5220 : { GREETING : "",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Nein, nein, nein, es war grad einer hier!",
             QUEST : "Ich merke jetzt, dass es diese Kredithaie sind!!!\aIch dachte, du wolltest mich retten!!!" },
    5221 : { GREETING : "",
             LEAVING : "",
             QUEST : "Weißt du was, vielleicht sind es gar nicht die Bots!\aKönntest du Fanny bitten, mir einen Beruhigungstrank zu mixen? Vielleicht hilft das ... _where_" },
    5222 : { LEAVING : "",
             QUEST : "Oh, dieser Harry, der ist schon ein Spaßvogel!\aIch mix was zusammen, das ihm hilft!\aOh, anscheinend habe ich keinen Stein des Weisen mehr...\aSei so lieb, lauf runter zum Teich und hol mir was.",
             INCOMPLETE_PROGRESS : "Hast du schon einen Stein des Weisen für mich?", },
    5223 : { QUEST : "Okay. Danke, Schatz.\aHier, bring das zu Harry. Das dürfte ihn voll beruhigen.",
             GREETING : "",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Nun geh schon, bring den Trank zu Harry.",
             },
    5224 : { GREETING : "",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Los, schnapp dir diese Prozessgeier für mich, ja?",
             QUEST : "Oh, Gott sei dank Du bist zurück!\aGib mir den Trank, schnell!!!\aGluckgluckgluck ...\aScheußlich!\aAber weißt du was? Ich bin schon viel ruhiger. Jetzt, da ich klar denken kann, merke ich ...\aEs waren die Prozessgeier, die mich die ganze Zeit verrückt gemacht haben!",
             COMPLETE : "Jungejunge! Jetzt kann ich mich entspannen!\aIch bin sicher, dass es hier irgend etwas gibt, was ich dir geben kann. Oh, nimm das!" },
    5225 : { QUEST : "Seit dem Vorfall mit dem Rübenbrot ist Phil Mürrisch stinksauer auf _toNpcName_.\aVielleicht kannst du Gert helfen, die Sache zwischen ihnen ins Lot zu bringen?_where_" },
    5226 : { QUEST : "Ja, du hast ja vielleicht gehört, dass Phil Mürrisch stinkesauer auf mich ist...\aIch wollte ja nur nett sein mit dem Rübenbrot.\aVielleicht kannst du mir helfen, ihn aufzumuntern.\aPhil hasst diese Monetomaten-Bots, besonders ihre Gebäude.\aWenn du ein paar Monetomaten-Gebäude zurückholst, hilft das vielleicht.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Vielleicht noch ein paar Gebäude?", },
    5227 : { QUEST : "Das ist unglaublich! Geh zu Phil und erzähle ihm, was du getan hast._where_" },
    5228 : { QUEST : "Ach, das hat er getan, ja?\aDieser Gert denkt wohl, er kommt so einfach davon, was?\aIch hab mir ja nur einen Zahn abgebrochen an seinem blöden Rübenbrot!\aVielleicht könntest du meinen Zahn zu Dr. Mummelgesicht bringen, damit der ihn wieder hinkriegt.",
             GREETING : "Mmmmrrrfff.",
             LEAVING : "Grummelgrummel.",
             INCOMPLETE_PROGRESS : "Du schon wieder? Ich dachte, du wolltest meinen Zahn reparieren lassen.",
             },
    5229 : { GREETING : "",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Ich arbeite noch an dem Zahn. Es dauert noch etwas.",
             QUEST : "Ja, dieser Zahn sieht wirklich ziemlich bös aus, hihi.\aVielleicht kann ich ja was machen, aber das wird etwas dauern.\aVielleicht kannst du ja währenddessen ein paar von diesen Monetomaten-Bots von der Straße räumen?\aDie verschrecken meine Kundschaft." },
    5267 : { GREETING : "",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Ich arbeite noch an dem Zahn. Es dauert noch etwas.",
             QUEST : "Ja, dieser Zahn sieht wirklich ziemlich bös aus, hihi.\aVielleicht kann ich ja was machen, aber das wird etwas dauern.\aVielleicht kannst du ja währenddessen ein paar von diesen Schachermaten-Bots von der Straße räumen?\aDie verschrecken meine Kundschaft." },
    5268 : { GREETING : "",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Ich arbeite noch an dem Zahn. Es dauert noch etwas.",
             QUEST : "Ja, dieser Zahn sieht wirklich ziemlich bös aus, hihi.\aVielleicht kann ich ja was machen, aber das wird etwas dauern.\aVielleicht kannst du ja währenddessen ein paar von diesen Rechtomaten-Bots von der Straße räumen?\aDie verschrecken meine Kundschaft." },
    5269 : { GREETING : "",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Ich arbeite noch an dem Zahn. Es dauert noch etwas.",
             QUEST : "Ja, dieser Zahn sieht wirklich ziemlich bös aus.\aVielleicht kann ich ja was machen, aber das wird etwas dauern.\aVielleicht kannst du ja währenddessen ein paar von diesen Chefomaten-Bots von der Straße räumen?\aDie verschrecken meine Kundschaft." },
    5230 : { GREETING: "",
             QUEST : "Ich bin froh, dass du wieder da bist!\aIch hab es aufgegeben, diesen alten Zahn zu reparieren, und habe Phil dafür einen neuen Goldzahn gemacht.\aLeider kam ein Ausbeuter herein und nahm in mir ab.\aDu holst ihn vielleicht noch ein, wenn du dich beeilst.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Hast du den Zahn schon gefunden?" },
    5270 : { GREETING: "",
             QUEST : "Ich bin froh, dass du wieder da bist!\aIch hab es aufgegeben, diesen alten Zahn zu reparieren, und habe Phil dafür einen neuen Goldzahn gemacht.\aLeider kam ein Großhirn herein und nahm in mir ab.\aDu holst es vielleicht noch ein, wenn du dich beeilst.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Hast du den Zahn schon gefunden?" },
    5271 : { GREETING: "",
             QUEST : "Ich bin froh, dass du wieder da bist!\aIch hab es aufgegeben, diesen alten Zahn zu reparieren, und habe Phil dafür einen neuen Goldzahn gemacht.\aLeider kam Mr. Hollywood herein und nahm in mir ab.\aDu holst ihn vielleicht noch ein, wenn du dich beeilst.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Hast du den Zahn schon gefunden?" },
    5272 : { GREETING: "",
             QUEST : "Ich bin froh, dass du wieder da bist!\aIch hab es aufgegeben, diesen alten Zahn zu reparieren, und habe Phil dafür einen neuen Goldzahn gemacht.\aLeider kam ein Großkotz herein und nahm in mir ab.\aDu holst ihn vielleicht noch ein, wenn du dich beeilst.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Hast du den Zahn schon gefunden?" },
    5231 : { QUEST : "Großartig, das ist der Zahn, hihi!\aBring ihn doch für mich zu Phil rüber, ja?",
             GREETING : "",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Ich wette, Phil möchte seinen neuen Zahn sehen.",
             },
    5232 : { QUEST : "Oh, danke.\aMmmrrrfff.\aWie sieht das aus, hm?\aOkay, du kannst Gert sagen, dass ich ihm verzeihe.",
             LEAVING : "",
             GREETING : "", },
    5233 : { QUEST : "Oh, das freut mich zu hören.\aIch dachte mir schon, dass der alte Phil nicht ewig auf mich sauer sein kann.\aAls Geste des guten Willens hab ich ihm dieses Kiefernzapfenbrot gebacken.\aKönntest du es zu ihm rüberbringen?",
             GREETING : "",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Mach lieber schnell. Kiefernzapfenbrot ist besser, wenn es noch warm ist.",
             COMPLETE : "Oh, was ist das denn? Für mich?\aMampf-mampf...\aAuuuu! Mein Zahn! Dieser Gert Gänsburger!\aNaja, ist ja nicht deine Schuld. Hier, du kannst das für deine Mühe haben.",
             },
    903 : { QUEST : "Du bist jetzt vielleicht soweit, _toNpcName_ den Schnee-Weisen wegen deiner Abschlussprüfung aufzusuchen._where_", },
    5234 : { GREETING: "",
             QUEST : "Aha, da bist du ja wieder.\aBevor wir anfangen, müssen wir was essen.\aBring uns etwas Krümelkäse für unsere Brühe.\aKrümelkäse kann man nur von Großhirn-Bots holen.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Wir brauchen immer noch Krümelkäse. " },
    5278 : { GREETING: "",
             QUEST : "Aha, da bist du ja wieder.\aBevor wir anfangen, müssen wir was essen.\aBring uns etwas Kaviar für unsere Brühe.\aKaviar kann man nur von Mr.-Hollywood-Bots holen.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Wir brauchen immer noch Kaviar." },
    5235 : { GREETING: "",
             QUEST : "Ein einfacher Mann isst mit einem einfachen Löffel.\aEin Bot hat mir meinen einfachen Löffel weggenommen, also kann ich nicht essen.\aBring mir meinen Löffel wieder. Ich glaube, ein Ausbeuter hat ihn weggenommen.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Ich muss einfach meinen Löffel haben." },
    5279 : { GREETING: "",
             QUEST : "Ein einfacher Mann isst mit einem einfachen Löffel.\aEin Bot hat mir meinen einfachen Löffel weggenommen, also kann ich nicht essen.\aBring mir meinen Löffel wieder. Ich glaube, ein Großkotz hat ihn weggenommen.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Ich muss einfach meinen Löffel haben." },
    5236 : { GREETING: "",
             QUEST : "Vielen Dank.\aSchlürf-schlürf...\aAhhh, nun musst du eine sprechende Kröte einfangen. Versuche mal, im Teich zu fischen.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Wo ist die sprechende Kröte?" },

    5237 : {  GREETING : "",
              LEAVING : "",
              INCOMPLETE_PROGRESS : "Du hast noch keinen Nachtisch geholt.",
              QUEST : "Oh, das ist tatsächlich eine sprechende Kröte. Gib sie mir mal.\aWas sagst du da, Kröte?\aAha.\aAha...\aDie Kröte hat gesprochen. Wir brauchen Nachtisch.\aBring uns ein paar Eistüten von _toNpcName_.\aDie Kröte möchte aus irgendwelchen Gründen Eistüten mit Rote-Bohnen-Geschmack._where_", },
    5238 : { GREETING: "",
             QUEST : "Der Weise hat dich also geschickt. Es tut mir Leid, aber wir haben seit kurzem keine Eistüten mit Rote-Bohnen-Geschmack mehr.\aWeißt du, ein paar Bots kamen rein und nahmen alle mit.\aSie sagten, sie wären für Mr. Hollywood, oder irgend so einen Quatsch.\aIch wäre sehr froh, wenn du sie mir zurückholen könntest.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Hast du schon alle meine Eistüten gefunden?" },
    5280 : { GREETING: "",
             QUEST : "Der Weise hat dich also geschickt. Es tut mir Leid, aber wir haben seit kurzem keine Eistüten mit Rote-Bohnen-Geschmack mehr.\aWeißt du, ein paar Bots kamen rein und nahmen alles mit.\aSie sagten, sie wären für das Großhirn, oder irgend so einen Quatsch.\aIch wäre sehr froh, wenn du sie mir zurückholen könntest.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Hast du schon alle meine Eistüten gefunden?" },
    5239 : { QUEST : "Danke, dass du meine Eistüten zurückgebracht hast!\aHier ist eine für Lil Altmann.",
             GREETING : "",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Bring das Eis lieber zu Lil Altmann, bevor es schmilzt.", },
    5240 : { GREETING: "",
             QUEST : "Sehr gut. Hier, für dich, Kröte ...\aSchlürf-schlürf ...\aOkay, jetzt sind wir fast fertig.\aWenn du mir nur noch etwas Puder bringen könntest, um meine Hände zu trocknen.\aIch denke, dass diese Großkotze manchmal Puder von ihren Perücken haben könnten.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Hast du Puder gefunden?" },
    5281 : { GREETING: "",
             QUEST : "Sehr gut. Hier, für dich, Kröte ...\aSchlürf-schlürf ...\aOkay, jetzt sind wir fast fertig.\aWenn du mir nur noch etwas Puder bringen könntest, um meine Hände zu trocknen.\aIch denke, dass diese Mr.-Hollywood-Bots manchmal Puder für ihre Nasen dabei haben.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Hast du Puder gefunden?" },
    5241 : { QUEST : "Okay.\aWie ich einmal sagte, um wirklich eine Torte zu werfen, darf man nicht mit der Hand werfen ...\a... sondern mit der Seele.\aIch weiß nicht, was das bedeutet, und deshalb werde ich hier sitzen und darüber nachdenken, während du Gebäude zurück eroberst.\aKomm wieder her, wenn du deine Aufgabe abgeschlossen hast.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Deine Aufgabe ist noch nicht abgeschlossen.", },
    5242 : { GREETING: "",
             QUEST : "Obgleich ich immer noch nicht weiß, wovon ich rede, bist du wahrhaft würdig.\aIch gebe dir eine letzte Aufgabe ...\aDie sprechende Kröte ist ein Er und sucht eine Freundin.\aFinde ein weitere sprechende Kröte. Die Kröte hat gesprochen.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Wo ist die andere sprechende Kröte?",
             COMPLETE : "Hui! Ich bin müde von all diesen Anstrengungen. Ich muss jetzt ruhen.\aHier, nimm deine Belohnung und hebe dich hinweg." },

    5243 : { QUEST : "Schwitze-Peter fängt schon an, die ganze Straße hinauf zu stinken.\aKannst du ihn vielleicht überreden, mal zu duschen oder so?_where_" },
    5244 : { GREETING: "",
             QUEST : "Ja, ich komm hier drin anscheinend ganz schön ins Schwitzen.\aMmmm, wenn ich vielleicht das undichte Rohr in meiner Dusche reparieren könnte ...\aIch glaube, ein Zahnrad von einem dieser winzigen Bots könnte helfen.\aGeh los und suche ein Zahnrad von einem Mikromanager, dann versuchen wir's.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Wo ist das Zahnrad, das du holen wolltest?" },
    5245 : { GREETING: "",
             QUEST : "Jau, das scheint zu funktionieren.\aAber ich fühle mich so allein, wenn ich dusche ...\aKönntest du mir vielleicht ein Quietschentchen fischen gehen, damit es mir Gesellschaft leistet?",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Kein Talentchen für das Entchen?" },
    5246 : { QUEST : "Das Entchen ist toll, aber ...\aDiese ganzen Gebäude hier machen mich nervös.\aIch wäre viel entspannter, wenn es weniger Gebäude gäbe.",
             LEAVING : "",
             COMPLETE : "Okay, ich dusch mich jetzt mal. Und hier ist auch was für dich.",
             INCOMPLETE_PROGRESS : "Ich hab immer noch ein Problem mit Gebäuden.", },
    5251 : { QUEST : "Ladewig Mädelsturm soll heute Abend auftreten.\aIch habe gehört, dass er irgendein Problem mit seinem Equipment hat._where_" },
    5252 : { GREETING: "",
             QUEST : "Oh yeah! Ich kann Hilfe gut gebrauchen.\aDiese Bots kamen rein und klauten mein ganzes Zeug, als ich den Transporter auslud.\aKannst du mir helfen und mein Mikrofon zurückholen?",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "He Mann, ich kann ohne mein Mikro nicht singen!" },
    5253 : { GREETING: "",
             QUEST : "Yeah, das ist mein Mikrofon.\aDanke, dass du es besorgt hast, aber...\aIch brauch echt noch mein Keyboard, um in die Tasten zu hauen.\aIch glaube, einer von diesen Unternehmensräubern hat mein Keyboard.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Noch keinen Erfolg mit meinem Keyboard?" },
    5273 : { GREETING: "",
             QUEST : "Yeah, das ist mein Mikrofon.\aDanke, dass du es besorgt hast, aber...\aIch brauch echt noch mein Keyboard, um in die Tasten zu hauen.\aIch glaube, einer von diesen Einmischern hat mein Keyboard.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Noch keinen Erfolg mit meinem Keyboard?" },
    5274 : { GREETING: "",
             QUEST : "Yeah, das ist mein Mikrofon.\aDanke, dass du es besorgt hast, aber...\aIch brauch echt noch mein Keyboard, um in die Tasten zu hauen.\aIch glaube, einer von diesen Kredithaien hat mein Keyboard.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Noch keinen Erfolg mit meinem Keyboard?" },
    5275 : { GREETING: "",
             QUEST : "Yeah, das ist mein Mikrofon.\aDanke, dass du es besorgt hast, aber...\aIch brauch echt noch mein Keyboard, um in die Tasten zu hauen.\aIch glaube, einer von diesen Prozessgeiern hat mein Keyboard.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Noch keinen Erfolg mit meinem Keyboard?" },
    5254 : { GREETING: "",
             QUEST : "Okay! Jetzt bin ich wieder voll dabei.\aWenn die nur nicht meine Plateauschuhe mitgenommen hätten ...\aDiese Schuhe sind wahrscheinlich bei einem Mr. Hollywood gelandet, wenn du mich fragst.",
             LEAVING : "",
             COMPLETE : "Okay! Jetzt geht's los.\aHallo Brrr!!!\aHä? Wo sind die denn alle?\aOkay, nimm das hier und trommle ein paar Fans für mich zusammen, ja?",
             INCOMPLETE_PROGRESS : "Ich kann ja wohl nicht barfuß auftreten, oder!?" },
    5282 : { GREETING: "",
             QUEST : "Okay! Jetzt bin ich wieder voll dabei.\aWenn die nur nicht meine Plateauschuhe mitgenommen hätten ...\aDiese Schuhe sind wahrscheinlich bei einem Großhirn gelandet, wenn du mich fragst.",
             LEAVING : "",
             COMPLETE : "Okay!! Jetzt geht's los.\aHallo Brrr!!!\aHä? Wo sind die denn alle?\aOkay, nimm das hier und trommle ein paar Fans für mich zusammen, ja?",
             INCOMPLETE_PROGRESS : "Ich kann ja wohl nicht barfuß auftreten, oder!?" },
    5283 : { GREETING: "",
             QUEST : "Okay! Jetzt bin ich wieder voll dabei.\aWenn die nur nicht meine Plateauschuhe mitgenommen hätten ...\aDiese Schuhe sind wahrscheinlich bei einem Ausbeuter gelandet, wenn du mich fragst.",
             LEAVING : "",
             COMPLETE : "Okay!! Jetzt geht's los.\aHallo Brrr!!!\aHä? Wo sind die denn alle?\aOkay, nimm das hier und trommle ein paar Fans für mich zusammen, ja?",
             INCOMPLETE_PROGRESS : "Ich kann ja wohl nicht barfuß auftreten, oder!?" },
    5284 : { GREETING: "",
             QUEST : "Okay! Jetzt bin ich wieder voll dabei.\aWenn die nur nicht meine Plateauschuhe mitgenommen hätten ...\aDiese Schuhe sind wahrscheinlich bei einem Großkotz gelandet, wenn du mich fragst.",
             LEAVING : "",
             COMPLETE : "Okay!! Jetzt geht's los.\aHallo Brrr!!!\aHä? Wo sind die denn alle?\aOkay, nimm das hier und trommle ein paar Fans für mich zusammen, ja?",
             INCOMPLETE_PROGRESS : "Ich kann ja wohl nicht barfuß auftreten, oder!?" },

    5255 : { QUEST : "Du siehst aus, als könntest du mehr Lach-Punkte gebrauchen.\aVielleicht macht dir _toNpcName_ ein gutes Angebot.\aLass es dir aber schriftlich geben ..._where_" },
    5256 : { GREETING : "",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Abgemacht ist abgemacht.",
             QUEST : "Du brauchst also Lach-Punkte, was?\aKlar hab ich'n Deal für dich!\aKümmere dich einfach für mich um ein paar Chefomaten-Bots ...\aUnd ich sorge dafür, dass es sich für dich lohnt." },
    5276 : { GREETING : "",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Abgemacht ist abgemacht.",
             QUEST : "Du brauchst also Lach-Punkte, was?\aKlar hab ich'n Deal für dich!\aKümmere dich einfach für mich um ein paar Rechtomaten-Bots ...\aUnd ich sorge dafür, dass es sich für dich lohnt." },
    5257 : { GREETING : "",
             LEAVING : "",
             COMPLETE : "Okay, aber ich bin mir sicher, dass ich dir gesagt hatte, du sollst ein paar Rechtomaten-Bots zusammentreiben.\aTja, wenn du das sagst, aber du hast dich nicht dran gehalten. ",
             INCOMPLETE_PROGRESS : "Ich glaube nicht, dass du fertig bist.",
             QUEST : "Du sagst, du bist fertig? Alle Bots vertrieben?\aDu hast da was falsch verstanden. Unsere Abmachung galt für Schachermaten-Bots.\aIch bin sicher, dass ich gesagt habe, du sollst ein paar Schachermaten-Bots für mich vertreiben." },
    5277 : { GREETING : "",
             LEAVING : "",
             COMPLETE : "Okay, aber ich bin mir sicher, dass ich dir gesagt hatte, du sollst ein paar Rechtomaten-Bots zusammentreiben.\aTja, wenn du das sagst, aber du hast dich nicht dran gehalten.",
             INCOMPLETE_PROGRESS : "Ich glaube nicht, dass du fertig bist.",
             QUEST : "Du sagst, du bist fertig? Alle Bots vertrieben?\aDu hast da was falsch verstanden. Unsere Abmachung galt für Monetomaten-Bots.\aIch bin sicher, dass ich gesagt habe, du sollst ein paar Monetomaten-Bots für mich vertreiben." },
    }

# ChatGarbler.py
ChatGarblerDog = ["wuff", "blaff", "rrr-wuff"]
ChatGarblerCat = ["miau", "muh"]
ChatGarblerMouse = ["quiek", "pieps", "quiekquiek"]
ChatGarblerHorse = ["wieher", "brrr"]
ChatGarblerRabbit = ["iiik", "schnuff", "schnuffschnuff", "trommel"]
ChatGarblerFowl = ["quak", "schnatter", "quakquak"]
ChatGarblerDefault = ["blah"]

# AvatarDNA.py
Bossbot = "Chefomat"
Lawbot = "Rechtomat"
Cashbot = "Monetomat"
Sellbot = "Schachermat"
BossbotS = "ein Chefomat"
LawbotS = "ein Rechtomat"
CashbotS = "ein Monetomat"
SellbotS = "ein Schachermat"
BossbotP = "Chefomaten"
LawbotP = "Rechtomaten"
CashbotP = "Monetomaten"
SellbotP = "Schachermaten"
BossbotSkelS = "ein Chefomat Skeletobot"
LawbotSkelS = "ein Rechtomat Skeletobot"
CashbotSkelS = "ein Monetomat Skeletobot"
SellbotSkelS = "ein Schachermat Skeletobot"
BossbotSkelP = "Chefomat Skeletobots"
LawbotSkelP = "Rechtomat Skeletobots"
CashbotSkelP = "Monetomat Skeletobots"
SellbotSkelP = "Schachermat Skeletobots"

# AvatarDetailPanel.py
AvatarDetailPanelOK = lOK
AvatarDetailPanelCancel = lCancel
AvatarDetailPanelClose = lClose
AvatarDetailPanelLookup = "Details zu %s werden gesucht."
AvatarDetailPanelFailedLookup = "Kann keine Deteils zu %s finden."
AvatarDetailPanelOnline = "Bezirk: %(district)s\nLocation: %(location)s"
AvatarDetailPanelOffline = "Bezirk: offline\nOrt: offline"

# AvatarPanel.py
AvatarPanelFriends = "Freunde"
AvatarPanelWhisper = "Flüstern"
AvatarPanelSecrets = "Geheimnisse"
AvatarPanelGoTo = "Gehe zu"
AvatarPanelIgnore = "Ignorieren"
#AvatarPanelCogDetail = "Dept: %s\nLevel: %s\n"
AvatarPanelCogLevel = "Level: %s"
AvatarPanelCogDetailClose = lClose

# DistributedAvatar.py
WhisperNoLongerFriend = "%s hat deine Freunde-Liste verlassen"
WhisperNowSpecialFriend = "%s ist jetzt dein geheimer Freund!"
WhisperComingToVisit = "%s kommt dich besuchen."
WhisperFailedVisit = "%s hat versucht dich zu besuchen."
WhisperTargetLeftVisit = "%s ist woanders hin gegangen. Versuch's nochmal!"
WhisperGiveupVisit = "%s konnte dich nicht finden, weil du dich herumtreibst!"
WhisperIgnored = "%s ignoriert dich!"
TeleportGreeting = "Hi, %s."
DialogSpecial = "ooo"
DialogExclamation = "!"
DialogQuestion = "?"
# Cutoff string lengths to determine how much barking to play
DialogLength1 = 6
DialogLength2 = 12
DialogLength3 = 20

# LocalAvatar.py
FriendsListLabel = "Freunde"
WhisperFriendComingOnline = "%s ist jetzt online!"
WhisperFriendLoggedOut = "%s hat sich abgemeldet."

# TeleportPanel.py
TeleportPanelOK = lOK
TeleportPanelCancel = lCancel
TeleportPanelYes = lYes
TeleportPanelNo = lNo
TeleportPanelCheckAvailability = "Versuche zu %s zu gehen."
TeleportPanelNotAvailable = "%s ist gerade beschäftigt, versuche es später noch einmal."
TeleportPanelIgnored = "%s ignoriert dich."
TeleportPanelNotOnline = "%s ist zur Zeit nicht online."
TeleportPanelWentAway = "%s ist weggegangen."
TeleportPanelUnknownHood = "Du weißt nicht, wie du zu %s kommst! "
TeleportPanelUnavailableHood = "%s ist zur Zeit nicht erreichbar, versuche es später noch einmal."
TeleportPanelDenySelf = "Du kannst nicht zu dir selbst gehen!"
TeleportPanelOtherShard = "%(avName)s ist im Bezirk %(shardName)s, und du bist im Bezirk %(myShardName)s. Möchtest du nach %(shardName)s wechseln?"

# DistributedBattleBldg.py
BattleBldgBossTaunt = "Ich bin der Chef."

# DistributedBattleFactory.py
FactoryBossTaunt = "Ich bin der Vorarbeiter."
FactoryBossBattleTaunt = "Ich möchte dich mit dem Vorarbeiter bekannt machen."

# HealJokes.py
ToonHealJokes = [
    ["Was hängt an der Wand und macht TICK-TOCK-TICK-TOCK-TICK-TOCK ...?",
     "Eine Spinne mit Stöckelschuhen. "],
    ["Was steht im Wald und macht Muh?",
     "Ein Hirsch, der Fremdspachen lernt."],
    ["Warum kann ein Gespenst schlecht lügen?",
     "Weil man es so gut durchschauen kann."],
    ["Wie kommt eine Ameise über den Fluss?",
     "Sie nimmt das A weg und fliegt rüber."],
    ["Welcher Vogel ist meistens traurig?",
     "Der Pechvogel."],
    ["Wo schmeckt der Apfelsaft am besten?",
     "Beim Trinken."],
    ["Was hat ein Mensch noch nie erzählt?",
     "Dass er gestorben ist."],
    ["Warum leben Eskimos länger?",
     "Weil sie nicht ins Gras beißen können."],
    ["Was spielen sportliche Schafe?",
     "Wolle-Ball."],
    ["Welche Biere schäumen am meisten?",
     "Die Bar-Biere."],
    ["Warum ging das Gerippe nicht über die Straße?",
     "Weil es nicht den Nerv dazu hatte."],
    ["Wie heißt das Reh mit Vornamen?",
     "Kartoffelpü."],
    ["Was ist grau und spritzt mit Marmelade?",
     "Eine Maus, die einen Pfannkuchen frisst."],
    ["In welchem Fall ist zwei mal zwei sechs?",
     "In gar keinem Fall."],
    ["Was kann man von einem Dreieck verwenden?",
     "Das Ei, der Rest ist Dreck!"],
    ["Wer hat es besser, der Kaffee oder der Tee?",
     "Der Kaffee; er darf sich setzen, der Tee muss ziehen."],
    ["Wie konnten die Leute im Mittelalter ohne Fernseher überleben?",
     "Gar nicht, sie leben ja nicht mehr."],
    ["Was passiert, wenn man einen weißen Hut ins Rote Meer taucht?",
     "Er wird nass."],
    ["Welche Zeiten sind die schönsten?",
     "Die Mahlzeiten."],
    ["Welches Spiel soll man immer anderen geben?",
     "Das Beispiel."],
    ["Was kann man nicht zum Frühstück essen?",
     "Mittag und Abendbrot."],
    ["Was gibt man einem Elefanten mit großen Füßen?",
     "Große Schuhe."],
    ["Was macht man, wenn man tiefer schlafen will?",
     "Man sägt die Beine vom Bett ab."],
    ["Welcher Satz hat keine Wörter?",
     "Der Kaffeesatz."],
    ["Was ergibt drei mal sieben?",
     "Feinen Sand."],
    ["Welchen Hang sollte man nicht hochsteigen?",
     "Den Vorhang."],
    ["Warum sind die Busse in Ostfriesland 10 Meter breit und 2 Meter lang?",
     "Weil alle vorn sitzen wollen."],
    ["Welche Hunde treten zu Weltmeisterschaften an?",
     "Boxer."],
    ["Was sagt man zu einem Gorilla mit Ohrenschützern?",
     "Alles, was man will, er kann es sowieso nicht hören."],
    ["Was mögen Katzen und Schwimmer?",
     "Das Kraulen."],
    ["Was reist um die ganze Welt und bleibt doch in der Ecke?",
     "Eine Briefmarke."],
    ["Was steht in der Mitte vom Stadion?",
     "Das d."],
    ["Wie lieben sich Igel?",
     "Gaaanz vorsichtig!"],
    ["Was ist schlimmer als ein tollwütiger Fuchs?",
     "Zwei tollwütige Füchse."],
    ["Was hängt mit verbranntem Hintern an der Wand?",
     "Die Bratpfanne."],
    ["Bei welchen Fischen stehen die Augen am engsten zusammen?",
     "Bei den kleinen."],
    ["Was steht mitten im Rhein und tutet?",
     "Ein Elefant im Urlaub."],
    ["In welche Richtung geht der Rauch einer E-Lok, die mit 100 kmh nach Westen fährt?",
     "Eine E-Lok macht gar keinen Rauch!"],
    ["Warum schauen die Schotten über den Rand ihrer Brille?",
     "Damit sich die Gläser nicht so schnell abnutzen."],
    ["Was ist am tiefsten, Bach Oder Tümpel?",
     "Die Oder."],
    ["Was passiert mit einem Engel, wenn er in einen Misthaufen fällt?",
     "Er bekommt Kotflügel."],
    ["Was hindert einen Reiter daran, auf dem Pferd zu sitzen?",
     "Der Sattel."],
    ["Wie sieht ein Anhalter aus, der Glück hatte?",
     "Mitgenommen."],
    ["Wie kriegt man einen Löwen in den Kühlschrank?",
     "Tür auf, Löwe rein, Tür zu."],
    ["Warum sieht man keine Elefanten auf Kirschbäumen?",
     "Weil sie sich gut getarnt haben."],
    ["Was kommt heraus, wenn man eine Katze mit einem Hund kreuzt?",
     "Ein Tier, das sich selbst jagt."],
    ["Worunter leiden Luftballons?",
     "Platzangst."],
    ["Woran merkt man, dass Ebbe ist?",
     "Wenn es beim Rudern staubt."],
    ["Warum ist Rätselraten gefährlich?",
     "Weil man sich den Kopf zerbricht."],
    ["Was haben nur Giraffen und andere Tiere nicht?",
     "Giraffenbabys."],
    ["Warum schlug der Mann die Uhr?",
     "Weil die Uhr zuerst schlug."],
    ["Welcher Peter macht den meisten Krach?",
     "Der Trompeter."],
    ["Was kommt heraus, wenn man einen Papagei mit einem Monster kreuzt?",
     "Ein Wesen, das immer einen Keks bekommt, wenn es einen verlangt."],
    ["Was sieht aus wie eine Katze, ist aber keine?",
     "Ein Kater."],
    ["Wann sagt ein Chinese Guten Morgen?",
     "Wenn er Deutsch gelernt hat."],
    ["Wo geht nachts das Licht hin?",
     "Schau mal im Kühlschrank nach!"],
    ["Wie hoch ist der höchste Berg?",
     "Höher als alle anderen."],
    ["Was ist das Ende von Allem?",
     "Der Buchstabe M."],
    ["Was liegt zwischen Berg und Tal?",
     "Und."],
    ["Womit würfeln die Eskimos?",
     "Mit Eiswürfeln."],
    ["Wohin fliegt die Wolke, wenn es sie juckt?",
     "Zum Wolkenkratzer."],
    ["Was hat sechs Augen und kann doch nicht sehen?",
     "Drei blinde Mäuse."],
    ["Was arbeitet nur, wenn es gefeuert wird?",
     "Eine Rakete."],
    ["Was macht der Wurm im Salat?",
     "Er schmeißt die Schnecken raus."],
    ["Was ist weiß und hüpft von Baum zu Baum?",
     "Tarzan im Nachthemd."],
    ["Was kommt heraus, wenn man einen Pinguin mit einem Tausendfüßler kreuzt?",
     "Tausend kalte Füße."],
    ["Wie viele Erbsen gehen in einen Topf?",
     "Erbsen können gar nicht gehen!"],
    ["Was ist beim Elefanten klein und beim Floh groß?",
     "Das F."],
    ["Warum haben Dinosaurier so einen langen Hals?",
     "Weil ihre Füße riechen."],
    ["Warum können Nilpferde nicht Fahrrad fahren?",
     "Weil sie keinen Daumen zum Klingeln haben."],
    ["Warum vergessen Elefanten nie etwas?",
     "Weil ihnen nie jemand etwas erzählt."],
    ["Woher wissen wir, dass die Erde rund ist?",
     "Weil wir uns die Sohlen schief laufen."],
    ["Warum hat der Elefant rote Augen?",
     "Damit er sich besser im Kirschbaum verstecken kann."],
    ["Warum hat der Schwan so einen langen Hals?",
     "Damit er bei Hochwasser nicht ertrinkt."],
    ["Kennst du den Sekundenwitz?",
     "Schon vorbei."],
    ["Was ist das älteste Instrument?",
     "Das Akkordeon, es hat die meisten Falten."],
    ["Wie verhindert man, dass ein Elefant durch ein Nadelöhr geht?",
     "Man macht einen Knoten in seinen Schwanz."],
    ["Was macht Ha-ha-ha-peng?",
     "Jemand, der sich kaputt lacht."],
    ["Warum legen Hühner Eier?",
     "Wenn sie sie werfen würden, würden sie kaputt gehen."],
    ["Warum sind die Fußstapfen vom Elefanten so groß?",
     "Weil sonst seine Füße nicht reinpassen!"],
    ["Was essen Elektriker zu Mittag?",
     "Kabelsalat."],
    ["Warum zieht der Wellensittich beim Schlafen ein Bein hoch?",
     "Wenn er beide hochzieht, fällt er von der Stange."],
    ["Woran erkennt man, dass ein Elefant im Kühlschrank war?",
     "Am Fußabdruck in der Butter."],
    ["Was ist der Unterschied zwischen einem Bäcker und einem Teppich?",
     "Der Bäcker muss um 3 aufstehen, der Teppich kann liegen bleiben."],
    ["Welchen Satz hört der Hai am liebsten?",
     "Mann über Bord!"],
    ["Was ist grau, wiegt 10 Pfund und quiekt?",
     "Eine Maus, die dringend mal Diät halten muss."],
    ["Welchen Vogel kann man mit zwei Buchstaben schreiben?",
     "NT"],
    ["Wie erpresst ein Hase einen Schneemann?",
     "Möhre her, sonst Fön!"],
    ["Warum sind Elefanten groß und grau?",
     "Wenn sie klein und gelb wären, wären sie Kanarienvögel."],
    ["Wann ist es gefährlich, in den Garten zu gehen?",
     "Wenn der Salat schießt."],
    ["Welche Tomaten kann man nicht essen?",
     "Die Automaten."],
    ["Warum hat "+ Donald +  " Zucker auf sein Kopfkissen gestreut?",
     "Er wollte süße Träume haben."],
    ["Warum brachte "+ Goofy +  " seinen Kamm zum Zahnarzt?",
     "Weil er alle Zähne verloren hatte."],
    ["Warum ließ "+ Goofy +  " das Gartentor offen?",
     "Damit die Blumen frische Luft kriegen."],
    ["Wie heißt die Frau vom Papagei?",
     "Mamagei."],
    ["Was hat Flügel, läuft aber lieber?",
     "Die Nase."],
    ["Warum duschte der Einbrecher?",
     "Um einen sauberen Abgang zu haben."],
    ["Was brennt Tag und Nacht?",
     "Die Brennnessel."],
    ["Was ist, wenn ein Schornsteinfeger in den Schnee fällt?",
     "Winter."],
    ["Warum ging "+ Pluto +  " mit einem Stein und Streichhölzern ins Bett?",
     "Mit dem Stein schmiss er das Licht aus, dann schaute er nach, ob es aus ist."],
    ["Was macht man, wenn man in der Wüste eine Schlange sieht?",
     "Man stellt sich hinten an."],
    ["Warum sind falsche Zähne wie Sterne?",
     "Beide kommen nachts heraus."],
    ["Was kann in der Hosentasche sein, selbst wenn nichts drin ist?",
     "Ein Loch."],
    ["Welches Tier ist das lustigste?",
     "Das Pferd, es veräppelt die Straße."],
    ["Welcher Bus überquerte als erster den Atlantik?",
     "Kolumbus."],
    ["Was ist schwarz und dreht sich immer im Kreis?",
     "Ein Maulwurf beim Hammerwerfen."],
    ["Was ist schwarz und hüpft auf einem Bein?",
     "Ein Maulwurf, dem beim Hammerwerfen der Hammer auf den Fuß fiel."],
    ["Warum sollte man nachts nicht in den Urwald gehen?",
     "Weil dann die Elefanten Fallschirmspringen üben."],
    ["Was ist der Unterschied zwischen einem Wasserfall?",
     "Je höher desto plumps."],
    ["Warum nahm "+ Goofy +  " eine Semmel mit aufs Klo?",
     "Um die WC-Ente zu füttern."],
    ["Warum trinken Katzen so gerne?",
     "Damit sie einen Kater kriegen."],
    ["Was sagte der große Schornstein zum kleinen Schornstein?",
     "Du bist doch zum Rauchen noch zu klein!"],
    ["Was ist schwarz-weiß gestreift und wird rot?",
     "Ein Zebra, das sich schämt."],
    ["Was ist der Unterschied zwischen einem Knochen und Schule?",
     "Der Knochen ist für den Hund und Schule für die Katz."],
    ["Was macht mmus-mmus?",
     "Eine Fliege, die rückwärts fliegt."],
    ["Was macht der Glaser, wenn er kein Glas mehr hat?",
     "Er trinkt aus der Flasche."],
    ["Was ist ein Anto?",
     "Ein Druckfehler, es sollte Auto heißen."],
    ["Was kommt heraus, wenn man einen Bären und ein Stinktier kreuzt?",
     "Puh der Bär."],
    ["Wie macht man eine Tuba sauber?",
     "Mit Tuben-Zahnpasta."],
    ["Was war am 6. Dezember 1924?",
     "Nikolaus."],
    ["Was ist klein, grün und dreieckig?",
     "Ein kleines grünes Dreieck."],
    ["Es hängt an der Wand und wenn's runterfällt, geht die Tür auf. Was ist das?",
     "Zufall."],
    ["Warum heißen Teigwaren Teigwaren?",
     "Weil sie einmal Teig waren."],
    ["Wie sagt man 'Postbote' ohne o?",
     "Briefträger."],
    ["Was kommt heraus, wenn man eine Kamera mit einem Krokodil kreuzt?",
     "Ein Schnappschuss."],
    ["Was ist braun und rennt durch den Wald?",
     "Ein ferngesteuertes Rennschnitzel."],
    ["Wo fängt ein Kreis an?",
     "Beim K."],
    ["Was kommt heraus, wenn man einen Elefanten mit einer Krähe kreuzt?",
     "Massenhaft umgeknickte Telefonmasten."],
    ["Schon mal einen Kühlschrank durch den Wald rennen sehen?",
     "Nein? Siehste, so schnell sind die!"],
    ["Was ist eine Karotte?",
     "Eine Kartoffel mit zu hohem Blutdruck."],
    ["Was ist weiß und hat sechs Ecken?",
     "Ist doch einfach! Ein Pingpongklötzchen."],
    ["Was ist grün, laut und gefährlich?",
     "Eine herandonnernde Herde Gurken."],
    ["Was ist, wenn sich zwei Jäger treffen?",
     "Dann sind beide tot."],
    ["Ein Elefant sitzt auf einem Ahornblatt. Wie kommt er wieder runter?",
     "Er wartet bis im Herbst sein Blatt abfällt."],
    ["Was ist schlimmer dran als eine Giraffe mit Halsweh?",
     "Ein Tausendfüßler mit Fußpilz."],
    ["Was macht ABC...schlürf...DEF...schlürf?",
     "Jemand, der Buchstabensuppe isst."],
    ["Wann hoppelt ein Hase über einen Baum?",
     "Wenn der Baum gefällt ist."],
    ["Was ist ein eisernes Abführmittel?",
     "Handschellen."],
    ["Was ist eine gesellige Hülsenfrucht?",
     "Eine Kontaktlinse."],
    ["Was ist weiß mit schwarzen und roten Punkten?",
     "Ein Dalmatiner, der die Masern hat."],
    ["Was sind Früchte des Zorns?",
     "Ohrfeigen."],
    ["Was macht ein Kaugummi, wenn er um die Ecke geht?",
     "Er bleibt kleben."],
    ["Was ist grau, wiegt 200 Pfund und sagt: Na, Miez-Miez-Miez?",
     "Eine 200-Pfund-Maus. "],
    ["Wie fängt man am besten ein Reh?",
     "Man schleicht sich an und streut ihm Salz auf den Schwanz."],
    ["Wie fängt man am besten ein Kaninchen?",
     "Man hockt sich hinter einen Busch und macht ein Geräusch wie ein Salatblatt. "],
    ["Wo kommt der Juli vor dem Juni?",
     "Im Duden."],
    ["Welches Tier dreht sich nach seinem Tod noch 150 Mal?",
     "Das Grillhähnchen."],
    ["Was hat ein Fell, miaut und jagt Mäuse unter Wasser?",
     "Ein Katzenfisch."],
    ["Monikas Vater hat fünf Töchter. Sie heißen Lala, Lele, Lili und Lulu. Wie heißt die fünfte?",
     "Na, Monika!"],
    ["Was ist außen grün und innen gelb?",
     "Eine als Gurke verkleidete Banane."],
    ["Was macht ein Ostfriese, der mit einem Messer auf dem Deich steht?",
     "Er sticht in See."],
    ["Was wiegt 4 Tonnen, hat einen Rüssel und ist leuchtend rot?",
     "Ein Elefant, dem etwas peinlich ist."],
    ["Was ist, wenn ein Schwein ums Eck geht?",
     "Es ist weg."],
    ["Was wird eine Tomate, wenn sie auf die Straße geht?",
     "Ketchup."],
    ["Was ist ein Cowboy, der sein Pferd verloren hat?",
     "Ein Sattelschlepper."],
    ["Was sagt die Erdnuss zum Elefanten?",
     "Gar nichts. Erdnüsse können nicht reden."],
    ["Was sagen Elefanten, wenn sie aufeinanderprallen?",
     "Die Welt ist klein, was?"],
    ["Was ist groß, grau, und telefoniert aus Afrika?",
     "Ein Telefant."],
    ["Was sagt der eine Floh zum anderen?",
     "Sollen wir laufen oder eine Katze nehmen?"],
    ["Was ist grün, glücklich, und hüpft von Grashalm zu Grashalm?",
     "Eine Freuschrecke."],
    ["Was ist schlimmer, als ein Wurm in dem Apfel zu finden, in den man gerade gebissen hat?",
     "Einen halben Wurm zu finden."],
    ["Was fängt mit Z an und kann schwimmen?",
     "Zwei Enten."],
    ["Was kommt heraus, wenn man eine Brieftaube mit einem Papagei kreuzt?",
     "Ein Vogel, der beim Fliegen nach dem Weg fragen kann."],
    ["Was ist der Unterschied zwischen einem Briefkasten und einem Elefanten?",
     "Schon mal versucht, einen Brief in einen Elefanten einzuwerfen?"],
    ["Was ist der Unterschied zwischen einem Sack Mehl und einem Saxofon?",
     "Blas mal rein!"],
    ["Was machst du, damit dein Computer nicht abstürzt?",
     "Ihn auf den Boden stellen."],
    ["Warum laufen Dudelsackspieler beim Spielen hin und her?",
     "Sie versuchen, den Tönen zu entkommen."],
    ["Warum tragen Elefanten Turnschuhe?",
     "Damit es nicht so plumpst, wenn sie aus den Bäumen springen."],
    ["Warum ist Ostfriesland so flach?",
     "Damit die Ostfriesen schon am Mittwoch sehen, wer Sonntag zu Besuch kommt."],
    ["Warum flog Aschenputtel aus dem Basketballteam?",
     "Es lief immer vom Ball weg."],
    ["Warum heißt der Löwe Löwe?",
     "Weil er durch die Wüste löwt."],
    ["Warum heißt die Haut Haut?",
     "Weil man drauf haut."],
    ["Warum macht der Hahn beim Krähen die Augen zu? ",
     "Er will die Hühner damit beeindrucken, dass er es auswendig kann."],
    ["Was sagt ein Papst zum anderen?",
     "Es gibt immer nur einen Papst ..."],
    ["Was sagt ein Magnet zum anderen?",
     "Ich finde dich echt anziehend ..."],
    ["Wie alt kann man in Japan werden?",
     "Mitsubishi Glück wird man Honda."],
    ["Was sagt ein Japaner zu seiner Frau, nachdem sie einen Sohn geboren hat?",
     "Its a Sony."],
    ["Warum ist "+ MickeyMouse +  " ins Weltall geflogen?",
     "Er wollte "+ Pluto +  "finden."],
    ]

# MovieHeal.py
MovieHealLaughterMisses = ("hmm","he","ha","Höhö")
MovieHealLaughterHits1= ("Hahaha","Hihi","Kicher","Ha Ha")
MovieHealLaughterHits2= ("MUA-HA-HA!","HO HO HO!","HA HA HA!")

# MovieSOS.py
MovieSOSCallHelp = "%s HILFE!"
MovieSOSWhisperHelp = "%s braucht Hilfe im Kampf!"
MovieSOSObserverHelp = "HILFE!"

# MovieNPCSOS.py
MovieNPCSOSGreeting = "Hi %s! Ich helfe gern!"
MovieNPCSOSGoodbye = "Bis später!"
MovieNPCSOSToonsHit = "Toons Treffen Immer!"
MovieNPCSOSCogsMiss = "Bots Hauen Immer Daneben!"
MovieNPCSOSRestockGags = "%s Gags werden aufgefüllt!"
MovieNPCSOSHeal = "Heilen"
MovieNPCSOSTrap = "Fallen stellen"
MovieNPCSOSLure = "Ködern"
MovieNPCSOSSound = "Volldröhnen"
MovieNPCSOSThrow = "Werfen"
MovieNPCSOSSquirt = "Spritzen"
MovieNPCSOSDrop = "Fallen lassen"
MovieNPCSOSAll = "Alle"

# MovieSuitAttacks.py
MovieSuitCancelled = "ABGEBROCHEN\nABGEBROCHEN\nABGEBROCHEN"

# RewardPanel.py
RewardPanelToonTasks = "Toon-Aufgaben"
RewardPanelItems = "Zurückeroberte Gegenstände"
RewardPanelMissedItems = "Nicht zurückeroberte Gegenstände"
RewardPanelQuestLabel = "Aufgabe %s"
RewardPanelCongratsStrings = ["Yeah!", "Glückwunsch!", "Wow!",
                              "Cool!", "Toll!", "Toon-tastisch!"]
RewardPanelNewGag = "Neuer %(gagName)s Gag für %(avName)s!"
RewardPanelMeritsMaxed = "Maximal"
RewardPanelMeritBarLabel = "Verdienste"
RewardPanelMeritAlert = "Beförderungsfähig!"

RewardPanelCogPart = "Du hast ein Teil eines Bot-Kostüms erhalten!"

# Cheesy effect descriptions: (short desc, sentence desc)
CheesyEffectDescriptions = [
    ("Normaler Toon", "du wirst normal"),
    ("Großer Kopf", "du bekommst einen großen Kopf"),
    ("Kleiner Kopf", "du bekommst einen kleinen Kopf"),
    ("Große Beine", "du bekommst große Beine"),
    ("Kleine Beine", "du bekommst kleine Beine"),
    ("Großer Toon", "du wirst etwas größer"),
    ("Kleiner Toon ", "du wirst etwas kleiner"),
    ("Flachporträt", "du wirst zweidimensional"),
    ("Flachprofil", "du wirst zweidimensional"),
    ("Durchsichtig", "du wirst durchsichtig"),
    ("Keine Farbe", "du wirst farblos"),
    ("Unsichtbarer Toon", "du wirst unsichtbar"),
    ]
CheesyEffectIndefinite = "Bis du einen anderen Effekt wählst, %(effectName)s%(whileIn)s."
CheesyEffectMinutes = "Die nächsten %(time)s Minuten, %(effectName)s%(whileIn)s."
CheesyEffectHours = "Die nächsten %(time)s Stunden, %(effectName)s%(whileIn)s."
CheesyEffectDays = "Dieie nächsten %(time)s Tage, %(effectName)s%(whileIn)s."
CheesyEffectWhileYouAreIn = " während du in %s bist"
CheesyEffectExceptIn = ", außer in %s"


# SuitBattleGlobals.py
SuitFlunky = "Kriecher"
SuitPencilPusher = "Griffel\3schieber"
SuitYesman = "Jasager"
SuitMicromanager = "Mikro\3manager"
SuitDownsizer = "Niedermacher"
SuitHeadHunter = "Köpfchen\3jäger"
SuitCorporateRaider = "Unternehmens\3räuber"
SuitTheBigCheese = "Großhirn"
SuitColdCaller = "Aufschwatzer"
SuitTelemarketer = "Tele\3marketer"
SuitNameDropper = "Wichtig\3tuer"
SuitGladHander = "Glücks\3händchen"
SuitMoverShaker = "Aufbauscher"
SuitTwoFace = "Falsch\3gesicht"
SuitTheMingler = "Einmischer"
SuitMrHollywood = "Mr. Hollywood"
SuitShortChange = "Keinmünz"
SuitPennyPincher = "Pfennig\3fuchser"
SuitTightwad = "Geizhals"
SuitBeanCounter = "Kieszähler"
SuitNumberCruncher = "Erbsen\3zähler"
SuitMoneyBags = "Geldsack"
SuitLoanShark = "Kredithai"
SuitRobberBaron = "Ausbeuter"
SuitBottomFeeder = "Schnäppchen\3jäger"
SuitBloodsucker = "Blut\3sauger"
SuitDoubleTalker = "Dumm\3schwätzer"
SuitAmbulanceChaser = "Unfall\3abzocker"
SuitBackStabber = "Heimtücker"
SuitSpinDoctor = "Schönredner"
SuitLegalEagle = "Prozessgeier"
SuitBigWig = "Großkotz"

# Singular versions (indefinite article)
SuitFlunkyS = "einen Kriecher"
SuitPencilPusherS = "einen Griffelschieber"
SuitYesmanS = "einen Jasager"
SuitMicromanagerS = "einen Mikromanager"
SuitDownsizerS = "einen Niedermacher"
SuitHeadHunterS = "einen Köpfchenjäger"
SuitCorporateRaiderS = "einen Unternehmensräuber"
SuitTheBigCheeseS = "einen Großhirn"
SuitColdCallerS = "einen Aufschwatzer"
SuitTelemarketerS = "einen Telemarketer"
SuitNameDropperS = "einen Wichtigtuer"
SuitGladHanderS = "eine Glückshändchen"
SuitMoverShakerS = "einen Aufbauscher"
SuitTwoFaceS = "einem Falschgesicht"
SuitTheMinglerS = "einen Einmischer"
SuitMrHollywoodS = "einen Mr. Hollywood"
SuitShortChangeS = "eine Keinmünz"
SuitPennyPincherS = "einen Pfennigfuchser"
SuitTightwadS = "einen Geizhals"
SuitBeanCounterS = "einen Kieszähler"
SuitNumberCruncherS = "einen Erbsenzähler"
SuitMoneyBagsS = "einen Geldsack"
SuitLoanSharkS = "einen Kredithai"
SuitRobberBaronS = "einen Ausbeuter"
SuitBottomFeederS = "einen Schnäppchenjäger"
SuitBloodsuckerS = "einen Blutsauger"
SuitDoubleTalkerS = "einen Dummschwätzer"
SuitAmbulanceChaserS = "einen Unfallabzocker"
SuitBackStabberS = "einem Heimtücker"
SuitSpinDoctorS = "einen Schönredner"
SuitLegalEagleS = "einen Prozessgeier"
SuitBigWigS = "einem Großkotz"

# Plural versions
SuitFlunkyP = "Kriecher"
SuitPencilPusherP = "Griffelschieber"
SuitYesmanP = "Jasager"
SuitMicromanagerP = "Mikromanager"
SuitDownsizerP = "Niedermacher"
SuitHeadHunterP = "Köpfchenjäger"
SuitCorporateRaiderP = "Unternehmensräuber"
SuitTheBigCheeseP = "Großhirne"
SuitColdCallerP = "Aufschwatzer"
SuitTelemarketerP = "Telemarketer"
SuitNameDropperP = "Wichtigtuer"
SuitGladHanderP = "Glückshändchen"
SuitMoverShakerP = "Aufbauscher"
SuitTwoFaceP = "Falschgesichter"
SuitTheMinglerP = "Einmischer"
SuitMrHollywoodP = "Mr. Hollywoods"
SuitShortChangeP = "Keinmünze"
SuitPennyPincherP = "Pfennigfuchser"
SuitTightwadP = "Geizhälse"
SuitBeanCounterP = "Kieszähler"
SuitNumberCruncherP = "Erbsenzähler"
SuitMoneyBagsP = "Geldsack"
SuitLoanSharkP = "Kredithaie"
SuitRobberBaronP = "Ausbeuter"
SuitBottomFeederP = "Schnäppchenjäger"
SuitBloodsuckerP = "Blutsauger"
SuitDoubleTalkerP = "Dummschwätzer"
SuitAmbulanceChaserP = "Unfallabzocker"
SuitBackStabberP = "Heimtücker"
SuitSpinDoctorP = "Schönredner"
SuitLegalEagleP = "Prozessgeier"
SuitBigWigP = "Großkotze"

SuitFaceOffDefaultTaunts = ['Huh!']

SuitFaceoffTaunts = {
    'b':  ["Hast du eine kleine Spende für mich?",
           "Du wirst böse gegen mich verlieren.",
           "Ich lass dich auf dem Trocknen zappeln.",
           "Ich bin A-positiv der Meinung, dass ich gewinnen werde.",
           "Du Null, sei doch nicht so \"negativ\".",
           "Wie hast du mich gefunden, ich bin sehr mobil.",
           "Ich muss dich mal kurz überschlagen.",
           "Du wirst gleich einen kleinen Imbiss brauchen.",
           "Wenn ich fertig bin, wirst du dich hinlegen müssen.",
           "Tut nur ganz kurz weh.",
           "Dir wird gleich schwindlig werden.",
           "Gutes Timing, ich muss mal wieder einen halben Liter nachfüllen.",
           ],
    'm':  ["Du weißt nicht, bei wem du dich da einmischst.",
           "Hast du dich schon mal bei jemandem wie mir eingemischt?",
           "Gut, zum Einmischen gehören mindestens zwei.",
           "Da wollen wir uns mal einmischen.",
           "Das scheint mir ein guter Ort zum Einmischen zu sein.",
           "Na, ist das nicht gemütlich?",
           "Du mischst bei deiner Niederlage mit.",
           "Ich werd mich gleich in deine Angelegenheiten einmischen.",
           "Bist du sicher, dass du dich einmischen willst?",
           ],
    'ms': ["Pass auf, du wirst gleich aufgebauscht!",
           "Bausch dich nicht auf.",
           "Weg oder ich bausch dich auf.",
           "Jetzt will ich aufbauschen.",
           "Das dürfte dich ein wenig aufbauschen.",
           "Fertig zum Aufbauschen!",
           "Ich bin zum Aufbauschen bereit.",
           "Sieh dich vor Toon, du bewegst dich auf bauschigem Boden!",
           "Das dürfte ein aufbauschender Augenblick werden.",
           "Ich bin aufgebauscht genug, dich zu erledigen.",
           "Schon aufgebauscht?",
           ],
    'hh': ["Ich bin eine Köpfchenlänge vor dir.",
           "Mach dir einen Kopf, gleich wird's ernst.",
           "Du wirst dir wünschen, du hättest mehr Köpfchen gehabt.",
           "Na prima, ich jage dir schon eine Weile hinterher!",
           "Das kostet dich das Köpfchen.",
           "Köpfchen hoch!",
           "Sieht aus, als wolltest du mit dem Kopf durch die Wand.",
           "Lust auf eine kleine Jagd?",
           "Die perfekte Jagdtrophäe für meine Sammlung.",
           "Du wirst gewaltige Kopfschmerzen kriegen.",
           "Verlier nicht das Köpfchen wegen mir.",
           ],
    'tbc': ["Pass auf, ich bin der Größte!",
            "Du darfst Hirni zu mir sagen.",
            "Hast du dir das gut überlegt? Ich bin größer als du!",
            "Ich dachte schon, du wolltest deinen Verstand strapazieren!",
            "Ich mach deine grauen Zellen schwarz.",
            "Meinst du nicht, dass mein Verstand überragend ist? ",
            "Ich mach gleich Hirn aus dir.",
            "Man sagt, ich sei sehr groß.",
            "Vorsicht, ich kenne deine Hirnströme!",
            "Pass auf, ich bin ein Superhirn in diesem Spiel!",
            "Dich zu erledigen wird mir eine große Freude sein.",
            ],
    'cr': ["ÜBERFALL!",
           "Du passt nicht in mein Unternehmen.",
           "Mach dich auf eine feindliche Übernahme gefasst.",
           "Sieht aus, als wärst du für eine Übernahme bereit.",
           "Das ist kein angemessenes Geschäftsgebaren.",
           "Du siehst ziemlich angreifbar aus.",
           "Höchste Zeit, deine Vermögenswerte zu überschreiben.",
           "Ich führe gerade eine Kampagne zum Abbau von Toons durch.",
           "Du bist gegen meine Ideen machtlos.",
           "Nur Ruhe, das ist alles nur zu deinem Besten.",
           ],
    'mh': ["Fertig für den Take?",
           "Licht, Kamera, Action!",
           "Los geht's.",
           "Die Rolle des besiegten Toon wird heute gespielt von - DIR!",
           "Diese Szene wird rausgeschnitten.",
           "Ich kenne schon mein Motiv für diese Szene. ",
           "Bist du bereit für deine letzte Szene?",
           "Gleich kommt dein Nachspann.",
           "Ich habe dir gesagt, du sollst mich nicht anrufen.",
           "Weiter mit der Show.",
           "There's no business like show business!",
           "Ich hoffe, du vergisst deinen Text nicht.",
           ],
    'nc': ["Sieht aus, als wären deine Erbsen gezählt.",
           "Ich hoffe, du magst es bissfest.",
           "Jetzt bist du aber schön auf einer Erbse ausgerutscht.",
           "Ist es schon Zeit zum Abkochen?",
           "Da wollen wir mal anzählen.",
           "Möchtest du vielleicht püriert werden?",
           "Du gibst mir ganz schön was zu zählen.",
           "Gleich gibt's was auf die Erbse.",
           "Na los, versuch dein Glück und sag eine Zahl.",
           "Du wirst die Erbsensuppe gleich auslöffeln müssen.",
           ],
    'ls': ["Die Zeit für die Rückzahlung ist gekommen.",
           "Du hattest schon eine Fristverlängerung",
           "Dein Kredit ist jetzt fällig.",
           "Ich werde jetzt die Kreditbremse ziehen.",
           "Nun, du hast um ein Darlehen gebeten und du hast es bekommen.",
           "Dafür wirst du bezahlen.",
           "Die Zahlung ist sofort fällig.",
           "Würdest du mir deine Aufmerksamkeit leihen?",
           "Gut, dass ich dich sehe, ich bin ziemlich in Rage.",
           "Zeit für einen schnellen Happen?",
           "Das ist doch mal ein guter Happen.",
           ],
    'mb': ["Jetzt wollen wir mal die dicken Säcke einfahren.",
           "Dich steck ich in den Sack.",
           "Papier oder Plastik?",
           "Hast du deinen Gepäckschein?",
           "Denk dran, Geld macht nicht glücklich.",
           "Vorsicht, ich habe hier schweres Gepäck.",
           "Du wirst Geldprobleme bekommen.",
           "Geld regiert gleich deine Welt.",
           "Ich bin reicher, als gut für dich ist.",
           "Man kann nie genug Geld haben!",
           ],
    'rb': ["Du bist ausgebeutet worden.",
           "Das ist meine Beute.",
           "Ich schlage Kapital aus dir!",
           "Ich hoffe, du machst gleich den Buckel krumm.",
           "Du wirst diese Ausbeutung melden müssen.",
           "Her mit der Beute!",
           "Ich bin ein fairer Kapitalist.",
           "Ich nehm dir alles ab, was du hast.",
           "Wenn das keine nette, fette Beute ist!",
           "Du hättest wissen sollen, dass man sich mit mir nicht einlässt.",
           ],
    'bs': ["Dreh mir nie den den Rücken zu.",
           "Du wirst nicht wieder heimkommen.",
           "Nimm das zurück, oder ich zahl's dir heim! ",
           "Die Tücke steckt im Detail.",
           "Das Böse lauert überall!",
           "Jetzt ist es zu spät heimzurennen! ",
           "Du wirst gleich die Tücken des Objekts kennen lernen.",
           "Komm du mir heim, Toon!",
           "Mit List und Tücke komme ich immer zum Ziel.",
           "Du wirst gleich tückische Kopfschmerzen bekommen.",
           "Heimtücke hilft immer.",
           ],
    'bw': ["Sei nicht so großkotzig.",
           "Da wird mir ja speiübel!",
           "Da laufe ich zu voller Größe auf, wenn du meinst! ",
           "Sieht aus, als würden wir unsere Größe messen.",
           "Du kannst mit Größe nicht umgehen.",
           "Gleich wird dir übel werden.",
           "Ich bin froh, dass du pünktlich zum Größenvergleich kommst.",
           "Du kriegst großen Ärger.",
           "Ich setz dir gleich was drauf!",
           "Ich bin hier eine Größe, kleiner Toon.",
           ],
    'le': ["Vorsicht, ich mache kurzen Prozess mit dir.",
           "Die Geier kreisen schon über dir...",
           "Ich hetz dir das Gesetz auf den Hals!",
           "Du solltest wissen, dass ich mich von Aas ernähre.",
           "Ich werde ein rechtlicher Albtraum für dich sein.",
           "Diesen Prozess kannst du nicht gewinnen.",
           "Du bist ein gefundenes Fressen für mich!",
           "Protzessier hier nicht rum, du kleiner Wicht.",
           "Ich habe Paragraphen ohne Ende!",
           "Ein Prozess ist besser als kein Prozess.",
           ],
    'sd': ["Du weißt nie, wo ich aufhören werde.",
           "Kleine Verschönerung gefällig?",
           "Ich werde dich jetzt zur Rede stellen.",
           "Du bist ja überhaupt nicht der Rede wert!",
           "Pass auf, wenn ich erst meine Rede schwinge!",
           "Mein schöner Toon, gleich bist du weg vom Fenster.",
           "Da hast du dir was Schönes eingebrockt.",
           "Es wird dir schlicht und ergreifend die Rede verschlagen.",
           "Möchtest du etwa mitreden?",
           "Ich habe zu diesem Thema meine eigene schöne Ansicht.",
           ],
    'f': ["Ich erzähl dem Chef, was du gemacht hast!",
          "Ich bin zwar ein Kriecher, aber ich kriech dich sicher!",
          "Auf deinem Rücken werde ich die Karriereleiter hochsteigen.",
          "Es wird dir nicht gefallen, wie ich arbeite.",
          "Der Chef zählt darauf, dass ich dich aufhalte.",
          "Du wirst dich in meinem Lebenslauf gut machen.",
          "An mir kommst du nicht vorbei.",
          "Mal sehen, wie du meine Arbeitsleistung bewertest.",
          "Beim Entlassen von Toons bin ich besonders gut.",
          "Du wirst meinen Chef nie zu sehen bekommen.",
          "Ich schick dich zurück auf den Spielplatz.",
          ],
    'p':  ["Ich radier dich aus!",
           "Hey, du kannst mich nicht herumschieben.",
           "Ich bin die Nummer 2!",
           "Ich wisch dich einfach weg.",
           "Ich setze jetzt den Schlusspunkt.",
           "Lass mich mal zum Punkt kommen.",
           "Mach schnell, mir wird schnell langweilig.",
           "Ich hasse es, wenn die Dinge aus dem Griffel geraten.",
           "Du willst also Unruhe stiften?",
           "Schieb dir den Griffel sonstwohin!",
           "Vorsicht, ich kann dich anschwärzen!",
           ],
    'ym': ["Ich glaube ja, das wird dir nicht gefallen.",
           "Ich weiß nicht, was nein bedeutet.",
           "Wollen wir uns treffen? Ich sage ja, jederzeit.",
           "Du brauchst eine positive Erfahrung.",
           "Ich werde einen positiven Eindruck hinterlassen.",
           "Ich habe mich noch nie geirrt.",
           "Ja, ich bin bereit für dich.",
           "Wenn du das möchtest, hast du meine Zustimmung.",
           "Du wirst einen positiven Bescheid erhalten.",
           "Ich bestätige die Zeit unseres Treffens.",
           "Ein Nein lasse ich nicht gelten.",
           ],
    'mm': ["Ich werde in dein Geschäft einsteigen!",
           "Manchmal kommen große Schläge in kleinen Portionen.",
           "Kein Job ist zu klein für mich.",
           "Ich möchte, dass das richtig gemacht wird, deshalb mach ich es selber.",
           "Du brauchst jemanden, der deine Angelegenheiten managt.",
           "Prima, ein Projekt!",
           "Du bist zu winzig für mich.",
           "Ich glaube, du brauchst etwas Anleitung.",
           "Ich werde mich umgehend um dich kümmern.",
           "Ich habe ein Auge auf jeden Schritt, den du tust.",
           "Bist du sicher, dass du das tun willst?",
           "Wir werden das auf meine Art regeln.",
           "Ich werde dir genau auf die Finger schauen.",
           "Ich bin ein kleiner Meister im Bloßstellen!",
           ],
    'ds': ["Ich mache alles nieder!",
           "Deine Möglichkeiten schwinden.",
           "Deine Einkünfte werden niedriger sein.",
           "Dein Wert für uns ist ziemlich niedrig.",
           "Sag nicht, ich soll dich niedermachen!",
           "Ich muss vielleicht ein paar Kürzungen einführen.",
           "Deine Chancen sind recht niedrig.",
           "Du siehst ja so niedergeschlagen aus!?",
           ],
    'cc': ["Überrascht, von mir zu hören?",
           "Du hast angerufen?",
           "Bist du bereit, meine Gebühren zu akzeptieren?",
           "Du musst sofort unterschreiben.",
           "Ich habe die besten Verbindungen.",
           "Bleib dran - ich bin da.",
           "Hast du auf meinen Anruf gewartet?",
           "Ich hatte gehofft, du würdest zurückrufen.",
           "Die Gebühren sind einfach sensationell.",
           "Ich rufe immer direkt an.",
           "Du stehst wohl auf der Leitung.",
           "Dieser Anruf kostet dich einiges.",
           "Na, klingelt's schon?",
           ],
    'tm': ["Ich werde das sehr unbequem für dich machen.",
           "Kann ich dich für einen Versicherungsplan interessieren?",
           "Du hättest meinen Anruf lieber nicht annehmen sollen.",
           "Jetzt wirst du mich nicht mehr los.",
           "Das ist ein ungünstiger Zeitpunkt? Gut.",
           "Ich hatte geplant, dir über den Weg zu laufen. ",
           "Für den Anruf wirst du bezahlen.",
           "Ich habe heute ein paar kostspielige Artikel für dich.",
           "Pech gehabt - ich mache Hausbesuche.",
           "Ich habe vor, dieses Geschäft schnell abzuschließen.",
           "Ich werde einen großen Teil deiner Mittel verbrauchen.",
           ],
    'nd': ["Für mich bist du ein namenloses Etwas.",
           "Du hast sicher nichts dagegen, wenn ich mich wichtig mache.",
           "Sind wir uns nicht schon begegnet?",
           "Beeilung, ich bin mit 'Mr. Hollywood' zum Essen verabredet.",
           "Hab ich schon erwähnt, dass ich den 'Einmischer' kenne?",
           "Du wirst mich nie vergessen.",
           "Ich kenne alle wichtigen Leute, die dir schaden können.",
           "Ich denke, ich mach mich mal ein bisschen wichtig.",
           "Sprich meinen Namen bitte wichtig aus.",
           "Du bist überhaupt nicht wichtig, Toon.",
           ],
    'gh': ["Ich lasse dir freie Hand, Toon.",
           "Darauf meine Hand.",
           "Das wird mir Glück bringen.",
           "Du wirst merken, dass ich ziemlich fest zupacke.",
           "Du kannst es handschriftlich kriegen.",
           "Da wollen wir gleich mal Hand anlegen.",
           "Ich würde sagen, du hast keinen glücklichen Tag erwischt.",
           "Bei dem musst du Glück haben.",
           "Ich kann ganz gute Glückstreffer landen.",
           "Ich lasse mir das Heft nicht aus der Hand nehmen.",
           "Möchtest du, dass ich dir noch etwas aushändige?",
           "Ich zeig dir gleich mal was von meiner Handarbeit.",
           "Du wirst mir noch aus der Hand fressen.",
           ],
    'sc': ["Das kostet mich keinen Cent.",
           "Gleich kommst du in Geldnöte.",
           "Du wirst gleich abgezockt.",
           "Das wird eine schnelle Heimzahlung.",
           "Mit dir bin ich gleich fertig.",
           "Was ich dir sage, kannst du für bare Münze nehmen.",
           "Ich zahl's dir mit gleicher Münze heim!",
           "Du kannst dir keine großen Sprünge erlauben.",
           "Ich habe kein Geld übrig für Toons.",
           "Gleich kriegst du kein Bein mehr auf den Boden!",
           "Pass auf - das wird kein Honigschlecken!",
           ],
    'pp': ["Das wird dich ein bisschen fuchsen.",
           "Mach mich nicht fuchsig!",
           "Vorsicht, ich bin ein ganz Ausgefuchster.",
           "Die Trauben hängen für dich zu hoch.",
           "Fuchs, ich hab die Gans gestohlen!",
           "Wer den Pfennig nicht ehrt, ist den Taler nicht wert.",
           "Ich hab nicht für fünf Pfennig Lust, mich lange mit dir aufzuhalten.",
           "Das wird dir gleich durch Mark und Pfennig gehen!",
           "Bei Kopf verlierst du, bei Zahl gewinne ich.",
           "Deine Gags sind keinen Pfennig wert.",
           ],
    'tw': ["Sieh zu, dass du schnell den Hals aus der Schlinge ziehst.",
           "Für dich immer noch Herr Geizhals.",
           "Jetzt geht es um deinen Hals.",
           "Ist das dein bestes Angebot?",
           "Da woll'n wir mal - Zeit ist Geld.",
           "Na dann - Hals und Beinbruch!",
           "Das kann dich den Hals kosten.",
           "Ich werd dir schon den Hals abschneiden!",
           "Ich hoffe, du kannst dir das leisten.",
           "Du kriegst wohl den Hals nicht voll genug!",
           "Ich werde ein großes Loch in dein Budget reißen.",
           ],
    'bc': ["Ich ziehe gern Toons von der Rechnung ab.",
           "Du kannst darauf zählen, dass du dafür bezahlen wirst.",
           "Kies stinkt nicht.",
           "Ich kann dich anzählen.",
           "Bei mir zählt jeder Kiesel.",
           "Dein Ausgabenbericht ist überfällig!",
           "Zeit für eine Buchprüfung.",
           "Da wollen wir doch mal in mein Büro gehen.",
           "Nicht für Kies und gute Worte.",
           "Ich habe dir einikies zu bieten.",
           "Ich werde dir Kiesel geben statt Brot!",
           ],
    'bf': ["Dich werd ich erlegen.",
           "Ich mach ein Schnäppchen aus dir!",
           "Toons kriegt man zum halben Preis.",
           "Prima, Resteverkauf!",
           "Perfektes Timing, die Geldfalle schnappt zu.",
           "Ich will gute Leistung für mein Geld!",
           "Lass uns mal über einen Preisnachlass reden.",
           "Ein Schnäppchen jagt das andere.",
           "Auf zum großen Halali!",
           "Dich jag ich mir zum Frühstück!",
           ],
    'tf': ["Du wirst das Gesicht verlieren!",
           "Ich sag dir's ins Gesicht - das wird eine Niederlage für dich.",
           "Da bist du an den Falschen geraten!",
           "Du bist auf dem falschen Dampfer, wenn du denkst, du gewinnst.",
           "Ein falsches Gesicht ist besser als gar keins.",
           "Die Angst steht dir doch schon ins Gesicht geschrieben.",
           "Mein wahres Gesicht zeig ich dir nicht.",
           "Falsch oder richtig?",
           "Du möchtest mir wohl ins Gesicht springen?",
           "Du weißt ja nicht, wen du vor dir hast.",
           "Du machst ein Gesicht wie zehn Tage Donnerwetter.",
           ],
    'dt': ["Ich bring dich in ganz dumme Verlegenheit.",
           "Tja, dumm gelaufen, was?",
           "Gegen dummes Geschwätz ist kein Kraut gewachsen.",
           "Ich schwatz dich in Grund und Boden.",
           "Die dümmsten Bauern haben díe größten Kartoffeln.",
           "Du wirst nachher ziemlich dumm aus der Wäsche gucken.",
           "Mich kannst du nicht für dumm verkaufen.",
           "Die Dummen sterben eben nicht aus.",
           "Komm mir nicht dumm!",
           "Haben wir noch was zu beschwatzen?",
           ],
    'ac': ["Leider wirst du heute einen Unfall haben!",
           "Hörst du eine Sirene?",
           "Das wird mir aber Spaß machen.",
           "Ich liebe den Klang von Blech auf Blech.",
           "Wenn's kracht, bin ich schon da!",
           "Bist du versichert?",
           "Ich hoffe, du hast die Krankentrage gleich mitgebracht.",
           "Ich bezweifle, dass du je wieder aufstehst.",
           "Von nun an geht's bergauf.",
           "Du wirst bald den Notdienst brauchen.",
           "Das ist nicht zum Lachen.",
           "Was dem einen sein Unfall, ist dem anderen seine Abzocke.",
           ]
    }

SuitAttackDefaultTaunts = ['Da hast du\'s!', 'Aufschreiben!']

SuitAttackNames = {
  'Audit' : 'Buchprüfung!',
  'Bite' : 'Beißen!',
  'BounceCheck' : 'Geplatzter Scheck',
  'BrainStorm' : 'Brainstorm!',
  'BuzzWord' : 'Schlagwort!',
  'Calculate' : 'Kalkulieren!',
  'Canned' : 'Rausgeschmissen!',
  'Chomp' : 'Mampfen!',
  'CigarSmoke' : 'Zigarrenrauch!',
  'ClipOnTie' : 'Ansteckkrawatte!',
  'Crunch' : 'Zermalmen!',
  'Demotion' : 'Zurückversetzung!',
  'Downsize' : 'Niedermachen!',
  'DoubleTalk' : 'Dummschwätzen!',
  'EvictionNotice' : 'Zwangsräumung!',
  'EvilEye' : 'Böser Blick!',
  'Filibuster' : 'Verschleppungstaktik!',
  'FillWithLead' : 'Mit Blei füllen!',
  'FiveOClockShadow' : "Augenringe!",
  'FingerWag' : 'Tz-Tz!',
  'Fired' : 'Gefeuert!',
  'FloodTheMarket' : 'Markt überfluten!',
  'FountainPen' : 'Füllfederhalter!',
  'FreezeAssets' : 'Vermögen einfrieren!',
  'Gavel' : 'Hammer!',
  'GlowerPower' : 'Finsterblick!',
  'GuiltTrip' : 'Bußgang!',
  'HalfWindsor' : 'Einfacher Windsor!',
  'HangUp' : 'Auflegen!',
  'HeadShrink' : 'Irrenarzt!',
  'HotAir' : 'Heiße Luft!',
  'Jargon' : 'Fachchinesisch!',
  'Legalese' : 'Juristenjargon!',
  'Liquidate' : 'Liquidieren!',
  'MarketCrash' : 'Börsenkrach!',
  'MumboJumbo' : 'Fauler Zauber!',
  'ParadigmShift' : 'Paradigmenwechsel!',
  'PeckingOrder' : 'Hackordnung!',
  'PickPocket' : 'Taschendieb!',
  'PinkSlip' : 'Blauer Brief!',
  'PlayHardball' : 'Hart durchgreifen!',
  'PoundKey' : 'Tasten drücken!',
  'PowerTie' : 'Kräfte messen!',
  'PowerTrip' : 'Ego-Trip!',
  'Quake' : 'Beben!',
  'RazzleDazzle' : 'Tamtam!',
  'RedTape' : 'Bürokratie!',
  'ReOrg' : 'Re-Org!',
  'RestrainingOrder' : 'Einstweilige Verfügung!',
  'Rolodex' : 'Rolodex!',
  'RubberStamp' : 'Abstempeln!',
  'RubOut' : 'Ausradieren!',
  'Sacked' : 'Entlassen!',
  'SandTrap' : 'Bunker!',
  'Schmooze' : 'Schmus!',
  'Shake' : 'Schütteln!',
  'Shred' : 'Shreddern!',
  'SongAndDance' : 'Getue!',
  'Spin' : 'Schönreden!',
  'Synergy' : 'Synergie!',
  'Tabulate' : 'Tabellarisieren!',
  'TeeOff' : 'Loslegen!',
  'ThrowBook' : 'Verurteilen!',
  'Tremor' : 'Schaudern!',
  'Watercooler' : 'Wasserkühler!',
  'Withdrawal' : 'Abhebung!',
  'WriteOff' : 'Abschreiben!',
  }

SuitAttackTaunts = {
    'Audit': ["Ich glaube, deine Bilanz stimmt nicht.",
              "Du bist wohl in den roten Zahlen.",
              "Lass mich mal bei der Buchhaltung helfen.",
              "Deine Sollseite ist viel zu hoch.",
              "Wir wollen mal dein Vermögen prüfen.",
              "Damit hast du jetzt Schulden.",
              "Sehen wir uns mal an, wie hoch die Forderungen sind.",
              "Damit dürfte dein Konto leer sein.",
              "Höchste Zeit, mal deine Ausgaben abzurechnen.",
              "Ich habe einen Fehler in deinen Büchern gefunden.",
              ],
    'Bite': ["Möchtest du einen Bissen?",
             "Versuch mal einen Bissen hiervon!",
             "Du beißt mehr ab, als du schlucken kannst.",
             "Hunde die beißen, bellen nicht.",
             "Da wirst du dir die Zähne dran ausbeißen.",
             "Achtung, ich beiße!",
             "Ich beiße nicht nur, wenn man mich in die Enge treibt.",
             "Ich hol mir nur schnell einen Bissen. ",
             "Ich habe den ganzen Tag noch keinen Bissen gegessen.",
             "Ich möchte nur ein Bissen essen. Ist das zuviel verlangt?",
             ],
    'BounceCheck': ["Ach, zu blöd, du bist witzlos.",
                    "Von dir steht noch eine Zahlung aus.",
                    "Ich glaube, das ist dein Scheck.",
                    "Du schuldest mir was.",
                    "Ich treibe diese Forderung ein.",
                    "Dieser Scheck ist kein gültiges Zahlungsmittel.",
                    "Man wird dir das in Rechnung stellen",
                    "Bezahle das.",
                    "Das wird dich was kosten.",
                    "Ich möchte das in bar kassieren.",
                    "Das fällt dir wieder auf die Füße.",
                    "Das ist ein falscher Fuffziger.",
                    "Ich ziehe eine Bearbeitungsgebühr ab.",
                    ],
    'BrainStorm':["Ich habe Regen vorhergesagt.",
                  "Hoffentlich hast du deinen Schirm dabei.",
                  "Ich möchte dich erleuchten.",
                  "Vielleicht fällt ja was vom Himmel?",
                  "Na, du strahlst ja gar nicht mehr, Toon?",
                  "Fertig für einen ordentlichen Guss?",
                  "Ich werde dich im Sturm nehmen.",
                  "Das nenn ich eine Blitzattacke.",
                  "Ich verteile gern kalte Duschen.",
                  ],
    'BuzzWord':["Entschuldigung, wenn ich weiter auf dich einhämmere.",
                "Hast du das Neueste schon gehört?",
                "Kannst du da mithalten?",
                "Kannst du es schon auswendig, Toon?",
                "Soll ich ein gutes Wort für dich einlegen?",
                "Jeder Schlag ein Treffer.",
                "Du solltest schlagende Argumente sammeln.",
                "Versuch mal, diesem Schlag auszuweichen.",
                "Pass auf, sonst kriegst du eins auf's Dach.",
                "Du hast anscheinend einen Schlaganfall.",
                ],
    'Calculate': ["Diese Zahlen ergeben doch einen Sinn!",
                  "Hast du darauf gezählt?",
                  "Wenn wir alles zusammenzählen, geht's abwärts mit dir.",
                  "Ich helfe dir mal, eins und eins zusammenzuzählen.",
                  "Hast du alle Ausgaben eingetragen?",
                  "Nach meiner Kalkulation wirst du dich nicht mehr lange halten können.",
                  "Hier ist das Endergebnis",
                  "Wow, deine Rechnung wird immer höher.",
                  "Versuch bloß nicht, diese Zahlen zu manipulieren! ",
                  Cogs +" : 1 Toons: 0",
                  ],
    'Canned': ["Na, wie sieht's draußen aus?",
               "Du kannst dich gleich wegschmeißen.",
               "Frisch rausgeschmissen ist halb verloren.",
               "Du schmeißt mit dem Schinken nach der Wurst.",
               "Der Rausschmiss lauert überall.",
               "Mensch, ärgere dich nicht.",
               "Eene-meene-maus, und du bist raus.",
               "Ich schmeiß dich raus!",
               "Ich schmeiß dich raus und mach mir nichts draus!",
               "Raus!!",
               ],
    'Chomp': ["Schau dir diese Raffzähne an!",
              "Mampf-mampf-mampf!",
              "Hier ist was zu mampfen.",
              "Suchst du nach was zu mampfen?",
              "Da wirst du ordentlich dran zu kauen haben.",
              "Dich verspeis ich zum Abendessen.",
              "Ich fress gern kleine Toons!",
              ],
    'ClipOnTie': ["Du solltest dich für unser Treffen lieber warm anziehen.",
                  "Ohne deinen Schlips kommst du nicht RAUS.",
                  "Die elegantesten "+ Cogs +  " tragen sowas.",
                  "Probier mal die Größe.",
                  "Für den Erfolg musst du dich gut anziehen.",
                  "Keine Krawatte, keine Bedienung.",
                  "Brauchst du Hilfe beim Anlegen?",
                  "Nichts strahlt so viel Macht aus wie eine gute Krawatte.",
                  "Schaun wir, mal, ob diese passt.",
                  "Die wird dir die Luft abdrücken.",
                  "Du solltest dich gut anziehen, bevor du RAUS gehst.",
                  "Ich denke, ich ziehe jetzt mal den Knoten fest.",
                  ],
    'Crunch': ["Du reibst dich wohl gerade auf.",
               "Malmzeit!",
               "Ich gebe dir mal was zu kauen!",
               "Hier, zermalm das mal!",
               "Da kann gut zermalmen.",
               "Magst du es lieber weich oder bissfest?",
               "Ich hoffe, du bist bereit für die Malmzeit.",
               "Siehst aus, als solltest du zermalmt werden!",
               "Ich zermalm dich wie einen Käfer."
               ],
    'Demotion': ["Du steigst auf der Karriereleiter ab.",
                 "Ich schick dich zurück in die Poststelle.",
                 "Gib dein Namensschild zurück.",
                 "Ab geht er, der Peter!",
                 "Du sitzt wohl fest.",
                 "Geh dorthin zurück, woher du gekommen bist.",
                 "Du sitzt in einer Sackgasse.",
                 "In nächster Zeit wird sich bei dir gar nichts bewegen.",
                 "Du kommst nirgendwo mehr hin.",
                 "Das wird ein schwarzer Fleck in deiner Personalakte.",
                 ],
    'Downsize': ["Komm runter!",
                 "Weißt du, wie du runter kommst?",
                 "Da wollen wir uns doch mal dran machen.",
                 "Was ist los? Du siehst so niedergeschlagen aus.",
                 "Geht's bergab?",
                 "Was geht nieder? Du!",
                 "Ich nehme mir gern Leute vor, die niedriger stehen als ich.",
                 "Warum mach ich dich nicht einfach fertig, um nicht zu sagen, nieder?",
                 "Wart ab, bis ich niederfahre!",
                 "Wirf dich nieder, du Wurm!",
                 "Du wirst gleich was Niederschmetterndes erleben.",
                 "Dieser Angriff macht alles nieder, was sich bewegt!",
                 ],
    # Hmmm - where is double talker?
    'EvictionNotice': ["Zeit für einen Umzug.",
                       "Pack deine Taschen, Toon.",
                       "Du solltest mal über eine neue Umgebung nachdenken.",
                       "Betrachte dich als abserviert.",
                       "Du bist mit der Miete im Rückstand.",
                       "Das wird extrem ungemütlich werden.",
                       "Ich werde dich mit der Wurzel ausgraben.",
                       "Ich schicke dich Packen.",
                       "Du bist hier fehl am Platz.",
                       "Bereite dich auf eine Verlegung vor.",
                       "Du bist reif für die Insel.",
                       ],
    'EvilEye': ["Dich trifft gleich mein böser Blick.",
                "Augenblick mal.",
                "Wart mal. Ich habe was im Auge.",
                "Ich lasse dich nicht aus den Augen!",
                "Könntest du das mal für mich im Auge behalten?",
                "Ich habe einen Blick für das Böse.",
                "Ich hau dir eins auf's Auge!",
                "Ich bin so bösartig, wie's nur geht!",
                "Ich pack dich direkt ins Auge des Sturms!",
                "Sieh dich vor, ich rolle schon mit den Augen!",
                ],
    'Filibuster':["Soll ich vollmachen?",
                  "Das hier wird eine Weile dauern.",
                  "Ich könnte den ganzen Tag damit zubringen.",
                  "Ich muss noch nicht mal zwischendurch Luft holen.",
                  "Es läuft und läuft und läuft ... ",
                  "Davon kann ich gar nicht genug kriegen.",
                  "Ich kann reden, bis dir schwarz vor Augen wird.",
                  "Ich kann reden, bis dir die Ohren abfallen?",
                  "Dann werd ich mal loslegen.",
                  "Ich krieg immer noch das eine oder andere Wort dazwischen.",
                  ],
    'FingerWag': ["Ich hab dir's schon tausend Mal gesagt.",
                  "Reiß dich zusammen, Toon.",
                  "Das ist nicht zum Lachen.",
                  "Ich komme gleich rüber!",
                  "Ich hab's satt, mich ständig zu wiederholen.",
                  "Ich denke doch, wir hatten das schon mal.",
                  "Du hast keinen Respekt vor uns"+ Cogs +  ".",
                  "Jetzt pass mal auf.",
                  "Bla-bla-bla-bla-bla.",
                  "Lege es nicht darauf an, dieses Treffen abzubrechen.",
                  "Muss ich selbst dazwischen gehen?",
                  "Wir haben das alles schon mal besprochen.",
                  ],
    'Fired': ["Ich hoffe, du hast was zum Naschen mitgebracht.",
              "Hier wird's gleich ziemlich warm werden.",
              "Das dürfte dir ein wenig einheizen.",
              "Ich hoffe, du bist kaltblütig.",
              "Heiß, heißer, am heißesten.",
              "Spiel lieber nicht mit dem Feuer.",
              "Wage es, die Glut zu schüren!",
              "Das feuert vielleicht!",
              "Kannst du noch Aua sagen?",
              "Ich hoffe, du hattest Sonnenschutz drauf.",
              "Jetzt kommst du dir wohl verbraten vor?",
              "Du wirst in Flammen aufgehen.",
              "Du wirst direkt in der Hölle landen.",
              "Du bist nichts als ein Strohfeuer.",
              "Ich glaube, ich kriege grad die flammende Wut.",
              "Gleich funkt's!",
              "Na, da brat mir einer'n Storch!",
              "Ich mach dir ordentlich Feuer unter'm Hintern.",
              ],
    'FountainPen': ["Das wird böse Spuren hinterlassen.",
                    "Jetzt wollen wir dich mal in die Tinte reiten.",
                    "Ich steck dich kopfüber ins Tintenfass.",
                    "Du wirst eine gute Reinigung nötig haben.",
                    "Du solltest dich mal umziehen.",
                    "Es sprudelt so schön aus diesem Füllfederhalter.",
                    "Hier, ich nehme meinen Stift.",
                    "Kannst du meine Schrift lesen?",
                    "Ich nenne das die Feder des Schicksals.",
                    "Deine Akte ist ein wenig befleckt ... ",
                    "Du sitzt ganz schön in der Tinte, was?",
                    ],
    'FreezeAssets': ["Dein Vermögen ist meins.",
                     "Kriegst du schon kalte Füße?",
                     "Ich hoffe, du hast keine Pläne.",
                     "Damit bist du erst mal auf Eis gelegt.",
                     "Es weht ein kalter Wind.",
                     "Der Winter schlägt diesjahr zeitig zu.",
                     "Das lässt mich völlig kalt.",
                     "Mein Plan hat sich jetzt herauskristallisiert.",
                     "Es wird dich ganz kalt erwischen.",
                     "Geh lieber nicht auf dem Eis tanzen.",
                     "Ich hoffe, du magst Kalte Platte.",
                     "Ich bewahre kühles Blut.",
                     ],
    'GlowerPower': ["Schaust du mich an?",
                    "Man sagt, ich hätte einen stechenden Blick.",
                    "Ich riskiere gern mal einen Blick.",
                    "Finster, finster, Nachtgespinster!",
                    "Schau mir in die Augen, Kleines!",
                    "Was hältst du von diesen ausdrucksvollen Augen?",
                    "Meine Augen sind das Beste an mir.",
                    "Diese Augen haben was.",
                    "Kuckuck, ich seh dich!",
                    "Sieh mich an ...",
                    "Wollen wir mal einen Blick auf deine Zukunft werfen?",
                    ],
    'GuiltTrip': ["Ich werde dir einen Bußgang verordnen!",
                  "Fühlst du dich schuldig?",
                  "Das ist alles deine Schuld!",
                  "Für mich bist du immer der Schuldige!",
                  "Wate im Sumpf deiner eigenen Schuld!",
                  "Ich spreche nie wieder mit dir!",
                  "Du solltest lieber sagen, dass es dir Leid tut.",
                  "Du hast es mit mir verdorben bis in die Steinzeit und zurück!",
                  "Fertig zum Gehen?",
                  "Ruf mich an, wenn du von deinem Gang zurück bist.",
                  "Wann kommst du von deinem Gang zurück?",
                  ],
    'HalfWindsor': ["Das ist die modischste Krawatte, die dir je unterkommen wird! ",
                    "Versuch mal, dich nicht zu verknoten.",
                    "Das ist erst der Anfang vom Ende.",
                    "Du hast Glück, dass ich nicht noch einen doppelten Windsor habe!",
                    "Diese Krawatte kannst du dir gar nicht leisten. ",
                    "Ich wette, du hast einen einfachen Windsor noch nicht mal GESEHEN! ",
                    "Diese Krawatte ist nicht in deiner Liga.",
                    "Diese Krawatte wäre bei dir reine Verschwendung.",
                    "Du bist noch nicht mal die Hälfte dieser Krawatte wert!",
                  ],
    'HangUp': ["Deine Verbindung ist unterbrochen worden.",
               "Auf Wiederhören!",
               "Es ist Zeit, dass ich unsere Verbindung beende.",
               "... und ruf mich ja nicht zurück!",
               "Klick!",
               "Dieses Gespräch ist beendet.",
               "Ich trenne diese Verbindung.",
               "Bei dir legen wohl die meisten wieder auf.",
               "Anscheinend hast du eine schwache Verbindung.",
               "Deine Zeit ist abgelaufen.",
               "Ich hoffe, dass das klar und deutlich bei dir ankommt.",
               "Falsch verbunden.",
               ],
    'HeadShrink': ["Du siehst ein wenig irre aus.",
                   "Schatz, ich hab den Toon verarztet.",
                   "Ärztlichen Glückwunsch.",
                   "Irren, bis der Arzt kommt.",
                   "Ich irre, daher bin ich.",
                   "Darüber musst du doch den Kopf nicht verlieren.",
                   "Bist du jetzt ganz verrückt geworden?",
                   "Kopf hoch! Oder lieber runter?",
                   "Manche Dinge sind verrückter, als sie scheinen.",
                   "Gute Toons kommen und irren.",
                   ],
    'HotAir':["Wir haben grad eine heiße Diskussion.",
              "Du hast wohl eine Hitzewallung.",
              "Ich koche gleich über.",
              "Nichts wird so heiß gegessen, wie es gekocht wird.",
              "Ess wäre besser für dich, du hättest heiße Neuigkeiten ...",
              "Immer dran denken, wo Rauch ist, ist auch Feuer.",
              "Du siehst ein bisschen ausgebrannt aus.",
              "Da löst sich wieder eine Versammlung in Rauch auf.",
              "Jetzt sollte ich wohl noch etwas Benzin ins Feuer gießen.",
              "Ich werde die Beziehung am Köcheln halten.",
              "Ich hab ein paar heiße Tipps für dich.",
              "Luftangriff!!!",
              ],
    'Jargon':["Was für ein Unsinn.",
              "Schau mal, ob du das kapierst.",
              "Ich hoffe, ich drücke mich klar und deutlich aus.",
              "Ich werde wohl lauter sprechen müssen.",
              "Ich bestehe darauf, meine Meinung zu sagen!",
              "Ich bin sehr direkt.",
              "Zu diesem Thema muss ich meine alleingültige Meinung ausführlich darstellen.",
              "Siehst du, Worte können doch verletzen.",
              "Verstehst du, was ich meine?",
              "Worte, Worte, nichts als Worte.",
              ],
    'Legalese':["Ich habe eine Unterlassungsanordnung für dich.",
                "Du wirst rechtlich gesehen verlieren.",
                "Bist du dir über die gesetzlichen Folgen im Klaren?",
                "Du stehst nicht über dem Gesetz!",
                "Du solltest gesetzlich verboten werden.",
                "Bei mir gibt's kein rückwirkendes Strafgesetz!",
                "Die Meinungen in diesem Schlagabtausch sind nicht die von Disneys Toontown Online.",
                "Wir haften nicht für Schäden, die durch diesen Schlagabtausch entstehen.",
                "Die Ergebnisse dieses Schlagabtauschs können unterschiedlich sein.",
                "Dieser Schlagabtausch verliert seine Gültigkeit soweit ein Verbot vorhanden ist.",
                "Du passt nicht in mein Rechtssystem!",
                "Du kannst mit Rechtsangelegenheiten nicht umgehen.",
                ],
    'Liquidate':["Ich halte die Dinge gern im Fluss.",
                 "Hast du vielleicht gerade Liquiditätsprobleme?",
                 "Ich werde dein Vermögen etwas bereinigen müssen.",
                 "Höchste Zeit, mit dem Strom zu schwimmen.",
                 "Denk dran, wenn es nass ist, rutscht man leicht aus.",
                 "Deine Zahlen schwimmen davon.",
                 "Du scheinst wegzurutschen.",
                 "Es fällt dir alles auf die Füße.",
                 "Ich würde sagen, deine Sache wird wässrig.",
                 "Du wirst weggespült.",
                 ],
    'MarketCrash':["Ich werde es hier mächtig krachen lassen.",
                   "Du wirst den Krach nicht überleben.",
                   "Ich bin mehr, als der Aktienmarkt vertragen kann.",
                   "Ich habe einen echten Crashkurs für dich!",
                   "Jetzt komme ich herabgestürzt!",
                   "Ich wüte wie ein Bulle.",
                   "Sieht aus, als würde die Börse krachen.",
                   "Du solltest lieber aussteigen!",
                   "Verkaufen! Schnell verkaufen!",
                   "Soll ich die Rezession anführen?",
                   "Alle steigen aus, solltest du das nicht auch tun?",
                   ],
    'MumboJumbo':["Ich will das mal ganz deutlich sagen.",
                  "So einfach ist das.",
                  "Genau so machen wir's.",
                  "Ich werde das mal für dich aufblasen.",
                  "Du sagst vielleicht Technikgelaber dazu.",
                  "Hier sind meine unbescheidenen Worte.",
                  "Junge, du nimmst den Mund vielleicht voll!",
                  "Manche nennen mich bombastisch.",
                  "Ich will nur mal was einwerfen.",
                  "Ich denke, das sind die richtigen Worte.",
                   ],
    'ParadigmShift':["Sieh dich vor! Ich bin ziemlich wechselhaft.",
                     "Bereite dich darauf vor, dass dein Paradigma ausgewechselt wird.",
                     "Das ist doch mal ein interessantes Paradigma.",
                     "Du wirst einfach ausgewechselt werden.",
                     "Ich glaube, jetzt musst du wechseln.",
                     "Dein Wechsel ist geplatzt!",
                     "Du hast in deinem ganzen Leben noch keinen solchen Wechsel erlebt! ",
                     "Ich wechsle dich aus wie nichts.",
                     "Der Wechsel ist perfekt, ob du's glaubst oder nicht.",
                     ],
    'PeckingOrder':["Da lachen ja die Hühner!",
                    "Mit dir habe ich noch ein Hühnchen zu rupfen.",
                    "Ich mach mit dir nicht viel Federlesen.",
                    "Ich werde ganz sicher den Vogel abschießen!",
                    "Du stehst in der Hackordnung ganz unten.",
                    "Lieber einen Vogel in meiner Hand als zehn auf deinem Dach!",
                    "Wir schrägen Vögel müssen zusammenhalten! ",
                    "Warum ich nicht auf jemandem rumhacke, der genauso groß ist wie ich? Nö.",
                    "Eine Krähe hackt der anderen kein Auge aus, dann schon lieber dir!",
                    ],
    'PickPocket': ["Ich möchte mal deine Wertsachen prüfen.",
                   "Guck mal, was ist denn das da drüben?",
                   "Als würde man einem Baby den Schnuller wegnehmen.",
                   "Was für ein Diebstahl!",
                   "Ich halte das mal für dich.",
                   "Behalte meine Hände immer gut im Auge.",
                   "Die Hand ist schneller als das Auge.",
                   "In meinem Ärmel ist gar nichts.",
                   "Die Geschäftsleitung übernimmt keine Verantwortung für verlorene Gegenstände.",
                   "Wer's findet, dem gehörts auch.",
                   "Du wirst überhaupt nichts merken.",
                   "Eins für mich, keins für dich.",
                   "Ich bin so frei.",
                   "Das wirst du nicht mehr brauchen ...",
                   ],
    'PinkSlip': ["Mach nur nicht blau.",
                 "Ist dir kalt? Du bist ganz blau.",
                 "Du wirst dein blaues Wunder erleben.",
                 "Na hoppla, bist du blau?",
                 "Pass nur auf, dass du nicht blau wirst!",
                 "Ich geb's dir mit Brief und Siegel!",
                 "Ich hau dich grün und blau.",
                 "Das hast du doch verbrieft, oder.",
                 "Blau steht dir nicht.",
                 "Hier ist dein blauer Brief, verschwinde hier!",
                 ],
    'PlayHardball': ["Du willst es also darauf anlegen?",
                     "Ich rate dir, dich nicht mit mir anzulegen.",
                     "Härte zeigen!",
                     "Na schlag doch, los!",
                     "Durch dich kann ich doch durchgreifen ...",
                     "Ich schaff hier gleich mal Ordnung.",
                     "Hart, aber gerecht.",
                     "Benimm dich, sonst fliegst du raus.",
                     "Wenn's hart auf hart kommt, verlierst du!",
                     "Wird ganz schön hart für dich!",
                     "Bist du hart im Nehmen?",
                     "Ich geb dir eine harte Nuss zu knacken!",
                    ],
    'PoundKey': ["Höchste Zeit für ein paar Rückrufe.",
                 "Verdrück dich!",
                 "Diese Sache wird dich unter Druck setzen.",
                 "Da will jemand die Preise drücken.",
                 "Ich habe eine Menge Druck zu bieten.",
                 "Jetzt bin ich am Drücker!",
                 "Ich geb nur mal diese Zahl ein.",
                 "Gleich mach ich dir Druck.",
                 "Du hast überhaupt keinen Tastsinn.",
                 "OK, Toon, ich drück dich an die Wand.",
                 ],
    'PowerTie': ["Ich komm später nochmal, du siehst ziemlich kraftlos aus.",
                 "Fertig zum Armdrücken?",
                 "Meine Damen und Herren, es steht unentschieden!",
                 "Du solltest lernen, deine Kräfte richtig zu messen.",
                 "Pass auf, ich nehme Maß!",
                 "Gleich ist das Maß voll!",
                 "Was maßt du dir an!?",
                 "Das gibt eine kräftige Abreibung!",
                 "Kraft meiner Wassersuppe werde ich dich erledigen!",
                 "Ich bin ein Teil von jener Kraft, die das Böse will und das Böse schafft!",
                 ],
    'PowerTrip': ["Pack deine Sachen, wir machen einen kleinen Trip.",
                  "Guter Trip?",
                  "Wie geht's dem Ego?",
                  "Wie war der Trip?",
                  "Lass dich nicht aufhalten!",
                  "Außer Spesen nichts gewesen.",
                  "Warum denn in die Ferne schweifen!",
                  "Besser schlecht gefahren als gut gelaufen. ",
                  "Mein Ego hält das aus.",
                  "Ego ist Ego.",
                  "Mein Ego ist größer als deins!",
                  ],
    'Quake': ["Beben und beben lassen.",
              "Hier bebt eine ganze Menge!",
              "Ich sehe dich in deinen Schuhen erbeben.",
              "Da kommt es schon, und es ist gewaltig!",
              "Das sprengt die Richter-Skala.",
              "Jetzt wird die Erde beben!",
              "He, was zittert da? Du!",
              "Schon mal ein Erdbeben erlebt?",
              "Du bewegst dich auf unsicherem Boden!",
              ],
    'RazzleDazzle': ["Viel Lärm um nichts.",
                     "Heute haun wir auf die Pauke!",
                     "Du kannst schon mal alle zusammentrommeln.",
                     "Ich mache gleich einen riesigen Aufriß!",
                     "Du wirst nach meiner Trommel tanzen!",
                     "Jetzt wird ein Fass aufgemacht.",
                     "Dir wird Hören und Sehen vergehen.",
                     "Wer wird denn hier so ein TamTam machen!",
                     "Willst du das an die große Glocke hängen?",
                     "Klappern gehört zum Handwerk.",
                     "Du wirst mit Pauken und Trompeten durchfallen!",
                     ],
    'RedTape': ["Besser Bürokratie als nie.",
                "Ich werde dich ein wenig aufhalten.",
                "Das geht alles seinen geregelten Gang.",
                "Ein Stempelchen gefällig?",
                "Dein Vorgang kommt in die Ablage P.",
                "Je länger, je lieber.",
                "Was lange währt, wird gut.",
                "Ich werde dich schon beschäftigen.",
                "Versuch nur mal, dich da durchzukämpfen.",
                "Du hast vergessen das Formular auszufüllen.",
                ],
    'ReOrg': ["Dir gefällt nicht, wie ich hier reorganisiert habe?",
              "Ein bisschen Reorganisation muss sein.",
              "Du bist ja gar nicht so schlecht, du musst nur umorganisiert werden.",
              "Gefallen dir meine organisatorischen Fähigkeiten?",
              "Ich dachte mir, ich sollte die Dinge mal anders aussehen lassen.",
              "Du musst dich besser organisieren!",
              "Du siehst ein bisschen desorganisiert aus.",
              "Halt mal still, während ich deine Gedanken reorganisiere. ",
              "Ich warte nur, bis du dich mal ein bisschen organisiert hast.",
              "Du hast doch nichts dagegen, wenn ich nur mal ein bisschen reorganisiere?",
              ],
    'RestrainingOrder': ["Ist ja nur einstweilig. ",
                         "Ich hau dir eine Einstweilige Verfügung um die Ohren!",
                         "Du darfst dich mir nicht mal auf zwei Meter nähern.",
                         "Vielleicht solltest du dich lieber fern halten.",
                         "Man sollte über dich verfügen.",
                         Cogs +" ! Haltet diesen Toon zurück!",
                         "Versuch doch mal, dich zurückzuhalten.",
                         "Ich hoffe, dass ich eine starke Verfügung bin für dich.",
                         "Probier mal, ob du diese Verfügung aufheben kannst!",
                         "Ich verfüge, dass du dich einstweilen zurückhalten sollst!",
                         "Warum fangen wir nicht mit einer Grundausbildung im Zusammenreißen an?"
                         ],
    'Rolodex': ["Deine Karte ist hier irgendwo drin.",
                "Hier ist die Nummer eines Schädlingsbekämpfers.",
                "Ich möchte dir meine Karte geben.",
                "Ich habe deine Nummer immer dabei.",
                "Ich habe alle Informationen über dich.",
                "Organisation ist alles.",
                "Schluss mit der Zettelwirtschaft!",
                "Pass auf, dass du nicht aus meiner Rotationskartei fliegst!",
                "Deine Schutzhülle nützt dir gar nichts.",
                "Kann ich dich so kontaktieren?",
                "Ich möchte sichergehen, dass wir in Verbindung bleiben.",
                ],
    'RubberStamp': ["Ich hinterlasse stets einen guten Eindruck.",
                    "Es ist wichtig, einen festen und gleichmäßigen Druck auszuüben.",
                    "Jedes Mal ein perfekter Abdruck.",
                    "Ich möchte dich abstempeln.",
                    "Du wirst ZURÜCK AN DEN ABSENDER geschickt.",
                    "Du wurdest für UNGÜLTIG erklärt.",
                    "Du wirst per EXPRESS verschickt.",
                    "Ich sorge dafür, dass du meine Mitteilung ERHALTEN wirst.",
                    "Du wirst dich nirgendwo hin verdrücken - erst die NACHNAHME bezahlen.",
                    "Ich brauche eine Antwort - es EILT! ",
                    ],
    'RubOut': ["Hokuspokus, Verschwindibus!",
               "Ich habe das Gefühl, dass du irgendwie weg bist.",
               "Ich habe beschlossen, dich auszulassen.",
               "Ich radiere immer aus, was mir nicht passt.",
               "Ich radiere nur mal diesen kleinen Fehler weg.",
               "Wenn ich will, verschwindet alles Störende.",
               "Ich gern alles schön sauber und ordentlich.",
               "Aus den Augen, aus dem Sinn!",
               "Grad sah ich dich noch, schon bist du weg ... ",
               "Schon wirst du blass und blässer ...",
               "Ich werde das Problem eliminieren.",
               "Ich werde mich mal um deine Problemzonen kümmern.",
               ],
    'Sacked':["Sieht aus, als würdest du entlassen werden.",
              "Und ab dafür.",
              "Du fliegst in hohem Bogen raus.",
              "Nimm deine Papiere und marschiere ab.",
              "Meine Feinde werden entlassen!",
              "Ich halte den Toontown-Rekord im Entlassen.",
              "Du wirst hier nicht mehr gebraucht.",
              "Deine Zeit ist um, du bist entlassen!",
              "Meinem Entlassungsangriff kann keine Verteidigung standhalten.",
              "Wieder einer weniger.",
              ],
    'Schmooze':["Du wirst das gar nicht merken.",
                "Das wird dir gut stehen.",
                "Das hast du dir verdient.",
                "Ich meine das ganz ehrlich.",
                "Mit Schmeicheleien komme ich überall hin.",
                "Ein Lob der Torheit!",
                "Jetzt wird aber richtig dick aufgetragen.",
                "Ich werde mich über deine guten Seiten auslassen.",
                "Dafür sollte man dir ordentlich auf die Schulter klopfen.",
                "Ich werd dir Loblieder singen, dass dir die Ohren klingen.",
                "Ich will dich ja nicht vom Sockel hauen, aber ... ",
                ],
    'Shake': ["Pass auf, ich schüttel gleich mit deinem Kopf!",
              "Bist du schüttelfest?",
              "Das wird eine Schüttel-Tour.",
              "Du wirst durch mein Schüttelsieb fallen.",
              "Muss man dich vor Gebrauch schütteln?",
              "Ich bin der Schüttler vom Dienst.",
              "Höchste Zeit in Deckung zu gehen.",
              "Du scheinst etwas zerschüttelt.",
              "Fertig zum Hände schütteln?",
              "Ich werde dich schütteln, nicht rühren!",
              "Das wird dich ordentlich durchschütteln.",
              "An meiner Macht lass ich nicht schütteln! ",
              ],
    'Shred': ["Ich muss ein paar gefährliche Dinge loswerden.",
              "Ich erhöhe meinen Durchsatz.",
              "Ich glaube, ich werde dich gleich mal entsorgen.",
              "Dadurch werden Beweise vernichtet.",
              "Jetzt kann man nichts mehr beweisen.",
              "Schau mal, ob du dir das wieder zusammensetzen kannst.",
              "Das dürfte dich auf eine angemessene Größe bringen.",
              "Ich werde diese Idee in Stücke reißen.",
              "Wir wollen doch nicht, dass das in falsche Hände gerät.",
              "Wie gewonnen, so zerronnen.",
              "Da fährt dein letztes Schnipselchen Hoffnung dahin!",
              ],
    'Spin': ["Wie wär's mit einer kleinen Redetour?",
             "Das kannst auch du nicht schönreden!",
             "Das wird ganz schön wehtun!",
             "Ich sag's dir mal vor.",
             "Pass auf. Das sind nur schöne Worte.",
             "Meinem Redeschwall ist keiner gewachsen!",
             "Da läuft dir ja die Zunge über ...",
             "Schön, dass du noch sprechen kannst.",
             "Nichts als Worte - aber schön.",
             ],
    'Synergy': ["Ich werde das vor den Ausschuss bringen.",
                "Dein Projekt ist gestrichen worden.",
                "Dein Budget wurde gekürzt.",
                "Wir strukturieren deine Abteilung um.",
                "Ich lasse darüber abstimmen, und du verlierst.",
                "Ich habe gerade die endgültige Zustimmung erhalten.",
                "Ein gutes Team kann sich jedes Problems entledigen.",
                "Ich komme wegen dieser Sache wieder auf dich zurück.",
                "Dann fangen wir mal an. ",
                "Betrachte das als Synergiekrise.",
                ],
    'Tabulate': ["Diese Zahlen ergeben keinen Sinn.",
                 "Nach meiner Rechnung verlierst du.",
                 "Jetzt wird tabula rasa gemacht.",
                 "Deine Rechnung geht nicht auf.",
                 "Bist du für diese Zahlen bereit?",
                 "Jetzt kriegst du die Quittung.",
                 "Zeit für die Endabrechnung.",
                 "Ich bringe die Dinge gern in Ordnung.",
                 "Und der aktuelle Stand ist ...",
                 "Diese Zahlen dürften sich als ziemlich wirksam erweisen.",
                 ],
    'TeeOff': ["Du bist noch nicht bereit.",
               "Jetzt geht's los!",
               "Jetzt fang ich erst mal richtig an.",
               "Hol schon mal den Wagen, Harry.",
               "Nichts überstürzen!",
               "Sieben auf einen Schlag!",
               "Der Sieg ist gewiss.",
               "Du stehst mir im Weg.",
               "Pass auf, wie ich Anlauf nehme ...",
               "Auch der längste Weg beginnt mit dem ersten Schritt.",
               "Aller Anfang ist schwer.",
               "Das ist der Anfang vom Ende.",
               ],
    'Tremor': ["Hast du das gespürt?",
               "Du hast doch keine Angst vor einem kleinen Zittern, oder?",
               "Das Zittern ist erst der Anfang.",
               "Du siehst zittrig aus.",
               "Ein kleines Beben hat noch niemandem geschadet.",
               "Bist du bereit zu zittern und zu zagen?",
               "Was ist los? Du siehst erschüttert aus.",
               "Das schaudert's dich, was?",
               "Was zitterst du vor Furcht?",
               ],
    'Watercooler': ["Das sollte dich abkühlen.",
                    "Ist das nicht erfrischend?",
                    "Das ist Wasser auf meine Mühlen.",
                    "Wasser gepredigt und Wein getrunken.",
                    "Mach keine Panik, das ist doch nur Mineralwasser.",
                    "Keine Angst, es ist gereinigt.",
                    "Aha, noch ein zufriedener Kunde.",
                    "Ich denke, dein Plan wird ins Wasser fallen.",
                    "Ich hoffe, deine Farben laufen nicht weg.",
                    "Kleine Abkühlung gefällig?",
                    "Das wäscht sich aus!",
                    "Die nächste Runde zahlst du.",
                    ],
    'Withdrawal': ["Ich glaube, du hast überzogen.",
                   "Ich hoffe, dass dein Kontostand hierfür ausreicht.",
                   "Das geht auf mein Konto.",
                   "Dein Konto ist gesperrt.",
                   "Du wirst bald was einzahlen müssen.",
                   "Du hast einen wirtschaftlichen Zusammenbruch erlitten.",
                   "Ich glaube, du steckst in der Krise.",
                   "Deine Finanzen sind abgestürzt.",
                   "Ich sehe eine absolute Talfahrt voraus.",
                   "Das Glück wendet sich.",
                   ],
    'WriteOff': ["Lass mich deine Verluste vergrößern.",
                 "Wir wollen aus einem schlechten Deal das Beste machen.",
                 "Es ist Zeit, die Bücher abzuschließen.",
                 "Das wird sich in deinen Büchern nicht gut ausnehmen.",
                 "Ich hoffe auf Dividenden.",
                 "Du musst deine Verluste nachweisen.",
                 "Einen Bonus kannst du vergessen.",
                 "Ich werde deine Zahlen ein wenig hin und her schieben.",
                 "Du wirst ein paar Verluste erleiden.",
                 "Das wird deinen Gewinn beeinträchtigen.",
                 ],
    }

# DistributedBuilding.py
BuildingWaitingForVictors = "Auf andere Spieler warten ...",

# Elevator.py
ElevatorHopOff = "Aussteigen"

# DistributedBuilding.py
# DistributedElevatorExt.py
CogsIncExt = ", AG "
CogsIncModifier = "%s"+ CogsIncExt
CogsInc = string.upper(Cogs) + CogsIncExt

# DistributedKnockKnockDoor.py
DoorKnockKnock = "Poch-poch."
DoorWhosThere = "Wer da?"
DoorWhoAppendix = " wer?"
DoorNametag = "Tür"

# FADoorCodes.py
# Strings associated with codes
FADoorCodes_UNLOCKED = None
FADoorCodes_TALK_TO_TOM = "Du brauchst Gags! Sprich mal mit Einweiser Eddie!"
FADoorCodes_DEFEAT_FLUNKY_HQ = "Komm wieder her, wenn du den Kriecher vertreiben hast!"
FADoorCodes_TALK_TO_HQ = "Hol dir deine Belohnung bei Mitarbeiter Harry!"
FADoorCodes_WRONG_DOOR_HQ = "Falsche Tür! Nimm die andere Tür zum Spielplatz!"
FADoorCodes_GO_TO_PLAYGROUND = "Falsch! Du musst doch zum Spielplatz!"
FADoorCodes_DEFEAT_FLUNKY_TOM = "Geh zu diesem Kriecher hin und schlage ihn!"
FADoorCodes_TALK_TO_HQ_TOM = "Hol dir deine Belohnung aus der Toontown-Zentrale!"
FADoorCodes_SUIT_APPROACHING = None  # no message, just refuse entry.
FADoorCodes_BUILDING_TAKEOVER = "Pass auf! Da ist ein BOT drin!"
FADoorCodes_DISGUISE_INCOMPLETE = "Man wird dich schnappen, wenn du da als Toon reingehst! Du musst erst deine Verkleidung als Bot vervollständigen!\n\nStelle deine Bot-Verkleidung aus Teilen aus der Fabrik zusammen."

# KnockKnockJokes.py
KnockKnockJokes = [
    ["Leiter",
    "Leiter ist heute geschlossen."],

    ["Albert",
    "Albert hier jemand rum?"],

    ["Andre",
    "Andre Tür, hier bist du falsch."],

    ["Anke",
    "Anke-tten schützt vor Fahrraddiebstahl."],

    ["Anna",
    "Anna-nas essen macht Spaß!"],

    ["Armin",
    "Armin-Arm gehen sie durch den Park."],

    ["Axel",
    "Axel Schweiß stinkt."],

    ["Basti",
    "Na, Basti Hose?"],

    ["Benno",
    "Wie soll dein Lehrer denn das Benno-ten?"],

    ["Ben",
    "Ben-zin wird auch immer teurer."],

    ["Boris",
    "Boris mir heiß!!"],

    ["Britt",
    "Gib mir mal deinen Britt-Stift zum Kleben!"],

    ["Clair",
    "Mein Bruder ist in die Clair-Grube gefallen."],

    ["Cindy",
    "Oh, Perlen - Cindy echt?"],

    ["Connie",
    "Habt ihr auch Connie-feren vorm Haus?"],

    ["Cora",
    "Cora-llenriffe gibt's in der Südsee."],

    ["Diana",
    "Ich war das nicht - Diana-re wars."],

    ["Dieter",
    "Dieter-miten zerfressen ganze Häuser."],

    ["Dirk",
    "Dirk-laubt sowieso keiner mehr was."],

    ["Ellen",
    "Ellen-bogenschützer sind gut für Skater."],

    ["Erich",
    "Erichten wir hier wollen wir unser Lager."],

    ["Ernst",
    "Ernst-haft, ich heiße wirklich "+ Flippy +  "."],

    ["Duck",
    Donald +" Duck-uckst du, was!"],

    ["Max",
    "Maxtu noch was essen?"],

    ["Ernest",
    "Ernest noch ins Bett!!"],

    ["Amos",
    "Amos-kito hat mich gestochen."],

    ["Alma",
    "Almaufwärts sieht's noch schöner aus."],

    ["Ernie",
    "Ernie-ste laut und heftig."],

    ["Esra",
    "Esra-icht nicht, was ich eingekauft habe."],

    ["Frank",
    "Du musst den Brief noch Frank-ieren."],

    ["Franz",
    "Franz-ösisch kann ich auch!"],

    ["Gerrit",
    "Er Gerrit dazwischen."],

    ["Ida",
    "W-Idas denn!"],

    ["Gitta",
    "Gitta-stäbe biegt man nicht so leicht auf."],

    ["Holger",
    "Ich Holger-ne ein Eis für euch."],

    ["Kaviar",
    "Kaviar keene Zähne mehr."],

    ["Kasimir",
    "Kasimir alle ausjeschlagen."],

    ["Inga",
    "Die Luftpumpe ist grad Inga-brauch."],

    ["Ingolf",
    "Ingolf bin ich ganz gut."],

    ["Iris",
    "Iris schlecht vom Essen."],

    ["Isolde",
    "Isolde baden, bin ganz dreckig."],

    ["Jan",
    "Janeinweißnicht."],

    ["Joe Kurt",
    "Joe-Kurt ess ich für mein Leben gern!"],

    ["Lasse",
    "Lasse reinfalln!"],

    ["Karl",
    "Muss mal auf den Karl-ender schauen."],

    ["Keith",
    "Kies kommt aus der Keith-Grube."],

    ["Thea",
    "Thea-terkarten sind ausverkauft."],

    ["Knut",
    "Knut-schen verboten!"],

    ["Lars",
    "Lars gut sein, ich hol's mir selber."],

    ["Lotte",
    "Lotte-rielose gibt's am Kiosk."],

    ["Marga",
    "Marga-rine ist keine mehr da."],

    ["Marina",
    "Machst du noch die Marina-de für das Fleisch?"],

    ["Martha",
    "Wenn du frech wirst, kommst du an den Martha-Pfahl!"],

    ["Moni",
    "Wie lange sitzt du schon vor dem Moni-tor?"],

    ["Naomi",
    "Naomi, müde?"],

    ["Neal",
    "Fahr doch mit ins Neal-Delta!"],

    ["Nick",
    "Papa las Zeitung und Nick-te ein."],

    ["Paul",
    "Wo ist denn auf diese Baustelle die Paul-eitung?"],

    ["Pepe",
    "Vorsicht, da sind Pepe-roni dran!"],

    ["Peter",
    "Peter-silie wächst im Garten."],

    ["Polly",
    "Polly-zei! Hilfe!"],

    ["Rainer",
    "Rainer Zufall, dass wir uns treffen."],

    ["Rosi",
    "Rosi-nen ess ich nicht."],

    ["Rudi",
    "Rudi-ch erst mal aus!"],

    ["Ruth",
    "Ruth ruth sich auch aus."],

    ["Sarah",
    "Er flog in den Schlamm und Sarah-benschwarz aus."],

    ["Steve",
    "Ist das dein richtiger Vater oder dein Steve-Vater?"],

    ["Sue",
    "Kommste mit in den Sue-permarkt?"],

    ["Theo",
    "Mein Theo-dorant wirkt nicht mehr!"],

    ["Tom",
    "Schmeiß nicht mit Tom-aten."],

    ["Till",
    "Till-siter schmeckt lecker, aber stinkt."],

    ["Vince",
    "So ein Vince-ling!"],

    ["Du",
    "Du - wer! Ist hier etwa jemand?"],

    ["Walter",
    "Walter-beiter arbeiten im Wald."],

    ["Wanda",
    "Da geht's steil runter, bleib lieber auf dem Wanda-Weg."],

    ["Wayne",
    "Na und, Wayne stört's?"],

    ["Werner",
    "Werner-vt hier?"],

    ["Willi",
    "Und bist du nicht Willi-g ..."],

    ["Wotan",
    "Wotan-nen wachsen, fallen Tannenzapfen."],

    ["Evi",
    "Evi eklig!!"],

    ["Izmir",
    "Izmir schlecht!"],

    ["Mitsubishi!",
    "Gesundheit!"],

    ["Komma",
    "Komma schnell rein!"],

    ["Fenster",
    "Fenster Lehrer merkt, kriegste Ärger!"],

    ["Eintritt",
    "Eintrittel davon reicht."],

    ["Purzel",
    "Du benimmst dich wie ein Elefant im Purzelanladen."],

    ["Tank",
    "Bitte schön."],

    ["Reh",
    "Iss schnell dein Erbsenpü-Reh."],

    ["Pizza",
    "Ich hab schon pizzahlt."],

    ["Denken",
    "Denken ich doch?"],

    ["Schaf",
    "Mann, das ist aber schaf gewürzt!"],

    ["Fahrrad",
    "Fahrrad ich dir nicht."],

    ["Lamm",
    "Lammentier hier nicht rum!"],

    ["Zunge",
    "Zunge, komm bald wieder ..."],

    ["Q",
    "Du blöde Q!"],

    ["Chris",
    "Chris du nicht mit, wer ich bin?"],

    ["Acht",
    "Achtung, ich komm jetzt rein."],

    ["Eishockey",
    "Eishockey mit dir?"],

    ["Kanufahrn",
    "Ich hab nichts, getrunken, ich kanufahrn."],

    ["Wirsing",
    "Machs gut und Auf Wirsing."],

    ["X",
    "Xtreme Temperaturen habt ihr hier."],

    ["Haydn",
    "Das macht `nen Haydnspaß."],

    ["Ente",
    "Enteweder - oder."],

    ["Feder",
    "Wenn die Feder mit ihren Söhnen ..."],

    ["Arm",
    "Lieber arm dran als Arm ab."],

    ["Nachname",
    "Schick das Paket per Nachname."],

    ["Gans",
    "Du bist gans schön frech!"],

    ["Ekel",
    "Schon mal so'n fetten Blutekel gesehen?"],

    ["Halligen",
    "Tolles Auto mit Halligen-Scheinwerfern!"],

    ["Schwein",
    "Schwein' ja garnicht mehr."],

    ["Fass",
    "Fass mich bloß nicht an!"],

    ["Welke Blume",
    "Welke Blume hättest du denn gern?"],

    ["Agatha",
    "Ich hab uns was schönes Agathat."],

    ["Ungarn",
    "Ich geb dir mein Fahrrad nur Ungarn."],

    ["Polen",
    "Du musst das Gerät umpolen."],

    ["Kanada ",
    "Tut mir Leid, Kanada."],

    ["Mrs.",
    "Mrs. Sippi und Miss Ouri"],

    ["Rhein",
    "Das war vielleicht ein Rheinfall!"],
]

# ChatInputNormal.py
ChatInputNormalSayIt = "Sag es"
ChatInputNormalCancel = lCancel
ChatInputNormalWhisper = "Flüstern"
ChatInputWhisperLabel = "Nach %s"

# ChatInputSpeedChat.py
SCEmoteNoAccessMsg = "Du hast noch keinen Zugriff\nauf dieses Gefühl."
SCEmoteNoAccessOK = lOK

# ChatManager.py
ChatManagerChat = "Chat"
ChatManagerWhisperTo = "Flüstern mit:"
ChatManagerWhisperToName = "Flüstern mit:\n%s"
ChatManagerCancel = lCancel
ChatManagerWhisperOffline = "%s ist offline."
OpenChatWarning = 'Du hast noch keine "Geheimen Freunde"! Du kannst nicht mit anderen Toons chatten, bevor sie nicht deine Geheimen Freunde sind.\n\nWenn jemand dein Geheimer Freund werden soll, dann klicke ihn an und wähle "Geheimnisse" aus der Einzelheitenliste. Natürlich kannst du immer über den Schnell-Chat mit allen sprechen.'
OpenChatWarningOK = lOK
UnpaidChatWarning = 'Wenn du dich eingetragen hast, kannst du dich mit dieser Schaltfläche mit deinen Freunden per Tastatur unterhalten. Bis dahin solltest du über den Schnell-Chat mit anderen Toons chatten.'
UnpaidChatWarningPay = "Jetzt eintragen!"
UnpaidChatWarningContinue = "Kostenlosen Probelauf fortsetzen"
PaidNoParentPasswordWarning = 'Wenn du dein Elternpasswort festgelegt hast, kannst du diese Schaltfläche aktivieren um dich per Tastatur mit deinen Freunden zu unterhalten. Bis dahin solltest du per Schnell-Chat mit anderen Toons chatten.'
PaidNoParentPasswordWarningSet = "Elternpasswort jetzt festlegen!"
PaidNoParentPasswordWarningContinue = "Weiter spielen"
PaidParentPasswordUKWarning = "Wenn der Chat aktiviert ist, kann dieser Button verwendet werden, um mit Freunden per Tastatur zu chatten. Bis dahin kannst du den Schnell-Chat nutzen, um mit anderen Toons zu chatten."
PaidParentPasswordUKWarningSet = "Jetzt Chat aktivieren!"
PaidParentPasswordUKWarningContinue = "Weiterspielen"
NoSecretChatAtAllTitle = "Chat mit Geheimen Freunden"
NoSecretChatAtAll = 'Damit du mit einem Freund chatten kannst, muss zuerst die Funktion Geheime Freunde aktiviert sein. Bei Geheime Freunde kann ein Mitglied mit einem anderen Mitglied nur über einen geheimen Code chatten, der außerhalb des Spieles vereinbart werden muss.\n\nUm diese Funktion zu aktivieren oder um mehr darüber zu erfahren, beende Toontown und klicke dann auf "Account-Optionen" auf der Toontown-Website.'
NoSecretChatAtAllOK = lOK
NoSecretChatWarningTitle = "Elterliche Kontrolle"
NoSecretChatWarning = 'Damit du mit einem Freund chatten kannst, muss zuerst die Funktion Geheime Freunde aktiviert sein. Bittet eure Eltern, sich mit ihrem Elternpasswort einzuloggen, um sich über die Funktion Geheime Freunde zu informieren und auf Elterliche Kontrolle zuzugreifen.'
NoSecretChatWarningOK = lOK
NoSecretChatWarningCancel = lCancel
NoSecretChatWarningWrongPassword = 'Das ist nicht das richtige Passwort. Bitte das Elternpasswort eingeben, das beim Bezahlen dieses Accounts festgelegt wurde. Es ist nicht dasselbe Passwort, das zum Spielen des Spiels verwendet wird.'

ActivateChat = """Bei Geheime Freunde kann ein Mitglied mit einem anderen Mitglied nur über einen geheimen Code chatten, der außerhalb des Spieles vereinbart werden muss. Für eine vollständige Beschreibung hier klicken:

Geheime Freunde wird nicht moderiert oder überwacht. Wenn Eltern ihrem Kind bzw. ihren Kindern erlauben, ihren Account mit der aktivierten Geheime-Freunde-Funktion zu nutzen, so empfehlen wir den Eltern, ihr Kind bzw. ihre Kinder zu beaufsichtigen, während sie spielen. Die Geheime-Freunde-Funktion kann jederzeit wieder deaktiviert werden.

Durch die Aktivierung der Geheime-Freunde-Funktion erkennen Sie an, dass mit der Geheime-Freunde-Funktion einige Risiken verbunden sein können und dass Sie über diese Risiken informiert wurden und sie akzeptieren.."""

ActivateChatYes = "Aktivieren"
ActivateChatNo = lCancel
ActivateChatMoreInfo = "Mehr Infos"
ActivateChatPrivacyPolicy = "Datenschutz"

LeaveToPay = """Zum Bezahlen wird das Spiel beendet und die Seita www.Toontown-online.de aufgerufen."""
LeaveToPayYes = "Bezahlen"
LeaveToPayNo = lCancel

LeaveToSetParentPassword = """Zum Festlegen des Elternpassworts wird das Spiel verlassen und www.Toontown-online.de aufgerufen."""
LeaveToSetParentPasswordYes = "Passwort festlegen"
LeaveToSetParentPasswordNo = lCancel

LeaveToEnableChatUK = """Um den Chat zu aktivieren, wird das Spiel verlassen und die Toontown-Webseite angezeigt."""
LeaveToEnableChatUKYes = "Chat aktivieren"
LeaveToEnableChatUKNo = lCancel

ChatMoreInfoOK = lOK
SecretChatActivated = 'Das System "Geheime Freunde" wurde aktiviert!\n\nSollten Sie es sich anders überlegen und diese Funktion später wieder deaktivieren wollen, klicken Sie auf "Account-Optionen" auf der Toontown-Website.'
SecretChatActivatedOK = lOK
ProblemActivatingChat = 'Hoppla! Wir konnten die Chatfunktion "Geheime Freunde" leider nicht aktivieren. \n\n%s\n\nBitte später wieder versuchen.'
ProblemActivatingChatOK = lOK

# CChatChatter.py

# Shared Chatter

SharedChatterGreetings = [
        "Hi, %!",
        "Huhu %, schön dich zu sehen.",
        "Ich freue mich, dass du heute da bist!",
        "Na hallo, %.",
        ]

SharedChatterComments = [
        "Das ist ein toller Name, %.",
        "Dein Name gefällt mir.",
        "Nimm dich in Acht vor den "+ Cogs +  ".",
        "Ach da kommt ja der Toon-Express!",
        "Ich muss ein Spiel der Toon-Express Spiel spielen machen, um ein paar Torten zu bekommen!",
        "Manchmal spiele ich ein Spiel der Toon-Express Spiele, nur um die Obsttorte zu essen!",
        "Puh, ich hab grad ein paar "+ Cogs +  " aufgehalten. Ich muss mich ausruhen!",
        "Ihh, manche von diesen "+ Cogs +  " sind ganz schön groß!",
        "Du siehst aus, als würde es dir Spaß machen.",
        "Oh Mann, ich mach mir grad `nen schönen Tag.",
        "Gefällt mir, was du da anhast.",
        "Ich glaube, ich gehe heute Nachmittag angeln.",
        "Viel Spaß in meiner Gegend.",
        "Ich hoffe, du genießt deinen Aufenthalt in Toontown.",
        "Wie ich höre, schneit es im Brrr.",
        "Bist du heute schon mit dem Toon-Express gefahren?",
        "Ich treffe gern neue Leute.",
        "Wow, da sind ja massenhaft "+ Cogs +  " im Brrr.",
        "Ich spiele gern Fangen. Du auch?",
        "Spiele beim Toon-Express machen Spaß.",
        "Ich bring gern andere zum Lachen.",
        "Es macht mir Spaß meinen Freunden zu helfen.",
        "Ähem, hast du dich verlaufen? Denk dran, dein Stadtplan befindet sich in deinem Sticker-Buch.",
        "Versuche, dich nicht in der Bürokratie der "+ Cogs +  " zu verheddern.",
        "Ich habe gehört, "+ Daisy +  " hat ein paar neue Blumen in ihren Garten gepflanzt.",
        "Wenn du die Taste 'Bild-Hoch' drückst, kannst du nach oben schauen!",
        "Wenn du bei der Übernahme von Bot-Gebäuden hilfst, kannst du dir einen Bronze-Stern verdienen!",
        "Wenn du die Tab-Taste drückst, kannst du verschiedene Ansichten deiner Umgebung sehen!",
        "Wenn du die Strg-Taste drückst, kannst du springen!",
        ]

SharedChatterGoodbyes = [
        "Ich muss jetzt weg, tschüss!",
        "Ich werde wohl mal ein Toon-Express Spiel spielen gehen.",
        "Also mach's gut bis später, %!",
        "Ich mach mich mal lieber an die Arbeit, diese "+ Cogs +  " zu stoppen.",
        "Jetzt muss ich mich mal in Bewegung setzen.",
        "Entschuldige, muss leider weg.",
        "Auf Wiedersehen.",
        "Bis später, %!",
        "Ich werde jetzt mal Napfkuchen werfen üben.",
        "Ich werde mich einer Gruppe anschließen und ein paar "+ Cogs +  " stoppen.",
        "War schön, dass ich dich heute getroffen habe, %.",
        "Ich hab heute viel zu tun. Da fang ich mal lieber an.",
        ]

# Lines specific to each character.
# If a talking char is mentioned, it cant be shared among them all

MickeyChatter = (
        [ # Greetings specific to Mickey
        "Willkommen in Toontown Mitte.",
        "Hi, ich heiße "+ Mickey +  ". Und du?",
        ],
        [ # Comments
        "Hey, hast du "+ Donald +  " gesehen?",
        "Ich seh mir mal an, wie der Nebel bei "+ Donald +  "s Dock hereinzieht.",
        "Wenn du meinen Kumpel "+ Goofy +  " siehst, grüß ihn von mir.",
        "Ich habe gehört "+ Daisy +  " hat ein paar neue Blumen in ihren Garten gepflanzt.",
        ],
        [ # Goodbyes
        "Ich gehe zum Melodienland, " + Minnie + " besuchen!",
        "Mensch, ich komme zu spät zu meiner Verabredung mit "+ Minnie +  "!",
        "Scheint Zeit zu sein für "+ Pluto +  "s Dinner.",
        "Ich denke, ich werde bei "+ Donald +  "s Dock schwimmen gehen.",
        "Es ist Zeit für ein Nickerchen. Ich gehe ins Traumland.",
        ]
    )

MinnieChatter = (
        [ # Greetings
        "Willkommen im Melodienland.",
        "Hi, ich heiße "+ Minnie +  ". Und du?",
        ],
        [ # Comments
        "Der Klang der Musik hallt von den Bergen wider!",
        "Du musst unbedingt mal auf dem großen Plattenteller-Karussell fahren!",
        "Du hast ein cooles Outfit, %.",
        "Hey, hast du "+ Mickey +  " gesehen?",
        "Wenn du meinen Freund  "+ Goofy +  " siehst, Gruß ihn von mir.",
        "Wow, da sind massenhaft "+ Cogs +  " in der Nähe von "+ Donald +  "s Traumland.",
        "Ich habe gehört, dass es bei "+ Donald +  "s Dock sehr neblig sein soll.",
        "Du musst unbedingt das Labyrinth in "+ Daisy +  "s Gärten ausprobieren.",
        "Ich glaube, ich geh mal ein paar Melodien einfangen.",
        "Hey %, schau mal da drüben.",
        "Ich liebe den Klang der Musik.",
        "Ich wette, du hast nicht gewusst, dass Melodienland auch manchmal Ton-Town genannt wird! Hihi!",
        "Ich spiele sehr gern das Pantomime-Spiel. Du auch?",
        "Ich bringe gern andere zum Kichern.",
        "Junge, den ganzen Tag in Pumps herumlaufen geht vielleicht auf die Füße!",
        "Hübsches Oberteil, %.",
        "Ist das da auf dem Boden ein Jelly Bean?",
        ],
        [ # Goodbyes
        "Mensch, ich komme zu spät zu meiner Verabredung mit "+ Mickey +  "!",
        "Scheint Zeit zu sein für "+ Pluto +  "s Dinner.",
        "Es ist Zeit für ein Nickerchen. Ich gehe ins Traumland.",
        ]
    )

GoofyChatter = (
        [ # Greetings
        "Willkommen in "+ Daisy +  "s Gärten.",
        "Hi, ich heiße "+ Goofy +  ". Und du?",
        "Möönsch, schön dich zu sehen %!",
        ],
        [ # Comments
        "Junge, in diesem Gartenlabyrinth kann man sich ganz schön leicht verlaufen! ",
        "Probier auf jeden Fall mal das Labyrinth hier aus. ",
        "Ich habe "+ Daisy +  " den ganzen Tag nicht gesehen.",
        "Ich frage mich, wo "+ Daisy +  " ist.",
        "Hey, hast du "+ Donald +  " gesehen?",
        "Wenn du meinen Freund "+ Mickey +  " siehst, grüß ihn von mir.",
        "Oje! Ich hab vergessen "+ Mickey +  " sein Frühstück hinzustellen!",
        "Möönsch da sind ja wirklich massenhaft "+ Cogs +  " in der Nähe von "+ Donald +  "s Dock.",
        "Es sieht aus, als ob "+ Daisy +  " ein paar neue Blumen in ihrem Garten gepflanzt hat.",
        "In der Brrr-Zweigstelle meines Gag-Ladens gibt es Hypno-Brillen im Angebot für nur 1 Jelly Bean!",
        "Goofys Gag-Läden bieten die besten Witze, Tricks und Zwerchfellkitzler von ganz Toontown!",
        "In Goofys Gag-Läden bringt jede Torte im Gesicht garantiert einen Lacher, oder du bekommst deine Jelly Beans zurück!"
        ],
        [ # Goodbyes
        "Ich gehe zum Melodienland, um " + Minnie + " zu besuchen!",
        "Mensch, ich komme zu spät zu meinem Spiel mit "+ Donald +  "!",
        "Ich glaube, ich werde bei "+ Donald +  "s Dock schwimmen gehen.",
        "Es ist Zeit für ein Nickerchen. Ich gehe ins Traumland.",
        ]
    )

DonaldChatter = (
        [ # Greetings
        "Willkommen im Traumland.",
        "Hi, ich heiße "+ Donald +  ". Und du?",
        ],
        [ # Comments
        "Manchmal läuft es mir hier kalt den Rücken hinunter.",
        "Probier auf jeden Fall das Labyrinth in "+ Daisy +  "s Gärten aus.",
        "Junge, geht's mir heute gut.",
        "Hey, hast du "+ Mickey +  " gesehen?",
        "Wenn du meinen Kumpel "+ Goofy +  " siehst, grüß ihn von mir.",
        "Ich werde wohl heute Nachmittag angeln gehen.",
        "Wow, da sind massenhaft "+ Cogs +  " bei "+ Donald +  "s Dock.",
        "Hey, habe ich dich nicht mal bei "+ Donald +  "s Dock mit dem Boot mitgenommen?",
        "Ich habe "+ Daisy +  " den ganzen Tag nicht gesehen.",
        "Ich habe gehört, dass "+ Daisy +  " ein paar neue Blumen in ihren Garten gepflanzt hat.",
        "Quak.",
        ],
        [ # Goodbyes
        "Ich gehe zum Melodienland, um " + Minnie + " zu besuchen!",
        "Mensch, ich komme zu spät zu meiner Verabredung mit "+ Daisy +  "!",
        "Ich glaube, ich werde bei meinem Dock schwimmen gehen.",
        "Ich glaube, ich kurve ein bisschen mit meinem Boot bei meinem Dock rum.",
        ]
    )

for chatter in [MickeyChatter,DonaldChatter,MinnieChatter,GoofyChatter]:
    chatter[0].extend(SharedChatterGreetings)
    chatter[1].extend(SharedChatterComments)
    chatter[2].extend(SharedChatterGoodbyes)


# ToontownClientRepository.py
TCRConnecting = "Verbindung wird gesucht ..."
# host, port
TCRNoConnectTryAgain = "Keine Verbindung zu %s:%s. Nochmal versuchen?"
TCRNoConnectProxyNoPort = "Keine Verbindung zu %s:%s.\n\nDu gehst über einen Proxy ins Internet, dieser Proxy erlaubt aber keine Verbindungen an Port %s.\n\nDu musst diesen Port öffnen oder deinen Proxy deaktivieren, um Toontown zu spielen. Wenn dein Proxy von deinem ISP zur Verfügung gestellt wurde, musst du deinen ISP kontaktieren und ihn bitten, diesen Port zu öffnen."
TCRNoDistrictsTryAgain = "Es sind keine Toontown-Bezirke erreichbar. Nochmal versuchen?"
TCRLostConnection = "Deine Internetverbindung zu Toontown ist getrennt worden."
TCRBootedReasons = {
    1: "Es ist ein unerwartetes Problem aufgetreten. Deine Verbindung wurde getrennt, aber du kannst erneut eine Verbindung herstellen und wieder in das Spiel einsteigen.",
    100: "Deine Verbindung wurde getrennt, weil sich gerade jemand auf einem anderen Computer mit deinem Account eingeloggt hat.",
    120: "Deine Verbindung wurde wegen eines Problems mit deiner Berechtigung zur Nutzung des Tastatur-Chats getrennt. ",
    122: "Bei deinem Versuch, dich in Toontown einzuloggen, ist ein unerwartetes Problem aufgetreten. Bitte wende dich an den Toontown-Kundendienst.",
    125: "Deine installierten Toontown-Dateien scheinen ungültig zu sein. Bitte benutze die Schaltfläche Spielen auf der offiziellen Toontown-Website, um Toontown zu starten.",
    126: "Du hast keine Administratorrechte.",
    151: "Du wurdest von einem Administrator ausgeloggt, der an den Toontown-Servern arbeitet.",
    153: "Der Toontown-Bezirk, in dem du spielst, wurde zurückgesetzt. Die Verbindungen aller Spieler, die sich gerade dort aufhielten wurden getrennt. Du kannst jedoch erneut eine Verbindung herstellen und wieder in das Spiel einsteigen.",
    288: "Deine Spielzeit in Toontown ist für diesen Monat abgelaufen.",
    349: "Deine Spielzeit in Toontown ist für diesen Monat abgelaufen.",
    }
TCRBootedReasonUnknownCode = "Es ist ein unerwartetes Problem aufgetreten (Fehlercode %s). Deine Verbindung wurde getrennt, aber du kannst erneut eine Verbindung herstellen und wieder in das Spiel einsteigen."
TCRTryConnectAgain = "\n\nErneut verbinden?"
# avName
TCRToontownUnavailable = "Toontown scheint vorübergehend nicht erreichbar zu sein, Verbindung wird weiter versucht ..."
TCRToontownUnavailableCancel = lCancel
TCRNameCongratulations = "GLÜCKWUNSCH!!"
TCRNameAccepted = "Dein Name wurde vom Toon-Rat\ngenehmigt.\n\nVon heute an heißt\ndu\n\"%s\" "
TCRServerConstantsProxyNoPort = "Keine Verbindung zu %s:%s.\n\nDu gehst über einen Proxy ins Internet, dieser Proxy erlaubt aber keine Verbindungen an Port %s.\n\nDu musst diesen Port öffnen oder deinen Proxy deaktivieren, um Toontown zu spielen. Wenn dein Proxy von deinem ISP zur Verfügung gestellt wurde, musst du deinen ISP kontaktieren und ihn bitten, diesen Port zu öffnen."
TCRServerConstantsProxyNoCONNECT = "Keine Verbindung zu %s:%s.\n\nDu gehst über einen Proxy ins Internet, dieser Proxy erlaubt aber keine Verbindungen an Port %s.\n\nDu musst diesen Port öffnen oder deinen Proxy deaktivieren, um Toontown zu spielen. Wenn dein Proxy von deinem ISP zur Verfügung gestellt wurde, musst du deinen ISP kontaktieren und ihn bitten, diese Funktion zu aktivieren."
TCRServerConstantsTryAgain = "Keine Verbindung zu %s.\n\nDer Toontown-Account-Server ist möglicherweise vorübergehend offline oder es gibt ein Problem mit deiner Internetverbindung.\n\nErneut versuchen?"
TCRServerDateTryAgain = "Konnte keine Serverdaten von %s bekommen. Erneut versuchen?"
AfkForceAcknowledgeMessage = "Dein Toon ist müde geworden und ins Bett gegangen."
PeriodTimerWarning = "Deine Spielzeit in Toontown ist für diesen Monat fast abgelaufen!"
PeriodForceAcknowledgeMessage = "Deine Spielzeit in Toontown ist für diesen Monat abgelaufen. Komm doch nächsten Monat wieder zum Spielen!"
TCREnteringToontown = "Toontown betreten ..."

# FriendInvitee.py
FriendInviteeTooManyFriends = "%s möchte dein Freund sein, aber du hast schon zu viele Freunde auf deiner Liste!"
FriendInviteeInvitation = "%s möchte dein Freund sein."
FriendInviteeOK = lOK
FriendInviteeNo = lNo

# FriendInviter.py
FriendInviterOK = lOK
FriendInviterCancel = lCancel
FriendInviterStopBeingFriends = "Freundschaft beenden"
FriendInviterYes = lYes
FriendInviterNo = lNo
FriendInviterClickToon = "Klicke auf den Toon, mit dem du Freunschaft schließen möchtest."
FriendInviterTooMany = "Du hast schon zu viele Freunde auf deiner Liste und kannst jetzt keinen hinzufügen. Du musst ein paar Freunde entfernen, wenn du mit %s Freundschaft schließen möchtest."
FriendInviterNotYet = "Möchtest du mit %s Freundschaft schließen?"
FriendInviterCheckAvailability = "Sehe nach, ob %s erreichbar ist."
FriendInviterNotAvailable = "%s ist zurzeit beschäftigt, versuche es später noch einmal."
FriendInviterWentAway = "%s ist weggegangen."
FriendInviterAlready = "%s ist schon mit dir befreundet."
FriendInviterAskingCog = "Frage, ob %s mit dir befreundet sein möchte."
FriendInviterAskingPet = "%s springt umher, rennt im Kreis herum und leckt dir das Gesicht ab."
FriendInviterAskingMyPet = "%s ist schon dein BESTER Freund."
FriendInviterEndFriendship = "Bist du sicher, dass du die Freundschaft mit %s beenden möchtest?"
FriendInviterFriendsNoMore = "Freundschaft mit %s beendet."
FriendInviterSelf = "Du bist schon mit dir selbst 'befreundet'!"
FriendInviterIgnored = "%s ignoriert dich."
FriendInviterAsking = "Frage, ob %s mit dir befreundet sein möchte. "
FriendInviterFriendSaidYes = "%s hat ja gesagt!"
FriendInviterFriendSaidNo = "%s hat nein, danke gesagt."
FriendInviterFriendSaidNoNewFriends = "%s sucht gerade keine neuen Freunde."
FriendInviterTooMany = "%s hat schon zu viele Freunde!"
FriendInviterMaybe = "%s konnte nicht antworten."
FriendInviterDown = "Kann gerade keine Freundschaften schließen."

FriendSecretIntro = "Wenn du Disneys Toontown Online mit jemandem spielst, den du im richtigen Leben kennst, könnt ihr Geheime Freunde werden. Mit der Tastatur kannst du mit diesen Geheimen Freunden chatten. Andere Toons werden nicht verstehen, was ihr sagt.\n\nDazu musst du ein Geheimnis erwerben. Erzähle das Geheimnis deinem Freund (oder deiner Freundin), aber niemand anderem. Wenn er/sie das Geheimnis auf seinem/ihrem Bildschitrm eintippt, seid ihr Geheime Freunde in Toontown!"
FriendSecretGetSecret = "Ein Geheimnis erwerben"
FriendSecretEnterSecret = "Wenn du ein Geheimnis von jemandem mitgeteilt bekommen hast, den du kennst, tippe es hier ein. "
FriendSecretOK = lOK
FriendSecretCancel = lCancel
FriendSecretGettingSecret = "Geheimnis erwerben ..."
FriendSecretGotSecret = "Hier ist dein neues Geheimnis. Schreibe es dir auf jeden Fall auf!\n\nDu darfst dieses Geheimnis nur an eine Person weitergeben! Wenn einmal jemand dein Geheimnis eingetippt hat, funktioniert es für niemand anderen mehr. Wenn du mehr als einer Person ein Geheimnis geben möchtest, musst du dir noch ein Geheimnis holen.\n\nDas Geheimnis wirkt nur für die nächsten zwei Tage. Dein Freund muss es eintippen, bevor es verschwindet, sonst wirkt es nicht mehr.\n\nDein Geheimnis ist:"
FriendSecretTooMany = "Entschuldige, du kannst heute leider keine Geheimnisse mehr bekommen. Du hattest schon mehr als dir zustehen!\n\nVersuch es morgen wieder."
FriendSecretTryingSecret = "Geheimnis ausprobieren ..."
FriendSecretEnteredSecretSuccess = "%s ist jetzt dein Geheimer Freund!"
FriendSecretEnteredSecretUnknown = "Das ist kein gültiges Geheimnis. Bist du sicher, dass du es richtig geschrieben hast?\n\nWenn du es richtig geschrieben hast, dann ist es vielleicht abgelaufen. Bitte deinen Freund, ein neues Geheimnis für dich zu holen (oder hole selbst eins und gib es deinem Freund)."
FriendSecretEnteredSecretFull = "Du kannst mit %s keine Freundschaft schließen, weil einer von euch beiden schon zu viele Freunde auf seiner Liste hat."
FriendSecretEnteredSecretFullNoName = "Ihr könnt keine Freundschaft schließen, weil einer von euch beiden schon zu viele Freunde auf seiner Liste hat."
FriendSecretEnteredSecretSelf = "Du hast gerade dein eigenes Geheimnis eingetippt! Jetzt kann niemand anders dieses Geheimnis verwenden."
FriendSecretNowFriends = "%s ist jetzt dein Geheimer Freund!"
FriendSecretNowFriendsNoName = "Ihr seid jetzt Geheime Freunde!"

# FriendsListPanel.py
FriendsListPanelNewFriend = "Neuer Freund"
FriendsListPanelSecrets = "Geheimnisse"
FriendsListPanelOnlineFriends = "FREUNDE\nONLINE"
FriendsListPanelAllFriends = "ALLE\nFREUNDE"
FriendsListPanelIgnoredFriends = "IGNORIERTE\nTOONS"
FriendsListPanelPets = "NAHE\nHAUSTIERE"

# TeaserPanel.py
TeaserTop = "Leider ist das im Rahmen des Test-Zugangs nicht möglich.\nWenn du jetzt abonnierst, kannst du diese coolen Features nutzen:"
TeaserOtherHoods = "Besuche alle sechs einzigartigen Stadtteile!"
TeaserTypeAName = "Nimm teil an toontastischen Wettbewerben!"
TeaserSixToons = "Baue dir mit einem einzigen Account bis zu sechs Toons!"
TeaserOtherGags = "Erwirb sechs Fähigkeitsstufen für sechs verschiedene Gag-Tracks!"
TeaserClothing = "Entwirf spezielle Kleidungsstücke für\ndeinen ganz persönlichen Toon!"
TeaserFurniture = "Kaufe Möbelstücke und richte damit dein Haus ein!"
TeaserCogHQ = "Dringe heimlich in gefährliche von\nBots beherrschte Bereiche vor!"
TeaserSecretChat = "Tausche mit Freunden Geheimnisse aus,\ndamit du mit ihnen online chatten kannst!"
TeaserCardsAndPosters = "Als offizieller Einwohner erhältst du den Toontown Willkommensbrief\nmit einem coolen Bot-Poster und schicken Toontown Aufklebern!"
TeaserHolidays = "Nimm an tollen Events der Stadt teil!"
TeaserQuests = "Löse Hunderte von Toon-Aufgaben, um Toontown mit zu retten!"
TeaserEmotions = "Kaufe Emotionen, damit dein Toon mehr Ausdruck bekommt!"
TeaserMinigames = "Spiele alle 8 Minigames!"
TeaserSubscribe = "Jetzt abonnieren"
TeaserContinue = "Probezeit fortsetzen"

# DownloadForceAcknowledge.py
# phase, percent
DownloadForceAcknowledgeMsg = "Du kannst leider nicht weitergehen, weil der Download vom %(phase)s erst zu %(percent)s%% abgeschlossen ist.\n\nBitte versuch es später noch einmal."

# DownloadWatcher.py
# phase, percent
DownloadWatcherUpdate = "%s wird heruntergeladen "
DownloadWatcherInitializing = "Download wird vorbereitet ..."

# Launcher.py
LauncherPhaseNames = {
    0   : " Vorbereitung",
    3   : " Toon Kreieren",
    3.5 : " Anleitung",
    4   : " Spielplatz",
    5   : " Straße",
    5.5 : " Grundstück",
    6   : " Viertel I",
    7   : Cog + "-Gebäude",
    8   : " Viertel II",
    9   : " Bot-Hauptquartier",
    }

# Lets make these messages a little more friendly
LauncherProgress = "%(name)s (%(current)s von %(total)s)"
LauncherStartingMessage = "Disneys Toontown Online wird gestartet ... "
LauncherDownloadFile = "Update für "+ LauncherProgress + " wird heruntergeladen ..."
LauncherDownloadFileBytes = "Update für "+ LauncherProgress + " wird heruntergeladen: %(bytes)s"
LauncherDownloadFilePercent = "Update für "+ LauncherProgress + " wird heruntergeladen: %(percent)s%%"
LauncherDecompressingFile = "Update für "+ LauncherProgress + " wird entkomprimiert ..."
LauncherDecompressingPercent = "Update für "+ LauncherProgress + " wird entkomprimiert: %(percent)s%%"
LauncherExtractingFile = "Update für "+ LauncherProgress + " wir extrahiert ..."
LauncherExtractingPercent = "Update für "+ LauncherProgress + " wird extrahiert: %(percent)s%%"
LauncherPatchingFile = "Update für "+ LauncherProgress + " wird implementiert ..."
LauncherPatchingPercent = "Update für "+ LauncherProgress + " wird implementiert: %(percent)s%%"
LauncherConnectProxyAttempt = "Verbindung zu Toontown: %s (Proxy: %s) Versuch: %s"
LauncherConnectAttempt = "Verbindung zu Toontown: %s Versuch %s"
LauncherDownloadServerFileList = "Update Toontown läuft ..."
LauncherCreatingDownloadDb = "Update Toontown läuft ..."
LauncherDownloadClientFileList = "UpdateToontown läuft ..."
LauncherFinishedDownloadDb = "Update Toontown läuft ... "
LauncherStartingToontown = "Toontown wird gestartet ..."
LauncherRecoverFiles = "Update Toontown läuft. Dateien werden wiederhergestellt ..."
LauncherCheckUpdates = "Updates für" + LauncherProgress
LauncherVerifyPhase = "Update Toontown läuft ..."

# AvatarChoice.py
AvatarChoiceMakeAToon = "Toon\nkreieren"
AvatarChoicePlayThisToon = "Toon\neinsetzen"
AvatarChoiceSubscribersOnly = " Jetzt\n\n\n\n\nabonnieren!"
AvatarChoiceDelete = "Löschen"
AvatarChoiceDeleteConfirm = "Hiermit wird %s für immer gelöscht."
AvatarChoiceNameRejected = "Name\nabgewiesen"
AvatarChoiceNameApproved = "Name\nbestätigt!"
AvatarChoiceNameReview = "Wird\ngeprüft"
AvatarChoiceNameYourToon = "Gib\ndeinem Toon einen Namen!"
AvatarChoiceDeletePasswordText = "Achtung! Damit wird %s für immer gelöscht. Gib dein Passwort ein um diesen Toon zu löschen."
AvatarChoiceDeleteConfirmText = "Achtung! Damit wird %(name)s für immer gelöscht. Wenn du sicher bist, dass du dies tun willst, gib \"%(confirm)s\" ein und klicke auf OK."
AvatarChoiceDeleteConfirmUserTypes = "Löschen"
AvatarChoiceDeletePasswordTitle = "Toon löschen?"
AvatarChoicePassword = "Passwort"
AvatarChoiceDeletePasswordOK = lOK
AvatarChoiceDeletePasswordCancel = lCancel
AvatarChoiceDeleteWrongPassword = "Das Passwort scheint nicht richtig zu sein. Gib dein Passwort ein um diesen Toon zu löschen."
AvatarChoiceDeleteWrongConfirm = "Du hast nicht das Richtige eingegeben. Um %(name)s zu löschen gib \"%(confirm)s\" ein und klicke auf OK. Die Anführungszeichen nicht tippen. Klicke auf Abbrechen, wenn du es dir anders überlegt hast."

# AvatarChooser.py
AvatarChooserPickAToon = "Such dir einen Toon zum Spielen aus"
AvatarChooserQuit = lQuit

# MultiPageTextFrame.py
MultiPageTextFrameNext = lNext
MultiPageTextFramePrev = 'Zurück'
MultiPageTextFramePage = 'Seite %s/%s'

# MemberAgreementScreen.py
MemberAgreementScreenTitle = 'Mitgliedsvertrag'
MemberAgreementScreenAgree = "Ich bin einverstanden"
MemberAgreementScreenDisagree = "Ich bin nicht einverstanden"
MemberAgreementScreenCancel = "Abbrechen"
MemberAgreementScreenWelcome = "Willkommen!"
MemberAgreementScreenOnYourWay = "Du bist dabei, offizielles Mitglied von"
MemberAgreementScreenToontown = "Disneys Toontown Online zu werden"
MemberAgreementScreenPricing = "Disneys Toontown Online kostet\nim ersten Monat. Jeder weiterer Monat kostet .\nUnd das Registrieren ist ganz leicht: Einfach die\nInformationen unten lesen, ausfüllen, und schon geht's los!"
MemberAgreementScreenCCUpFrontPricing = "Trage dich jetzt für deine KOSTENLOSE -tägige Probezeit ein. Du kannst während dieser Probezeit jederzeit abbrechen,\n ohne dass Kosten anfallen. Am Ende\nder kostenlosen Probezeit wird automatisch eine Rechnung für\nden ersten Monat gestellt, und dann für jeden weiteren Monat."
MemberAgreementScreenGetParents = "Du musst 18 Jahre oder älter sein, um Disneys Toontown Online zu abonnieren. Bitte deine Eltern oder einen Erziehungsberechtigten um Hilfe. "
MemberAgreementScreenGetParentsUnconditional = "Du musst 18 Jahre oder älter sein, um Disneys Toontown Online zu abonnieren. Wenn du unter 18 bist, bitte deine Eltern oder einen Erziehungsberechtigten um Hilfe."
MemberAgreementScreenMustBeOlder = "Du musst 18 Jahre oder älter sein, um Disneys Toontown Online zu abonnieren. Bitte deine Eltern oder einen Erziehungsberechtigten um Hilfe."
MemberAgreementScreenYouMustAgree = "Um Disneys Toontown Online zu abonnieren musst du dem Mitgliedsvertrag zustimmen."
MemberAgreementScreenYouMustAgreeOk = "OK"
MemberAgreementScreenYouMustAgreeQuit = "Beenden"
MemberAgreementScreenAgreementTitle = "Mitgliedsvertrag"
MemberAgreementScreenClickNext = "Klicke auf \"Weiter\", um zur nächsten Seite zu gelangen."
# this is useful for tweaking the member agreement:
#import LocalizerEnglish; import Localizer
#reload(LocalizerEnglish);reload(Localizer);page=toonbase.tcr.memberAgreementScreen.memAgreement.getCurPage();toonbase.tcr.loginFSM.request('freeTimeInform');toonbase.tcr.loginFSM.request('memberAgreement');toonbase.tcr.memberAgreementScreen.memAgreement.setPage(page)
MemberAgreementScreenLegalText = [
"""





""" # spacing for graphics; start next section on a new line (i.e. """\nText)
"""
DISNEYS TOONTOWN ONLINE MITGLIEDSCHAFTSVERTRAG

Lizenzbedingungen für die entgeltliche Nutzung von „T-Online Disney's Toontown Online\"


§ 1 Allgemeines


1.\tDie T-Online International AG (im Weiteren „T-Online AG\" genannt) mit Sitz in 64331 Weiterstadt räumt dem Nutzer auf der Grundlage dieser Lizenzbedingungen die Möglichkeit ein, die von der T-Online AG oder Dritten überlassene Software, die der Nutzer auf seinem Rechner installiert, um auf das Spiel „T-Online Disney's Toontown Online\" zugreifen zu können (im weiteren \"Software\" genannt), und die bei der T-Online AG oder einem Dritten gespeicherte Software (im weiteren \"MMPG\" genannt für massively multi player game software), auf die der Nutzer online zugreifen kann, um alleine oder mit mehreren Spielern gemeinsam spielen zu können, entsprechend den Regelungen dieser Lizenzbedingungen und der Leistungsbeschreibung des Spiels zu nutzen. Die Software und das MMPG werden im weiteren gemeinsam „Toontown\" genannt. Soweit sich aus diesen Lizenzbedingungen keine abweichenden Regelungen ergeben, finden darüber hinaus die Allgemeinen Geschäftsbedingungen der T-Online International AG Anwendung. Die Allgemeinen Geschäftsbedingungen können im Bereich \"Kundencenter\" auf www.t-online.de abgerufen werden.


2.\tDer Nutzer erkennt durch seine Anmeldung die nachfolgenden Lizenzbedingungen in vollem Umfang an. Etwaige entgegenstehende Lizenzbedingungen oder Allgemeine Geschäftsbedingungen des Nutzers sind ausgeschlossen.


§ 2 Nutzungsrecht, Lizenzerwerb, Vertragslaufzeit


1.\tDer Vertrag über das Nutzungsrecht ist mit der Anmeldung des Nutzers und der Bereitstellung der Software durch die T-Online AG geschlossen. Das Nutzungsrecht an „Toontown\" ist nicht ausschließlich, nicht unterlizenzierbar, nicht übertragbar und auf die vertragliche Laufzeit begrenzt. Der Nutzer ist berechtigt, die Software auf einem Rechner und ausschließlich zu privaten Zwecken zu nutzen und MMPG online zu nutzen. Der Nutzer ist nicht zu einer kommerziellen Nutzung der Software berechtigt, insbesondere die Verbreitung und der Vertrieb sind ausdrücklich untersagt.


2.\tDer Nutzer erhält keine Nutzungsrechte an Toontown, die über die in § 2 Ziffer 1 geregelten Nutzungsrechte hinausgehen. Das Recht am geistigen Eigentum sowie sonstige Rechte an Toontown verbleiben bei der T-Online AG und/oder deren Lieferanten.


§ 3 Vervielfältigungsrechte,  Weitergabe an Dritte


1.\tDer Nutzer darf die Software zur Installation der Software von der Internetseite der T-Online AG auf den Massenspeicher der eingesetzten Hardware sowie zum Laden der Software in den Arbeitsspeicher vervielfältigen. Darüber hinaus ist der Nutzer berechtigt, eine Vervielfältigung der Software zu Sicherungszwecken vorzunehmen.


2.\tDer Nutzer darf die Software und das Recht zur Nutzung von MMPG nicht an Dritte übertragen.


§ 4 Programmänderungen


1.\tDie Rückübersetzung des überlassenen Programmcodes in andere Codeformen (Dekompilierung) sowie sonstige Arten der Rückerschließung der verschiedenen Herstellungsstufen der Software (Reverse-Engineering) sind unzulässig, sofern sich aus anderen lizenzrechtlichen oder gesetzlichen Bestimmungen nichts Gegenteiliges ergibt.


2.\tDie Entfernung eines Kopierschutzes oder ähnlicher Schutzroutinen ist unzulässig.


3.\tProgrammänderungen zum Zwecke der Fehlerbeseitigung oder der Erweiterung des Funktionsumfangs sind unzulässig. Urhebervermerke, Kennzeichnungen sonstiger gewerblicher Schutzrechte oder Seriennummern und andere Merkmale, die einer Identifikation der Software oder Hardware dienen, dürfen auf keinen Fall entfernt oder verändert werden.


§ 5 Mängelhaftung


1.\tDem Nutzer ist bekannt, dass Software (einschließlich MMPG) nie frei von Mängeln ist. Die T-Online AG haftet nur für solche Mängel, die die Gebrauchstauglichkeit von Toontown erheblich einschränken, sofern die T-Online AG den Mangel nicht arglistig verschwiegen hat oder für die entsprechende Beschaffenheit eine Garantie übernommen hat.


2.\tMit der Angabe von Leistungsdaten oder sonstigen Beschreibungen von Toontown, auch wenn sie auf DIN und / oder sonstige Normen Bezug nehmen, übernimmt die T-Online AG keine Garantie für die Beschaffenheit von Toontown.


3.\tBei erheblichen Mängeln der Software bietet die T-Online AG nach Wahl der T-Online AG kostenfreie Nachbesserung oder Ersatzlieferung an.


§ 6 Schadensersatzhaftung


1.\tEine uneingeschränkte Haftung der T-Online AG nach den gesetzlichen Bestimmungen auf Schadensersatz besteht nur, soweit die der T-Online AG zurechenbare Pflichtverletzung auf Vorsatz oder grober Fahrlässigkeit beruht. Soweit die der T-Online AG zurechenbare Pflichtverletzung auf einfacher Fahrlässigkeit beruht und eine wesentliche Vertragspflicht in einer den Vertragszweck gefährdenden Weise schuldhaft verletzt ist, ist die Schadensersatzhaftung auf den zum Zeitpunkt der Vertragsschlusses vorhersehbaren Schaden beschränkt, der typischerweise in vergleichbaren Fällen eintritt. Die Haftung der T-Online AG ist ausgeschlossen, sofern der Nutzer Toontown nicht entsprechend den Regelungen dieser Lizenzbedingungen und der Leistungsbeschreibung einsetzt und ihm oder Dritten dadurch Schaden verursacht wird. In diesem Fall stellt der Nutzer die T-Online AG von allen Ansprüchen des Dritten im Innenverhältnis frei. Im Falle von Schäden wegen Datenverlustes haftet die T-Online AG nur, soweit der Nutzer seine Daten in anwendungsadäquaten Intervallen, mindestens jedoch einmal täglich, in geeigneter Form gesichert hat.


2.\tDie Haftung nach den Bestimmungen des Produkthaftungsgesetzes bleibt unberührt. Unberührt bleibt auch die Haftung wegen Verletzung von Leben, Körper und Gesundheit sowie bei Übernahme einer Garantie.


3.\tIm Übrigen ist die Haftung der T-Online AG ausgeschlossen.


§ 7 Schlussklauseln


1.\tEs findet das Recht der Bundesrepublik Deutschland unter Ausschluss des UN-Kaufrechts sowie der Kollisionsnormen des Internationalen Privatrechts (IPR) Anwendung.


2.\tSoweit der Nutzer Kaufmann, eine juristische Person des öffentlichen Rechts oder ein öffentlich-rechtliches Sondervermögen ist, ist der ausschließlich Gerichtsstand der Sitz der T-Online AG. Die T-Online AG behält sich vor, gerichtliche Schritte gegen den Nutzer auch an dessen allgemeinen Gerichtsstand einzuleiten.


3.\tSollten einzelne Bestimmungen dieser Lizenzbedingungen unwirksam oder nichtig sein oder werden, so berührt dies die Gültigkeit der übrigen Bestimmungen dieser Lizenzbedingungen nicht.


4.\tÄnderungen, Ergänzungen oder eine Aufhebung dieses Vertrages bedürfen der Schriftform. Dies gilt auch für eine Regelung, mit der das Erfordernis der Schriftform geändert oder aufgehoben wird.


Stand: September 2004,
"""]

# BillingScreen.py
BillingScreenCCTypeInitialText = 'Bitte auswählen'
BillingScreenCreditCardTypes = ['Visa', 'American Express', 'MasterCard']
BillingScreenTitle = "Bitte Rechnungsdaten eingeben"
BillingScreenAccountName = "Account-Name"
BillingScreenEmail = "Rechnungs-/Eltern-E-Mail-Adresse"
BillingScreenEmailConfirm = "E-Mail-Adresse bestätigen"
BillingScreenCreditCardType = "Kreditkartentyp"
BillingScreenCreditCardNumber = "Kreditkartennummer"
BillingScreenCreditCardExpires = "Gültig bis"
BillingScreenCreditCardName = "Name wie auf der Kreditkarte"
#BillingScreenAgreementText = """*"""
BillingScreenAgreementText = """Durch Anklicken des Buttons \"Kaufen\" erkläre ich mich gemäß den Regelungen zum Datenschutz einverstanden, dass mein Kind/meine Kinder die interaktiven Features nutzen darf/dürfen, die durch das Elternpasswort autorisiert werden, das ich auf der nächsten Seite einrichte."""
BillingScreenBillingAddress = "Rechnungsadresse: Straße 1"
BillingScreenBillingAddress2 = "Straße 2 (falls zutreffend)"
BillingScreenCity = "Ort"
BillingScreenCountry = "Land"
BillingScreenState = "Staat"
BillingScreenZipCode = "Postleitzahl"
BillingScreenCAProvince = "Provinz oder Territorium"
BillingScreenProvince = "Provinz (falls zutreffend)"
BillingScreenPostalCode = "Postleitzahl"
BillingScreenPricing = " für den ersten Monat, dann pro Monat"
BillingScreenSubmit = "Kaufen"
BillingScreenCancel = "Abbrechen"
BillingScreenConfirmCancel = "Kauf abbrechen?"
BillingScreenConfirmCancelYes = "Ja"
BillingScreenConfirmCancelNo = "Nein"
BillingScreenPleaseWait = "Bitte warten ..."
BillingScreenConnectionErrorSuffix = ".\nBitte später nochmals versuchen."
BillingScreenEnterEmail = "Bitte geben Sie Ihre E-Mail-Adresse ein."
BillingScreenEnterEmailConfirm = "Bitte tippen Sie Ihre E-Mail-Adresse noch einmal ein."
BillingScreenEnterValidEmail = "Bitte geben Sie eine gültige E-Mail-Adresse ein."
BillingScreenEmailMismatch = "Die von Ihnen eingegebenen E-Mail-Adressen stimmen nicht überein. Bitte nochmals versuchen."
BillingScreenEnterAddress = "Bitte geben Sie Ihre vollständige Rechnungsadresse ein."
BillingScreenEnterValidState = "Bitte geben Sie ein Kürzel aus zwei Buchstaben für Ihren Staat ein."
BillingScreenChooseCreditCardType = "Bitte wählen Sie einen Kreditkartentyp."
BillingScreenEnterCreditCardNumber = "Bitte geben Sie Ihre Kreditkartennummer ein."
BillingScreenEnterValidCreditCardNumber = "Bitte überprüfen Sie Ihre Kreditkartennummer."
BillingScreenEnterValidSpecificCreditCardNumber = "Bitte geben Sie eine gültige %s Kreditkartennummer ein."
BillingScreenEnterValidCreditCardExpDate = "Bitte geben Sie ein korrektes Gültigkeitsdatum für die Kreditkarte ein."
BillingScreenEnterNameOnCard = "Bitte geben Sie den Namen ein, der auf Ihrer Kreditkarte steht."
BillingScreenCreditCardProblem = "Beim Bearbeiten Ihrer Kreditkarte trat ein Fehler auf."
BillingScreenTryAnotherCC = "Andere Karte versuchen?"
# Fill in %s with phone number from account server
BillingScreenCustomerServiceHelp = "\n\nWenn Sie Hilfe benötigen, rufen Sie bitte den Kundenservice unter %s an."
BillingScreenCCProbQuit = lQuit
BillingScreenWhySafe = "Kreditkartensicherheit"
BillingScreenWhySafeTitle = "Kreditkartensicherheit"
BillingScreenWhySafeCreditCardGuarantee = "KREDITKARTENGARANTIE"
BillingScreenWhySafeJoin = "JETZT MITGLIED VON"
BillingScreenWhySafeToontown = "DISNEYS TOONTOWN ONLINE"
BillingScreenWhySafeToday = "WERDEN!"
BillingScreenWhySafeClose = lClose
BillingScreenWhySafeText = [
"""




Wir verwenden die Secure-Sockets-Layer-Technologie (SSL), die Ihre Kreditkarteninformationen verschlüsselt, so dass sie geheim und geschützt bleiben. Diese Technologie bietet Sicherheit beim Eingeben und Übermitteln Ihrer Kreditkarteninformationen über das Internet.
Diese Sicherheitstechnologie schützt Ihre Internetkommunikation durch:

     Serverauthentifizierung (schützt gegen Betrug)
     Geheimhaltung durch Verschlüsselung (schützt gegen Lauschen)
     Datenintegrität (schützt gegen Zerstörung)

Um Ihnen noch zusätzliche Sicherheit zu bieten, werden alle Kreditkartennummern in einem Computer gespeichert, der nicht mit dem Internet verbunden ist. Nachdem Sie sie eingegeben haben, wird Ihre vollständige Kreditkartennummer über ein eigenes Interface in diesen sicheren Computer übertragen. Ihre Kreditkartennummer wird nirgendwo sonst gespeichert.



Ihre Kreditkarteninformationen sind also bei Disneys Toontown Online nicht nur sicher - wir garantieren dies auch!
Für jedes Abonnement von Disneys Toontown Online gilt unsere Kreditkartengarantie. Wenn ohne ihr Verschulden und als direkte Folge der Übermittlung Ihrer Kreditkartendaten an Disney unberechtigte Belastungen auf Ihrem Kontoauszug erscheinen, kommen wir bis zu einer Höhe von 50 Euro für den von Ihrer Bank geforderten Betrag auf.

Bei Problemen melden Sie diese bitte nach dem üblichen Verfahren an Ihren Kreditkartenanbieter und nehmen Sie auch mit uns unverzüglich Kontakt auf. Die meisten Kreditkartenunternehmen kommen für alle Belastungen auf, die sich aus einer unberechtigten Nutzung ergeben, sind aber berechtigt, eine Eigenhaftung von bis zu 50 Euro von Ihnen zu verlangen. Wir werden Ihnen diesen nicht durch Ihre Kreditkarte abgedeckten Betrag erstatten.
Was bedeutet dies für Sie? Es bedeutet, dass Sie auf die Sicherheit und den Service vertrauen können, die mit Ihrem Abonnement von Disneys Toontown Online verbunden sind.

Worauf warten Sie also noch?
""",
]
BillingScreenPrivacyPolicy = "Datenschutz"
BillingScreenPrivacyPolicyClose = lClose
BillingScreenPrivacyPolicyText = [
"""
Datenschutz

F1 Welche Art von Informationen werden durch Websites der Walt Disney Internet Group (WDIG) erfasst und wie geschieht dies?

Wir bieten die meisten unserer attraktiven Produkte und Leistungen auf unseren Websites an, ohne dabei personenbezogene Informationen zu erfassen. Sie können also meist anonym auf unseren Websites surfen und z.B. Nachrichtenmeldungen auf ABCNEWS.com lesen, ohne personenbezogene Daten angeben zu müssen.

Von Ihnen zur Verfügung gestellte Informationen
Es gibt jedoch auch einige Angebote auf unseren Websites, für die personenbezogene Daten angegeben werden müssen. Dazu gehören die Teilnahme an einem Wettbewerb oder Gewinnspiel, ein Kauf oder ein Abonnement oder eine Kontaktaufnahme mit uns. Wenn personenbezogene Daten erfasst werden, wissen Sie dies stets, da Sie ein Formular ausfüllen müssen. Bei den meisten Angeboten erfassen wir nur Namen, E-Mail-Adresse, Geburtsdatum, Geschlecht und Postleitzahl. Wenn Sie etwas kaufen, erfassen wir auch Liefer- und Rechnungsadresse, Telefonnummer sowie Kreditkarteninformationen. Je nachdem, was Sie kaufen, benötigen wir eventuell noch andere persönliche Angaben, wie zum Beispiel Ihre Konfektionsgröße.
""","""
Automatisch erfasste Informationen
Einige Informationen über Sie werden auf WDIG-Websites auch automatisch erfasst, so dass dies möglicherweise für Sie nicht direkt deutlich wird. Wenn Sie unsere Website besuchen, wird zum Beispiel Ihre IP-Adresse erfasst, damit wir wissen, wohin wir von Ihnen angefragte Informationen schicken sollen. Eine IP-Adresse steht oft für den Ort, von dem aus Sie ins Internet gelangen; das kann zum Beispiel Ihr ISP (Internet Service Provider), Ihr Unternehmen oder Ihre Universität sein. Diese Informationen sind nicht personenbezogen. Solche automatisch erfassten Informationen werden dafür verwendet, unsere Websites für Sie interessanter und nützlicher zu gestalten. Dazu gehört auch, dass wir Werbepartnern dabei helfen, Anzeigen für unsere Website zu entwickeln, die unseren Gästen gefallen könnten. Diese Art Information kombinieren wir normalerweise jedoch nicht mit personenbezogenen Informationen. Dies geschieht nur dann, wenn ein Besucher identifiziert werden soll, um die Einhaltung unserer Hausordnung oder Servicebedingungen zu sichern oder unseren Service, unsere Website, unsere Gäste oder andere zu schützen.

Was sind Cookies und wie verwendet WDIG sie?
Cookies sind Informationen, die eine Website an Ihren Computer schickt, während Sie die Website besuchen. Dadurch kann sich die Website wichtige Informationen \"merken\", durch die Sie diese Website noch besser nutzen können. WDIG und andere Internet-Unternehmen verwenden Cookies für zahlreiche Zwecke. DisneyStore.com z.B. nutzt Cookies, um sich die Artikel in Ihrem Warenkorb zu merken und sie zu verarbeiten, und alle WDIG-Seiten nutzen Cookies um sicherzustellen, dass Kinder keine unmoderierten Chaträume betreten können.

Sie können sich von Ihrem Computer immer eine Meldung geben lassen, wenn ein Cookie geschickt wird, oder sich dafür entscheiden, überhaupt keine Cookies zuzulassen. Dies stellen Sie über Ihren Browser ein (z.B. Netscape Navigator oder Internet Explorer). Jeder Browser ist ein wenig anders; schauen Sie daher im Hilfe-Menü Ihres Browsers nach, wie Sie Ihre Cookies richtig einstellen. Wenn Sie die Cookies ausschalten, können Sie auf viele WDIG-Features nicht zugreifen, durch die Ihr Weberlebnis effizienter wird - z.B. die oben genannten Features - und manche unserer Serviceleistungen funktionieren möglicherweise nicht richtig.
""","""
F2 Wie nutzt WDIG die erfassten personenbezogenen Informationen?

Personenbezogene Informationen werden von WDIG nur sehr begrenzt genutzt. So verwenden wir die Informationen um Transaktionen auszuführen. Wenn Sie zum Beispiel ein Fantasy- Team auf ESPN.com kaufen, verwenden wir Ihre Informationen, um Ihre Bestellung zu bearbeiten; wenn Sie uns kontaktieren, weil Sie Hilfe benötigen, verwenden wir Ihre Informationen dazu, uns bei Ihnen zu melden. Oder wir verwenden erfasste Informationen, um Sie zu benachrichtigen, wenn Sie bei einem Spiel oder Wettbewerb gewonnen haben, Ihnen per E-Mail Updates und Newsletter über unsere Websites zu schicken. Wir verwenden die von Ihnen zur Verfügung gestellten Informationen auch um Ihnen per E-Mail Informationen über WDIG-Werbeaktionen und Sonderangebote unserer Sponsoren zuzusenden.
""","""
F3 Gibt WDIG Informationen an Unternehmen oder andere Organisationen weiter, die nicht zur Familie der WDIG-Websites gehören?

Sie gehören für unser Geschäft zum Wertvollsten, was wir haben. Es gehört nicht zu unserer Geschäftstätigkeit, Informationen über unsere Gäste zu verkaufen. Wir werden Ihre Angaben jedoch weitergeben oder Ihnen im Auftrag anderer Unternehmen (siehe unten) Informationen zuschicken, wenn sich daraus ein Wert für unsere Gäste ergibt. Wir geben Informationen außerdem auch aus Sicherheitsgründen weiter. 
Unternehmen, die stellvertretend für WDIG handeln
Zuweilen beauftragen wir Unternehmen, für uns Produkte oder Dienstleistungen zum Kunden zu bringen, z.B. ein Transportunternehmen, das ein Paket liefert. In diesen Fällen müssen wir Ihre Angaben an diese weitergeben. Diese Unternehmen handeln damit stellvertretend für WDIG und dürfen die Angaben ausschließlich zur Lieferung des Produktes oder der Dienstleistung verwenden.",
""","""
Unternehmen, die Aktionen, Produkte oder Dienstleistungen anbieten
Gelegentlich bieten wir gemeinsam mit einem Sponsor Aktionen an, wie zum Beispiel Gewinnspiele oder kostenlose Abonnements. Wir geben in diesem Fall Ihre Angaben an die Sponsoren weiter, wenn diese sie benötigen, um Ihnen ein Produkt zu schicken, zum Beispiel bei einem Zeitschriftenabonnement. Wir können Ihre Angaben auch an diese Sponsoren weitergeben, damit sie weiter über Sonderangebote informieren können, jedoch nur, wenn Sie uns Ihre Einwilligung dazu geben. Wir werden sie in diesem Fall auch nur an diesen speziellen Sponsor weitergeben. Zusätzlich versendet WDIG gelegentlich E-Mail-Angebote im Auftrag von außenstehenden Sponsoren. In diesem Fall teilen wir Ihren Namen diesem Dritten nicht mit - wir führen das Mailing für ihn durch. Auch hier schicken wir Ihnen diese E-Mails nur, wenn Sie Ihre Einwilligung dazu gegeben haben.

Partner für Inhalte
Auf einigen unserer Websites bieten wir Inhalte, die von einer Partnerwebsite (einer dritten Partei) erstellt wurden. Zum Beispiel bietet ESPN.com Einkaufsmöglichkeiten bei Dritten. In einigen Fällen erfassen solche Websites Dritter Informationen, um die Transaktionen zu erleichtern oder um die Nutzung ihrer Inhalte produktiver und effizienter zu gestalten. In diesen Fällen werden die Informationen zwischen WDIG und diesen Sponsoren ausgetauscht.

Werbepartner und Network-Werbepartner
Um den Datenschutz für unsere Gäste zu erhöhen, gestattet WDIG nur solchen Unternehmen auf unseren Websites zu werben, die eigene Datenschutzbestimmungen haben. Wenn Sie auf eine Anzeige geklickt und die WDIG-Website verlassen haben, gelten unsere Bestimmungen zum Datenschutz nicht mehr. Sie müssen daher die Datenschutzbestimmungen des Werbepartners lesen um zu erfahren, wie der Datenschutz auf dessen Website gehandhabt wird.
""","""
Außerdem werden viele Geschäftsanzeigen durch dritte Unternehmen betreut und auf unserer Website platziert. Diese Unternehmen nennen wir  \"Network-Werbepartner\". Network-Werbepartner erfassen nicht personenbezogene Informationen, wenn Sie auf eine ihrer Bannerwerbungen klicken oder darüber streichen. Die Informationen werden automatisch erfasst, so dass Sie möglicherweise nicht merken, dass Informationen dies geschieht. Die Network-Werbepartner sammeln diese Informationen, damit sie Ihnen Anzeigen zeigen können, die für Sie relevanter und interessanter sind. Wenn Sie mehr über Network-Werbepartner lesen wollen oder wenn Sie nicht möchten, dass Network-Werbepartner diese nicht personenbezogenen Informationen über Sie sammeln, klicken Sie hier.

Verkauf oder Kauf von Unternehmen
Das Online-Geschäft befindet sich noch in einer recht frühen Phase und verändert und entwickelt sich rasch. Da wir von WDIG ständig nach Wegen suchen, unsere Geschäftstätigkeit zu verbessern, kann es vorkommen, dass wir ein Unternehmen kaufen oder verkaufen. Wenn wir ein Unternehmen kaufen oder verkaufen, werden meist die erfassten Namen als Bestandteil des Geschäftes mit übertragen. Informationen über registrierte Nutzer werden mit genutzt. Wenn wir jedoch ein Unternehmen kaufen, werden wir die Wünsche der Kunden jenes Unternehmens im Hinblick auf E-Mail-Kommunikation respektieren. Falls wir ein Unternehmen verkaufen, werden wir alles in unserer Macht stehende tun, dass Ihre Wünsche an uns in Bezug auf die E-Mail-Kommunikation auch weiterhin respektiert werden.

Organisationen, die zum Schutz der Sicherheit unserer Gäste und unserer Websites beitragen
Wir geben persönliche Informationen weiter, wenn dies laut Gesetz erforderlich ist, zum Beispiel aufgrund einer gerichtlichen Verfügung. Ferner zur Durchsetzung unserer Servicebedingungen oder der Regeln von Websites oder Spielen oder zum Schutz der Sicherheit unserer Gäste und unserer Websites.
""","""
F4 Welche Wahlmöglichkeiten habe ich in Bezug auf die Erfassung, Nutzung und Weitergabe meiner Informationen durch WDIG?

Sie können einen großen Teil unserer Website nutzen, ohne uns irgendwelche personenbezogenen Informationen zu geben. Wenn Sie sich bei uns registrieren oder uns personenbezogene Informationen geben, haben Sie eine Wahlmöglichkeit zum Zeitpunkt der Erfassung Ihrer Informationen - Sie können die E-Mail-Kommunikation durch WDIG und unsere Partner einschränken. Sie können ferner jederzeit verlangen, dass WDIG Ihnen keine weiteren E-Mails mehr schickt, indem Sie sich entweder aus diesem Schriftverkehr abmelden oder mit uns über memberservices@help.go.com Kontakt aufnehmen. Wie oben schon erwähnt, gibt es auch die Möglichkeit, die automatisch gesammelten Informationen einzuschränken - allerdings werden dann manche unserer Features nicht funktionieren.
""","""
F5 Welche Art Sicherheit bietet WDIG?

Die Sicherheit aller personenbezogenen Daten unserer Gäste liegt uns sehr am Herzen. WDIG ergreift daher technische, vertragliche, administrative und direkte Sicherheitsmaßnahmen, um die Informationen aller Besucher zu schützen. Wenn Sie Kreditkarteninformationen angeben, schützen wir diese mit Hilfe der Secure Socket Layer (SSL)-Verschlüsselung. Sie können aber auch selbst Ihre Informationen noch besser schützen. Geben Sie zum Beispiel nie Ihr Passwort weiter, da es den Zugriff auf alle Ihre Account-Informationen ermöglicht. Vergessen Sie auch nicht, Ihren Account abzumelden und Ihr Browserfenster zu schließen, wenn Sie das Surfen im Web beenden, so dass andere Personen, die denselben Computer benutzen, nicht auf Ihre Daten zugreifen können.
""","""
F6 Wie kann ich auf meine Account-Daten zugreifen?

Sie können unter Account-Optionen (http://play.toontown.com auf die personenbezogenen Daten zugreifen, die Sie uns bei der Registrierung gegeben haben. Loggen Sie sich mit Ihrem Account-Namen und dem Elternpasswort ein. Auf der Startseite finden Sie Anweisungen, wie Sie Ihr Passwort wieder beschaffen können, wenn Sie es vergessen haben.
Sie können uns auch kontaktieren, indem Sie auf irgend einer WDIG-Seite unten auf \"Kontakt\" klicken und im Dropdown-Menü \"Registrierung/Personalisierung\" wählen oder uns eine E-Mail direkt an memberservices@help.go.com schicken. Bitte vergessen Sie in der E-Mail nicht die notwendigen Angaben zu Ihrem Account, damit wir Ihnen bei Ihrer Frage oder Bitte behilflich sein können.
""","""
F7 An wen wende ich mich mit Fragen oder Bedenken bezüglich dieser Datenschutzbestimmungen?

Wenn Sie weitere Hilfe benötigen, schicken Sie eine E-Mail mit Ihren Fragen oder Anmerkungen an memberservices@help.go.com
Oder per Post an:

Member Services
Walt Disney Internet Group
506 2nd Avenue
Suite 2100
Seattle, WA 98104, USA
oder rufen Sie uns an: (509)-742-4698

Die Walt Disney Internet Group ist Lizenznehmerin des TRUSTe Privacy Program. Wenn Sie meinen, dass WDIG auf Ihre Anfrage nicht oder nicht ausreichend geantwortet hat, wenden Sie sich bitte an TRUSTe unter http://www.truste.org/users/users_watchdog.html.
*Sie müssen 18 Jahre alt sein oder die Erlaubnis eines Elternteils oder Erziehungsberechtigten haben, um diese Nummer zu wählen.
""","""
Datenschutzbestimmungen für Kinder:
Wir sind uns darüber im Klaren, dass wir zusätzlichen Datenschutz für Kinder, die unsere Websites besuchen, bieten müssen.

F1 Was für Informationen erfassen WDIG-Websites über Kinder im Alter von 12 Jahren oder darunter?

Kinder können auf Disney.com oder anderen WDIG-Websites surfen, sich Inhalte ansehen und einige Spiele spielen, ohne dass personenbezogene Informationen erfasst werden. Außerdem bieten wir gelegentlich auch moderierte Chaträume an, in denen keine personenbezogenen Informationen erfasst oder weitergeleitet werden. In manchen Bereichen ist es jedoch erforderlich, auch von Kindern personenbezogene Informationen zu erfassen, um die Teilnahme an einer Aktivität zu ermöglichen (zum Beispiel an einem Wettbewerb) oder um mit anderen zu kommunizieren (über E-Mail oder Pinnwände).
Wir sind bei WDIG der Meinung, dass von Kindern im Alter von 12 und darunter nicht mehr personenbezogene Informationen erfasst werden sollen, als für ihre Teilnahme an unseren Online-Aktivitäten unbedingt notwendig ist. Außerdem ist es Websites für Kinder im Alter von 12 oder darunter auch gesetzlich nicht gestattet, mehr Informationen zu erfassen als sie benötigen.

Die einzigen personenbezogenen Informationen, die wir von Kindern erfassen, sind Vorname, E-Mail-Adresse der Eltern und Geburtsdatum des Kindes. Wir fragen das Geburtsdatum ab, um das Alter der Besucher unserer Website festzustellen. Möglicherweise erfassen wir auch persönliche Informationen, wie den Namen eines Haustieres, um so den Kindern zu helfen, sich wieder an ihren Login-Namen und das Passwort zu erinnern, falls sie sie vergessen haben.


Eltern können aber von uns jederzeit verlangen, dass die erfassten Angaben über ihr Kind aus der Datenbank entfernt werden. Wenn Sie den Account Ihres Kindes deaktivieren möchten, schicken Sie bitte eine E-Mail an ms_support@help.go.com, geben Sie den Login-Namen Ihres Kindes und das Passwort an und bitten Sie darum, den Account zu löschen.
""","""
F2 Wie geht WDIG mit den erfassten personenbezogenen Daten im Hinblick auf Verwendung und Weitergabe um?

Die über Kinder im Alter von 12 oder darunter erfassten Daten werden unter keinen Umständen für irgendwelche Marketing- oder Werbezwecke verwendet, weder innerhalb noch außerhalb der Websites von WDIG.
Die über Kinder im Alter von 12 oder darunter erfassten Daten werden einzig und allein von WDIG-Websites genutzt und zwar für Services (zum Beispiel Kalender) oder für Spiele bzw. Wettbewerbe und Gewinnspiele. Gäste im Alter von 12 oder darunter dürfen zwar an einigen Wettbewerben teilnehmen, bei denen Daten erfasst werden; Benachrichtigungen und Preise werden jedoch immer an die Adresse des Elternteils oder Erziehungsberechtigten geschickt, die beim ersten Registrierungsverfahren angegeben wurde. Für die Veröffentlichung der vollständigen Namen, Altersangaben oder Bilder von Personen im Alter von 12 oder darunter ist die Einwilligung der Eltern oder Erziehungsberechtigten erforderlich. Manchmal wird eine nicht identifizierbare Version des Namens eines Kindes veröffentlicht. In diesen Fällen werden die Eltern nicht unbedingt um Erlaubnis gebeten.

Wir gestatten Kindern im Alter von 12 oder darunter nicht, sich in unmoderierten Chaträumen aufzuhalten.

Wir geben persönliche Informationen über Kinder heraus, wenn dies laut Gesetz erforderlich ist, zum Beispiel aufgrund einer gerichtlichen Verfügung, zur Durchsetzung unserer Servicebedingungen oder der Regeln für unsere Websites oder Spiele oder zum Schutz der Sicherheit unserer Gäste und unserer Websites.
""","""
F3 Benachrichtigt WDIG die Eltern über die Erfassung von Informationen über Kinder im Alter von 12 oder darunter?

Wenn Kinder im Alter von 12 oder darunter sich bei uns registrieren, schicken wir einem Elternteil oder Erziehungsberechtigten immer eine Benachrichtigung per E-Mail. Außerdem bitten wir die Eltern um ihre ausdrückliche Zustimmung, bevor wir ihren Kindern gestatten, E-Mail, Pinnwände und andere Features zu nutzen, bei denen personenbezogene Informationen im Internet veröffentlicht und an Nutzer aller Altersgruppen weitergegeben werden können.
Wir geben Eltern außerdem 48 Stunden Zeit, um Registrierungen zurückzuweisen, die Kinder vornehmen, um an Spielen und Wettbewerben teilzunehmen. Wenn wir keine Rückantwort erhalten, gehen wir davon aus, dass die Registrierung des Kindes bei uns in Ordnung geht. Wenn sich ein Kind registriert hat, darf es an allen künftigen Spielen und Wettbewerben teilnehmen, für die eine Registrierung notwendig ist, und die Eltern werden nicht nochmals benachrichtigt. In diesem Fall verwenden wir die erfassten Informationen nur dazu, Eltern zu benachrichtigen, wenn ein Kind in einem Spiel oder Wettbewerb gewonnen hat. Wir verwenden diese Informationen aber für keinen anderen Zweck.
""","""
F4 Wie können Eltern auf die Informationen über ihre Kinder zugreifen?

Es gibt drei Möglichkeiten, die Informationen anzusehen, die über Kinder im Alter von 12 oder darunter erfasst wurden.

Wenn Eltern ihren Kindern den Zugang zu interaktiven Features wie Pinnwänden erlauben, müssen sie einen Familien-Account einrichten. Ist ein Familien-Account eingerichtet, kann der Hauptinhaber des Accounts die personenbezogenen Informationen über alle Familienmitglieder, einschließlich des Kindes, ansehen und bearbeiten. Sie können auf diese Informationen zugreifen, indem Sie sich auf der Seite Dein Account in Ihren Familien-Account einloggen.

Wenn Sie nicht bereits Mitglied einer der WDIG-Websites sind, können Sie die personenbezogenen Informationen Ihres Kindes ansehen, indem Sie sich in den Account Ihres Kindes auf der Homepage von Account-Optionen einloggen. Sie brauchen dazu den Account-Namen und das Passwort Ihres Kindes. Auf der Homepage Dein Account finden Sie eine Anleitung, wie Sie das Passwort Ihres Kindes erhalten können, falls es vergessen wurde.

Sie können sich auch per E-Mail an ms_support@help.go.com an den Kundendienst wenden, um die Informationen zu sehen, die von Ihrem Kind angegeben oder über Ihr Kind erfasst wurden. Wenn Sie noch keinen Familien-Account eingerichtet haben, benötigen Sie in diesem Fall den Benutzernamen und das Passwort Ihres Kindes. Vergessen Sie bitte in der E-Mail nicht Angaben wie den Account-Namen des Kindes und die E-Mail-Adresse der Eltern, die uns helfen, den Account Ihres Kindes zu finden, damit wir Ihnen bei Ihrer Frage oder Bitte behilflich sein können.
""","""
Q5 Welche Art Sicherheit bietet WDIG?
    
Die Sicherheit aller personenbezogenen Daten unserer Gäste liegt uns sehr am Herzen. WDIG ergreift daher technische, vertragliche, administrative und direkte Sicherheitsmaßnahmen, um die Informationen aller Besucher zu schützen. Wenn Sie Kreditkarteninformationen angeben, schützen wir diese mit Hilfe der Secure Socket Layer (SSL)-Verschlüsselung. Sie können aber auch selbst Ihre Informationen noch besser schützen. Geben Sie zum Beispiel nie Ihr Passwort weiter, da es den Zugriff auf alle Ihre Account-Informationen ermöglicht. Vergessen Sie auch nicht Ihren Account abzumelden und Ihr Browserfenster zu schließen, wenn Sie das Surfen im Web beenden, so dass andere Personen, die denselben Computer benutzen, nicht auf Ihre Daten zugreifen können.
"""",""""
F6 Wie wird WDIG die Eltern benachrichtigen, wenn sich diese Datenschutzbestimmungen ändern?
    
Falls WDIG diese Datenschutzbestimmungen ändert, werden wir die Eltern per E-Mail benachrichtigen.
    
F7 An wen wende ich mich mit Fragen oder Bedenken bezüglich dieser Datenschutzbestimmungen?
    
Wenn Sie weitere Hilfe benötigen, schicken Sie eine E-Mail mit Ihren Fragen oder Anmerkungen an ms_support@help.go.com
Oder per Post an:
    
Member Services
Walt Disney Internet Group
506 2nd Avenue
Suite 2100
Seattle, WA 98104, USA
oder rufen Sie uns an: (509) 742-4698
    
Die Walt Disney Internet Group ist Lizenznehmerin des TRUSTe Privacy Program. Wenn Sie meinen, dass WDIG auf Ihre Anfrage nicht oder nicht ausreichend geantwortet hat, wenden Sie sich bitte an TRUSTe http://www.truste.org/users/users_watchdog.html.
*Sie müssen 18 Jahre alt sein oder die Erlaubnis eines Elternteils oder Erziehungsberechtigten haben, um diese Nummer zu wählen.\n"
""",
]
BillingScreenCountryNames = {
    "US" : "Vereinigte Staaten (USA)",
    "CA" : "Kanada",
    "AF" : "Afghanistan",
    "AL" : "Albanien",
    "DZ" : "Algerien",
    "AS" : "Amerikanisch Samoa",
    "AD" : "Andorra",
    "AO" : "Angola",
    "AI" : "Anguilla",
    "AQ" : "Antarktis",
    "AG" : "Antigua und Barbuda",
    "AR" : "Argentinien",
    "AM" : "Armenien",
    "AW" : "Aruba",
    "AU" : "Australien",
    "AT" : "Österreich",
    "AZ" : "Aserbaidschan",
    "BS" : "Bahamas",
    "BH" : "Bahrain",
    "BD" : "Bangladesh",
    "BB" : "Barbados",
    "BY" : "Weißrussland",
    "BE" : "Belgien",
    "BZ" : "Belize",
    "BJ" : "Benin",
    "BM" : "Bermudas",
    "BT" : "Bhutan",
    "BO" : "Bolivien",
    "BA" : "Bosnien-Herzegowina",
    "BW" : "Botswana",
    "BV" : "Bouvet-Insel",
    "BR" : "Brasilien",
    "IO" : "Britisches Territorium im Indischen Ozean",
    "BN" : "Brunei",
    "BG" : "Bulgarien",
    "BF" : "Burkina Faso",
    "BI" : "Burundi",
    "KH" : "Kambodscha",
    "CM" : "Kamerun",
    "CV" : "Kapverden",
    "KY" : "Cayman-Inseln",
    "CF" : "Zentralafrikanische Republik",
    "TD" : "Tschad",
    "CL" : "Chile",
    "CN" : "China",
    "CX" : "Weihnachtsinseln",
    "CC" : "Kokosinseln",
    "CO" : "Kolumbien",
    "KM" : "Komoren",
    "CG" : "Kongo",
    "CK" : "Cook-Inseln",
    "CR" : "Costa Rica",
    "CI" : "Elfenbeinküste",
    "HR" : "Kroatien",
    "CU" : "Kuba",
    "CY" : "Zypern",
    "CZ" : "Tschechische Republik",
    "CS" : "Tschechoslowakei (ehemals)",
    "DK" : "Dänemark",
    "DJ" : "Dschibouti",
    "DM" : "Dominica",
    "DO" : "Dominikanische Republik",
    "TP" : "Ost-Timor",
    "EC" : "Ecuador",
    "EG" : "Ägypten",
    "SV" : "El Salvador",
    "GQ" : "Äquatorialguinea",
    "ER" : "Eritrea",
    "EE" : "Estland",
    "ET" : "Äthiopien",
    "FK" : "Falklandinseln (Malvinen)",
    "FO" : "Faröer-Inseln ",
    "FJ" : "Fidscbi",
    "FI" : "Finnland",
    "FR" : "Frankreich",
    "FX" : "Frankreich, Europäisches",
    "GF" : "Französisch-Guyana",
    "PF" : "Französisch-Polynesien",
    "TF" : "Französische Südliche Gebiete",
    "GA" : "Gabun",
    "GM" : "Gambia",
    "GE" : "Georgien",
    "DE" : "Deutschland",
    "GH" : "Ghana",
    "GI" : "Gibraltar",
    "GB" : "Großbritannien",
    "GR" : "Griechenland",
    "GL" : "Grönland",
    "GD" : "Grenada",
    "GP" : "Guadeloupe",
    "GU" : "Guam",
    "GT" : "Guatemala",
    "GN" : "Guinea",
    "GW" : "Guinea-Bissau",
    "GY" : "Guyana",
    "HT" : "Haiti",
    "HM" : "Heardinsel und McDonalds-Inseln",
    "HN" : "Honduras",
    "HK" : "Hongkong",
    "HU" : "Ungarn",
    "IS" : "Island",
    "IN" : "Indien",
    "ID" : "Indonesien",
    "IR" : "Iran",
    "IQ" : "Irak",
    "IE" : "Irland",
    "IL" : "Israel",
    "IT" : "Italien",
    "JM" : "Jamaika",
    "JP" : "Japan",
    "JO" : "Jordanien",
    "KZ" : "Kasachstan",
    "KE" : "Kenia",
    "KI" : "Kiribati",
    "KP" : "Nordkorea",
    "KR" : "Südkorea",
    "KW" : "Kuwait",
    "KG" : "Kirgisistan",
    "LA" : "Laos",
    "LV" : "Lettland",
    "LB" : "Libanon",
    "LS" : "Lesotho",
    "LR" : "Liberia",
    "LY" : "Libyen",
    "LI" : "Liechtenstein",
    "LT" : "Litauen",
    "LU" : "Luxemburg",
    "MO" : "Macau",
    "MK" : "Mazedonien",
    "MG" : "Madagaskar",
    "MW" : "Malawi",
    "MY" : "Malaysia",
    "MV" : "Malediven",
    "ML" : "Mali",
    "MT" : "Malta",
    "MH" : "Marshallinseln",
    "MQ" : "Martinique",
    "MR" : "Mauretanien",
    "MU" : "Mauritius",
    "YT" : "Mayotte",
    "MX" : "Mexiko",
    "FM" : "Mikronesien",
    "MD" : "Moldawien",
    "MC" : "Monaco",
    "MN" : "Mongolei",
    "MS" : "Montserrat",
    "MA" : "Marokko",
    "MZ" : "Mosambik",
    "MM" : "Burma",
    "NA" : "Namibia",
    "NR" : "Nauru",
    "NP" : "Nepal",
    "NL" : "Niederlande",
    "AN" : "Niederländische Antillen",
    "NT" : "Neutrale Zone",
    "NC" : "Neukaledonien",
    "NZ" : "Neuseeland",
    "NI" : "Nicaragua",
    "NE" : "Niger",
    "NG" : "Nigeria",
    "NU" : "Niue",
    "NF" : "Norfolk-Inseln",
    "MP" : "Nördliche Marianainseln",
    "NO" : "Norwegen",
    "OM" : "Oman",
    "PK" : "Pakistan",
    "PW" : "Palau",
    "PA" : "Panama",
    "PG" : "Papua-Neuguinea",
    "PY" : "Paraguay",
    "PE" : "Peru",
    "PH" : "Philippinen",
    "PN" : "Pitcairn",
    "PL" : "Polen",
    "PT" : "Portugal",
    "PR" : "Puerto Rico",
    "QA" : "Katar",
    "RE" : "Reunion",
    "RO" : "Rumänien",
    "RU" : "Russland",
    "RW" : "Ruanda",
    "GS" : "Süd-Georgia u. Südl. Sandwich-I.",
    "KN" : "St. Kitts und Nevis",
    "LC" : "St. Lucia",
    "VC" : "St. Vincent und die Grenadinen",
    "WS" : "Samoa",
    "SM" : "San Marino",
    "ST" : "Sao Tomé und Principe",
    "SA" : "Saudi-Arabien",
    "SN" : "Senegal",
    "SC" : "Seychellen",
    "SL" : "Sierra Leone",
    "SG" : "Singapur",
    "SK" : "Slowakische Republik",
    "SI" : "Slowenien",
    "Sb" : "Solomon-Inseln",
    "SO" : "Somalia",
    "ZA" : "Südafrika",
    "ES" : "Spanien",
    "LK" : "Sri Lanka",
    "SH" : "St. Helena",
    "PM" : "St. Pierre und Miquelon",
    "SD" : "Sudan",
    "SR" : "Surinam",
    "SJ" : "Svalbard und Jan Mayen Inseln",
    "SZ" : "Swasiland",
    "SE" : "Schweden",
    "CH" : "Schweiz",
    "SY" : "Syrien",
    "TW" : "Taiwan",
    "TJ" : "Tatschikistan",
    "TZ" : "Tansania",
    "TH" : "Thailand",
    "TG" : "Togo",
    "TK" : "Tokelau",
    "TO" : "Tonga",
    "TT" : "Trinidad und Tobago",
    "TN" : "Tunesien",
    "TR" : "Türkei",
    "TM" : "Turkmenistan",
    "TC" : "Turks- and Caicosinseln",
    "TV" : "Tuvalu",
    "UG" : "Uganda",
    "UA" : "Ukraine",
    "AE" : "Vereinigte Arabische Emirate",
    "UK" : "Vereinigtes Königreich",
    "UY" : "Uruguay",
    "UM" : "Vereinigte Staaten, umliegende Inseln",
    "SU" : "UdSSR (ehemals)",
    "UZ" : "Usbekistan",
    "VU" : "Vanuatu",
    "VA" : "Vatikan",
    "VE" : "Venezuela",
    "VN" : "Vietnam",
    "VG" : "Jungferninseln (Britisch) ",
    "VI" : "Jungferninseln (US.)",
    "WF" : "Wallis und Futuna Islands",
    "EH" : "Westsahara",
    "YE" : "Jemen",
    "YU" : "Jugoslawien",
    "ZR" : "Zaire",
    "ZM" : "Sambia",
    "ZW" : "Simbabwe",
    }
BillingScreenStateNames = {
    "AL" : "Alabama",
    "AK" : "Alaska",
    "AR" : "Arkansas",
    "AZ" : "Arizona",
    "CA" : "Kalifornien",
    "CO" : "Colorado",
    "CT" : "Connecticut",
    "DE" : "Delaware",
    "FL" : "Florida",
    "GA" : "Georgia",
    "HI" : "Hawaii",
    "IA" : "Iowa",
    "ID" : "Idaho",
    "IL" : "Illinois",
    "IN" : "Indiana",
    "KS" : "Kansas",
    "KY" : "Kentucky",
    "LA" : "Lousiana",
    "MA" : "Massachusetts",
    "MD" : "Maryland",
    "ME" : "Maine",
    "MI" : "Michigan",
    "MN" : "Minnesota",
    "MO" : "Missouri",
    "MS" : "Mississippi",
    "MT" : "Montana",
    "NE" : "Nebraska",
    "NC" : "North Carolina",
    "ND" : "North Dakota",
    "NH" : "New Hampshire",
    "NJ" : "New Jersey",
    "NM" : "New Mexico",
    "NV" : "Nevada",
    "NY" : "New York",
    "OH" : "Ohio",
    "OK" : "Oklahoma",
    "OR" : "Oregon",
    "PA" : "Pennsylvania",
    "RI" : "Rhode Island",
    "SC" : "South Carolina",
    "SD" : "South Dakota",
    "TN" : "Tennessee",
    "TX" : "Texas",
    "UT" : "Utah",
    "VA" : "Virginia",
    "VT" : "Vermont",
    "WA" : "Washington",
    "WI" : "Wisconsin",
    "WV" : "West Virginia",
    "WY" : "Wyoming",
    "DC" : "District of Columbia",
    "AS" : "Amerikanisch Samoa",
    "GU" : "Guam",
    "MP" : "Nördliche Marianainseln",
    "PR" : "Puerto Rico",
    "VI" : "Jungferninseln",
    "FPO" : ["Midway Island",
             "Kingman Reef",
             ],
    "APO" : ["Wake Island",
             "Johnston Island",
             ],
    "MH" : "Marshall-Inseln",
    "PW" : "Palau",
    "FM" : "Mikronesien",
    }
BillingScreenCanadianProvinces = {
    'AB' : 'Alberta',
    'BC' : 'British Columbia',
    'MB' : 'Manitoba',
    'NB' : 'New Brunswick',
    'NF' : 'Neufundland',
    'NT' : 'Northwest Territories',
    'NS' : 'Nova Scotia',
    #'XX' : 'Nunavut',
    'ON' : 'Ontario',
    'PE' : 'Prince Edward Island',
    'QC' : 'Quebec',
    'SK' : 'Saskatchewan',
    'YT' : 'Yukon',
    }
ParentPassword = "Elternpasswort"

WelcomeScreenHeading = "Willkommen!"
WelcomeScreenOk = "DAS SPIEL GEHT LOS!"
WelcomeScreenSentence1 = "Du bist jetzt offizielles Mitglied von"
WelcomeScreenToontown = "Disneys Toontown Online"
WelcomeScreenSentence2 = "Denk dran, später deine E-Mails nach aufregenden Neuigkeiten über Disneys Toontown Online durchzusehen!"

# TTAccount.py
# Fill in %s with phone number from account server
TTAccountCallCustomerService = "Bitte Kundendienst anrufen unter %s."
# Fill in %s with phone number from account server
TTAccountCustomerServiceHelp = "\nWenn du Hilfe brauchst, ruf bitte den Kundendienst an unter %s."
TTAccountIntractibleError = "Es ist ein Fehler aufgetreten."

# LoginScreen.py
LoginScreenUserName = "Name des Accounts"
LoginScreenPassword = "Passwort"
LoginScreenLogin = "Login"
LoginScreenCreateAccount = "Account einrichten"
LoginScreenForgotPassword = "Passwort vergessen?"
LoginScreenQuit = "Beenden"
LoginScreenLoginPrompt = "Bitte Benutzernamen und Passwort eingeben."
LoginScreenBadPassword = "Falsches Passwort.\nBitte erneut versuchen."
LoginScreenInvalidUserName = "Ungültiger Benutzername.\nBitte erneut versuchen."
LoginScreenUserNameNotFound = "Benutzernamen nicht gefunden.\nBitte erneut versuchen oder neuen Account einrichten."
LoginScreenPeriodTimeExpired = "Entschuldige, du hast dein Zeitkontingent für diesen Monat in Toontown schon aufgebraucht. Kommt bitte am Ersten des nächsten Monats wieder."
LoginScreenNoNewAccounts = "Wir können zurzeit leider keine neuen Accounts akzeptieren."
LoginScreenTryAgain = "Erneut versuchen"

# NewPlayerScreen.py
NewPlayerScreenNewAccount = "Kostenlosen Probelauf starten"
NewPlayerScreenLogin = "Schon Mitglied "
NewPlayerScreenQuit = lQuit

# FreeTimeInformScreen.py
FreeTimeInformScreenDontForget = "Vergiss nicht, deine kostenlose Probezeit\nwird in"
FreeTimeInformScreenNDaysLeft = FreeTimeInformScreenDontForget + " nur %s Tagen ablaufen!"
FreeTimeInformScreenOneDayLeft = FreeTimeInformScreenDontForget + " 1 Tag ablaufen!"
FreeTimeInformScreenNHoursLeft = FreeTimeInformScreenDontForget + " nur %s Stunden ablaufen!"
FreeTimeInformScreenOneHourLeft = FreeTimeInformScreenDontForget + " 1 Stunde ablaufen!"
FreeTimeInformScreenLessThanOneHourLeft = FreeTimeInformScreenDontForget + " weniger als 1 Stunde ablaufen!"
FreeTimeInformScreenSecondSentence = "Aber es ist noch Zeit,\noffizielles Mitglied von Disneys Toontown Online zu werden!"
FreeTimeInformScreenOops = "HOPPLA"
FreeTimeInformScreenExpired = " , deine kostenlose Probezeit ist jetzt vorbei!\nMöchtest du offizielles Mitglied von Disneys Toontown Online werden?\nMelde dich sofort an, dann geht der Spaß gleich weiter!"
FreeTimeInformScreenExpiredQuitText = "Geht gerade nicht? Macht nichts, wir heben\ndeinen Toon für dich auf! Aber beeil dich! Wir können deinen Toon\nnur bis zu 1 Woche aufheben, nachdem\n deine kostenlose Probezeit abgelaufen ist."
FreeTimeInformScreenExpiredCCUF = "Du hast Disneys\nToontown Online noch nicht bezahlt. Um diesen Account zu nutzen,\nmusst du dich jetzt mit einer Kreditkarte registrieren.\nMelde dich sofort an, dann geht der Spaß gleich weiter! "
FreeTimeInformScreenExpiredQuitCCUFText = "Geht gerade nicht? Macht nichts, wir heben\ndeinen Account für dich auf! Aber beeil dich! Wir können deinen Account\nnur bis zu 1 Woche aufheben."
FreeTimeInformScreenPurchase = "Jetzt abonnieren!"
FreeTimeInformScreenFreePlay = "Kostenlose Probezeit fortsetzen"
FreeTimeInformScreenQuit = lQuit

# DateOfBirthEntry.py
DateOfBirthEntryMonths = ['Jan.', 'Febr.', 'März', 'Apr.', 'Mai', 'Juni',
                          'Juli', 'Aug.', 'Sept.', 'Okt.', 'Nov.', 'Dez.',]
DateOfBirthEntryDefaultLabel = "Geburtsdatum"

# CreateAccountScreen.py
CreateAccountScreenUserName = "Account-Name"
CreateAccountScreenPassword = "Passwort"
CreateAccountScreenConfirmPassword = "Passwort bestätigen"
CreateAccountScreenFree = "KOSTENLOS"
CreateAccountScreenFreeTrialLength = "Um deinen %s-day-tägigen Probelauf zu starten, musst\ndu einen Account einrichten."
CreateAccountScreenInstructionsUsername = "Tippe den Account-Namen ein, den du gerne verwenden möchtest:"
CreateAccountScreenInstructionsPassword = "Tippe ein Passwort ein:"
CreateAccountScreenInstructionsConfirmPassword = "Tippe zur Sicherheit dein Passwort noch einmal ein:"
CreateAccountScreenInstructionsDob = "Gib dein Geburtsdatum ein:"
CreateAccountScreenCancel = "Abbrechen"
CreateAccountScreenSubmit = "Weiter"
CreateAccountScreenConnectionErrorSuffix = ".\n\nBitte versuche es später noch einmal."
CreateAccountScreenNoAccountName = "Bitte gib einen Account-Namen ein."
CreateAccountScreenAccountNameTooShort = "Dein Account-Name muss mindestens %s Zeichen lang sein. Bitte erneut versuchen."
CreateAccountScreenPasswordTooShort = "Dein Passwort muss mindestens %s Zeichen lang sein. Bitte erneut versuchen."
CreateAccountScreenPasswordMismatch = "Die eingegeben Passwörter stimmten nicht überein. Bitte erneut versuchen."
CreateAccountScreenInvalidDob = "Bitte gib dein Geburtsdatum ein."
CreateAccountScreenUserNameTaken = "Dieser Benutzername ist schon vergeben. Bitte erneut versuchen."
CreateAccountScreenInvalidUserName = "Ungültiger Benutzername.\nBitte erneut versuchen."
CreateAccountScreenUserNameNotFound = "Benutzernamen nicht gefunden.\nBitte erneut versuchen oder neuen Account einrichten."
CreateAccountScreenEmailInstructions = "Bitte gib deine E-Mail-Adresse ein.\nWarum? Aus zwei Gründen:\n1. Wenn du  dein Passwort vergisst, können wir es dir zuschicken!\n2. Wir können dir die neuesten Informationen über\nDisneys Toontown Online schicken."
CreateAccountScreenEmailInstructionsUnder13 = "Du hast angegeben, dass du unter 13 Jahre alt bist.\nZum Einrichten eines Accounts benötigen wir die E-Mail-Adresse eines Elternteils oder Erziehungsberechtigten."
CreateAccountScreenEmailConfirm = "Tippe die E-Mail-Adresse zur Sicherheit noch einmal ein:"
CreateAccountScreenEmailPanelSubmit = "Weiter"
CreateAccountScreenEmailPanelCancel = "Abbrechen"
CreateAccountScreenInvalidEmail = "Bitte gib die vollständige E-Mail-Adresse ein."
CreateAccountScreenEmailMismatch = "Die eingegebenen E-Mail-Adressen stimmten nicht überein. Bitte erneut versuchen."

# SecretFriendsInfoPanel.py
SecretFriendsInfoPanelOk = lOK
SecretFriendsInfoPanelText = ["""
Die Funktion Geheime Freunde

Durch die Funktion Geheime Freunde kann ein Mitglied direkt mit anderen Mitgliedern von Disneys Toontown Online (dem "Service") chatten, sobald die Mitglieder eine Geheime-Freunde-Verbindung eingerichtet haben. Wenn Ihr Kind versucht, die Funktion Geheime Freunde zu nutzen, werden wir Sie bitten Elternpasswort einzugeben, um damit Ihre Zustimmung zur Nutzung dieser Funktion durch Ihr Kind zu bestätigen. Im Folgenden eine ausführliche Beschreibung der Einrichtung einer Geheime-Freunde-Verbindung zwischen zwei Mitgliedern, die wir "Sally" und "Mike" nennen wollen.
1. Ein Elternteil von Sally und ein Elternteil von Mike aktivieren jeweils die Funktion Geheime Freunde, indem sie ihr jeweiliges Elternpasswort eingeben, und zwar entweder (a) im Bereich Account-Optionen innerhalb des Service oder (b) auf Aufforderung während des Spiels durch ein Pop-Up Elterliche Kontrolle.
2. Sally fordert innerhalb des Service ein Geheimnis an (wie unten beschrieben).
""","""
3. Sallys Geheimnis wird Mike außerhalb des Service mitgeteilt (indem Sally das Geheimnis  entweder Mike selbst sagt oder an eine andere Person weitergibt.)
4. Mike teilt Sallys Geheimnis dem Service mit, und zwar innerhalb von 48 Stunden nachdem Sally das Geheimnis beim Service angefordert hat.
5. Dann benachrichtigt der Service Mike, dass Sally Mikes Geheime Freundin geworden ist. Ebenso benachrichtigt der Service Sally, dass Mike ihr Geheimer Freund geworden ist.
6. Sally und Mike können nun direkt miteinander chatten, bis entweder einer von beiden die Geheime-Freunde-Verbindung löst oder bis die Funktion Geheime Freunde für Sally oder Mike durch den jeweiligen Elternteil deaktiviert wird. Die Geheime-Freunde-Verbindung kann also jederzeit deaktiviert werden, und zwar (a) indem eines der Mitglieder den Geheimen Freund aus seiner Freundesliste entfernt (wie im Service beschrieben) oder (b) indem ein Elternteil dieses Mitglieds die Funktion Geheime Freunde deaktiviert, indem es den Bereich Accout-Optionen aufruft und den dort beschriebenen Schritten folgt.
""","""
Ein Geheimnis ist ein computergenerierter Zufallscode, der einem bestimmten Mitglied zugeordnet wird. Das Geheimnis muss dazu verwendet werden, binnen 48 Stunden nach Anforderung des Geheimnisses eine Geheime-Freunde-Verbindung zu aktivieren, ansonsten ist die Zeit für das Geheimnis abgelaufen und es kann nicht mehr verwendet werden. Außerdem kann ein Geheimnis nur zur Einrichtung einer Geheime-Freunde-Verbindung verwendet werden. Um weitere Geheime-Freunde-Verbindungen herzustellen, muss ein Mitglied für jeden zusätzlichen Geheimen Freund ein eigenes Geheimnis anfordern.

Geheime Freundschaften sind nicht übertragbar. Wenn zum Beispiel Sally Mikes Geheime Freundin wird und Mike der Geheime Freund von Jessica, wird Sally nicht automatisch auch Jessicas Geheime Freundin. Damit Sally und Jessica Geheime Freunde werden können, muss eine von ihnen ein neues Geheimnis vom Service anfordern und es der anderen mitteilen.
""","""
Geheime Freunde kommunizieren miteinander in einem freien interaktiven Chat. Der Inhalt dieses Chats wird direkt von den teilnehmenden Mitgliedern eingegeben und durch den Service verarbeitet, der von der Walt Disney Internet Group ("WDIG"), 506 2nd Avenue, Suite 2100, Seattle, WA 98104 (Telefon (509)-742-4698, E-Mail ms_support@help.go.com) betrieben wird. Wir raten unseren Mitgliedern zwar keine persönlichen Informationen auszutauschen, wie zum Beispiel Vor- und Nachnamen, E-Mail-Adressen, Postadressen oder Telefonnummern. Wir können jedoch nicht garantieren, dass ein solcher Austausch persönlicher Daten nicht erfolgt. Aus dem Geheime-Freunde-Chat werden die meisten unanständigen Redewendungen zwar automatisch herausgefiltert, doch erfolgt durch uns keine Moderation oder Beaufsichtigung. Wenn Eltern ihren Kindern die Nutzung ihres Accounts mit aktivierter Geheime-Freunde-Funktion erlauben, raten wir ihnen, ihre Kinder zu beaufsichtigen, während sie im Service spielen.
""","""
WDIG verwendet den Inhalt des Geheime-Freunde-Chats einzig und allein zur Übermittlung dieses Inhalts an den Geheimen Freund des Mitglieds und macht diesen Inhalt keinem Dritten bekannt, außer (1) dies ist gesetzlich erforderlich, zum Beispiel aufgrund einer gerichtlichen Verfügung; (2) um die für den Service geltenden Nutzungsbestimmungen durchzusetzen (die auf der Homepage des Service eingesehen werden können); oder (3) um die Sicherheit der Mitglieder des Service und des Service selbst zu schützen. Auf Verlangen kann ein Elternteil eines Kindes in jeden von diesem Kind beigesteuerten Inhalt des Geheime-Freunde-Chats Einsicht nehmen und diesen löschen, sofern ein solcher Chat-Inhalt nicht bereits durch WDIG aus ihren Dateien gelöscht wurde. Gemäß den gesetzlichen Bestimmungen über den Online-Datenschutz bei Kindern ist es uns nicht gestattet, die Teilnahme eines Kindes an irgendeiner Aktivität (einschließlich Geheime Freunde) von der Angabe persönlicher Daten des Kindes abhängig zu machen, sofern diese Daten nicht für die Teilnahme an einer solchen Aktivität unbedingt erforderlich sind.
""","""
Außerdem erkennen wir wie bereits gesagt das Recht eines Elternteils an, die Zustimmung zu einer weiteren Nutzung der Funktion Geheime Freunde durch das Kind zurückzunehmen. Durch Aktivieren der Geheime-Freunde-Funktion erkennen Sie an, dass mit der Möglichkeit des Chattens der Mitglieder über die Funktion Geheime Freunde gewisse Risiken verbunden sind und dass Sie über solche Risiken informiert wurden und sie in Kauf nehmen.
"""
]

# ParentPasswordScreen.py
ParentPasswordScreenTitle = "Elterliche Kontrolle"
ParentPasswordScreenPassword = "Elternpasswort erstellen"
ParentPasswordScreenConfirmPassword = "Elternpasswort bestätigen"
ParentPasswordScreenSubmit = "Elternpasswort einrichten"
ParentPasswordScreenConnectionErrorSuffix = ".\nBitte später erneut versuchen."
ParentPasswordScreenPasswordTooShort = "Ihr Passwort muss mindestens %s Zeichen lang sein. Bitte erneut versuchen."
ParentPasswordScreenPasswordMismatch = "Die eingegebenen Passwörter stimmten nicht überein. Bitte erneut versuchen."
ParentPasswordScreenConnectionProblemJustPaid = "Beim Versuch, den Account-Server zu erreichen, ist ein Fehler aufgetreten. Machen Sie sich jedoch keine Gedanken, Ihre Bezahlung ist trotzdem angekommen.\n\nSie werden beim nächsten Login gebeten werden, Ihr Passwort noch einmal einzurichten."
ParentPasswordScreenConnectionProblemJustLoggedIn = "Beim Versuch, den Account-Server zu erreichen, ist ein Fehler aufgetreten. Bitte versuchen Sie es später noch einmal."
ParentPasswordScreenSecretFriendsMoreInfo = "Mehr Informationen"
ParentPasswordScreenInstructions = """Bitte erstellen Sie ein \"Elternpasswort\" für diesen Account. Das Elternpasswort wird später benötigt:

  1.  Wenn wir Sie bitten, der Nutzung bestimmter interaktiver 
       Funktion von Toontown durch Ihr Kind/Ihre Kinder 
       zuzustimmen, wie zum Beispiel der Funktion \"Geheime Freunde\". 
       Für eine vollständige Beschreibung der Funktion \"Geheime Freunde\" 
       und wie Ihr Kind/Ihre Kinder dadurch mit anderen Mitgliedern von Toontown 
       kommunizieren kann/können, klicken Sie bitte 
       die Schaltfläche '""" + ParentPasswordScreenSecretFriendsMoreInfo + """' unten an. 
       Zur Aktivierung dieser Funktion ist Ihre Zustimmung erforderlich.

2. Um Rechnungs- und Account-Daten auf der 
    Toontown-Website zu aktualisieren.
"""
ParentPasswordScreenAdvice = "Halten Sie dieses Elternpasswort unbedingt geheim, damit Sie die Nutzung der interaktiven Features Ihres Accounts durch Ihr Kind/Ihre Kinder immer unter Kontrolle behalten."
ParentPasswordScreenPrivacyPolicy = "Datenschutz"

# ForgotPasswordScreen.py
ForgotPasswordScreenTitle = "Wenn Sie Ihr Passwort vergessen, schicken wir es Ihnen gern zu."
ForgotPasswordScreenInstructions = "Geben Sie hier Ihren Account-Namen ein ODER die E-Mail-Adresse, die Sie uns gegeben haben. "
ForgotPasswordScreenEmailEntryLabel = "E-Mail-Adresse"
ForgotPasswordScreenOr = "ODER"
ForgotPasswordScreenAcctNameEntryLabel = "Account-Name"
ForgotPasswordScreenSubmit = "Senden"
ForgotPasswordScreenCancel = lCancel
ForgotPasswordScreenEmailSuccess = "Ihr Passwort wurde an '%s' geschickt."
ForgotPasswordScreenEmailFailure = "E-Mail-Adresse nicht gefunden: '%s'."
ForgotPasswordScreenAccountNameSuccess = "Ihr Passwort wurde an die E-Mail-Adresse geschickt, die Sie bei der Einrichtung Ihres Accounts angegeben haben."
ForgotPasswordScreenAccountNameFailure = "Account nicht gefunden: %s"
ForgotPasswordScreenNoEmailAddress = "Dieser Account wurde von einer Person unter 13 Jahren eingerichtet und hat keine E-Mail-Adresse. Wir können leider kein Passwort zuschicken.\n\nSie können aber gern einen neuen Accout einrichten!"
ForgotPasswordScreenInvalidEmail = "Bitte geben Sie eine gültige E-Mail-Adresse ein."

# GuiScreen.py
GuiScreenToontownUnavailable = "Toontown scheint vorübergehend nicht erreichbar zu sein, weiterer Versuch ..."
GuiScreenCancel = "Abbrechen"

# AchievePage.py
AchievePageTitle = "Erfolge\n(Demnächst)"

# PhotoPage.py
PhotoPageTitle = "Foto\n(Demnächst)"

# BuildingPage.py
BuildingPageTitle = "Gebäude\n(Demnächst)"

# InventoryPage.py
InventoryPageTitle = "Gags"
InventoryPageDeleteTitle = "GAGS LÖSCHEN"
InventoryPageTrackFull = "Du hast alle Gags im Ablauf %s."
InventoryPagePluralPoints = "Du bekommst einen neuen %(trackName)s-Gag, \nwenn du noch %(numPoints)s\n%(trackName)s-Punkte machst."
InventoryPageSinglePoint = "Du bekommst einen neuen\n%(trackName)s-Gag, wenn du noch\n%(numPoints)s %(trackName)s-Punkte machst."
InventoryPageNoAccess = "Du hast noch keinen Zugang zu Ablauf %s."

# NPCFriendPage.py
NPCFriendPageTitle = "SOS Toons"

# NPCFriendPanel.py
NPCFriendPanelRemaining = "Bleiben %s"

# MapPage.py
MapPageTitle = "Stadtplan"
MapPageBackToPlayground = "Zurück zum Spielplatz"
MapPageBackToCogHQ = "Zurück zum Bot-Hauptquartier"
MapPageGoHome = "Nach Hause"
# hood name, street name
MapPageYouAreHere = "Du bist in: %s\n%s"
MapPageYouAreAtHome = "Du bist auf\ndeinem Grundstück"
MapPageYouAreAtSomeonesHome = "Du bist auf dem Grundstück von %s "
MapPageGoTo = "Gehe zu\n%s"

# OptionsPage.py
OptionsPageTitle = "Optionen"
OptionsPagePurchase = "Jetzt abonnieren!"
OptionsPageLogout = "Logout"
OptionsPageExitToontown = "Toontown verlassen"
OptionsPageMusicOnLabel = "Musik an."
OptionsPageMusicOffLabel = "Musik aus."
OptionsPageSFXOnLabel = "Soundeffekte an."
OptionsPageSFXOffLabel = "Soundeffekte aus."
OptionsPageFriendsEnabledLabel = "Anfragen neuer Freunde akzeptieren."
OptionsPageFriendsDisabledLabel = "Anfragen neuer Freunde nicht akzeptieren."
OptionsPageSpeedChatStyleLabel = "Schnell-Chat-Farbe"
OptionsPageDisplayWindowed = "Im Fenster"
OptionsPageSelect = "Auswählen"
OptionsPageToggleOn = "Einschalten"
OptionsPageToggleOff = "Ausschalten"
OptionsPageChange = "Wechseln"
OptionsPageDisplaySettings = "Bildschirm: %(screensize)s, %(api)s"
OptionsPageDisplaySettingsNoApi = "Bildschirm: %(screensize)s"
OptionsPageExitConfirm = "Toontown verlassen?"

DisplaySettingsTitle = "Anzeigeeinstellungen"
DisplaySettingsIntro = "Mit den folgenden Einstellungen kannst du die Darstellung von Toontown auf deinem Computer konfigurieren. Wenn bei dir keine Probleme auftreten, müssen sie wahrscheinlich nicht geändert werden."
DisplaySettingsIntroSimple = "Du kannst die Bildschirmauflösung auf einen höheren Wert einstellen, damit Text und Bild in Toontown deutlicher dargestellt werden. Bei manchen Grafikkarten kann dies aber dazu führen, dass das Spiel nicht so gut läuft oder überhaupt nicht funktioniert."

DisplaySettingsApi = "Grafik-API:"
DisplaySettingsResolution = "Auflösung:"
DisplaySettingsWindowed = "In einem Fenster"
DisplaySettingsFullscreen = "Ganzer Bildschirm"
DisplaySettingsApply = "Verwenden"
DisplaySettingsCancel = lCancel
DisplaySettingsApplyWarning = "Wenn du OK drückst, ändern sich die Einstellungen für die Anzeige. Wenn die neue Konfiguration für deinen Computer nicht geeignet ist, kehrt die Anzeige nach %s Sekunden zur ursprünglichen Konfiguration zurück."
DisplaySettingsAccept = "Drücke OK, um die neuen Einstellungen zu behalten, oder Abbrechen, um sie rückgängig zu machen. Wenn du gar nichts tust, gehen die Einstellungen nach %s Sekunden automatisch zurück."
DisplaySettingsRevertUser = "Deine vorherigen Anzeigeeinstellungen wurden wiederhergestellt."
DisplaySettingsRevertFailed = "Die gewählten Anzeigeeinstellungen funktionieren auf deinem Computer nicht. Deine vorherigen Anzeigeeinstellungen wurden wiederhergestellt."


# TrackPage.py
TrackPageTitle = "Gag-Ablauf Training"
TrackPageShortTitle = "Gag-Training"
TrackPageSubtitle = "Löse Toon-Aufgaben um zu lernen, wie man neue Gags einsetzt!"
TrackPageTraining = "Du übst das Einsetzen von %s Gags.\nWenn du alle 16 Aufgaben bewältigst, wirst du\nin der Lage sein, %s Gags im Kampf einzusetzen."
TrackPageClear = "Du übst im Moment keinen Gag-Typ."
TrackPageFilmTitle = "%s\nTraining\nFilm"
TrackPageDone = "ENDE"

# QuestPage.py
QuestPageToonTasks = "Toon-Aufgaben"
# questName, toNpcName, toNpcBuilding, toNpcStreetName, toNpcLocationName, npcName
#QuestPageDelivery = "%s\nTo: %s\n  %s\n  %s\n  %s\n\nFrom: %s"
# questName, toNpcName, toNpcBuilding, toNpcStreetName, toNpcLocationName, npcName
#QuestPageVisit = "%s %s\n  %s\n  %s\n  %s\n\nFrom: %s"
# questName, toNpcName, toNpcBuilding, toNpcStreetName, toNpcLocationName
# Choose between trackA and trackB.
#
# To choose, go see:
#   Flippy
#   Town Hall
#   Playground
#   Toontown Central
#QuestPageTrackChoice = "%s\n\nTo choose, go see:\n  %s\n  %s\n  %s\n  %s"
# questName, npcName, buildingName, streetName, locationName
QuestPageChoose = "Wählen"
# building name, street name, Npc location
QuestPageDestination = "%s\n%s\n%s"
# npc name, building name, street name, Npc location
QuestPageNameAndDestination = "%s\n%s\n%s\n%s"

QuestPosterHQOfficer = "Mitarbeiter in der Zentrale"
QuestPosterHQBuildingName = "Toontown-Zentrale"
QuestPosterHQStreetName = "In irgendeiner Straße"
QuestPosterHQLocationName = "In irgendeinem Viertel"

QuestPosterTailor = "Schneider"
QuestPosterTailorBuildingName = "Bekleidungsgeschäft"
QuestPosterTailorStreetName = "Irgendwo auf dem Spielplatz"
QuestPosterTailorLocationName = "In irgendeinem Viertel"
QuestPosterPlayground = "Auf dem Spielplatz"
QuestPosterAtHome = "Bei deinem Haus"
QuestPosterInHome = "In deinem Haus"
QuestPosterOnPhone = "An deinem Telefon"
QuestPosterEstate = "Auf deinem Grundstück"
QuestPosterAnywhere = "Irgendwo in den\nStraßen der Stadt"
QuestPosterAuxTo = "nach:"
QuestPosterAuxFrom = "von:"
QuestPosterAuxFor = "für:"
QuestPosterAuxOr = "oder:"
QuestPosterAuxReturnTo = "Zurückkehren\nzu:"
QuestPosterFun = "Nur so zum Spaß!"
QuestPosterFishing = "ANGELN GEHEN"
QuestPosterComplete = "Komplett"

# ShardPage.py
ShardPageTitle = "Bezirke"
ShardPageHelpIntro = "Jeder Bezirk ist ein Abbild der Toontown-Welt."
ShardPageHelpWhere = "Du bist zurzeit im Bezirk \"%s\"."
ShardPageHelpWelcomeValley = "Du bist zurzeit im Bezirk 'Willkommens-Tal' in \"%s\"."
ShardPageHelpMove = "Um zu einem anderen Bezirk zu kommen, klicke auf seinen Namen."

ShardPagePopulationTotal = "Gesamtbevölkerung Toontown:\n%d"
ShardPageScrollTitle = "Bezirk Bevölkerungszahl"

# SuitPage.py
SuitPageTitle = "Bot-Galerie"
SuitPageMystery = "???"
SuitPageQuota = "%s von %s"
SuitPageCogRadar = "%s anwesend"
SuitPageBuildingRadarS = "%s Gebäude"
SuitPageBuildingRadarP = "%s Gebäude"

# DisguisePage.py
DisguisePageTitle = "Bot-Verkleidung"
DisguisePageMeritAlert = "Bereit zur\nBeförderung!"
DisguisePageCogLevel = "Level %s"
DisguisePageMeritFull = "Voll"

# FishPage.py
FishPageTitle = "Angeln"
FishPageTitleTank = "Fischeimer"
FishPageTitleCollection = "Fischalbum"
FishPageTitleTrophy = "Angeltrophäen"
FishPageWeightStr = "Gewicht: "
FishPageWeightLargeS = "%d kg"
FishPageWeightLargeP = "%d kg "
FishPageWeightSmallS = "%d g"
FishPageWeightSmallP = "%d g"
FishPageWeightConversion = 16
FishPageValueS = "Wert: %d Jelly Bean"
FishPageValueP = "Wert: %d Jelly Beans"
FishPageTotalValue = ""
FishPageCollectedTotal = "Gesammelte Fischarten: %d von %d"
FishPageRodInfo = "%s Angelrute\n%d - %d Pfund"
FishPageTankTab = "Eimer"
FishPageCollectionTab = "Album"
FishPageTrophyTab = "Trophäen"

FishPickerTotalValue = "Fische: %s / %s\nWert: %d Jelly Beans"

UnknownFish = "???"

FishingRod = "%s Angelrute"
FishingRodNameDict = {
    0 : "Zweig",
    1 : "Bambus",
    2 : "Hartholz",
    3 : "Stahl",
    4 : "Gold",
    }
FishTrophyNameDict = {
    0 : "Guppy",
    1 : "Elritze",
    2 : "Fisch",
    3 : "Fliegender Fisch",
    4 : "Hai",
    5 : "Swordfish",
    6 : "Killer Whale",
    }

# QuestChoiceGui.py
QuestChoiceGuiCancel = lCancel

# TrackChoiceGui.py
TrackChoiceGuiChoose = "Auswählen"
TrackChoiceGuiCancel = lCancel
TrackChoiceGuiHEAL = 'Durch Aufheitern kannst du andere Toons im Kampf heilen.'
TrackChoiceGuiTRAP = 'Fallen Stellen sind mächtige Gags, die zusammen mit einem Köder verwendet werden müssen.'
TrackChoiceGuiLURE = 'Du kannst Köder verwenden, um Bots zu betäuben oder in Fallen Stellen zu locken.'
TrackChoiceGuiSOUND = 'Sound-Gags wirken bei allen Bots, aber nicht besonders stark.'
TrackChoiceGuiDROP = "Fall-Gags richten viel Schaden an, sind jedoch nicht besonders genau."

# EmotePage.py
EmotePageTitle = "Ausdrucksmöglichkeiten / Gefühle"
EmotePageDance = "Du hast die folgende Tanzfolge aufgestellt:"
EmoteJump = "Springen"
EmoteDance = "Tanzen"
EmoteHappy = "Glücklich"
EmoteSad = "Traurig"
EmoteAnnoyed = "Verärgert"
EmoteSleep = "Schläfrig"

# Emote.py
# List of emotes in the order they should appear in the SpeedChat.
# Must be in the same order as the function list (EmoteFunc) in Emote.py
EmoteList = [
    "Winken",
    "Glücklich",
    "Traurig",
    "Ärgerlich",
    "Schläfrig",
    "Achselzucken",
    "Tanzen",
    "Denken",
    "Gelangweilt",
    "Applaus",
    "Überrascht",
    "Verwirrt",
    "Verspotten",
    "Verbeugen",
    "Sehr traurig",
    "Breites Grinsen",
    "Lachen",
    lYes,
    lNo,
    lOK,
    ]

EmoteWhispers = [
    "%s winkt.",
    "%s ist glücklich.",
    "%s ist traurig.",
    "%s ist ärgerlich.",
    "%s ist schläfrig.",
    "%s zuckt die Achseln.",
    "%s tanzt.",
    "%s zwinkert.",
    "%s ist gelangweilt.",
    "%s applaudiert.",
    "%s ist überrascht.",
    "%s ist verwirrt.",
    "%s macht sich über dich lustig.",
    "%s verbeugt sich vor dir.",
    "%s ist sehr traurig.",
    "%s grinst.",
    "%s lacht.",
    "%s sagt Ja.",
    "%s sagt Nein.",
    "%s sagt OK.",
    ]

# Reverse lookup:  get the index from the name.
EmoteFuncDict = {
    "Winken"   : 0,
    "Glücklich"  : 1,
    "Traurig"    : 2,
    "Ärgerlich"  : 3,
    "Schläfrig" : 4,
    "Achselzucken"  : 5,
    "Tanzen"  : 6,
    "Zwinkern"   : 7,
    "Gelangweilt"  : 8,
    "Applaus" : 9,
    "Überrascht" : 10,
    "Verwirrt"  : 11,
    "Verspotten"  : 12,
    "Verbeugen"    : 13,
    "Sehr traurig" : 14,
    "Breites Grinsen" : 15,
    "Lachen" : 16,
    lYes    : 17,
    lNo     : 18,
    lOK     : 19,
    }

# SuitBase.py
SuitBaseNameWithLevel = "%(name)s\n%(dept)s\nLevel %(level)s"

# SuitDialog.py
SuitBrushOffs = {
    'f':  ["Ich komme zu spät zu einem Meeting.",
           ],
    'p':  ["Schieb ab.",
           ],
    'ym': ['Jasager sagt NEIN.',
           ],
    None: ["Das ist mein freier Tag.",
           "Ich glaube, du bist im falschen Büro.",
           "Deine Leute sollen meine Leute anrufen.",
           "Du bist überhaupt nicht in der Lage, dich mit mir zu treffen.",
           "Sprich mit meiner Sekretärin."]
    }

# HealthForceAcknowledge.py
HealthForceAcknowledgeMessage = "Du kannst den Spielplatz erst verlassen, wenn dein Lach-O-Meter lächelt!"

# InventoryNew.py
InventoryTotalGags = "Gags insgesamt\n%d / %d"
InventoryDelete = "LÖSCHEN"
InventoryDone = "FERTIG"
InventoryDeleteHelp = "Klicke auf einen Gag um ihn zu LÖSCHEN."
InventorySkillCredit = "Erfahrung Punkte: %s"
InventorySkillCreditNone = "Erfahrung Punkte: Keine"
InventoryDetailAmount = "%(numItems)s / %(maxItems)s"
# acc, damage_string, damage, single_or_group
InventoryDetailData = "Genauigkeit: %(accuracy)s\n%(damageString)s: %(damage)d\n%(singleOrGroup)s"
InventoryTrackExp = "%(curExp)s / %(nextExp)s"
InventoryAffectsOneCog = "Wirkt auf: Einen "+ Cog
InventoryAffectsOneToon = "Wirkt auf: Einen Toon"
InventoryAffectsAllToons = "Wirkt auf: Alle Toons"
InventoryAffectsAllCogs = "Wirkt auf: Alle "+ Cogs
InventoryHealString = "AUFHEITERN"
InventoryDamageString = "Schaden"
InventoryBattleMenu = "KAMPFMENÜ "
InventoryRun = "RENNEN"
InventorySOS = "SOS"
InventoryPass = "AUSSETZEN"
InventoryClickToAttack = "Klick auf einen\nGag um\nanzugreifen"

# NPCForceAcknowledge.py
NPCForceAcknowledgeMessage = "Du musst mit dem Toon-Express fahren, ehe du gehst.\n\n\n\n\n\nDu findest den Toon-Express neben Goofys Gag-Laden."
NPCForceAcknowledgeMessage2 = "Du hast die Suche nach dem Toon-Express wirklich hervorragend gemeistert!\nMelde dich nun in der Toontown-Zentrale zurück.\n\n\n\n\n\nDie Toontown-Zentrale befindet sich in der Nähe der Spielplatzmitte."
NPCForceAcknowledgeMessage3 = "Vergiss nicht, mit dem Toon-Express zu fahren.\n\n\n\n\n\nDu findest ihn neben Goofys Gag-Laden."
NPCForceAcknowledgeMessage4 = "Glückwunsch! Du hast den Toon-Express gefunden und bist damit gefahren!\n\n\n\n\n\nMelde dich nun in der Toontown-Zentrale zurück."

# Toon.py
ToonSleepString = ". . . ZZZ . . ."

# Movie.py
MovieTutorialReward1 = "Du hast 1 Wurfpunkt erhalten! Wenn du 10 hast, bekommst du einen neuen Gag!"
MovieTutorialReward2 = "Du hast 1 Spritzpunkt erhalten! Wenn du 10 hast, bekommst du einen neuen Gag!"
MovieTutorialReward3 = "Gute Arbeit! Gut gemacht! Du hast deine erste Toon-Aufgabe erledigt!"
MovieTutorialReward4 = "Gehe zur Toontown-Zentrale, um deine Belohnung abzuholen!"
MovieTutorialReward5 = "Viel Spaß!"

# ToontownBattleGlobals.py
BattleGlobalTracks = ['Aufheitern', 'Fallen Stellen', 'Ködern', 'Volldröhnen', 'Werfen', 'Spritzen', 'Fallenlassen']
BattleGlobalNPCTracks = ['neu auffüllen', 'Toons treffen', 'Bots verfehlen']
BattleGlobalAvPropStrings = (
    ('Feder', 'Megafon', 'Lippenstift', 'Bambusrohr', 'Zauberpuder', 'Jonglierbälle'),
    ('Bananenschale', 'Harke', 'Murmeln', 'Treibsand', 'Falltür', 'TNT'),
    ('1-Euro-Schein', 'Kleiner Magnet', '5-Euro-Schein', 'Großer Magnet', '10-Euro-Schein', 'Hypno-Brille'),
    ('Motorradhupe', 'Trillerpfeife', 'Signalhorn', 'Auugah', 'Elefantenrüssel', 'Nebelhorn'),
    ('Napfkuchen', 'Obsttortenstück', 'Kremtortenstück', 'Ganze Obsttorte', 'Ganze Kremtorte', 'Geburtstagstorte'),
    ('Spritzblume', 'Glas Wasser', 'Spritzpistole', 'Seltersflasche', 'Feuerwehrschlauch', 'Sturmwolke'),
    ('Blumentopf', 'Sandsack', 'Amboss', 'Großes Gewicht', 'Safe', 'Konzertflügel')
    )
BattleGlobalAvPropStringsSingular = (
    ('eine Feder', 'ein Megafon', 'ein Lippenstift', 'ein Bambusrohr', 'ein Zauberpuder', 'ein Satz Jonglierbälle '),
    ('eine Bananenschale', 'eine Harke', 'ein Satz Murmeln', 'eine Treibsandstelle', 'eine Falltür', 'ein TNT'),
    ('ein 1-Euro-Schein', 'ein kleiner Magnet', 'ein 5-Euro-Schein', 'ein großer Magnet', 'ein 10-Euro-Schein', 'eine Hypno-Brille'),
    ('eine Motorradhupe', 'eine Trillerpfeife', 'ein Signalhorn', 'ein Auugah', 'ein Elefantenrüssel', 'ein Nebelhorn'),
    ('ein Napfkuchen', 'ein Obsttortenstück', 'ein Kremtortenstück', 'eine ganze Obsttorte', 'eine ganze Kremtorte', 'eine Geburtstagstorte'),
    ('eine Spritzblume', 'ein Glas Wasser', 'eine Spritzpistole', 'eine Seltersflasche', 'ein Feuerwehrschlauch', 'eine Sturmwolke'),
    ('ein Blumentopf', 'ein Sandsack', 'ein Amboss', 'ein großes Gewicht', 'ein Safe', 'ein Konzertflügel')
    )
BattleGlobalAvPropStringsPlural = (
    ('Federn', 'Megafone', 'Lippenstifte', 'Bambusrohre', 'Zauberpuders', 'Jonglierballsätze'),
    ('Bananenschalen', 'Harken', 'Murmelsätze', 'Treibsandstellen', 'Falltüren','TNTs'),
    ('1-Euro-Scheine', 'Kleine Magneten', '5-Euro-Scheine', 'Große Magneten','10-Euro-Scheine', 'Hypno-Brillen'),
    ('Motorradhupen', 'Trillerpfeifen', 'Signalhörner', 'Auugahs', 'Elefantenrüssel', 'Nebelhörner'),
    ('Napfkuchen', 'Obsttortenstücke', 'Kremtortenstücke','Ganze Obsttorten', 'Ganze Kremtorten', 'Geburtstagstorten '),
    ('Spritzblumen', 'Gläser mit Wasser', 'Spritzpistolen','Seltersflaschen', 'Feuerwehrschläuche', 'Sturmwolken'),
    ('Blumentöpfe', 'Sandsäcke', 'Ambosse', 'Große Gewichte', 'Safes','Konzertflügel')
    )
BattleGlobalAvTrackAccStrings = ("Mittel", "Perfekt", "Niedrig", "Hoch", "Mittel", "Hoch", "Niedrig")

AttackMissed = "VORBEI"

NPCCallButtonLabel = 'RUFEN'

# ToontownGlobals.py

# (to, in, location)
# reference the location name as [-1]; it's guaranteed to be the last entry
# This table may contain names for hood zones (N*1000) that are not
# appropriate when referring to the hood as a whole. See the list of
# names below this table for hood names.
GlobalStreetNames = {
    20000 : ("zur",     "in der",     "Einweisungsgasse"), # Tutorial
    1000  : ("zum", "auf dem", "Spielplatz"),
    1100  : ("zum",     "auf dem",     "Muschel-Boulevard"),
    1200  : ("zur",     "in der",     "Seetangstraße"),
    1300  : ("zur",     "auf der",     "Leuchtturmgasse"),
    2000  : ("zum", "auf dem", "Spielplatz"),
    2100  : ("zur",     "in der",     "Albernstraße"),
    2200  : ("zur",     "in der",     "Hohlgasse"),
    2300  : ("zum",     "auf dem",     "Kasperwinkel"),
    3000  : ("zum", "auf dem", "Spielplatz"),
    3100  : ("zum",     "im",     "Walrossweg"),
    3200  : ("zur",     "in der",     "Schneestraße"),
    4000  : ("zum", "auf dem", "Spielplatz"),
    4100  : ("zur",     "auf der",     "Sopran-Allee"),
    4200  : ("zum",     "auf dem",     "Bass-Promenade"),
    4300  : ("zur",     "auf der",     "Tenor-Terrasse"),
    5000  : ("zum", "auf dem", "Spielplatz"),
    5100  : ("zur",     "in der",     "Ulmenstraße"),
    5200  : ("zur",     "in der",     "Ahornstraße"),
    5300  : ("zur",     "in der",     "Eichenstraße"),
    9000  : ("zum", "auf dem", "Spielplatz"),
    9100  : ("zur",     "in der",     "Schlafliedgasse"),
    10000 : ("zum",     "im",     "Chefomat-Hauptquartier"),
    10100 : ("zur", "in der", "Chefomat-Hauptquartier-Lobby"),
    11000 : ("zum", "auf dem", "Schachermat-HQ-Hof"),
    11100 : ("zur", "in der", "Schachermat-HQ-Lobby"),
    11200 : ("zur", "in der", "Schachermat-Fabrik"),
    11500 : ("zur", "in der", "Schachermat-Fabrik"),
    12000 : ("zum",     "im",     "Monetomat-Hauptquartier"),
    12100 : ("zur", "in der", "Monetomat-Hauptquartier-Lobby"),
    13000 : ("zum",     "im",     "Gesetzomat-Hauptquartier"),
    13100 : ("zur", "in der", "Gesetzomat-Hauptquartier-Lobby"),
    }

# reference the location name as [-1]; it's guaranteed to be the last entry
DonaldsDock       = ("zu",     "in",     "Donalds Dock")
ToontownCentral   = ("nach",     "in",     "Toontown Mitte")
TheBrrrgh         = ("zu",     "in",     "Das Brrr")
MinniesMelodyland = ("zu",     "in",     "Minnies Melodienland")
DaisyGardens      = ("zu",     "in",     "Daisys Gärten")
ConstructionZone  = ("zur", "in der", "Bauzone")
FunnyFarm         = ("zur", "auf der", "Spaßfarm")
GoofyStadium      = ("zum",     "im",     "Goofy-Stadion")
DonaldsDreamland  = ("zu",     "in",     "Donalds Traumland")
BossbotHQ         = ("zum",     "im",     "Chefomat-Hauptquartier")
SellbotHQ         = ("zum",     "im",     "Schachermat-HQ")
CashbotHQ         = ("zum",     "im",     "Monetomat-Hauptquartier")
LawbotHQ          = ("zum",     "im",     "Gesetzomat-Hauptquartier")
Tutorial          = ("zur", "in der ", "Einweisung")
MyEstate          = ("zu",     "in",     "Dein Haus")
WelcomeValley     = ("zum",     "im",     "Willkommens-Tal")

Factory = 'Fabrik'
Headquarters = 'Toontown-Zentrale'
SellbotFrontEntrance = 'Vordereingang'
SellbotSideEntrance = 'Seiteneingang'

FactoryNames = {
    0 : 'Fabrik-Nachbildung',
    11500 : 'Schachermat-Bot-Fabrik',
    }

FactoryTypeLeg = 'Bein'
FactoryTypeArm = 'Arm'
FactoryTypeTorso = 'Oberkörper'

# ToontownLoader.py
LoaderLabel = "Laden ..."

# PlayGame.py
HeadingToHood = "Läuft %(to)s %(hood)s..." # hood name
HeadingToYourEstate = "Läuft zu deinem Grundstück ..."
HeadingToEstate = "Läuft zu %ss Grundstück ..."  # avatar name
HeadingToFriend = "Läuft zum Grundstück von %ss Freund ..."  # avatar name

# Hood.py
HeadingToPlayground = "Läuft zum Spielplatz ..."
HeadingToStreet = "Läuft %(to)s %(street)s..." # Street name

# TownBattle.py
TownBattleRun = "Den ganzen Weg zurück zum Spielplatz rennen?"

# TownBattleChooseAvatarPanel.py
TownBattleChooseAvatarToonTitle = "WELCHER TOON?"
TownBattleChooseAvatarCogTitle = "WELCHER "+ string.upper(Cog) +  "?"
TownBattleChooseAvatarBack = "ZURÜCK"

# TownBattleSOSPanel.py
TownBattleSOSNoFriends = "Es sind keine Freunde da!"
TownBattleSOSWhichFriend = "Welchen Freund rufen?"
TownBattleSOSNPCFriends = "Gerettete Toons"
TownBattleSOSBack = "ZURÜCK"

# TownBattleToonPanel.py
TownBattleToonSOS = "SOS"
TownBattleUndecided = "?"
TownBattleHealthText = "%(hitPoints)s/%(maxHit)s"

# TownBattleWaitPanel.py
TownBattleWaitTitle = "Warten auf\nandere Spieler ..."
TownSoloBattleWaitTitle = "Bitte warten ..."
TownBattleWaitBack = "ZURÜCK"

TownBattleSOSPetInfoOK = lOK

# Trolley.py
TrolleyHFAMessage = "Du darfst erst in den Toon-Express einsteigen, wenn dein Lach-O-Meter lächelt."
TrolleyTFAMessage = "Du darfst erst in den Toon-Express einsteigen, wenn" + Mickey + " es sagt."
TrolleyHopOff = "Aussteigen"

# DistributedFishingSpot.py
FishingExit = "Ausgang"
FishingCast = "Werfen"
FishingAutoReel = "Automatik-Rolle"
FishingItemFound = "Du hast was gefangen"
FishingCrankTooSlow = "Zu\nlangsam"
FishingCrankTooFast = "Zu\nschnell"
FishingFailure = "Du hast nichts gefangen!"
FishingFailureTooSoon = "Hol die Schnur nicht ein, ehe etwas angebissen hat. Warte, bis der Schwimmer sich schnell rauf und runter bewegt!"
FishingFailureTooLate = "Achte darauf die Schnur einzuholen, während der Fisch noch knabbert!"
FishingFailureAutoReel = "Die Automatik-Rolle hat diesmal nicht funktioniert. Dreh die Kurbel mit der Hand, genau mit der richtigen Geschwindigkeit, damit du etwas fängst!"
FishingFailureTooSlow = "Du hast die Kurbel zu langsam gedreht. Einige Fische sind schneller als andere. Versuche, den Geschwindigkeitsanzeiger in der Mitte zu halten!"
FishingFailureTooFast = "Du hast die Kurbel zu schnell gedreht. Einige Fische sind langsamer als andere. Versuche, den Geschwindigkeitsanzeiger in der Mitte zu halten!"
FishingOverTankLimit = "Dein Fischeimer ist voll. Verkaufe deine Fische an die Tierhandlung und komm zurück."
FishingBroke = "Du hast keine Jelly Beans mehr als Ködern! Fahr mit dem Toon-Express oder verkaufe Fische an die Tierhandlung und verdiene dir dadurch mehr Jelly Beans."
FishingHowToFirstTime = "Die Schaltfläche Werfen anklicken und herunterziehen. Je weiter du nach unten ziehst, desto kräftiger ist dein Wurf. Stell deine Angel so ein, dass du die Fischziele triffst.\n\nVersuch's mal!"
FishingHowToFailed = "Die Schaltfläche Werfen anklicken und herunterziehen. Je weiter du nach unten ziehst, desto kräftiger ist dein Wurf. Stell deine Angel so ein, dass du die Fischziele triffst.\n\nVersuch's nochmal!"
FishingBootItem = "Ein alter Stiefel"
FishingJellybeanItem = "%s Jelly Beans"
FishingNewEntry = "Neue Art!"
FishingNewRecord = "Neuer Rekord!"

# FishPoker
FishPokerCashIn = "Kassiere\n%s\n%s"
FishPokerLock = "Sperren"
FishPokerUnlock = "Freigeben"
FishPoker5OfKind = "5 von einer Sorte"
FishPoker4OfKind = "4 von einer Sorte"
FishPokerFullHouse = "Full House"
FishPoker3OfKind = "3 von einer Sorte"
FishPoker2Pair = "2 Paar"
FishPokerPair = "Paar"

# DistributedTutorial.py
TutorialGreeting1 = "Hi %s!"
TutorialGreeting2 = "Hi %s!\nKomm mal her!"
TutorialGreeting3 = "Hi %s!\nKomm mal her!\nVerwende dazu die Pfeil-Tasten!"
TutorialMickeyWelcome = "Willkommen in Toontown!"
TutorialFlippyIntro = "Ich möchte dir meinen Freund"+ Flippy +  " vorstellen ..."
TutorialFlippyHi = "Hi, %s!"
TutorialQT1 = "Zum Sprechen kannst du das hier benutzen."
TutorialQT2 = "Zum Sprechen kannst du das hier benutzen.\nKlick darauf und wähle dann 'Hi'."
TutorialChat1 = "Zum Sprechen kannst einen von diesen Schaltflächen benutzen."
TutorialChat2 = "Die blaue Schaltfläche erlaubt dir, über die Tastatur chatten."
TutorialChat3 = "Vorsicht! Die meisten Mitspieler werden dich nicht verstehen, wenn du die Tastatur benutzt."
TutorialChat4 = "Die grüne Schaltfläche öffnet den %s."
TutorialChat5 = "Jeder kann dich verstehen, wenn du den %s benutzt."
TutorialChat6 = "Versuch mal, 'Hi' zu sagen."
TutorialBodyClick1 = "Sehr gut!"
TutorialBodyClick2 = "Ich freue mich, dich kennen zu lernen. Wollen wir Freunde werden?"
TutorialBodyClick3 = "Wenn du mit"+ Flippy +  "Freundschaft schließen willst, klicke ihn an ..."
TutorialHandleBodyClickSuccess = "Gut gemacht!"
TutorialHandleBodyClickFail = "Knapp daneben. Versuche mal, direkt auf"+ Flippy +  "zu klicken ..."
TutorialFriendsButton = "Nun klicke auf die Schaltfläche 'Freunde' unter"+ Flippy +  "s Bild in der rechten Ecke."
TutorialHandleFriendsButton = "Und dann klicke auf die Schaltfläche 'Ja'."
TutorialOK = lOK
TutorialYes = lYes
TutorialNo = lNo
TutorialFriendsPrompt = "Möchtest du gern mit "+ Flippy +  " Freundschaft schließen?"
TutorialFriendsPanelMickeyChat = Flippy +" ist einverstanden, dein Freund zu sein. Klicke auf 'OK', um abzuschließen."
TutorialFriendsPanelYes = Flippy +" hat Ja gesagt!"
TutorialFriendsPanelNo = "Das ist nicht besonders freundlich!"
TutorialFriendsPanelCongrats = "Glückwunsch! Du hast deinen ersten Freund."
TutorialFlippyChat1 = "Komm mich besuchen, wenn du für deine erste Toon-Aufgabe bereit bist!"
TutorialFlippyChat2 = "Ich bin in der Toonhalle!"
TutorialAllFriendsButton = "Du kannst alle deine Freunde sehen, wenn du auf die Schaltfläche 'Freunde' klickst. Probiere es aus ... "
TutorialEmptyFriendsList = "Im Moment ist deine Liste leer, weil "+ Flippy +  " kein richtiger Mitspieler ist."
TutorialCloseFriendsList = "Klicke auf den die Schaltfläche 'Schließen', damit die\nListe verschwindet"
TutorialShtickerButton = "Die Schaltfläche in der Ecke rechts unten öffnet dein Sticker-Buch. Probier es aus ..."
TutorialBook1 = "Das Buch enthält viele nützliche Informationen, zum Beispiel diesen Stadtplan von Toontown."
TutorialBook2 = "Du kannst auch die Fortschritte bei deinen Toon-Aufgaben kontrollieren."
TutorialBook3 = "Wenn du fertig bist, klicke wieder auf die Buch-Schaltfläche, damit es sich schließt."
TutorialLaffMeter1 = "Auch das hier wirst du brauchen ..."
TutorialLaffMeter2 = "Auch das hier wirst du brauchen ...\nEs ist dein Lach-O-Meter."
TutorialLaffMeter3 = "Wenn dich"+ Cogs +  " angreifen, sinkt er."
TutorialLaffMeter4 = "Wenn du auf einem Spielplatz wie diesem hier bist, geht er wieder nach oben."
TutorialLaffMeter5 = "Wenn du Toon-Aufgaben löst, bekommst du Belohnungen, wie zum Beispiel eine Erhöhung deiner Lachstärke."
TutorialLaffMeter6 = "Pass gut auf! Wenn die "+ Cogs +  " dich besiegen, verlierst du alle deine Gags."
TutorialLaffMeter7 = "Um mehr Gags zu bekommen, musst du die Toon-Express Spiele spielen."
TutorialTrolley1 = "Folge mir zum Toon-Express!"
TutorialTrolley2 = "Spring auf!"
TutorialBye1 = "Spiel ein paar Spiele!"
TutorialBye2 = "Spiel ein paar Spiele!\nKaufe ein paar Gags!"
TutorialBye3 = "Geh zu "+ Flippy +  ", wenn du fertig bist!"

# TutorialForceAcknowledge.py
TutorialForceAcknowledgeMessage = "Du gehst in die falsche Richtung! Suche"+ Mickey +  "!"

# SpeedChat

# Used several places in the game. Defined globally because
# we keep changing the name
GlobalSpeedChatName = "Schnell-Chat"

SCMenuEmotions  = "EMOTIONEN"
SCMenuCustom    = "MEINE REDEWENDUNGEN"
SCMenuCog       = "BOT-SPRACHE"
SCMenuHello     = "HALLO"
SCMenuBye       = "AUF WIEDERSEHEN"
SCMenuHappy     = "GLÜCKLICH"
SCMenuSad       = "TRAURIG"
SCMenuFriendly  = "FREUNDLICH"
SCMenuSorry     = "BEDAUERND"
SCMenuStinky    = "SAUER"
SCMenuPlaces    = "ORTE"
SCMenuToontasks = "TOON-AUFGABEN"
SCMenuBattle    = "KAMPF"
SCMenuGagShop   = "GAG-LADEN"
SCMenuFactory   = "FABRIK"
SCMenuFactoryMeet = "TREFFEN"
SCMenuFriendlyYou                = "Du ..."
SCMenuFriendlyILike              = "Ich mag ... "
SCMenuPlacesLetsGo               = "Lass uns ... gehen."
SCMenuToontasksMyTasks           = "MEINE AUFGABEN"
SCMenuToontasksYouShouldChoose   = "Ich glaube, du solltest ... wählen."
SCMenuBattleLetsUse              = "Nehmen wir doch ..."

# These are all the standard SpeedChat phrases.
# The indices must fit into 16 bits (0..65535)
SpeedChatStaticText = {
    # top-level
    1 : lYes,
    2 : lNo,
    3 : lOK,

    # Hello
    100 : "Hi!",
    101 : "Hallo!",
    102 : "Hallo du!",
    103 : "Hey!",
    104 : "Tach!",
    105 : "Tag alle zusammen!",
    106 : "Willkommen in Toontown!",
    107 : "Wie steht's?",
    108 : "Wie geht's so?",
    109 : "Hallo?",

    # Bye
    200 : "Tschüss!",
    201 : "Bis später!",
    202 : "Bis dann!",
    203 : "Schönen Tag noch!",
    204 : "Viel Spaß!",
    205 : "Viel Glück!",
    206 : "Ich bin gleich wieder da.",
    207 : "Ich muss jetzt weg.",

    # Happy
    300 : ":-)",
    301 : "Huhu!",
    302 : "Hurra!",
    303 : "Cool!",
    304 : "Juhu!",
    305 : "Yeah!",
    306 : "Haha!",
    307 : "Hihi!",
    308 : "Wow!",
    309 : "Toll!",
    310 : "Hui!",
    311 : "Jungejunge!",
    312 : "Jabbadabbadu!",
    313 : "Jippieh!",
    314 : "Holdrio!",
    315 : "Toontastisch!",

    # Sad
    400 : ":-(",
    401 : "Oh nein!",
    402 : "Och, nö!",
    403 : "Quatsch!",
    404 : "Mist!",
    405 : "Autsch!",
    406 : "Uff!",
    407 : "Nein!!!",
    408 : "Iiih!",
    409 : "Hä?",
    410 : "Ich brauch mehr Lach-Punkte.",

    # Friendly
    500 : "Danke!",
    501 : "Kein Problem.",
    502 : "Gern geschehen!",
    503 : "Aber immer!",
    504 : "Nein danke.",
    505 : "Gute Teamarbeit!",
    506 : "Das hat Spaß gemacht!",
    507 : "Bitte sei mein Freund!",
    508 : "Lass uns zusammenarbeiten!",
    509 : "Ihr seid großartig!",
    510 : "Bist du neu hier?",
    511 : "Hast du gewonnen?",
    512 : "Das ist glaube ich zu riskant für dich.",
    513 : "Brauchst du Hilfe?",
    514 : "Kannst du mir helfen?",

    # Friendly "Du ..."
    600 : "Du siehst gut aus.",
    601 : "Du bist umwerfend!",
    602 : "Du fetzt!",
    603 : "Du bist ein Genie!",

    # Friendly "Mir gefällt ..."
    700 : "Mir gefällt dein Name.",
    701 : "Mir gefällt, wie du aussiehst.",
    702 : "Mir gefällt dein Oberteil.",
    703 : "Mir gefällt dein Rock.",
    704 : "Mir gefallen deine Shorts.",
    705 : "Mir gefällt dieses Spiel!",

    # Sorry
    800 : "Entschuldige!",
    801 : "Hoppla!",
    802 : "Entschuldige, kämpfe gerade gegen ein paar Bots!",
    803 : "Entschuldige, muss mir gerade Jelly Beans beschaffen!",
    804 : "Entschuldige, ich löse gerade eine Toon-Aufgabe!",
    805 : "Entschuldige, ich musste überraschend weg.",
    806 : "Entschuldige, ich wurde aufgehalten.",
    807 : "Entschuldige, ich kann nicht.",
    808 : "Ich konnte nicht mehr länger warten.",
    809 : "Ich kann dich nicht verstehen.",
    810 : "Verwende den %s." % GlobalSpeedChatName,

    # Stinky
    900 : "Hey!",
    901 : "Bitte geh weg!",
    902 : "Hör auf damit!",
    903 : "Das war nicht nett!",
    904 : "Sei nicht so gemein!",
    905 : "Du bist blöd!",
    906 : "Schicke eine Fehlermeldung. ",
    907 : "Ich hänge fest.",

    # Places
    1000 : "Lass uns gehen!",
    1001 : "Kannst du dich zu mir teleportieren?",
    1002 : "Sollen wir gehen?",
    1003 : "Wohin sollten wir gehen?",
    1004 : "Wo lang?",
    1005 : "Hier lang.",
    1006 : "Folge mir.",
    1007 : "Warte auf mich!",
    1008 : "Lass uns auf meinen Freund warten.",
    1009 : "Lass uns andere Toons suchen.",
    1010 : "Warte hier.",
    1011 : "Wart mal einen Moment.",
    1012 : "Wir treffen uns hier.",
    1013 : "Kannst du zu mir nach Hause kommen?",

    # Places "Komm ..."
    1100 : "Komm, wir fahren mit dem Toon-Express!",
    1101 : "Komm, wir gehen zum Spielplatz zurück!",
    1102 : "Komm, wir kämpfen gegen die %s!" % Cogs,
    1103 : "Komm, wir übernehmen ein %s-Gebäude!" % Cog,
    1104 : "Komm, wir fahren mit dem Aufzug!",
    1105 : "Komm, wir gehen zu Toontown Mitte!",
    1106 : "Komm, wir gehen zu Donalds Dock!",
    1107 : "Komm, wir gehen zu Minnies Melodienland!",
    1108 : "Komm, wir gehen zu Daisys Gärten!",
    1109 : "Komm, wir gehen zu Das Brrr!",
    1110 : "Komm, wir gehen zu Donalds Traumland!",
    1111 : "Komm, wir gehen zu mir nach Hause!",

    # Toontasks
    1200 : "An welcher Toon-Aufgabe arbeitest du?",
    1201 : "Lass uns daran arbeiten.",
    1202 : "Das ist nicht, was ich suche.",
    1203 : "Ich werde danach suchen.",
    1204 : "Es ist nicht in dieser Straße.",
    1205 : "Ich habe es noch nicht gefunden.",
    1299 : "Ich muss mir eine Toon-Aufgabe holen.",

    # Toontasks "Wenn du mein Rat willst, wähle ...  "
    1300 : "Wenn du mein Rat willst, wähle Aufheitern.",
    1301 : "Wenn du mein Rat willst, wähle Volldröhnen.",
    1302 : "Wenn du mein Rat willst, wähle Fallen lassen.",
    1303 : "Wenn du mein Rat willst, wähle Fallen stellen.",
    1304 : "Wenn du mein Rat willst, wähle Ködern.",

    # Battle
    1400 : "Schnell!",
    1401 : "Netter Schuss!",
    1402 : "Hübscher Gag!",
    1403 : "Daneben!",
    1404 : "Du hast's geschafft!",
    1405 : "Wir haben's geschafft!",
    1406 : "Los jetzt!",
    1407 : "Kinderspiel!",
    1408 : "Das war ja leicht!",
    1409 : "Lauf!",
    1410 : "Hilfe!",
    1411 : "Puh!",
    1412 : "Wir sitzen in der Klemme.",
    1413 : "Ich brauche mehr Gags.",
    1414 : "Ich brauche ein Tooning.",
    1415 : "Du solltest mal aussetzen.",

    # Battle "Nehmen wir..."
    1500 : "Nehmen wir Aufheitern!",
    1501 : "Nehmen wir Fallen stellen!",
    1502 : "Nehmen wir Ködern!",
    1503 : "Nehmen wir Volldröhnen!",
    1504 : "Nehmen wir Werfen!",
    1505 : "Nehmen wir Spritzen!",
    1506 : "Nehmen wir Fallen lassen!",

    # Gag Shop
    1600 : "Ich hab genügend Gags.",
    1601 : "Ich brauche mehr Jelly Beans.",
    1602 : "Ich auch.",
    1603 : "Mach schon!",
    1604 : "Noch einen?",
    1605 : "Nochmal spielen?",
    1606 : "Komm, wir spielen nochmal.",

    # Factory
    1700 : "Wir trennen uns hier am besten.",
    1701 : "Wir bleiben besser zusammen.",
    1702 : "Komm, wir kämpfen gegen die Bots.",
    1703 : "Tritt auf den Schalter.",
    1704 : "Geh durch die Tür.",

    # Sellbot Factory
    1803 : "Ich bin am Vordereingang.",
    1804 : "Ich bin in der Lobby.",
    1805 : "Ich bin im Gang vor der Lobby.",
    1806 : "Ich bin im Gang vor der Lobby.",
    1807 : "Ich bin im Getrieberaum.",
    1808 : "Ich bin im Kesselraum.",
    1809 : "Ich bin auf dem östlichen Laufsteg.",
    1810 : "Ich bin im Farbmischer.",
    1811 : "Ich bin im Farbmischer-Lagerraum.",
    1812 : "Ich bin auf dem Westsilo-Laufsteg.",
    1813 : "Ich bin im Rohrleitungsraum. ",
    1814 : "Ich bin auf der Treppe zum Rohrleitungsraum.",
    1815 : "Ich bin im Leitungskanalraum.",
    1816 : "Ich bin am Seiteneingang.",
    1817 : "Ich bin im Stampfer-Gang.",
    1818 : "Ich bin vor dem Lava-Raum.",
    1819 : "Ich bin im Lava-Raum.",
    1820 : "Ich bin im Lava-Lagerraum.",
    1821 : "Ich bin auf dem westlichen Laufsteg.",
    1822 : "Ich bin im Ölraum.",
    1823 : "Ich bin am Lagerhaus-Beobachtungsstand.",
    1824 : "Ich bin im Lagerhaus.",
    1825 : "Ich bin vor dem Farbmischer.",
    1827 : "Ich bin vor dem Ölraum.",
    1830 : "Ich bin im Ostsilo-Kontrollraum.",
    1831 : "Ich bin im Westsilo-Kontrollraum.",
    1832 : "Ich bin im Mittelsilo-Kontrollraum.",
    1833 : "Ich bin am Ostsilo.",
    1834 : "Ich bin auf dem West-Silo.",
    1835 : "Ich bin auf dem Mittelsilo.",
    1836 : "Ich bin auf dem Westsilo.",
    1837 : "Ich bin am Ostsilo.",
    1838 : "Ich bin auf dem Ostsilo-Laufsteg.",
    1840 : "Ich bin oben auf dem Westsilo.",
    1841 : "Ich bin oben auf dem Ostsilo.",
    1860 : "Ich bin im Westsilo-Aufzug.",
    1861 : "Ich bin im Ostsilo-Aufzug.",

    # Sellbot Factory continued
    1903 : "Treffen wir uns am Vordereingang.",
    1904 : "Treffen wir uns in der Lobby.",
    1905 : "Treffen wir uns im Gang vor der Lobby.",
    1906 : "Treffen wir uns im Gang vor der Lobby.",
    1907 : "Treffen wir uns im Getrieberaum.",
    1908 : "Treffen wir uns im Kesselraum.",
    1909 : "Treffen wir uns auf dem östlichen Laufsteg.",
    1910 : "Treffen wir uns im Farbmischer.",
    1911 : "Treffen wir uns im Farbmischer-Lagerraum.",
    1912 : "Treffen wir uns auf dem Westsilo-Laufsteg.",
    1913 : "Treffen wir uns im Rohleitungsraum.",
    1914 : "Treffen wir uns auf der Treppe zum Rohrleitungsraum.",
    1915 : "Treffen wir uns im Leitungskanalraum",
    1916 : "Treffen wir uns am Seiteneingang.",
    1917 : "Treffen wir uns im Stampfer-Gang.",
    1918 : "Treffen wir uns vor dem Lava-Raum. ",
    1919 : "Treffen wir uns im Lava-Raum.",
    1920 : "Treffen wir uns im Lava-Lagerraum.",
    1921 : "Treffen wir uns auf dem westlichen Laufsteg.",
    1922 : "Treffen wir uns im Ölraum.",
    1923 : "Treffen wir uns auf dem Lagerhaus-Beobachtungsstand.",
    1924 : "Treffen wir uns im Lagerhaus.",
    1925 : "Treffen wir uns draußen vor dem Farbmischer.",
    1927 : "Treffen wir uns draußen vor dem Ölraum.",
    1930 : "Treffen wir uns im Ostsilo-Kontrollraum.",
    1931 : "Treffen wir uns im Westsilo-Kontrollraum.",
    1932 : "Treffen wir uns im Mittelsilo-Kontrollraum.",
    1933 : "Treffen wir uns am Ostsilo.",
    1934 : "Treffen wir uns auf dem Westsilo.",
    1935 : "Treffen wir uns auf dem Mittelsilo.",
    1936 : "Treffen wir uns auf dem Westsilo.",
    1937 : "Treffen wir uns am Ostsilo.",
    1938 : "Treffen wir uns auf dem Ostsilo-Laufsteg.",
    1940 : "Treffen wir uns oben auf dem Westsilo.",
    1941 : "Treffen wir uns oben auf dem Ostsilo.",
    1960 : "Treffen wir uns im Westsilo-Aufzug.",
    1961 : "Treffen wir uns im Ostsilo-Aufzug.",

    # These are used only for the style settings in the OptionsPage
    # These should never actually be spoken or listed on the real speed chat
    2000 : "Violett",
    2001 : "Blau",
    2002 : "Cyan",
    2003 : "Türkis",
    2004 : "Grün",
    2005 : "Gelb",
    2006 : "Orange",
    2007 : "Rot",
    2008 : "Pink",
    2009 : "Braun",

    # cog phrases for disguised toons
    # (just references to cog dialog above)

    # common cog phrases
    20000 : SuitBrushOffs[None][0],
    20001 : SuitBrushOffs[None][1],
    20002 : SuitBrushOffs[None][2],
    20003 : SuitBrushOffs[None][3],
    20004 : SuitBrushOffs[None][4],

    # specific cog phrases
    20005: SuitFaceoffTaunts['bf'][0],
    20006: SuitFaceoffTaunts['bf'][1],
    20007: SuitFaceoffTaunts['bf'][2],
    20008: SuitFaceoffTaunts['bf'][3],
    20009: SuitFaceoffTaunts['bf'][4],
    20010: SuitFaceoffTaunts['bf'][5],
    20011: SuitFaceoffTaunts['bf'][6],
    20012: SuitFaceoffTaunts['bf'][7],
    20013: SuitFaceoffTaunts['bf'][8],
    20014: SuitFaceoffTaunts['bf'][9],

    20015: SuitFaceoffTaunts['nc'][0],
    20016: SuitFaceoffTaunts['nc'][1],
    20017: SuitFaceoffTaunts['nc'][2],
    20018: SuitFaceoffTaunts['nc'][3],
    20019: SuitFaceoffTaunts['nc'][4],
    20020: SuitFaceoffTaunts['nc'][5],
    20021: SuitFaceoffTaunts['nc'][6],
    20022: SuitFaceoffTaunts['nc'][7],
    20023: SuitFaceoffTaunts['nc'][8],
    20024: SuitFaceoffTaunts['nc'][9],

    20025: SuitFaceoffTaunts['ym'][0],
    20026: SuitFaceoffTaunts['ym'][1],
    20027: SuitFaceoffTaunts['ym'][2],
    20028: SuitFaceoffTaunts['ym'][3],
    20029: SuitFaceoffTaunts['ym'][4],
    20030: SuitFaceoffTaunts['ym'][5],
    20031: SuitFaceoffTaunts['ym'][6],
    20032: SuitFaceoffTaunts['ym'][7],
    20033: SuitFaceoffTaunts['ym'][8],
    20034: SuitFaceoffTaunts['ym'][9],
    20035: SuitFaceoffTaunts['ym'][10],

    20036: SuitFaceoffTaunts['ms'][0],
    20037: SuitFaceoffTaunts['ms'][1],
    20038: SuitFaceoffTaunts['ms'][2],
    20039: SuitFaceoffTaunts['ms'][3],
    20040: SuitFaceoffTaunts['ms'][4],
    20041: SuitFaceoffTaunts['ms'][5],
    20042: SuitFaceoffTaunts['ms'][6],
    20043: SuitFaceoffTaunts['ms'][7],
    20044: SuitFaceoffTaunts['ms'][8],
    20045: SuitFaceoffTaunts['ms'][9],
    20046: SuitFaceoffTaunts['ms'][10],

    20047: SuitFaceoffTaunts['bc'][0],
    20048: SuitFaceoffTaunts['bc'][1],
    20049: SuitFaceoffTaunts['bc'][2],
    20050: SuitFaceoffTaunts['bc'][3],
    20051: SuitFaceoffTaunts['bc'][4],
    20052: SuitFaceoffTaunts['bc'][5],
    20053: SuitFaceoffTaunts['bc'][6],
    20054: SuitFaceoffTaunts['bc'][7],
    20055: SuitFaceoffTaunts['bc'][8],
    20056: SuitFaceoffTaunts['bc'][9],
    20057: SuitFaceoffTaunts['bc'][10],

    20058: SuitFaceoffTaunts['cc'][0],
    20059: SuitFaceoffTaunts['cc'][1],
    20060: SuitFaceoffTaunts['cc'][2],
    20061: SuitFaceoffTaunts['cc'][3],
    20062: SuitFaceoffTaunts['cc'][4],
    20063: SuitFaceoffTaunts['cc'][5],
    20064: SuitFaceoffTaunts['cc'][6],
    20065: SuitFaceoffTaunts['cc'][7],
    20066: SuitFaceoffTaunts['cc'][8],
    20067: SuitFaceoffTaunts['cc'][9],
    20068: SuitFaceoffTaunts['cc'][10],
    20069: SuitFaceoffTaunts['cc'][11],
    20070: SuitFaceoffTaunts['cc'][12],

    20071: SuitFaceoffTaunts['nd'][0],
    20072: SuitFaceoffTaunts['nd'][1],
    20073: SuitFaceoffTaunts['nd'][2],
    20074: SuitFaceoffTaunts['nd'][3],
    20075: SuitFaceoffTaunts['nd'][4],
    20076: SuitFaceoffTaunts['nd'][5],
    20077: SuitFaceoffTaunts['nd'][6],
    20078: SuitFaceoffTaunts['nd'][7],
    20079: SuitFaceoffTaunts['nd'][8],
    20080: SuitFaceoffTaunts['nd'][9],

    20081: SuitFaceoffTaunts['ac'][0],
    20082: SuitFaceoffTaunts['ac'][1],
    20083: SuitFaceoffTaunts['ac'][2],
    20084: SuitFaceoffTaunts['ac'][3],
    20085: SuitFaceoffTaunts['ac'][4],
    20086: SuitFaceoffTaunts['ac'][5],
    20087: SuitFaceoffTaunts['ac'][6],
    20088: SuitFaceoffTaunts['ac'][7],
    20089: SuitFaceoffTaunts['ac'][8],
    20090: SuitFaceoffTaunts['ac'][9],
    20091: SuitFaceoffTaunts['ac'][10],
    20092: SuitFaceoffTaunts['ac'][11],

    20093: SuitFaceoffTaunts['tf'][0],
    20094: SuitFaceoffTaunts['tf'][1],
    20095: SuitFaceoffTaunts['tf'][2],
    20096: SuitFaceoffTaunts['tf'][3],
    20097: SuitFaceoffTaunts['tf'][4],
    20098: SuitFaceoffTaunts['tf'][5],
    20099: SuitFaceoffTaunts['tf'][6],
    20100: SuitFaceoffTaunts['tf'][7],
    20101: SuitFaceoffTaunts['tf'][8],
    20102: SuitFaceoffTaunts['tf'][9],
    20103: SuitFaceoffTaunts['tf'][10],

    20104: SuitFaceoffTaunts['hh'][0],
    20105: SuitFaceoffTaunts['hh'][1],
    20106: SuitFaceoffTaunts['hh'][2],
    20107: SuitFaceoffTaunts['hh'][3],
    20108: SuitFaceoffTaunts['hh'][4],
    20109: SuitFaceoffTaunts['hh'][5],
    20110: SuitFaceoffTaunts['hh'][6],
    20111: SuitFaceoffTaunts['hh'][7],
    20112: SuitFaceoffTaunts['hh'][8],
    20113: SuitFaceoffTaunts['hh'][9],
    20114: SuitFaceoffTaunts['hh'][10],

    20115: SuitFaceoffTaunts['le'][0],
    20116: SuitFaceoffTaunts['le'][1],
    20117: SuitFaceoffTaunts['le'][2],
    20118: SuitFaceoffTaunts['le'][3],
    20119: SuitFaceoffTaunts['le'][4],
    20120: SuitFaceoffTaunts['le'][5],
    20121: SuitFaceoffTaunts['le'][6],
    20122: SuitFaceoffTaunts['le'][7],
    20123: SuitFaceoffTaunts['le'][8],
    20124: SuitFaceoffTaunts['le'][9],

    20125: SuitFaceoffTaunts['bs'][0],
    20126: SuitFaceoffTaunts['bs'][1],
    20127: SuitFaceoffTaunts['bs'][2],
    20128: SuitFaceoffTaunts['bs'][3],
    20129: SuitFaceoffTaunts['bs'][4],
    20130: SuitFaceoffTaunts['bs'][5],
    20131: SuitFaceoffTaunts['bs'][6],
    20132: SuitFaceoffTaunts['bs'][7],
    20133: SuitFaceoffTaunts['bs'][8],
    20134: SuitFaceoffTaunts['bs'][9],
    20135: SuitFaceoffTaunts['bs'][10],

    20136: SuitFaceoffTaunts['cr'][0],
    20137: SuitFaceoffTaunts['cr'][1],
    20138: SuitFaceoffTaunts['cr'][2],
    20139: SuitFaceoffTaunts['cr'][3],
    20140: SuitFaceoffTaunts['cr'][4],
    20141: SuitFaceoffTaunts['cr'][5],
    20142: SuitFaceoffTaunts['cr'][6],
    20143: SuitFaceoffTaunts['cr'][7],
    20144: SuitFaceoffTaunts['cr'][8],
    20145: SuitFaceoffTaunts['cr'][9],

    20146: SuitFaceoffTaunts['tbc'][0],
    20147: SuitFaceoffTaunts['tbc'][1],
    20148: SuitFaceoffTaunts['tbc'][2],
    20149: SuitFaceoffTaunts['tbc'][3],
    20150: SuitFaceoffTaunts['tbc'][4],
    20151: SuitFaceoffTaunts['tbc'][5],
    20152: SuitFaceoffTaunts['tbc'][6],
    20153: SuitFaceoffTaunts['tbc'][7],
    20154: SuitFaceoffTaunts['tbc'][8],
    20155: SuitFaceoffTaunts['tbc'][9],
    20156: SuitFaceoffTaunts['tbc'][10],

    20157: SuitFaceoffTaunts['ds'][0],
    20158: SuitFaceoffTaunts['ds'][1],
    20159: SuitFaceoffTaunts['ds'][2],
    20160: SuitFaceoffTaunts['ds'][3],
    20161: SuitFaceoffTaunts['ds'][4],
    20162: SuitFaceoffTaunts['ds'][5],
    20163: SuitFaceoffTaunts['ds'][6],
    20164: SuitFaceoffTaunts['ds'][7],

    20165: SuitFaceoffTaunts['gh'][0],
    20166: SuitFaceoffTaunts['gh'][1],
    20167: SuitFaceoffTaunts['gh'][2],
    20168: SuitFaceoffTaunts['gh'][3],
    20169: SuitFaceoffTaunts['gh'][4],
    20170: SuitFaceoffTaunts['gh'][5],
    20171: SuitFaceoffTaunts['gh'][6],
    20172: SuitFaceoffTaunts['gh'][7],
    20173: SuitFaceoffTaunts['gh'][8],
    20174: SuitFaceoffTaunts['gh'][9],
    20175: SuitFaceoffTaunts['gh'][10],
    20176: SuitFaceoffTaunts['gh'][11],
    20177: SuitFaceoffTaunts['gh'][12],

    20178: SuitFaceoffTaunts['pp'][0],
    20179: SuitFaceoffTaunts['pp'][1],
    20180: SuitFaceoffTaunts['pp'][2],
    20181: SuitFaceoffTaunts['pp'][3],
    20182: SuitFaceoffTaunts['pp'][4],
    20183: SuitFaceoffTaunts['pp'][5],
    20184: SuitFaceoffTaunts['pp'][6],
    20185: SuitFaceoffTaunts['pp'][7],
    20186: SuitFaceoffTaunts['pp'][8],
    20187: SuitFaceoffTaunts['pp'][9],

    20188: SuitFaceoffTaunts['b'][0],
    20189: SuitFaceoffTaunts['b'][1],
    20190: SuitFaceoffTaunts['b'][2],
    20191: SuitFaceoffTaunts['b'][3],
    20192: SuitFaceoffTaunts['b'][4],
    20193: SuitFaceoffTaunts['b'][5],
    20194: SuitFaceoffTaunts['b'][6],
    20195: SuitFaceoffTaunts['b'][7],
    20196: SuitFaceoffTaunts['b'][8],
    20197: SuitFaceoffTaunts['b'][9],
    20198: SuitFaceoffTaunts['b'][10],
    20199: SuitFaceoffTaunts['b'][11],

    20200: SuitFaceoffTaunts['f'][0],
    20201: SuitFaceoffTaunts['f'][1],
    20202: SuitFaceoffTaunts['f'][2],
    20203: SuitFaceoffTaunts['f'][3],
    20204: SuitFaceoffTaunts['f'][4],
    20205: SuitFaceoffTaunts['f'][5],
    20206: SuitFaceoffTaunts['f'][6],
    20207: SuitFaceoffTaunts['f'][7],
    20208: SuitFaceoffTaunts['f'][8],
    20209: SuitFaceoffTaunts['f'][9],
    20210: SuitFaceoffTaunts['f'][10],

    20211: SuitFaceoffTaunts['mm'][0],
    20212: SuitFaceoffTaunts['mm'][1],
    20213: SuitFaceoffTaunts['mm'][2],
    20214: SuitFaceoffTaunts['mm'][3],
    20215: SuitFaceoffTaunts['mm'][4],
    20216: SuitFaceoffTaunts['mm'][5],
    20217: SuitFaceoffTaunts['mm'][6],
    20218: SuitFaceoffTaunts['mm'][7],
    20219: SuitFaceoffTaunts['mm'][8],
    20220: SuitFaceoffTaunts['mm'][9],
    20221: SuitFaceoffTaunts['mm'][10],
    20222: SuitFaceoffTaunts['mm'][11],
    20223: SuitFaceoffTaunts['mm'][12],
    20224: SuitFaceoffTaunts['mm'][13],

    20225: SuitFaceoffTaunts['tw'][0],
    20226: SuitFaceoffTaunts['tw'][1],
    20227: SuitFaceoffTaunts['tw'][2],
    20228: SuitFaceoffTaunts['tw'][3],
    20229: SuitFaceoffTaunts['tw'][4],
    20230: SuitFaceoffTaunts['tw'][5],
    20231: SuitFaceoffTaunts['tw'][6],
    20232: SuitFaceoffTaunts['tw'][7],
    20233: SuitFaceoffTaunts['tw'][8],
    20234: SuitFaceoffTaunts['tw'][9],
    20235: SuitFaceoffTaunts['tw'][10],

    20236: SuitFaceoffTaunts['mb'][0],
    20237: SuitFaceoffTaunts['mb'][1],
    20238: SuitFaceoffTaunts['mb'][2],
    20239: SuitFaceoffTaunts['mb'][3],
    20240: SuitFaceoffTaunts['mb'][4],
    20241: SuitFaceoffTaunts['mb'][5],
    20242: SuitFaceoffTaunts['mb'][6],
    20243: SuitFaceoffTaunts['mb'][7],
    20244: SuitFaceoffTaunts['mb'][8],
    20245: SuitFaceoffTaunts['mb'][9],

    20246: SuitFaceoffTaunts['m'][0],
    20247: SuitFaceoffTaunts['m'][1],
    20248: SuitFaceoffTaunts['m'][2],
    20249: SuitFaceoffTaunts['m'][3],
    20250: SuitFaceoffTaunts['m'][4],
    20251: SuitFaceoffTaunts['m'][5],
    20252: SuitFaceoffTaunts['m'][6],
    20253: SuitFaceoffTaunts['m'][7],
    20254: SuitFaceoffTaunts['m'][8],

    20255: SuitFaceoffTaunts['mh'][0],
    20256: SuitFaceoffTaunts['mh'][1],
    20257: SuitFaceoffTaunts['mh'][2],
    20258: SuitFaceoffTaunts['mh'][3],
    20259: SuitFaceoffTaunts['mh'][4],
    20260: SuitFaceoffTaunts['mh'][5],
    20261: SuitFaceoffTaunts['mh'][6],
    20262: SuitFaceoffTaunts['mh'][7],
    20263: SuitFaceoffTaunts['mh'][8],
    20264: SuitFaceoffTaunts['mh'][9],
    20265: SuitFaceoffTaunts['mh'][10],
    20266: SuitFaceoffTaunts['mh'][11],

    20267: SuitFaceoffTaunts['dt'][0],
    20268: SuitFaceoffTaunts['dt'][1],
    20269: SuitFaceoffTaunts['dt'][2],
    20270: SuitFaceoffTaunts['dt'][3],
    20271: SuitFaceoffTaunts['dt'][4],
    20272: SuitFaceoffTaunts['dt'][5],
    20273: SuitFaceoffTaunts['dt'][6],
    20274: SuitFaceoffTaunts['dt'][7],
    20275: SuitFaceoffTaunts['dt'][8],
    20276: SuitFaceoffTaunts['dt'][9],

    20277: SuitFaceoffTaunts['p'][0],
    20278: SuitFaceoffTaunts['p'][1],
    20279: SuitFaceoffTaunts['p'][2],
    20280: SuitFaceoffTaunts['p'][3],
    20281: SuitFaceoffTaunts['p'][4],
    20282: SuitFaceoffTaunts['p'][5],
    20283: SuitFaceoffTaunts['p'][6],
    20284: SuitFaceoffTaunts['p'][7],
    20285: SuitFaceoffTaunts['p'][8],
    20286: SuitFaceoffTaunts['p'][9],
    20287: SuitFaceoffTaunts['p'][10],

    20288: SuitFaceoffTaunts['tm'][0],
    20289: SuitFaceoffTaunts['tm'][1],
    20290: SuitFaceoffTaunts['tm'][2],
    20291: SuitFaceoffTaunts['tm'][3],
    20292: SuitFaceoffTaunts['tm'][4],
    20293: SuitFaceoffTaunts['tm'][5],
    20294: SuitFaceoffTaunts['tm'][6],
    20295: SuitFaceoffTaunts['tm'][7],
    20296: SuitFaceoffTaunts['tm'][8],
    20297: SuitFaceoffTaunts['tm'][9],
    20298: SuitFaceoffTaunts['tm'][10],

    20299: SuitFaceoffTaunts['bw'][0],
    20300: SuitFaceoffTaunts['bw'][1],
    20301: SuitFaceoffTaunts['bw'][2],
    20302: SuitFaceoffTaunts['bw'][3],
    20303: SuitFaceoffTaunts['bw'][4],
    20304: SuitFaceoffTaunts['bw'][5],
    20305: SuitFaceoffTaunts['bw'][6],
    20306: SuitFaceoffTaunts['bw'][7],
    20307: SuitFaceoffTaunts['bw'][8],
    20308: SuitFaceoffTaunts['bw'][9],

    20309: SuitFaceoffTaunts['ls'][0],
    20310: SuitFaceoffTaunts['ls'][1],
    20311: SuitFaceoffTaunts['ls'][2],
    20312: SuitFaceoffTaunts['ls'][3],
    20313: SuitFaceoffTaunts['ls'][4],
    20314: SuitFaceoffTaunts['ls'][5],
    20315: SuitFaceoffTaunts['ls'][6],
    20316: SuitFaceoffTaunts['ls'][7],
    20317: SuitFaceoffTaunts['ls'][8],
    20318: SuitFaceoffTaunts['ls'][9],
    20319: SuitFaceoffTaunts['ls'][10],

    20320: SuitFaceoffTaunts['rb'][0],
    20321: SuitFaceoffTaunts['rb'][1],
    20322: SuitFaceoffTaunts['rb'][2],
    20323: SuitFaceoffTaunts['rb'][3],
    20324: SuitFaceoffTaunts['rb'][4],
    20325: SuitFaceoffTaunts['rb'][5],
    20326: SuitFaceoffTaunts['rb'][6],
    20327: SuitFaceoffTaunts['rb'][7],
    20328: SuitFaceoffTaunts['rb'][8],
    20329: SuitFaceoffTaunts['rb'][9],

    20330: SuitFaceoffTaunts['sc'][0],
    20331: SuitFaceoffTaunts['sc'][1],
    20332: SuitFaceoffTaunts['sc'][2],
    20333: SuitFaceoffTaunts['sc'][3],
    20334: SuitFaceoffTaunts['sc'][4],
    20335: SuitFaceoffTaunts['sc'][5],
    20336: SuitFaceoffTaunts['sc'][6],
    20337: SuitFaceoffTaunts['sc'][7],
    20338: SuitFaceoffTaunts['sc'][8],
    20339: SuitFaceoffTaunts['sc'][9],
    20340: SuitFaceoffTaunts['sc'][10],

    20341: SuitFaceoffTaunts['sd'][0],
    20342: SuitFaceoffTaunts['sd'][1],
    20343: SuitFaceoffTaunts['sd'][2],
    20344: SuitFaceoffTaunts['sd'][3],
    20345: SuitFaceoffTaunts['sd'][4],
    20346: SuitFaceoffTaunts['sd'][5],
    20347: SuitFaceoffTaunts['sd'][6],
    20348: SuitFaceoffTaunts['sd'][7],
    20349: SuitFaceoffTaunts['sd'][8],
    20350: SuitFaceoffTaunts['sd'][9],
    }


# These indexes, defined above, will construct a submenu in the FACTORY menu
# to allow the user to describe all the places he might want to meet
SCFactoryMeetMenuIndexes = (1903, 1904, 1906, 1907, 1908, 1910, 1913,
                            1915, 1916, 1917, 1919, 1922, 1923,
                            1924, 1932, 1940, 1941)


# CustomSCStrings: SpeedChat phrases available for purchase.  It is
# safe to remove entries from this list, which will disable them for
# use from any toons who have already purchased them.  Note that the
# index numbers are stored directly in the database, so once assigned
# to a particular phrase, a given index number should never be
# repurposed to any other phrase.
CustomSCStrings = {
    # Series 1
    10 : "Na gut.",
    20 : "Warum nicht?",
    30 : "Natürlich!",
    40 : "So ist es richtig.",
    50 : "Genau!",
    60 : "Wie steht's?",
    70 : "Aber sicher!",
    80 : "Bingo!",
    90 : "Du machst wohl Witze!",
    100 : "Klingt gut.",
    110 : "Sowas Verrücktes!",
    120 : "Unglaublich!",
    130 : "So ein Mist!",
    140 : "Mach dir nichts draus.",
    150 : "Grrrr!",
    160 : "Was gibt's Neues?",
    170 : "Hey, hey, hey!",
    180 : "Bis morgen.",
    190 : "Bis zum nächsten Mal.",
    200 : "Tschau, Kakao.",
    210 : "Bis dann, Mann.",
    220 : "Ich muss bald weg.",
    230 : "Da bin ich aber nicht sicher!",
    240 : "Du bist raus!",
    250 : "Autsch, das tut weh!",
    260 : "Erwischt!",
    270 : "Bitte!",
    280 : "Tausend Dank!",
    290 : "Du siehst echt klasse aus!",
    300 : "Augenblick mal!",
    310 : "Kann ich dir helfen?",
    320 : "Sag ich doch!",
    330 : "Wenn's dir nicht passt, hau doch ab.",
    340 : "Das haut den stärksten Seemann vom Deck!",
    350 : "Das ist doch mal was Besonderes!",
    360 : "Hör auf mit dem Blödsinn!",
    370 : "Hat's dir die Sprache verschlagen?",
    380 : "Du hast dich gerade unbeliebt gemacht.",
    390 : "Was haben wir denn da?",
    400 : "Ich muss mal einen Toon besuchen.",
    410 : "Krieg dich wieder ein!",
    420 : "Drück dich jetzt nicht!",
    430 : "Du gibst `ne schöne Zielscheibe ab.",
    440 : "Wie du willst!",
    450 : "Absolut!",
    460 : "Süß!",
    470 : "Das fetzt!",
    480 : "Yeah, Baby!",
    490 : "Fang mich doch!",
    500 : "Du musst erst geheilt werden.",
    510 : "Du brauchst mehr Lach-Punkte.",
    520 : "Ich bin gleich wieder da.",
    530 : "Ich hab Hunger.",
    540 : "Ja, genau!",
    550 : "Ich bin müde.",
    560 : "Ich bin bereit!",
    570 : "Das langweilt mich.",
    580 : "Das gefällt mir!",
    590 : "Das war aber spannend!",
    600 : "Spring!",
    610 : "Hast du Gags?",
    620 : "Was ist los?",
    630 : "Immer mit der Ruhe.",
    640 : "Mit Geduld und Spucke fängt man eine Mucke.",
    650 : "Geschafft!",
    660 : "Achtung!",
    670 : "Fertig!",
    680 : "Los!",
    690 : "Komm, hier lang!",
    700 : "Du hast gewonnen!",
    710 : "Ich sage Ja.",
    720 : "Ich sage Nein.",
    730 : "Ich mach mit.",
    740 : "Ich mach nicht mit.",
    750 : "Bleib hier, ich komme wieder.",
    760 : "Das ging aber fix!",
    770 : "Hast du das gesehen?",
    780 : "Wonach riecht es hier?",
    790 : "Das stinkt zum Himmel!",
    800 : "Mir egal.",
    810 : "Passt genau.",
    820 : "Dann wollen wir mal loslegen!",
    830 : "Alle hier lang!",
    840 : "Was soll das denn?",
    850 : "Der Scheck ist in der Post.",
    860 : "Das hab ich gehört!",
    870 : "Redest du mit mir?",
    880 : "Danke, ich bleib die ganze Woche hier.",
    890 : "Hmm.",
    900 : "Ich nehme das hier.",
    910 : "Ich hab's!",
    920 : "Das gehört mir!",
    930 : "Bitte, nimm es.",
    940 : "Sei vorsichtig, das könnte gefährlich sein.",
    950 : "Keine Sorge!",
    960 : "Ach, du meine Güte!",
    970 : "Hui!",
    980 : "Auuuuu!",
    990 : "Alle Mann an Bord!",
    1000 : "Wahnsinn!",
    1010 : "Sei nicht so neugierig.",
    # Series 2
    2000 : "Sei nicht kindisch!",
    2010 : "Bin ich froh, dich zu sehen!",
    2020 : "Bitte sehr.",
    2030 : "Hast du dich heraus halten können?",
    2040 : "Lieber spät als nie!",
    2050 : "Bravo!",
    2060 : "Mal im Ernst, Leute ...",
    2070 : "Willst du dich uns anschließen?",
    2080 : "Bis später dann!",
    2090 : "Anders überlegt?",
    2100 : "Komm und hol's dir!",
    2110 : "Ach je!",
    2120 : "Ich freue mich, deine Bekanntschaft zu machen.",
    2130 : "Tu nichts, was ich nicht auch tun würde!",
    2140 : "Du solltest nicht mal dran denken!",
    2150 : "Gib nicht auf!",
    2160 : "Erwarte nicht zuviel.",
    2170 : "Frag nicht.",
    2180 : "Du hast gut reden.",
    2190 : "Jetzt reichts!",
    2200 : "Ausgezeichnet!",
    2210 : "Dass ich dich hier treffe!",
    2220 : "Gib mir `ne Chance.",
    2230 : "Das freut mich zu hören.",
    2240 : "Nur zu, tu mir den Gefallen!",
    2250 : "Trau dich!",
    2260 : "Gut gemacht!",
    2270 : "Schön, dich zu sehen!",
    2280 : "Ich muss jetzt los! Tschüss!",
    2290 : "Muss mich auf den Weg machen.",
    2300 : "Bleib mal da drin.",
    2310 : "Einen Moment mal.",
    2320 : "Amüsier dich gut!",
    2330 : "Viel Spaß!",
    2340 : "Hab nicht den ganzen Tag Zeit!",
    2350 : "Immer ruhig mit den jungen Pferden!",
    2360 : "Quatsch!",
    2370 : "Das ist ja nicht zu fassen!",
    2380 : "Das glaube ich nicht.",
    2390 : "Ich schulde dir was.",
    2400 : "Ich habe dich schon verstanden.",
    2410 : "Ich glaube schon.",
    2420 : "Ich finde, du solltest aussetzen.",
    2430 : "Ich wünschte, ich hätte das gesagt.",
    2440 : "An deiner Stelle würde ich das nicht tun.",
    2450 : "Gerne!",
    2460 : "Ich helfe meinem Freund.",
    2470 : "Ich bin die ganze Woche hier.",
    2480 : "Stell dir das mal vor!",
    2490 : "Gerade noch rechtzeitig ...",
    2500 : "Es ist erst vorbei, wenn's vorbei ist.",
    2510 : "Ich hab nur laut gedacht.",
    2520 : "Lass von dir hören.",
    2530 : "Ein Hundewetter!",
    2540 : "Mach hin!",
    2550 : "Fühl dich wie zu Hause.",
    2560 : "Vielleicht ein anderes Mal.",
    2570 : "Was dagegen, wenn ich mich anschließe?",
    2580 : "Schön hast du's hier.",
    2590 : "Nett, mit dir zu reden.",
    2600 : "Zweifellos.",
    2610 : "Ohne Quatsch!",
    2620 : "Überhaupt nicht.",
    2630 : "So eine Frechheit!",
    2640 : "Von mir aus.",
    2650 : "Geht in Ordnung.",
    2660 : "Bitte recht freundlich!",
    2670 : "Was sagst du da?",
    2680 : "Bitteschön!",
    2690 : "Nimm's leicht.",
    2700 : "Erst mal tschüss.",
    2710 : "Danke, nein danke.",
    2720 : "Das schießt den Vogel ab!",
    2730 : "Das ist ja lustig.",
    2740 : "So isses!",
    2750 : "Da ist eine Bot-Invasion im Gang!",
    2760 : "Tschüssi.",
    2770 : "Pass auf!",
    2780 : "Gut gemacht!",
    2790 : "Was geht ab?",
    2800 : "Was tut sich?",
    2810 : "Hört sich gut an.",
    2820 : "Jawollja.",
    2830 : "Darauf kannst du wetten.",
    2840 : "Das kannst du dir selbst ausrechnen.",
    2850 : "Du gehst schon?",
    2860 : "Du bringst mich zum Lachen!",
    2870 : "Du nimmst rechts.",
    2880 : "Du bist auf dem absteigenden Ast!",
    # Series 3
    3000 : "Alles, was du willst.",
    3010 : "Darf ich mitmachen?",
    3020 : "Die Rechnung, bitte.",
    3030 : "Sei dir nicht zu sicher.",
    3040 : "Ich bin so frei.",
    3050 : "Mach dich nicht heiß!",
    3060 : "Du weißt das wohl!",
    3070 : "Achte nicht auf mich.",
    3080 : "Heureka!",
    3090 : "Stell dir das vor!",
    3100 : "Vergiss es!",
    3110 : "Gehst du in meine Richtung?",
    3120 : "Ich gratuliere!",
    3130 : "Ach du Schreck.",
    3140 : "Schöne Zeit noch!",
    3150 : "Kopf hoch!",
    3160 : "Jetzt geht das wieder los.",
    3170 : "Was sagst du dazu?",
    3180 : "Wie gefällt dir das?",
    3190 : "Ich glaube schon.",
    3200 : "Ich glaube nicht.",
    3210 : "Ich komme noch mal auf dich zurück.",
    3220 : "Ich bin ganz Ohr.",
    3230 : "Ich hab zu tun.",
    3240 : "Das meine ich ernst!",
    3250 : "Ich bin sprachlos.",
    3260 : "Halt die Ohren steif!",
    3270 : "Lass es mich wissen!",
    3280 : "Lass die Torte fliegen!",
    3290 : "Ebenso, da bin ich sicher.",
    3300 : "Mach fix!",
    3310 : "Mensch, wie die Zeit vergeht!",
    3320 : "Kein Kommentar.",
    3330 : "Das lässt sich schon eher hören!",
    3340 : "Von mir aus.",
    3350 : "Angenehm.",
    3360 : "Geht in Ordnung.",
    3370 : "Na sicher.",
    3380 : "Tausend Dank.",
    3390 : "Das schon eher.",
    3400 : "So ist es richtig!",
    3410 : "Ich muss jetzt ab in die Falle.",
    3420 : "Vertrau mir!",
    3430 : "Bis zum nächsten Mal.",
    3440 : "Warte mal!",
    3450 : "So muss es laufen!",
    3460 : "Was führt dich her?",
    3470 : "Was ist passiert?",
    3480 : "Was nun?",
    3490 : "Du zuerst.",
    3500 : "Du nimmst links.",
    3510 : "Das hättest du wohl gerne!",
    3520 : "Du bist jetzt schon erledigt!",
    3530 : "Du bist das Verrückteste, was ich kenne!",
    # Series 4
    4000 : "Toons sind spitze!",
    4010 : "Bots reden zuviel!",
    4020 : "Toons aller Länder, vereinigt euch!",
    4030 : "Hallo Partner!",
    4040 : "Ich bin dir was schuldig.",
    4050 : "Armer schwarzer Kater!",
    4060 : "Ich hau mich jetzt in die Falle.",
    4070 : "Ich zügle meinen Zorn!",
    4080 : "Diese Stadt ist nicht groß genug für uns beide!",
    4090 : "Aufsitzen!",
    4100 : "Zieh!!!",
    4110 : "Da draußen ist noch viel Gold zu holen!",
    4120 : "Glücklichen Ritt!",
    4130 : "An dieser Stelle reite ich in die untergehende Sonne ...",
    4140 : "Lass uns abhauen!",
    4150 : "Dich sticht wohl der Hafer?",
    4160 : "Das hält ja kein Pferd aus!",
    4170 : "Klar wie Kloßbrühe.",
    4180 : "Ich glaub schon.",
    4190 : "Da woll’n wir mal losreiten!",
    4200 : "Denk mal gut drüber nach!",
    4210 : "Ich sitz wieder fest im Sattel!",
    4220 : "Ruf mal die üblichen Verdächtigen zusammen.",
    4230 : "Auf die Pferde, Männer!",
    4240 : "Greif nach den Sternen.",
    4250 : "Ich mach mich bereit.",
    4260 : "Immer langsam mit den jungen Pferden!",
    4270 : "Ich schieße immer übers Ziel hinaus.",
    4280 : "Wir sprechen uns noch.",
    4290 : "Das haut den stärksten Mann vom Pferd!",
    4300 : "Mach dir nicht in die Hosen.",
    4310 : "Hast wohl ‘ne Glückssträhne?",
    4320 : "Was geht denn hier ab wie achtzig wilde Pferde?",
    4330 : "Beweg dein Hinterteil!",
    4340 : "Ich glaub, mich tritt ein Pferd!",
    4350 : "Was sehen meine entzündeten Augen!",
    4360 : "Hier ist nicht viel los.",
    4370 : "Lass mal Dampf ab.",
    4380 : "Du siehst ja aus wie vom Pferd gefallen!",
    4390 : "Dir werd ich’s zeigen!",
    # Series 6
    6000 : "Ich bin scharf auf was Süßes!",
    6010 : "Ich bin eine Naschkatze.",
    6020 : "Das ist ‘ne halbgebackene Sache.",
    6030 : "Als würde man einem Kind den Schokoriegel klauen!",
    6040 : "Die sind im Dutzend billiger.",
    6050 : "Die sollen sich die Zähne dran ausbeißen!",
    6060 : "Das ist die Creme auf der Torte.",
    6070 : "Aber bitte mit Sahne!",
    6080 : "Ich fühl mich wie ein Kind allein im Bonbonregal!",
    6090 : "Ich will das größte Stück vom Kuchen.",
    6100 : "In der Kürze liegt die Würze.",
    6110 : "Du kriegst es wohl nicht gebacken.",
    6120 : "Das ist Keks.",
    6130 : "Na, schönen Dank für Backobst!",
    6140 : "Wir sind doch nicht aus Zucker!",
    6150 : "Du bist mir ja vielleicht ein harter Keks!",
    6160 : "So und nicht anders bröselt der Keks!",
    6170 : "Das ist wie Wasser statt Schokolade.",
    6180 : "Willst du mich einwickeln?",
    6190 : "Mit etwas Zucker lässt sich die bittere Medizin schlucken.",
    6200 : "Du bist, was du isst!",
    6210 : "Käseleicht!",
    6220 : "Geh mir nicht auf den Keks!",
    6230 : "Das ist das süße Leben.",
    6240 : "Das geht ja runter wie Butter!",
    6250 : "Das geht ja wie’s Brezelbacken!",
    6260 : "Das ist ja allererste Sahne!",
    6270 : "Wir wollen mal nicht um den heißen Brei herumreden.",
    6280 : "Poch-poch ...",
    6290 : "Herein, wenn’s kein Schneider ist!",

    # Halloween
    10000 : "Das ist hier eine Geisterstadt.",
    10001 : "Nettes Kostüm!",
    10002 : "Ich glaube, hier spukt es.",
    10003 : "Geld oder Leben!",
    10004 : "Huuu!",
    10005 : "Fröhliches Geistern!",
    10006 : "Fröhliches Halloween!",
    10007 : "Ich muss mich jetzt in einen Kürbis verwandeln.",
    10008 : "Spuktastisch!",
    10009 : "Schaurig!",
    10010 : "Das ist gruselig!",
    10011 : "Ich hasse Spinnen!",
    10012 : "Hast du das gehört?",
    10013 : "Du hast nicht den Hauch einer Chance!",
    10014 : "Du hast mich erschreckt!",
    10015 : "Das ist gespenstisch!",
    10016 : "Das ist verrückt!",
    10017 : "Das war seltsam ...",
    10018 : "Leichen im Keller?",
    10019 : "Hab ich dich erschreckt?",

    # Fall Festivus
    11000 : "Pah! Humbug!",
    11001 : "Schmoll nicht!",
    11002 : "Brrr!",
    11003 : "Komm wieder runter!",
    11004 : "Komm und hol's dir!",
    11005 : "Sei kein Frosch.",
    11006 : "Hau ordentlich rein!",
    11007 : "Frohe Feiertage!",
    11008 : "Prosit Neujahr!",
    11009 : "Schönes Fest!",
    11010 : "Lass dir die Gans schmecken!",
    11011 : "Hohoho!",
    11012 : "Wir sind eingeschneit!",
    11013 : "Das ist Schnee von gestern.",
    11014 : "Leise rieselt der Schnee!",
    11015 : "Alle Mann an die Geschenke!",
    11016 : "Frohe Weihnachten!",
    11017 : "Wie wär’s mit einer Schlittenfahrt?",
    11018 : "Ohne Schnee und Eis kein Preis!",
    11019 : "Es weihnachtet schwer!",

    # Valentines
    12000 : "Sei mein!",
    12001 : "Sei mein Schatz!",
    12002 : "Glückwunsch zum Valentinstag!",
    12003 : "Oh, wie niedlich.",
    12004 : "Ich steh auf dich.",
    12005 : "Das ist jugendliche Schwärmerei.",
    12006 : "Hab dich lieb!",
    12007 : "Willst du mein Valentine sein?",
    12008 : "Du bist ein Schatz.",
    12009 : "Du bist süß wie Honig.",
    12010 : "Du bist niedlich.",
    12011 : "Lass dich umarmen.",
    12012 : "Hübsch!",
    12013 : "Das ist goldig!",
    12014 : "Nicht wie Rosen ...",
    12015 : "Nicht wie Nelken ...",
    12016 : "Das ist lieb!",

    # St. Patricks Day
    13000 : "Einen wunderschönen Morgen, wünsch ich dir!",
    13001 : "Frohe Ostern!",
    13002 : "Fröhliche Ostereier!",
    13003 : "Viel Glück beim Suchen.",
    13004 : "Ich bin grün vor Neid.",
    13005 : "Du Glückspilz!",
    13006 : "Du bist mein Glückskleeblatt!",
    13007 : "Du bringst mir Glück!",
    }

# indices into cog phrase arrays
SCMenuCommonCogIndices = (20000, 20004)
SCMenuCustomCogIndices = {
    'bf' : (20005, 20014),
    'nc' : (20015, 20024),
    'ym' : (20025, 20035),
    'ms' : (20036, 20046),
    'bc' : (20047, 20057),
    'cc' : (20058, 20070),
    'nd' : (20071, 20080),
    'ac' : (20081, 20092),
    'tf' : (20093, 20103),
    'hh' : (20104, 20114),
    'le' : (20115, 20124),
    'bs' : (20125, 20135),
    'cr' : (20136, 20145),
    'tbc' : (20146, 20156),
    'ds' : (20157, 20164),
    'gh' : (20165, 20177),
    'pp' : (20178, 20187),
    'b' : (20188, 20199),
    'f' : (20200, 20210),
    'mm' : (20211, 20224),
    'tw' : (20225, 20235),
    'mb' : (20236, 20245),
    'm' : (20246, 20254),
    'mh' : (20255, 20266),
    'dt' : (20267, 20276),
    'p' : (20277, 20287),
    'tm' : (20288, 20298),
    'bw' : (20299, 20308),
    'ls' : (20309, 20319),
    'rb' : (20320, 20329),
    'sc' : (20330, 20331),
    'sd' : (20341, 20350),
    }

# Playground.py
PlaygroundDeathAckMessage = "Die "+ Cogs +  " haben all deine Gags weggenommen!\n\nDu bist traurig. Du darfst den Spielplatz nicht verlassen, bis du fröhlich bist."

# FactoryInterior.py
ForcedLeaveFactoryAckMsg = "Der Vorarbeiter war erledigt, bevor du ihn erreichen konntest. Du hast keine Bot-Teile erbeuten können."

# DistributedFactory.py
HeadingToFactoryTitle = "Auf dem Weg zu %s..."
ForemanConfrontedMsg = "%s kämpft gegen den Vorarbeiter!"

# DistributedMinigame.py
MinigameWaitingForOtherPlayers = "Warte auf andere Spieler ..."
MinigamePleaseWait = "Bitte warten ..."
DefaultMinigameTitle = "Minigame-Name"
DefaultMinigameInstructions = "Minigame-Anleitungen"
HeadingToMinigameTitle = "Auf dem Weg zu %s..." # minigame title

# MinigamePowerMeter.py
MinigamePowerMeterLabel = "Kraftmesser"
MinigamePowerMeterTooSlow = "Zu\nlangsam"
MinigamePowerMeterTooFast = "Zu\nschnell"

# DistributedMinigameTemplate.py
MinigameTemplateTitle = "Minigame-Vorlage"
MinigameTemplateInstructions = "Das ist eine Mustervorlage für ein Minigame. Verwende sie, um neue Minigames zu erfinden."

# DistributedCannonGame.py
CannonGameTitle = "Kanonen-Spiel"
CannonGameInstructions = "Schieße deinen Toon so schnell du kannst in den Wasserturm. Zum Zielen kannst du die Maus oder die Pfeiltasten verwenden. Sei schnell, dann gewinnst du eine große Belohnung für alle!"
CannonGameReward = "BELOHNUNG"

# DistributedTugOfWarGame.py
TugOfWarGameTitle = "Tauziehen"
TugOfWarInstructions = "Tippe abwechselnd auf die linke und rechte Pfeiltaste. Versuche das genau so schnell zu machen, dass der grüne Strich auf gleicher Höhe mit der roten Linie liegt. Wenn du zu schnell oder zu langsam tippst, landest du im Wasser!"
TugOfWarGameGo = "LOS!"
TugOfWarGameReady = "Fertig ..."
TugOfWarGameEnd = "Gut gespielt!"
TugOfWarGameTie = "Unentschieden!"
TugOfWarPowerMeter = "Kraftmesser"

# DistributedPatternGame.py
PatternGameTitle = "Vorbild "+ Minnie
PatternGameInstructions = Minnie +" wird dir einen Tanz vormachen. "+ \
                          "Versuche "+ Minnie +  "s Tanz mit den Pfeiltasten genau so zu wiederholen, wie du ihn siehst!"
PatternGameWatch   = "Achte genau auf die Tanzschritte ..."
PatternGameGo      = "LOS!"
PatternGameRight   = "Gut, %s!"
PatternGameWrong   = "Hoppla!"
PatternGamePerfect = "Das war ausgezeichnet, %s!"
PatternGameBye     = "Danke für's Mitspielen!"
PatternGameWaitingOtherPlayers = "Warte auf andere Spieler ..."
PatternGamePleaseWait = "Bitte warten ..."
PatternGameFaster = "Du warst\nschneller!"
PatternGameFastest = "Du warst\nam schnellsten!"
PatternGameYouCanDoIt = "Na los!\nDu kannst das!"
PatternGameOtherFaster = "\nwar schneller!"
PatternGameOtherFastest = "\nwar am schnellsten!"
PatternGameGreatJob = "Gut gemacht!"
PatternGameRound = "Runde %s!" # Round 1! Round 2! ..

# DistributedRaceGame.py
RaceGameTitle = "Renn-Spiel"
RaceGameInstructions = "Klicke auf eine Zahl. Wähle klug! Du kommst nur voran, wenn niemand anders dieselbe Zahl gewählt hat."
RaceGameWaitingChoices = "Warten, bis die Mitspieler gewählt haben ..."
RaceGameCardText = "%(name)s gewinnt: %(reward)s"
RaceGameCardTextBeans = "%(name)s erhält: %(reward)s"
RaceGameCardTextHi1 = "%(name)s ist ein toller Toon!"  # this category might eventually have secret game hints, etc

# RaceGameGlobals.py
RaceGameForwardOneSpace    = " 1 Feld vorwärts"
RaceGameForwardTwoSpaces   = " 2 Felder vorwärts"
RaceGameForwardThreeSpaces = " 3 Felder vorwärts"
RaceGameBackOneSpace    = " 1 Feld zurück"
RaceGameBackTwoSpaces   = " 2 Felder zurück"
RaceGameBackThreeSpaces = " 3 Felder zurück"
RaceGameOthersForwardThree = " alle anderen \n3 Felder vorwärts"
RaceGameOthersBackThree = " alle anderen \n3 Felder zurück"
RaceGameInstantWinner = "Sieger auf einen Schlag!"
RaceGameJellybeans2 = "2 Jelly Beans"
RaceGameJellybeans4 = "4 Jelly Beans"
RaceGameJellybeans10 = "10 Jelly Beans!"

# DistributedRingGame.py
RingGameTitle = "Ringe-Spiel"
# color
RingGameInstructionsSinglePlayer = "Versuche, durch so viele der %s Ringe zu schwimmen, wie du kannst. Benutze zum Schwimmen die Pfeiltasten."
# color
RingGameInstructionsMultiPlayer = "Versuche, durch die %s Ringe zu schwimmen. Andere Spieler werden es mit den Ringen in anderen Farben versuchen. Benutze zum Schwimmen die Pfeiltasten."
RingGameMissed = "VORBEI"
RingGameGroupPerfect = "GRUPPE\nPERFEKT!!"
RingGamePerfect = "PERFEKT!"
RingGameGroupBonus = "GRUPPENBONUS"

# RingGameGlobals.py
ColorRed = "roten"
ColorGreen = "grünen"
ColorOrange = "orangen"
ColorPurple = "violetten"
ColorWhite = "weißen"
ColorBlack = "schwarzen"
ColorYellow = "gelben"

# DistributedTagGame.py
TagGameTitle = "Fangen-Spiel"
TagGameInstructions = "Sammle die Münzen. Du kannst keine Münze einsammeln, wenn du fangen musst."
TagGameYouAreIt = "Du bist dran!"
TagGameSomeoneElseIsIt = "%s ist dran!"

# DistributedMazeGame.py
MazeGameTitle = "Labyrinth-Spiel"
MazeGameInstructions = "Sammle die Münzen. Versuche, sie alle zu bekommen, aber hüte dich vor den "+ Cogs +  "!"

# DistributedCatchGame.py
CatchGameTitle = "Achtung Fallobst"
CatchGameInstructions = "Fange so viele %(fruit)s auf, wie du kannst. Hüte dich vor den "+ Cogs +  " und fang möglichst keine %(badThing)s!"
CatchGamePerfect = "PERFEKT!"
CatchGameApples      = 'Äpfel'
CatchGameOranges     = 'Orangen'
CatchGamePears       = 'Birnen'
CatchGameCoconuts    = 'Kokosnüsse'
CatchGameWatermelons = 'Wassermelonen'
CatchGamePineapples  = 'Ananas'
CatchGameAnvils      = 'Ambosse'

# DistributedPieTossGame.py
PieTossGameTitle = "Tortenwurf-Spiel"
PieTossGameInstructions = "Wirf mit Torten nach den Zielen."

# MinigameRulesPanel.py
MinigameRulesPanelPlay = "SPIELEN"

# Purchase.py
GagShopName = "Goofys Gag-Laden"
GagShopPlayAgain = "NOCHMAL\nSPIELEN"
GagShopBackToPlayground = "ZURÜCK ZUM\nSPIELPLATZ"
GagShopYouHave = "Du hast %s Jelly Beans zur Verfügung"
GagShopYouHaveOne = "Du hast 1 Jelly Bean zur Verfügung"
GagShopTooManyProps = "Entschuldige, du hast zu viele Hilfsmittel"
GagShopDoneShopping = "EINKAUF\nFERTIG"
# name of a gag
GagShopTooManyOfThatGag = "Entschuldige, du hast schon genug %s"
GagShopInsufficientSkill = "Dafür bist du noch nicht geschickt genug"
# name of a gag
GagShopYouPurchased = "Du hast %s gekauft"
GagShopOutOfJellybeans = "Entschuldige, du hast keine Jelly Beans mehr!"
GagShopWaitingOtherPlayers = "Warte auf andere Spieler ..."
# these show up on the avatar panels in the purchase screen
GagShopPlayerDisconnected = "%s hat die Verbindung abgebrochen."
GagShopPlayerExited = "%s hat das Spiel verlassen"
GagShopPlayerPlayAgain = "Nochmal spielen"
GagShopPlayerBuying = "Kaufen"

# MakeAToon.py
#
# The voices for GenderShopQuestionMickey and Minnie should not be played simultaneously.
# Options are as follows:
# 1: Mickey first and Minnie follow in a few second.
# 2: When player moves cursor onto the character, the voice to be played.
#    But the voice shouldn't be played while other character is talking.
# Please choose whichever feasible.
#
GenderShopQuestionMickey = "Klicke auf mich, um einen männlichen Toon zu erstellen!"
GenderShopQuestionMinnie = "Klicke auf mich, um einen weiblichen Toon zu erstellen!"
GenderShopFollow = "Folge mir!"
GenderShopSeeYou = "Bis später!"
GenderShopBoyButtonText = "Junge"
GenderShopGirlButtonText = "Mädchen"

# BodyShop.py
BodyShopHead = "Kopf"
BodyShopBody = "Körper"
BodyShopLegs = "Beine"

# ColorShop.py
ColorShopHead = "Kopf"
ColorShopBody = "Körper"
ColorShopLegs = "Beine"
ColorShopToon = "Farbe"
ColorShopParts = "Teile"
ColorShopAll = "Alle"

# ClothesShop.py
ClothesShopShorts = "Shorts"
ClothesShopShirt = "Oberteil"
ClothesShopBottoms = "Unterteil"

MakeAToonDone = "Fertig"
MakeAToonCancel = lCancel
MakeAToonNext = lNext
MakeAToonLast = "Zurück"
CreateYourToon = "Drücke auf die Pfeile, um deinen Toon zu erstellen."
CreateYourToonTitle = "Deinen Toon erstellen"
CreateYourToonHead = "Klicke auf die 'Kopf'-Pfeile, um verschiedene Tiere auszusuchen."
MakeAToonClickForNextScreen = "Klicke auf den Pfeil unten, um auf die nächste Seite zu gelangen."
PickClothes = "Drücke auf die Pfeile, um dir die Kleidungsstücke für deinen Toon auszusuchen!"
PickClothesTitle = "Suche deine Kleidung aus"
PaintYourToon = "Klicke auf die Pfeile, um deinen Toon zu färben!"
PaintYourToonTitle = "Deinen Toon färben"
MakeAToonYouCanGoBack = "Du kannst auch zurückgehen, um den Körper zu ändern!"
MakeAFunnyName = "Suche dir mit meiner Maschine einen lustigen Namen aus!"
MustHaveAFirstOrLast1 = "Dein Toon sollte einen Vor- oder Nachnamen haben, meinst du nicht?"
MustHaveAFirstOrLast2 = "Möchtest du nicht, dass dein Toon einen Vor- oder Nachnamen hat?"
ApprovalForName1 = "Genau, dein Toon hat einen tollen Namen verdient!"
ApprovalForName2 = "Toon-Namen sind die besten Namen von allen!"
MakeAToonLastStep = "Letzter Schritt vor dem Besuch von Toontown!"
PickANameYouLike = "Wähle einen Namen, der dir gefällt!"
NameToonTitle = "Gib deinem Toon einen Namen"
TitleCheckBox = "Titel"
FirstCheckBox = "Vorname"
LastCheckBox = "Nachname"
RandomButton = "Beliebig"
NameShopSubmitButton = "Absenden"
TypeANameButton = "Namenseingabe"
TypeAName = "Dir gefallen diese Namen nicht?\nHier klicken -->"
PickAName = "Probier's mit dem Namenwahl-Spiel!\nHier klicken -->"
PickANameButton = "Namenwahl"
RejectNameText = "Dieser Name ist nicht zulässig. Versuch's bitte noch einmal."
WaitingForNameSubmission = "Namen absenden ..."

# NameShop.py
NameShopNameMaster = "NameMaster_german.txt"
NameShopPay = "Jetzt abonnieren!"
NameShopPlay = "Kostenlose Probezeit"
NameShopOnlyPaid = "Nur Benutzer, die bezahlt haben,\ndürfen ihren Toons selbst Namen geben.\nBis du dich für ein Abonnement entschieden hast, wird\ndein Toon folgenden Namen haben:\n"
NameShopContinueSubmission = "Weiter absenden"
NameShopChooseAnother = "Anderen Namen wählen"
NameShopToonCouncil = "Der Rat von Toontown\nwird deinen\nNamen prüfen. "+ \
                      "Die Prüfung kann\nein paar Tage dauern.\nInzwischen bekommst\ndu folgenden Namen zugeteilt:\n "
PleaseTypeName = "Bitte gib deinen Namen ein:"
AllNewNames = "Alle neuen Namen\nbedürfen der Genehmigung\ndurch den Rat von Toontown."
NameShopNameRejected = "Der Name, den du\nbeantragt hast,\nwurde abgelehnt."
NameShopNameAccepted = "Glückwunsch!\nDer Name, den du\nbeantragt hast,\nwurde angenommen!"
NoPunctuation = "Du kannst in deinem Namen keine Satzzeichen verwenden!"
PeriodOnlyAfterLetter = "Du kannst einen Punkt in deinem Namen verwenden, aber nur nach einem Buchstaben."
ApostropheOnlyAfterLetter = "Du kannst einen Apostroph in deinem Namen verwenden, aber nur nach einem Buchstaben."
NoNumbersInTheMiddle = "In der Mitte eines Wortes dürfen keine Ziffern erscheinen."
ThreeWordsOrLess = "Dein Name darf nur aus höchstens drei Wörtern bestehen."
CopyrightedNames = (
    "micky",
    "micky maus",
    "mickymaus",
    "minnie",
    "minnie maus",
    "minniemaus",
    "donald",
    "donald duck",
    "donaldduck",
    "pluto",
    "goofy",
    )
NumToColor = ['Weiß', 'Pfirsichorange', 'Hellrot', 'Rot', 'Kastanienbraun',
              'Ockergelb', 'Braun', 'Hautfarben', 'Korallenrot', 'Orange',
              'Gelb', 'Cremeweiß', 'Zitronengelb', 'Lindgrün', 'Meergrün',
              'Grün', 'Hellblau', 'Blaugrün', 'Blau',
              'Immergrün', 'Königsblau', 'Schieferblau', 'Lila',
              'Lavendellila', 'Pink']
AnimalToSpecies = {
    'dog'    : 'Hund',
    'cat'    : 'Katze',
    'mouse'  : 'Maus',
    'horse'  : 'Pferd',
    'rabbit' : 'Kaninchen',
    'duck'   : 'Ente',
    'fowl'   : 'Ente',
    }
NameTooLong = "Der Name ist zu lang. Bitte versuche es noch einmal."
ToonAlreadyExists = "Du hast schon einen Toon namens %s!"
NameAlreadyInUse = "Der Name ist schon vergeben!"
EmptyNameError = "Du musst erst einen Namen eingeben."
NameError = "Dieser Name geht leider nicht."

# NameCheck.py
NCTooShort = 'Dieser Name ist zu kurz.'
NCNoDigits = 'Dein Name darf keine Zahlen enthalten.'
NCNeedLetters = 'Jedes Wort in deinem Namen muss mehrere Buchstaben enthalten.'
NCNeedVowels = 'Jedes Wort in deinem Namen muss einige Vokale (Selbstlaute) enthalten.'
NCAllCaps = 'Dein Name darf nicht nur aus Großbuchstaben bestehen.'
NCMixedCase = 'Dieser Name hat zu viele Großbuchstaben.'
NCBadCharacter = "Dein Name darf das Zeichen '%s' nicht enthalten."
NCGeneric = 'Dieser Name geht leider nicht.'
NCTooManyWords = 'Dein Name darf nicht mehr als vier Wörter lang sein.'
NCDashUsage = ("Bindestriche dürfen nur verwendet werden, um zwei Wörter zu verbinden"
               "(wie bei 'Klaus-Dieter').")
NCCommaEdge = "Dein Name darf nicht mit einem Komma beginnen oder enden."
NCCommaAfterWord = "Du darfst ein Wort nicht mit einem Komma beginnen lassen."
NCCommaUsage = ('In diesem Namen sind Kommas nicht richtig eingesetzt. Kommas müssen zeigen,'
                'dass zwei Wörter zusammengehören, wie in dem Namen "Quiselda Quittung, RA". '
                'Nach Kommas muss ein Leerzeichen folgen.')
NCPeriodUsage = ('In diesem Namen sind Punkte nicht richtig eingesetzt. Punkte sind'
                 'nur gestattet in Wörtern wie "Dr.", "Frl.", "J.T." usw.')
NCApostrophes = 'Dieser Name hat zu viele Apostrophe.'

# DistributedTrophyMgrAI.py
RemoveTrophy = "Toontown-Zentrale: Die " + Cogs + " haben eines der von dir geretteten Gebäude eingenommen!"

# toon\DistributedNPCTailor/Clerk/Fisherman.py
STOREOWNER_TOOKTOOLONG = 'Brauchst du mehr Zeit zum Nachdenken?'
STOREOWNER_GOODBYE = 'Bis später!'
STOREOWNER_NEEDJELLYBEANS = 'Du musst mit dem Toon-Express fahren, dann bekommst du in paar Jelly Beans.'
STOREOWNER_GREETING = 'Wähle aus, was du kaufen möchtest.'
STOREOWNER_BROWSING = 'Du kannst stöbern, aber zum Kaufen brauchst du eine Kleidermarke.'
STOREOWNER_NOCLOTHINGTICKET = 'Du brauchst eine Kleidermarke, um Kleidung zu kaufen.'
# translate
STOREOWNER_NOFISH = 'Komm wieder her, um der Tierhandlung gegen Jelly Beans Fische zu verkaufen.'
STOREOWNER_THANKSFISH = 'Danke! Die Tierhandlung wird sich freuen. Tschüss!'

STOREOWNER_NOROOM = "Hmm... du solltest vielleicht in deinem Schrank erst etwas Platz schaffen, bevor du neue Kleidung kaufst.\n"
STOREOWNER_CONFIRM_LOSS = "Dein Schrank ist voll. Du wirst die Kleidung verlieren, die du gerade trägst."
STOREOWNER_OK = lOK
STOREOWNER_CANCEL = lCancel
STOREOWNER_TROPHY = "Wow! Du hast %s von %s Fischen gesammelt. Dafür verdienst du eine Trophäe und eine Lach-Spritze!"
# end translate

# NewsManager.py
SuitInvasionBegin1 = lToonHQ+": Eine Bot-Invasion hat begonnen!!!"
SuitInvasionBegin2 = lToonHQ+": %s haben Toontown eingenommen!!!"
SuitInvasionEnd1 = lToonHQ+": Die %s-Invasion ist beendet!!!"
SuitInvasionEnd2 = lToonHQ+": Die Toons haben wieder einmal gesiegt!!!"
SuitInvasionUpdate1 = lToonHQ+": Die Bot-Invasion liegt jetzt bei %s Bots!!!"
SuitInvasionUpdate2 = lToonHQ+": Wir müssen sie besiegen, diese %s!!!"
SuitInvasionBulletin1 = lToonHQ+": Es ist eine Bot-Invasion im Gange!!!"
SuitInvasionBulletin2 = lToonHQ+": %s haben Toontown eingenommen!!!"

# DistributedHQInterior.py
LeaderboardTitle = "Toon-Aufgebot"
# QuestScript.txt
QuestScriptTutorialMickey_1 = "Toontown hat einen neuen Einwohner! Hast du ein paar Extra-Gags?"
QuestScriptTutorialMickey_2 = "Klar, %s!"
QuestScriptTutorialMickey_3 = "Einweiser Ede wird dir alles über die Bots erzählen.\aIch muss jetzt los! Tschüss!"
QuestScriptTutorialMickey_4 = "Komm bitte näher! Verwende die Pfeiltasten, um dich zu bewegen."

# These are needed to correspond to the Japanese gender specific phrases
QuestScriptTutorialMinnie_1 = "Toontown hat einen neuen Einwohner! Hast du ein paar Extra-Gags?"
QuestScriptTutorialMinnie_2 = "Klar, %s!"
QuestScriptTutorialMinnie_3 = "Einweise Ede wird dir alles über die Bots erzählen.\aIch muss jetzt los! Tschüss!"
#

#
# If there is "\a" between the sentence, we would like to have one of the following sequence.
# 1: display 1st text with 1st voice -> when voice finished, arrow appear. -> if player pushes the arrow button, display 2nd text with 2nd voice.
# 2: display 1st text with 1st voice and altomatically display 2nd text with 2nd voice.
# 3: display 1st text and play 1st voice (arrow is displayed) -> whenever player pushes the button, the voice will be skipped and display 2nd text with 2nd voice.
# Anyway, we need to have some "Skip" rule while playing the voice because from DCV(Disney Character Voice)'s view, it is not preferrable to have voice skipped.
#

QuestScript101_1 = "Das hier sind BOTS. BOTS sind Roboter, die versuchen Toontown einzunehmen. "
QuestScript101_2 = "Es gibt viele verschiedene Arten von BOTS und ..."
QuestScript101_3 = "... sie verwandeln fröhliche Toon-Gebäude ..."
QuestScript101_4 = "... in hässliche Bot-Gebäude!"
QuestScript101_5 = "Aber BOTS vertragen keinen Spaß!"
QuestScript101_6 = "Ein guter Gag stoppt sie."
QuestScript101_7 = "Es gibt viele Gags, aber nimm für den Anfang erst mal diese."
QuestScript101_8 = "Ach ja! Du brauchst auch noch ein Lach-O-Meter!"
QuestScript101_9 = "Wenn dein Lach-O-Meter zu weit absinkt, wirst du traurig!"
QuestScript101_10 = "Nur ein fröhlicher Toon ist ein gesunder Toon!"
QuestScript101_11 = "OH NEIN! Vor meinem Laden steht ein BOT!"
QuestScript101_12 = "BITTE HILF MIR! Besiege diesen Bot!"
QuestScript101_13 = "Hier ist deine erste Toon-Aufgabe!"
QuestScript101_14 = "Beeil dich! Gehe los und besiege diesen Kriecher!"

QuestScript110_1 = "Gute Arbeit, wie du diesen Kriecher besiegt hast. Ich werde dir dafür ein Sticker-Buch geben ... "
QuestScript110_2 = "In dem Buch sind lauter nützliche Sachen."
QuestScript110_3 = "Öffne es, dann zeig ich sie dir."
QuestScript110_4 = "Der Stadtplan zeigt, wo du warst."
QuestScript110_5 = "Blättere um, dann siehst du deine Gags ..."
QuestScript110_6 = "Oje du hast keine Gags! Ich gebe dir eine Aufgabe."
QuestScript110_7 = "Blättere um, dann siehst du deine Aufgaben."
QuestScript110_8 = "Gehe zum Toon-Express, spiele Spiele und verdiene Jelly Beans, um dir Gags zu kaufen. "
QuestScript110_9 = "Zum Toon-Express kommst du, wenn du durch die Tür hinter mir zum Spielplatz gehst."
QuestScript110_10 = "Mache bitte nun das Buch zu und suche den Toon-Express!"
QuestScript110_11 = "Komm bitte wieder zurück zur Toontown-Zentrale, wenn du fertig bist. Tschüss!"

QuestScriptTutorialBlocker_1 = "Na hallo!"
QuestScriptTutorialBlocker_2 = "Hallo?"
QuestScriptTutorialBlocker_3 = "Oh, du weißt nicht, wie man den Schnell-Chat benutzt!"
QuestScriptTutorialBlocker_4 = "Klicke auf die Schaltfläche, um etwas zu sagen."
QuestScriptTutorialBlocker_5 = "Sehr gut!\aDort, wo du hingehst, sind viele Toons, mit denen man sich unterhalten kann."
QuestScriptTutorialBlocker_6 = "Wenn du mit deinen Freunden über die Tastatur chatten willst, kannst du eine andere Schaltfläche benutzen."
QuestScriptTutorialBlocker_7 = "Sie heißt 'Chat'-Schaltfläche. Du musst offizieller Einwohner von Toontown sein, um sie zu benutzen."
QuestScriptTutorialBlocker_8 = "Viel Glück! Bis später!"

QuestScript120_1 = "Klasse, du hast den Toon-Express gut gefunden!\aÜbrigens, kennst du Bankier Bob schon?\aEr ist ein ziemlicher Naschkater.\aFühr dich doch bei ihm gleich mal gut ein, indem du ihm diesen Schokoriegel als kleines Geschenk mitbringst."
QuestScript120_2 = "Bankier Bob sitzt drüben in der Toontown Bank."

QuestScript121_1 = "Mmh, danke für den Schokoriegel.\aHör mal, wenn du mir helfen kannst, geb ich dir eine Belohnung.\aDiese Bots haben die Schlüssel zu meinem Safe gestohlen. Erledige Bots, um einen gestohlenen Schlüssel zu finden.\aWenn du einen Schlüssel findest, bring ihn wieder her zu mir."
QuestScript130_1 = " Klasse, du hast den Toon-Express gut gefunden!\aÜbrigens habe ich heute ein Paket für Professor Peter erhalten.\aEs muss wohl die neue Kreide sein, die er bestellt hat.\aKannst du es ihm bitte bringen?\aEr ist drüben in der Schule."

QuestScript131_1 = "Oh, danke für die Kreide.\aWas?!?\aDiese Bots haben meine Tafel gestohlen. Erledige Bots, um meine gestohlene Tafel zu finden.\aWenn du sie findest, bring sie wieder her zu mir."

QuestScript140_1 = " Klasse, du hast den Toon-Express gut gefunden!\aÜbrigens habe ich da einen Freund, Bibliothekar Bertie, der ein ziemlicher Bücherwurm ist.\aIch habe letztens dieses Buch für ihn gefunden, als ich drüben in Donalds Dock war.\aKönntest du es ihm bringen? Er ist normalerweise in der Bibliothek."

QuestScript141_1 = "Oh ja, mit diesem Buch ist meine Sammlung fast vollständig.\aLass mal sehen ...\aÄhm, öh ...\aWo hab ich denn jetzt meine Brille hingelegt?\aIch hatte sie noch, kurz bevor diese Bots mein Gebäude einnahmen.\aErledige Bots, um meine gestohlene Brille zu finden.\aWenn du sie findest, bring sie wieder her zu mir und du bekommst eine Belohnung."

QuestScript145_1 = "Wie ich sehe, hattest du kein Problem mit dem Toon-Express!\aHör mal, die Bots haben unseren Schwamm gestohlen.\aGeh raus auf die Straße und kämpfe gegen Bots, bis du den Schwamm zurückgeholt hast.\aZur Straße gelangst du so durch einen der Tunnel:"
QuestScript145_2 = "Wenn du unseren Schwamm findest, bring ihn hierher zurück.\aVergiss nicht: Wenn du Gags brauchst, fahr mit dem Toon-Express.\aUnd wenn du deine Lach-Punkte nachfüllen musst, sammle Eistüten auf dem Spielplatz."

QuestScript150_1 = "Großartige Arbeit!\aDie nächste Aufgabe ist vielleicht für dich alleine zu schwer ..."
QuestScript150_2 = "Suche einen Mitspieler, mit dem du dich anfreunden kannst, und benutze die Schaltfläche 'Neuer Freund'."
QuestScript150_3 = "Wenn du einen Freund gefunden hast, komm wieder her."
QuestScript150_4 = "Manche Aufgaben sind für einen allein zu schwierig!"

# To make sure the language checker is working
# DO NOT TRANSLATE THIS
MissingKeySanityCheck = "Ignorier mich"

BossCogName = "Vize\npräzident"
BossCogNameWithDept = "%(name)s\n%(dept)s"
BossCogPromoteDoobers = "Ihr werdet hiermit zu richtigen %s ernannt. Glückwunsch!"
BossCogDoobersAway = { 's' : "Geh los! Und erledige das Geschäft!" }
BossCogWelcomeToons = "Willkommen, neue Bots!"
BossCogPromoteToons = "Ihr werdet hiermit zu richtigen %s ernannt. Glück ..."
CagedToonInterruptBoss = "He! Hallo! He, ihr da!"
CagedToonRescueQuery = "Seid ihr Toons also gekommen, um mich zu befreien?"
BossCogDiscoverToons = "Was? Toons! Getarnt!"
BossCogAttackToons = "Angriff!!"
CagedToonDrop = [
    "Großartig! Ihr macht ihn fertig!",
    "Bleibt ihm auf den Fersen! Er flüchtet!",
    "Ihr macht das prima!",
    "Fantastisch! Jetzt habt ihr ihn gleich!",
    ]
CagedToonPrepareBattleTwo = "Passt auf, er versucht, zu entwischen!\aHelft mir mal alle - kommt hier rauf und haltet ihn auf!"
CagedToonPrepareBattleThree = "Hurra, ich bin fast frei!\aJetzt musst du den Bot-VP direkt angreifen.\aIch hab einen ganzen Stapel Torten, die du nehmen kannst!\aSpring hoch und berühre den Boden meines Käfigs, dann gebe ich dir ein paar Torten.\aDrück die Taste Einfg., um Torten zu werfen, wenn du sie hast!"
BossBattleNeedMorePies = "Du brauchst mehr Torten!"
BossBattleHowToGetPies = "Spring hoch und berühre den Käfig, um Torten zu bekommen."
BossBattleHowToThrowPies = "Drücke die Taste Einfg., um Torten zu werfen!"
CagedToonYippee = "Jippieh!"
CagedToonThankYou = "Es ist toll, frei zu sein!\aDanke für deine Hilfe!\aIch stehe in deiner Schuld.\aWenn du jemals Hilfe im Kampf brauchst, ruf mich einfach!\aKlicke einfach auf die Schaltfläche SOS, um mich zu rufen."
CagedToonPromotion = "\aHör mal - dieser Bot-VP hat deine Beförderungspapiere zurückgelassen.\aIch reiche sie auf dem Weg nach draußen für dich ein, damit du befördert wirst!"
CagedToonLastPromotion = "\aWow, du hast auf deinem Bot-Anzug der Stufe %s erreicht!\aHöher wird kein Bot befördert.\aDu kannst keinen höheren Bot-Anzug mehr erreichen, aber du kannst auf jeden Fall weiter Toons retten!"
CagedToonHPBoost = "\aDu hast viele Toons aus diesem HQ gerettet.\aDer Rat von Toontown hat beschlossen, dir noch einen Lach-Punkt zu geben. Herzlichen Glückwunsch!"
CagedToonMaxed = "\aIch sehe, dass du einen Bot-Anzug der Stufe %s hast. Sehr beeindruckend!\aIm Namen des Rates von Toontown vielen Dank dafür, dass du zurückgekommen bist, um noch mehr Toons zu retten!"
CagedToonGoodbye = "Bis dann!"


CagedToonBattleThree = {
    10: "Gut gesprungen, %(toon)s. Hier sind ein paar Torten!",
    11: "Hi, %(toon)s! Nimm dir ein paar Torten!",
    12: "He, %(toon)s! Du hast jetzt ein paar Torten!",

    20: "He, %(toon)s! Spring zu meinem Käfig hoch und hol dir ein paar Torten zum Werfen!",
    21: "Hi, %(toon)s!  Benutze die Strg.-Taste, um hochzuspringen und meinen Käfig zu berühren!",

    100: "Drücke die Einfg-Taste, um eine Torte zu werfen.",
    101: "Der blaue Kraftmesser zeigt an, wie hoch deine Torte fliegt.",
    102: "Versuche zuerst, eine Torte in sein Fahrgestell zu schmettern, um seinen Antrieb außer Gefecht zu setzen.",
    103: "Warte, bis die Tür aufgeht, und wirf eine Torte direkt hinein.",
    104: "Wenn er benommen ist, wirf sie in sein Gesicht oder gegen seine Brust, um ihn umzuschmeißen!",
    105: "Einen guten Treffer erkennst du daran, dass der Platscher farbig ist.",
    106: "Wenn du einen Toon mit einer Torte triffst, erhält der Toon dadurch einen Lach-Punkt!",
    }
CagedToonBattleThreeMaxGivePies = 12
CagedToonBattleThreeMaxTouchCage = 21
CagedToonBattleThreeMaxAdvice = 106

BossElevatorRejectMessage = "Du kannst erst in diesen Aufzug einsteigen, wenn du dir eine Beförderung verdient hast."

# Types of catalog items--don't translate yet.
FurnitureTypeName = "Möbel"
PaintingTypeName = "Gemälde"
ClothingTypeName = "Kleidung"
ChatTypeName = "Schnell-Chat\3Wendung"
EmoteTypeName = "Schauspiel\3Unterricht"
PoleTypeName = "Angelrute"
WindowViewTypeName = "Aussicht"

FurnitureYourOldCloset = "dein alter Kleiderschrank"
FurnitureYourOldBank = "deine alte Sparbüchse"

# How to put quotation marks around chat items--don't translate yet.
ChatItemQuotes = '"%s"'

# CatalogFurnitureItem.py--don't translate yet.
FurnitureNames = {
  100 : "Sessel",
  105 : "Sessel",
  110 : "Stuhl",
  120 : "Schreibtischsessel",
  130 : "Blockstuhl",
  140 : "Hummerstuhl",
  145 : "Rettungswesten\3Stuhl",
  150 : "Sattelstuhl",
  160 : "Eingeborenenstuhl",
  170 : "Kuchenstuhl",
  200 : "Bett",
  205 : "Bett",
  210 : "Bett",
  220 : "Badewannenbett ",
  230 : "Laubbett",
  240 : "Bootbett",
  250 : "Kaktushängematte",
  260 : "Eiskrembett",
  300 : "Altes Klavier",
  310 : "Orgel mit Pfeifen",
  400 : "Kamin",
  410 : "Kamin",
  420 : "Runder Kamin",
  430 : "Kamin",
  440 : "Apfelkamin",
  500 : "Kleiderschrank",
  502 : "Schrank f. 15 Kleidungsstücken",
  510 : "Kleiderschrank",
  512 : "Schrank f. 15 Kleidungsstücken",
  600 : "Niedrige Lampe",
  610 : "Hohe Lampe",
  620 : "Tischlampe",
  625 : "Tischlampe",
  630 : "Blumenlampe ",
  640 : "Blumenlampe",
  650 : "Quallenlampe",
  660 : "Quallenlampe",
  670 : "Cowboylampe",
  700 : "Polstersessel",
  705 : "Polstersessel",
  710 : "Couch",
  715 : "Couch",
  720 : "Heucouch",
  730 : "Kuchensofa",
  800 : "Schreibtisch",
  810 : "Blockschreibtisch",
  900 : "Schirmständer",
  910 : "Garderobe",
  920 : "Mülltonne",
  930 : "Roter Pilz",
  940 : "Gelber Pilz",
  950 : "Garderobe",
  960 : "Fassständer",
  970 : "Kaktuspflanze",
  980 : "Tipi",
  1000 : "Großer Teppisch",
  1010 : "Runder Teppich",
  1015 : "Runder Teppich",
  1020 : "Kleiner Teppich",
  1030 : "Laubmatte",
  1100 : "Vitrine",
  1110 : "Vitrine",
  1120 : "Hohes Bücherregal",
  1130 : "Niedriges Regal",
  1140 : "Eisbechertruhe",
  1200 : "Beistelltisch",
  1210 : "Kleiner Tisch",
  1215 : "Kleiner Tisch",
  1220 : "Couchtisch",
  1230 : "Couchtisch",
  1240 : "Schnorchlertisch",
  1250 : "Kekstisch",
  1260 : "Nachttisch",
  1300 : "Büchse f. 1000 Jelly Beans",
  1310 : "Büchse f. 2500 Jelly Beans",
  1320 : "Büchse f. 5000 Jelly Beans",
  1330 : "Büchse f. 7500 Jelly Beans",
  1340 : "Büchse f. 10000 Jelly Beans",
  1399 : "Telefon",
  1400 : "Cezanne-Toon",
  1410 : "Blumen",
  1420 : "Moderner Micky",
  1430 : "Rembrandt-Toon",
  1440 : "Toonschaft",
  1441 : "Whistlers Pferd",
  1442 : "Toon-Stern",
  1443 : "Keine Torte",
  1500 : "Radio",
  1510 : "Radio",
  1520 : "Radio",
  1530 : "Fernseher",
  1600 : "Niedrige Vase",
  1610 : "Hohe Vase",
  1620 : "Niedrige Vase",
  1630 : "Hohe Vase",
  1640 : "Niedrige Vase",
  1650 : "Niedrige Vase",
  1660 : "Korallenvase",
  1661 : "Muschelvase",
  1700 : "Popcorn-Wagen",
  1710 : "Marienkäfer",
  1720 : "Springbrunnen",
  1725 : "Waschmaschine",
  1800 : "Aquarium",
  1810 : "Aquarium",
  1900 : "Schwertfisch",
  1910 : "Hammerhai",
  1920 : "Hängende Hörner",
  1930 : "Einfacher Sombrero",
  1940 : "Schicker Sombrero",
  1950 : "Traumfänger",
  1960 : "Hufeisen",
  1970 : "Bisonporträt",
  2000 : "Zuckerschaukel",
  2010 : "Kuchenrutsche",
  3000 : "Bananensplit-Wanne",
  10000 : "Kleiner Kürbis",
  10010 : "Großer Kürbis",
  }

# CatalogClothingItem.py--don't translate yet.
ClothingArticleNames = (
    "Oberteil",
    "Oberteil",
    "Oberteil",
    "Hosen",
    "Hosen",
    "Rock",
    "Hosen",
    )

ClothingTypeNames = {
    1400 : "Matthias Hemd",
    1401 : "Jessicas Bluse",
    1402 : "Marissas Bluse",
    }

# CatalogSurfaceItem.py--don't translate yet.
SurfaceNames = (
    "Tapete",
    "Zierleiste",
    "Bodenbelag",
    "Wandvertäfelung",
    "Einfassung",
    )

WallpaperNames = {
    1000 : "Pergament",
    1100 : "Mailand",
    1200 : "Dover",
    1300 : "Victoria",
    1400 : "Newport",
    1500 : "Idylle",
    1600 : "Harlekin",
    1700 : "Mond",
    1800 : "Sterne",
    1900 : "Blumen",
    2000 : "Garten im Frühling",
    2100 : "Architektonischer Garten",
    2200 : "Renntag",
    2300 : "Treffer!",
    2400 : "7. Himmel",
    2500 : "Kletterranke",
    2600 : "Frühling",
    2700 : "Kokeshi-Puppe",
    2800 : "Sträußchen",
    2900 : "Engelhai",
    3000 : "Blasen",
    3100 : "Blasen",
    3200 : "Go-Fisch",
    3300 : "Stoppfisch",
    3400 : "Seepferdchen",
    3500 : "Meeresmuscheln",
    3600 : "Unterwasser",
    3700 : "Stiefel",
    3800 : "Kaktus",
    3900 : "Cowboyhut",
    10100 : "Katzen",
    10200 : "Fledermäuse",
    11000 : "Schneeflocken",
    11100 : "Stechpalmenblatt",
    11200 : "Schneemann",
    13000 : "Kleeblatt",
    13100 : "Kleeblatt",
    13200 : "Regenbogen",
    13300 : "Kleeblatt",
    }

FlooringNames = {
    1000 : "Hartholzboden",
    1010 : "Teppich",
    1020 : "Rhombische Fliese",
    1030 : "Rhombische Fliese",
    1040 : "Gras",
    1050 : "Beige Ziegel",
    1060 : "Rote Ziegel",
    1070 : "Quadratische Fliese",
    1080 : "Stein",
    1090 : "Plankenweg",
    1100 : "Schotterstraße",
    1110 : "Holzplatte",
    1120 : "Fliese",
    1130 : "Wabe",
    1140 : "Wasser",
    1150 : "Strandplatte",
    1160 : "Strandplatte",
    1170 : "Strandplatte",
    1180 : "Strandplatte",
    1190 : "Sand",
    10000 : "Eiswürfel",
    10010 : "Iglu",
    11000 : "Kleeblatt",
    11010 : "Kleeblatt",
    }

MouldingNames = {
    1000 : "Knorrig",
    1010 : "Angestrichen",
    1020 : "Gebiss",
    1030 : "Blumen ",
    1040 : "Blumen",
    1050 : "Marienkäfer",
    }

WainscotingNames = {
    1000 : "Angestrichen",
    1010 : "Holzpaneel",
    1020 : "Holz",
    }

# CatalogWindowItem.py--don't translate yet.
WindowViewNames = {
    10 : "Großer Garten",
    20 : "Wilder Garten",
    30 : "Griechischer Garten",
    40 : "Stadtlandschaft",
    50 : "Wilder Westen",
    60 : "Unter Wasser",
    70 : "Tropische Insel",
    80 : "Sternenhimmel",
    90 : "Tiki-Pool",
    100 : "Eisige Grenze",
    110 : "Farmland",
    120 : "Eingeborenenlager",
    130 : "Hauptstraße",
    }

# don't translate yet
NewCatalogNotify = "Bei deinem Telefon gibt es neue Artikel zu bestellen!"
NewDeliveryNotify = "Eine neue Lieferung ist in deinem Briefkasten angekommen!"
CatalogNotifyFirstCatalog = "Dein erster Kuhtalog ist eingetroffen! Du kannst damit neue Sachen für dich oder dein Haus bestellen."
CatalogNotifyNewCatalog = "Dein Kuhtalog Nr. %s ist eingetroffen! Du kannst jetzt zu deinem Telefon gehen und Artikel aus diesem Kuhtalog bestellen."
CatalogNotifyNewCatalogNewDelivery = "Eine neue Lieferung ist in deinem Briefkasten angekommen! Und dein Kuhtalog Nr. %s ist auch eingetroffen!"
CatalogNotifyNewDelivery = "Eine neue Lieferung ist in deinem Briefkasten angekommen!"
CatalogNotifyNewCatalogOldDelivery = "Dein Kuhtalog Nr. %s ist eingetroffen und es warten immer noch Artikel in deinem Briefkasten!"
CatalogNotifyOldDelivery = "In deinem Briefkasten warten immer noch ein paar Artikel darauf, dass du sie abholst!"
CatalogNotifyInstructions = "Klicke auf der Stadtplanseite in deinem Sticker-Buch auf die Schaltfläche 'Nach Hause' und geh dann zum Telefon in deinem Haus."
CatalogNewDeliveryButton = "Neue\nLieferung!"
CatalogNewCatalogButton = "Neuer\nKuhtalog"
CatalogSaleItem = "Ausverkauf! "

# don't translate yet
DistributedMailboxEmpty = "Dein Briefkasten ist derzeit leer. Komm wieder her, um nach Lieferungen zu sehen, wenn du von deinem Telefon aus eine Bestellung aufgegeben hast!"
DistributedMailboxWaiting = "Dein Briefkasten ist derzeit noch leer, aber das von dir bestellte Paket ist unterwegs. Schau später nochmal nach!"
DistributedMailboxReady = "Deine Bestellung ist angekommen!"
DistributedMailboxNotOwner = "Entschuldige, das ist nicht dein Briefkasten."
DistributedPhoneEmpty = "Du kannst von jedem Telefon aus spezielle Artikel für dich und dein Haus bestellen. Im Laufe der Zeit werden neue Artikel zur Bestellung angeboten.\n\nIm Moment gibt es für dich keine Artikel zu bestellen, aber schau später nochmal nach!"

# don't translate yet
Clarabelle = "Klarabella"
MailboxExitButton = "Briefkasten schließen"
MailboxAcceptButton = "Diesen Artikel nehmen"
MailboxOneItem = "Dein Briefkasten enthält 1 Artikel."
MailboxNumberOfItems = "Dein Briefkasten enthält %s Artikel."
MailboxGettingItem = "%s wird aus dem Briefkasten genommen."
MailboxItemNext = "Nächster\nArtikel"
MailboxItemPrev = "Vorheriger\nArtikel"
CatalogCurrency = "Jelly Beans"
CatalogHangUp = "Auflegen"
CatalogNew = "NEU"
CatalogBackorder = "LIEFERRÜCKSTAND"
CatalogPagePrefix = "Seite"
CatalogGreeting = "Hallo! Danke für deinen Anruf bei Klarabellas Kuhtalog. Kann ich dir helfen?"
CatalogGoodbyeList = ["Wiederhören!",
                      "Bis zum nächsten Mal!",
                      "Vielen Dank für deinen Anruf!",
                      "OK, tschüss dann!",
                      "Tschüss!",
                      ]
CatalogHelpText1 = "Blättere um, dann kommst du zu den Verkaufsartikeln."
CatalogSeriesLabel = "Serie %s"
CatalogPurchaseItemAvailable = "Herzlichen Glückwunsch zum Neuerwerb! Du kannst ihn sofort benutzen."
CatalogPurchaseItemOnOrder = "Herzlichen Glückwunsch! Die gekauften Artikel werden demnächst an deinen Briefkasten geliefert."
CatalogAnythingElse = "Kann ich noch etwas für dich tun?"
CatalogPurchaseClosetFull = "Dein Schrank ist voll. Du kannst diesen Artikel trotzdem kaufen, aber dann wirst du etwas aus deinem Schrank entfernen müssen, damit er dann hineinpasst.\n\nMöchtest du diesen Artikel immer noch kaufen? "
CatalogAcceptClosetFull = "Dein Schrank ist voll. Du musst hinein gehen und etwas aus deinem Schrank entfernen, damit dieser Artikel Platz hat. Erst dann kannst du ihn aus dem Briefkasten holen."
CatalogAcceptShirt = "Du trägst jetzt dein neues Oberteil. Was du vorher anhattest, wurde in deinen Schrank verschoben."
CatalogAcceptShorts = "Du trägst jetzt deine neuen Hosen. Was du vorher anhattest, wurde in deinen Schrank verschoben."
CatalogAcceptSkirt = "Du trägst jetzt deinen neuen Rock. Was du vorher anhattest, wurde in deinen Schrank verschoben."
CatalogAcceptPole = "Mit deiner neuen Angelrute kannst du jetzt größere Fische angeln gehen!"
CatalogAcceptPoleUnneeded = "Du hast schon eine bessere Angelrute als diese hier! "
CatalogPurchaseHouseFull = "Dein Haus ist voll. Du kannst diesen neuen Artikel trotzdem kaufen, aber dann wirst du etwas aus deinem Haus entfernen müssen, damit er dann hineinpasst.\n\nMöchtest du diesen Artikel immer noch kaufen?"
CatalogAcceptHouseFull = "Dein Haus ist voll. Du musst hinein gehen und etwas aus deinem Haus entfernen, damit dieser Artikel Platz hat. Erst dann kannst du ihn aus dem Briefkasten holen."
CatalogAcceptInAttic = "Dein neuer Artikel ist jetzt auf deinem Dachboden. Du kannst ihn ins Haus holen, indem du hinein gehst und auf die Schaltfläche 'Möbel rücken' klickst."
CatalogAcceptInAtticP = "Deine neuen Artikel sind jetzt auf deinem Dachboden. Du kannst sie in deinem Haus aufstellen, indem du hinein gehst und auf die Schaltfläche 'Möbel rücken' klickst."
CatalogPurchaseMailboxFull = "Dein Briefkasten ist voll! Du kannst diesen Artikel erst kaufen, wenn du ein paar Artikel aus deinem Briefkasten herausgenommen hast."
CatalogPurchaseOnOrderListFull = "Du hast zur Zeit zu viele Bestellungen auf deiner Liste. Du kannst erst dann weitere Artikel bestellen, wenn einige der bereits bestellten eingetroffen sind."
CatalogPurchaseGeneralError = "Der Artikel konnte wegen eines spielinternen Fehlers nicht gekauft werden: Fehlercode %s."
CatalogAcceptGeneralError = "Der Artikel konnte wegen eines spielinternen Fehlers nicht aus deinem Briefkasten entfernt werden: Fehlercode %s."

# don't translate yet
HDMoveFurnitureButton = "Möbel\nrücken"
HDStopMoveFurnitureButton = "Rücken\nfertig"
HDAtticPickerLabel = "Auf dem Dachboden"
HDInRoomPickerLabel = "Im Zimmer"
HDInTrashPickerLabel = "Im Müll"
HDDeletePickerLabel = "Löschen?"
HDInAtticLabel = "Dachboden"
HDInRoomLabel = "Zimmer"
HDInTrashLabel = "Müll"
HDToAtticLabel = "Auf den Dachboden\nstellen"
HDMoveLabel = "Rücken"
HDRotateCWLabel = "Drehung rechts"
HDRotateCCWLabel = "Drehung links"
HDReturnVerify = "Diesen Artikel wieder auf den Dachboden stellen?"
HDReturnFromTrashVerify = "Diesen Artikel aus dem Müll wieder auf den Dachboden stellen?"
HDDeleteItem = "OK anklicken, um diesen Artikel in den Müll zu befördern, oder Abbrechen, um ihn zu behalten."
HDNonDeletableItem = "Du kannst diese Teile nicht löschen!"
HDNonDeletableBank = "Du kannst deine Sparbüchse nicht löschen!"
HDNonDeletableCloset = "Du kannst deinen Kleiderschrank nicht löschen!"
HDNonDeletablePhone = "Du kannst dein Telefon nicht löschen!"
HDNonDeletableNotOwner = "Du kannst %s's Sachen nicht löschen!"
HDHouseFull = "Dein Haus ist voll. Du musst noch etwas aus deinem Haus oder von deinem Dachboden löschen, bevor du diesen Artikel wieder aus dem Müll holen kannst."

HDHelpDict = {
    "DoneMoving" : "Zimmer einrichten beenden.",
    "Attic" : "Liste der Gegenstände auf dem Dachboden anzeigen. Auf dem Dachboden werden Gegenstände aufbewährt, die nicht in deinem Zimmer sind.",
    "Room" : "Liste der Gegenstände im Zimmer anzeigen. Nützlich, um verlorene Gegenstände zu finden.",
    "Trash" : "Gegenstände im Müll anzeigen. Die ältesten Gegenstände werden nach einer Weile oder wenn der Müll überquillt, gelöscht.",
    "ZoomIn" : "Zimmeransicht vergrößern.",
    "ZoomOut" : "Zimmeransicht verkleinern.",
    "SendToAttic" : "Das aktuelle Möbelstück zum Lagern auf den Dachboden schicken.",
    "RotateLeft" : "Nach links.",
    "RotateRight" : "Nach rechts.",
    "DeleteEnter" : "Zum Löschen-Modus wechseln.",
    "DeleteExit" : "Löschen-Modus verlassen.",
    "FurnitureItemPanelDelete" : "%s in den Müll werfen.",
    "FurnitureItemPanelAttic" : "%s in das Zimmer stellen.",
    "FurnitureItemPanelRoom" : "%s wieder auf den Dachboden stellen.",
    "FurnitureItemPanelTrash" : "%s wieder auf den Dachboden stellen.",
    }



# don't translate yet
MessagePickerTitle = "Du hast zu viele Redewendungen. Um \n\"%s\"\n zu kaufen, musst du eine zum Entfernen auswählen:"
MessagePickerCancel = lCancel
MessageConfirmDelete = "Bist du sicher, dass du \"%s\" aus deinem Schnell-Chat-Menü entfernen möchtest?"


# don't translate yet
CatalogBuyText = "Kaufen"
CatalogOnOrderText = "Bestellt"
CatalogPurchasedText = "Schon\ngekauft"
CatalogPurchasedMaxText = "Schon\nMaximum gekauft"
CatalogVerifyPurchase = "%(item)s für %(price)s Jelly Beans kaufen?"
CatalogOnlyOnePurchase = "Du kannst nur jeweils einen dieser Artikel haben. Wenn du diesen kaufst, ersetzt er %(old)s.\n\nBist du sicher, dass du %(item)s für %(price)s Jelly Beans kaufen willst?"

# don't translate yet
CatalogExitButtonText = "Auflegen"
CatalogCurrentButtonText = "Zu aktuellen Artikeln"
CatalogPastButtonText = "Zu früheren Artikeln"

TutorialHQOfficerName = "Mitarbeiter Harry"

# NPCToons.py
NPCToonNames = {
    # These are for the tutorial. We do not actually use the zoneId here
    # But the quest posters need to know his name
    20000 : "Einweiser-Ede",
    999 : "Toon-Schneider",
    1000 : "Toontown-Zentrale",
    20001 : Flippy,

    #
    # Toontown Central
    #

    # Toontown Central Playground

    # This Flippy DNA matches the tutorial Flippy
    # He is in Toon Hall
    2001 : Flippy,
    2002 : "Bankier Bob",
    2003 : "Professor Peter",
    2004 : "Schneiderin Flicka",
    2005 : "Bibliothekar Berti",
    2006 : "Angestellter Angelo",
    2011 : "Angestellte Angela",
    2007 : lHQOfficerM,
    2008 : lHQOfficerM,
    2009 : lHQOfficerF,
    2010 : lHQOfficerF,
    # NPCFisherman
    2012 : "Tierhandlungs-\nAngestellter",
    # NPCPetClerks
    2013 : "Angestellter Bimmel",
    2014 : "Angestellte Bammel",
    2015 : "Angestellter Bummel",

    # Silly Street
    2101 : "Zahnarzt Zacharias",
    2102 : "Sheriff Sherry",
    2103 : "Nies-Kitty",
    2104 : lHQOfficerM,
    2105 : lHQOfficerM,
    2106 : lHQOfficerF,
    2107 : lHQOfficerF,
    2108 : "Kanarienvogel Kohlengrube",
    2109 : "Barbera Blubber",
    2110 : "Eddi Kett",
    2111 : "Dancing Diego",
    2112 : "Dr. Hein",
    2113 : "Rollo der Erstaunliche",
    2114 : "Drees Rum",
    2115 : "Sheila Scherenschnitt",
    2116 : "Haumichblau MacDougal",
    2117 : "Mutter Eklig",
    2118 : "Kaspar Kasper",
    2119 : "Hanni Haha",
    2120 : "Professor Pünktchen",
    2121 : "Madam Gicker",
    2122 : "Harry Afferei",
    2123 : "Spamonia Biggels",
    2124 : "T.P. Rolle",
    2125 : "Paul Felz",
    2126 : "Professor Lachsalv",
    2127 : "Hellwig Heller",
    2128 : "Bert Bekloppt",
    2129 : "Frank Furter",
    2130 : "Schöna Spötter",
    2131 : "Federa Wedel",
    2132 : "Bartel Dös",
    2133 : "Dr. B. Geistert",
    2134 : "Stille Simone",
    2135 : "Maria",
    2136 : "Pit Prust",
    2137 : "Heikyung Glücklich",
    2138 : "Maldon",
    2139 : "Thoralf Tropf",
    2140 : "Fischer Billy",

    # Loopy Lane
    2201 : "Postmeister Peter",
    2202 : "Mira Spaß",
    2203 : lHQOfficerM,
    2204 : lHQOfficerM,
    2205 : lHQOfficerF,
    2206 : lHQOfficerF,
    2207 : "Willy Weisacker",
    2208 : "Kleb Endreim",
    2209 : "Chlodewig Gluckser",
    2210 : "Tee Hee",
    2211 : "Sally Spuck",
    2212 : "Sebastian Seltsam",
    2213 : "Alla Rad",
    2214 : "Felix Fleck",
    2215 : "Sid Selters",
    2216 : "Verigissmein Machsgut",
    2217 : "Hainer Fressdich",
    2218 : "Isja Lustig",
    2219 : "Chefkoch Schafskopf",
    2220 : "Edwin Eisenmann",
    2221 : "Hanna Haft",
    2222 : "Kurtzi Schluss",
    2223 : "Zelina Zerfetzdich",
    2224 : "Qualm-Ede",
    2225 : "Fischer Droopy",

    # Punchline Place
    2301 : "Dr. Verdreht",
    2302 : "Professor Krümmdich",
    2303 : "Schwester Stefanie",
    2304 : lHQOfficerM,
    2305 : lHQOfficerM,
    2306 : lHQOfficerF,
    2307 : lHQOfficerF,
    2308 : "Nancy Gas",
    2309 : "Blau Fleck",
    2311 : "Franz Schwellader",
    2312 : "Dr. Sensibel",
    2313 : "Lucy Hemdenklecks",
    2314 : "Schleuder-Ned",
    2315 : "Kauma Bröckchen",
    2316 : "Cindy Streusel",
    2318 : "Tony Maroni",
    2319 : "Beppo",
    2320 : "Alfredo Hartgekocht",
    2321 : "Fischer Punchy",

    #
    # Donald's Dock
    #

    # Donald's Dock Playground
    1001 : "Angestellter Willi",
    1002 : "Angestellter Billy",
    1003 : lHQOfficerM,
    1004 : lHQOfficerF,
    1005 : lHQOfficerM,
    1006 : lHQOfficerF,
    1007 : "Jacko Buxehude",
    # NPCFisherman
    1008 : "Tierhandlungs-\nAngestellter",
    # NPCPetClerks
    1009 : "Angestellter Kleff",
    1010 : "Angestellte Schnurr",
    1011 : "Angestellter Pieps",

    # Barnacle Blvd.
    1101 : "Kalle Kiel",
    1102 : "Käpt'n Karl",
    1103 : "Frank Fischtran",
    1104 : "Doktor Weitblick",
    1105 : "Admiral Hook",
    1106 : "Frau Bleiche",
    1107 : "Herr Robiks",
    1108 : lHQOfficerM,
    1109 : lHQOfficerF,
    1110 : lHQOfficerM,
    1111 : lHQOfficerF,
    1112 : "Gary Gluckgluck",
    1113 : "Bärbel Backbord",
    1114 : "Charlie Schluck",
    1115 : "Quiselda Quittung, RA",
    1116 : "Bernikel-Bessie",
    1117 : "Käpt'n Igitt",
    1118 : "Hacker Haarig",
    1121 : "Linde Rinde",
    1122 : "Seebär Stan",
    1123 : "Elektra Egel",
    1124 : "Schlappo Docknagel",
    1125 : "Eileen Überbord",
    1126 : "Fischer Barney",

    # Seaweed Street
    1201 : "Bernikel-Barbara",
    1202 : "Adalbert",
    1203 : "Achim",
    1204 : "Sturmi See",
    1205 : lHQOfficerM,
    1206 : lHQOfficerF,
    1207 : lHQOfficerM,
    1208 : lHQOfficerF,
    1209 : "Professor Planke",
    1210 : "Geng Wei",
    1211 : "Wind Beutel",
    1212 : "Zeko Zungenbrenner",
    1213 : "Dante Delfin",
    1214 : "Stürmische Kate",
    1215 : "Unda Wassa",
    1216 : "Rod Rolle",
    1217 : "Meerlinde Tang",
    1218 : "Stiller Tim",
    1219 : "G. Strandet",
    1220 : "Karla Kanal",
    1221 : "Blasius McKee",
    1222 : "Chef Ahoi",
    1223 : "Cal Kalmar",
    1224 : "Aaltje Ritter",
    1225 : "Lobgott Lenzpumpe",
    1226 : "Hauke Ruck",
    1227 : "Cora Llenriff",
    1228 : "Fischer Reed",

    # Lighthouse Lane
    1301 : "Alice",
    1302 : "Mark",
    1303 : "Gerts",
    1304 : "Swetlana",
    1305 : lHQOfficerM,
    1306 : lHQOfficerF,
    1307 : lHQOfficerM,
    1308 : lHQOfficerF,
    1309 : "Gischt",
    1310 : "Max Made",
    1311 : "Florentina Schwipps",
    1312 : "Elmar Kiel",
    1313 : "Willie Woge",
    1314 : "Ralph Rostig",
    1315 : "Doktor Drift",
    1316 : "Wilma Wehr",
    1317 : "Paula Proporz",
    1318 : "Stephan Schlauchboot",
    1319 : "Trutz Trockendock",
    1320 : "Ted Stillsee",
    1321 : "Dina Docker",
    1322 : "Anka Kette",
    1323 : "Ned Stinktopf",
    1324 : "Perlchen Taucher",
    1325 : "Nobu Netz",
    1326 : "Felicia Chips",
    1327 : "Coralie Platsch",
    1328 : "Fred Flunder",
    1329 : "Shelly Seetang",
    1330 : "Porter Hohl",
    1331 : "Rudi Ruder",
    1332 : "Fischer Shane",

    #
    # The Brrrgh
    #

    # The Brrrgh Playground
    3001 : "Betty Friert",
    3002 : lHQOfficerM,
    3003 : lHQOfficerF,
    3004 : lHQOfficerM,
    3005 : lHQOfficerM,
    3006 : "Angestellter Lenny",
    3007 : "Angestellte Penny",
    3008 : "Kord Hose",
    # NPCFisherman
    3009 : "Tierhandlungs-\nAngestellter",
    # NPCPetClerks
    3010 : "Angestellter Hoppel",
    3011 : "Angestellte Poppel",
    3012 : "Angestellter Moppel",

    # Walrus Way
    3101 : "Herr Krug",
    3102 : "Tante Frostbeule",
    3103 : "Fred",
    3104 : "Huta",
    3105 : "Feinfrost-Freddy",
    3106 : "Gert Gänseburger",
    3107 : "Patty Passport",
    3108 : "Schlitten-Schorsch",
    3109 : "Kate",
    3110 : "Hähnchenjung",
    3111 : "Großschnauz Gandalf",
    3112 : "Lil Altmann",
    3113 : "Hysterie-Harry",
    3114 : "Gerald der Gefährliche",
    3115 : lHQOfficerM,
    3116 : lHQOfficerF,
    3117 : lHQOfficerM,
    3118 : lHQOfficerM,
    3119 : "Gruselkurt",
    3120 : "Mike Mück",
    3121 : "Joe Shocker",
    3122 : "Rudi Rödel",
    3123 : "Frank Lloyd Ice",
    3124 : "Egon Eisberg",
    3125 : "Oberst Oberlecker",
    3126 : "Colestra Belle",
    3127 : "Ichvall Duvällst",
    3128 : "George Klebrig",
    3129 : "Bäckers Brigitte",
    3130 : "Sandy",
    3131 : "Lorenzo Faulus",
    3132 : "Brennda",
    3133 : "Dr. Stuntbild",
    3134 : "Salomon Salonlöwe",
    3135 : "Nele Durchweicht",
    3136 : "Gilda Glücklich",
    3137 : "Herr Frier",
    3138 : "Chefkoch Pfuschsuppe",
    3139 : "Oma Eisstrumpf",
    3140 : "Fischerin Lucille",

    # Sleet Street
    3201 : "Tante Arktis",
    3202 : "Schütti",
    3203 : "Walter",
    3204 : "Dr. K.-Ann Gutsehen",
    3205 : "Huckelberry Schlitzauge",
    3206 : "Vitalia Wucht",
    3207 : "Dr. Mummelgesicht",
    3208 : "Felix Mürrisch",
    3209 : "Guido Kichererbs",
    3210 : "Halbaffen-Sam",
    3211 : "Fanny Friert",
    3212 : "Fred Frost",
    3213 : lHQOfficerM,
    3214 : lHQOfficerF,
    3215 : lHQOfficerM,
    3216 : lHQOfficerM,
    3217 : "Schwitze-Peter",
    3218 : "Blanka Blau",
    3219 : "Tom Tandemfrost",
    3220 : "Herr Schneuz",
    3221 : "Nell Schnee",
    3222 : "Mindy Kaltwind",
    3223 : "Chappy",
    3224 : "Frieda Frostbiss",
    3225 : "Glatt Eis",
    3226 : "Nico Laus",
    3227 : "Sonny Strahl",
    3228 : "Wynn Stoß",
    3229 : "Hernie Gurt",
    3230 : "Glatzen-Günthi",
    3231 : "Eisbrecher",
    3232 : "Fischer Albert",

    #
    # Minnie's Melody Land
    #

    # Minnie's Melody Land Playground
    4001 : "Molly Molloy",
    4002 : lHQOfficerM,
    4003 : lHQOfficerF,
    4004 : lHQOfficerF,
    4005 : lHQOfficerF,
    4006 : "Angestellte Fa",
    4007 : "Angestellter Ray",
    4008 : "Schneiderin Harmony",
    # NPCFisherman
    4009 : "Tierhandlungs-\nAngestellter",
    # NPCPetClerks
    4010 : "Angestellter Chris",
    4011 : "Angestellter Max",
    4012 : "Angestellte Mädchen für Alles",

    # Alto Ave.
    4101 : "Tom",
    4102 : "Fifi",
    4103 : "Dr. Karies",
    4104 : lHQOfficerM,
    4105 : lHQOfficerF,
    4106 : lHQOfficerF,
    4107 : lHQOfficerF,
    4108 : "Quint",
    4109 : "Carlos",
    4110 : "Metra Gnom",
    4111 : "Tom Summ",
    4112 : "Tina",
    4113 : "Madam Benimm",
    4114 : "Der Verstimmte Erik",
    4115 : "Barbara Sevilla",
    4116 : "Piccolo",
    4117 : "Mandy Liehne",
    4118 : "Toilettenwart Tobi",
    4119 : "Moe Zart",
    4120 : "Viola Polster",
    4121 : "Gis Dur",
    4122 : "Minzie Bass",
    4123 : "Blitz-Ted",
    4124 : "Einar Tönig",
    4125 : "Melodie Weber",
    4126 : "Mel Canto",
    4127 : "Fulminante Füße",
    4128 : "Luciano Knüller",
    4129 : "Zenzi Zwiefacher",
    4130 : "Metal-Mike",
    4131 : "Abraham Armoire",
    4132 : "Louise Louise",
    4133 : "Scott Poplin",
    4134 : "Disco-Dave",
    4135 : "Beinhart Singvogel",
    4136 : "Patty Pause",
    4137 : "Tony Taub",
    4138 : "Violino Schlüssel",
    4139 : "Harmony Süßlich",
    4140 : "Ned Plump",
    4141 : "Fischer Jed",

    # Baritone Blvd.
    4201 : "Tina",
    4202 : "Barry",
    4203 : "Holz-Michel",
    4204 : lHQOfficerM,
    4205 : lHQOfficerF,
    4206 : lHQOfficerF,
    4207 : lHQOfficerF,
    4208 : "Hediheda",
    4209 : "Alma Abgedroschen",
    4211 : "Carl Concerto",
    4212 : "Detektiv Klagelied",
    4213 : "Tizia Tinnitus",
    4214 : "Fina Fußangel",
    4215 : "Veit Vibrato",
    4216 : "Gummy Pfeiffer",
    4217 : "Anton Schönherr",
    4218 : "Willma Pusten",
    4219 : "Abi Andante",
    4220 : "Kurt Finger",
    4221 : "Michi Madrigal",
    4222 : "Johann Doon",
    4223 : "Terry Taktstock",
    4224 : "Dschungel-Jim",
    4225 : "Zewa Zisch",
    4226 : "Herta Halslanger",
    4227 : "Die Stille Fancesca",
    4228 : "Susi Stimmt",
    4229 : "Belinda Blöd",
    4230 : "Julius Joculator",
    4231 : "Karla Quetschkommode",
    4232 : "Hedi Musi",
    4233 : "Karli Karpfen",
    4234 : "Johann Sträußchen",
    4235 : "Fischer Larry",

    # Tenor Terrace
    4301 : "Yuki",
    4302 : "Anna",
    4303 : "Leo",
    4304 : lHQOfficerM,
    4305 : lHQOfficerF,
    4306 : lHQOfficerF,
    4307 : lHQOfficerF,
    4308 : "Tabitha",
    4309 : "Marshall",
    4310 : "Martha Mopp",
    4311 : "Shanty Sänger",
    4312 : "Martin Satch",
    4313 : "Tauber Rudolf",
    4314 : "Dana Gander",
    4315 : "Undine Uhrwerk",
    4316 : "Tim Tango",
    4317 : "Dicky Zehe",
    4318 : "Bob Marlin",
    4319 : "Rinky Dink",
    4320 : "Cammy Coda",
    4321 : "Laurel Laute",
    4322 : "Randy Rhythmus",
    4323 : "Hanna Hogg",
    4324 : "Elli",
    4325 : "Bankier Bert",
    4326 : "Brenda Brett",
    4327 : "Flim Flam",
    4328 : "Wagner",
    4329 : "Nele Prompter",
    4330 : "Quentin",
    4331 : "Fabulo Costello",
    4332 : "Ziggy",
    4333 : "Harry",
    4334 : "Fast Freddie",
    4335 : "Fischer Walden",

    #
    # Daisy Gardens
    #

    # Daisy Gardens Playground
    5001 : lHQOfficerM,
    5002 : lHQOfficerM,
    5003 : lHQOfficerF,
    5004 : lHQOfficerF,
    5005 : "Angestellte Anemone",
    5006 : "Angestellter Camillo",
    5007 : "Rosa Blüte",
    # NPCFisherman
    5008 : "Tierhandlungs-\nAngestellter",
    # NPCPetClerks
    5009 : "Angestellte Ann Genehm",
    5010 : "Angestellter Tom A. Te",
    5011 : "Angestellter Johannes Beere",

    # Elm Street
    5101 : "Artie",
    5102 : "Susan",
    5103 : "Volker",
    5104 : "Schmetterding",
    5105 : "Jack",
    5106 : "Barbier Björn",
    5107 : "Postbote Felipe",
    5108 : "Gastwirtin Gastrinde",
    5109 : lHQOfficerM,
    5110 : lHQOfficerM,
    5111 : lHQOfficerF,
    5112 : lHQOfficerF,
    5113 : "Dr. Keim",
    5114 : "Welk",
    5115 : "Schleia Kraut",
    5116 : "Werner Vegetaro",
    5117 : "Früchtchen",
    5118 : "Pop Corn",
    5119 : "Grizzly Beer",
    5120 : "Gopher",
    5121 : "Erika Erbsschot",
    5122 : "Oswald Haufen",
    5123 : "Edda Ecker",
    5124 : "Pops Wund",
    5125 : "Pelikano Platsch",
    5126 : "Madam Mund",
    5127 : "Polly Pollen",
    5128 : "Susanna Setzling",
    5129 : "Fischerin Sally",

    # Maple Street
    5201 : "Hake",
    5202 : "Erika",
    5203 : "Lisa",
    5204 : "Bert",
    5205 : "Leopold Löwenzahn",
    5206 : "Rebert Grün",
    5207 : "Sofie Spritzer",
    5208 : "Silke Such",
    5209 : lHQOfficerM,
    5210 : lHQOfficerM,
    5211 : lHQOfficerF,
    5212 : lHQOfficerF,
    5213 : "Big Bauersmann",
    5214 : "Jukenda Ausschlag",
    5215 : "Karola Knolle",
    5216 : "Stinke-Jim",
    5217 : "Greg Gründaumen",
    5218 : "Rocky Rhododendron",
    5219 : "Lars Bizeps",
    5220 : "Lauf-Mascha",
    5221 : "Rosa Flamingo",
    5222 : "Heul-Suse",
    5223 : "Pfützen-Paule",
    5224 : "Onkel Landmann",
    5225 : "Pamela Pfanda",
    5226 : "Torf Moss",
    5227 : "Begonia Buddelbier",
    5228 : "Grabo Schmutzfink",
    5229 : "Fischerin Lily",

    # Oak street
    5301 : "Mitarbeiter der Zentrale",
    5302 : "Mitarbeiter der Zentrale",
    5303 : "Mitarbeiter der Zentrale",
    5304 : "Mitarbeiter der Zentrale",
    5305 : "Crystal",
    5306 : "B. Last",
    5307 : "Tiffany Lache",
    5308 : "Nelly Nörgel",
    5309 : "Ru Kola",
    5310 : "Timotheus",
    5311 : "Richterin McIntosh",
    5312 : "Bienhart",
    5313 : "Trainer Bemoost",
    5314 : "A. Meisenhügel",
    5315 : "Onkel Hollunder",
    5316 : "Onkel Keim",
    5317 : "Detektivin Lima",
    5318 : "Cäsar",
    5319 : "Rose",
    5320 : "April",
    5321 : "Professor Tausendschön",
    5322 : "Fischerin Rose",

    #
    # Dreamland
    #

    # Dreamland Playground
    9001 : "Susan Dämmerts",
    9002 : "Tom Tiefschlaf",
    9003 : "Dennis Dösig",
    9004 : lHQOfficerF,
    9005 : lHQOfficerF,
    9006 : lHQOfficerM,
    9007 : lHQOfficerM,
    9008 : "Angestellte Jill",
    9009 : "Angestellter Phil",
    9010 : "Abigail Abgetragen",
    # NPCFisherman
    9011 : "Tierhandlungs-\nAngestellter",
    # NPCPetClerks
    9012 : "Angestellte Sarah Bande",
    9013 : "Angestellte Anne Mone",
    9014 : "Angestellter Steve Mütterchen",

    # Lullaby Lane
    9101 : "Ed",
    9102 : "Big Mama",
    9103 : "PJ",
    9104 : "Süße Schlummerei",
    9105 : "Professor Gähn",
    9106 : "Maxim",
    9107 : "Kuschel",
    9108 : "Zwinky Zwirbel",
    9109 : "Traum-Daphne",
    9110 : "Kathy Minz",
    9111 : "Feler Suche",
    9112 : "Wiegenlied-Wiegand",
    9113 : "Uri Uhrwerk",
    9114 : "Lida Schatten",
    9115 : "Babyface MacDougal",
    9116 : "Der Mit Den Schafen Tanzt",
    9117 : "Sissy Feierabend",
    9118 : "Klara Nacht",
    9119 : "Steini",
    9120 : "Sarah Schlummer",
    9121 : "Zuzanna Zukurzdeck",
    9122 : "Dickie Augen",
    9123 : "Teddy Behr",
    9124 : "Nina Nachtlicht",
    9125 : "Dr. Unscharf",
    9126 : "Hella Wach",
    9127 : "Betty Bettdeck",
    9128 : "Hartmut Hammer",
    9129 : "Bertha Bettschwein",
    9130 : "Nathaniel Nachttopf",
    9131 : "Susan Siesta",
    9132 : lHQOfficerF,
    9133 : lHQOfficerF,
    9134 : lHQOfficerF,
    9135 : lHQOfficerF,
    9136 : "Fischer Taylor",

    # Tutorial IDs start at 20000, and are not part of this table.
    # Don't add any Toon id's at 20000 or above, for this reason!
    # Look in TutorialBuildingAI.py for more details.

    }

# These building titles are output from the DNA files
# Run ppython $TOONTOWN/src/dna/DNAPrintTitles.py to generate this list
# DO NOT EDIT THE ENTRIES HERE -- EDIT THE ORIGINAL DNA FILE
zone2TitleDict = {
    # titles for: phase_4/dna/toontown_central_sz.dna
    2513 : ("Toontown Rathaus", ""),
    2514 : ("Toontown Bank", ""),
    2516 : ("Toontown Schule", ""),
    2518 : ("Bibliothek Toontown", ""),
    2519 : ("Gag-Laden", ""),
    2520 : ("Toontown Zentrale", ""),
    2521 : ("Bekleidungsgeschäft", ""),
    # titles for: phase_5/dna/toontown_central_2100.dna
    2601 : ("Zahnklempnerei Breites Lächeln", ""),
    2602 : ("", ""),
    2603 : ("Eingleis-Bergbau", ""),
    2604 : ("Quatschwasch & Reinigung", ""),
    2605 : ("Toontown Schilderfabrik", ""),
    2606 : ("", ""),
    2607 : ("Springende Bohnen", ""),
    2610 : ("Dr. Hein Faltspinsel", ""),
    2611 : ("", ""),
    2616 : ("Kostümverleih Falschbart", ""),
    2617 : ("Verrückte Stunts", ""),
    2618 : ("Drehrumbum", ""),
    2621 : ("Papierflugzeuge", ""),
    2624 : ("Lustige Rowdys", ""),
    2625 : ("Haus des Schlechten Geschmacks", ""),
    2626 : ("Kaspars Witzreparaturen", ""),
    2629 : ("Der Lachplatz", ""),
    2632 : ("Clownschule", ""),
    2633 : ("Hehe-Tee-Laden", ""),
    2638 : ("Toontown Spielhaus", ""),
    2639 : ("Affereien", ""),
    2643 : ("Dosenflaschen", ""),
    2644 : ("Unpraktische Witze", ""),
    2649 : ("Spiel- und Spaßladen", ""),
    2652 : ("", ""),
    2653 : ("", ""),
    2654 : ("Lachlektionen", ""),
    2655 : ("Spielgeld-Bausparkasse", ""),
    2656 : ("Gebrauchte Clownautos", ""),
    2657 : ("Franks Faxen", ""),
    2659 : ("Freude Schöner Spötterfunken", ""),
    2660 : ("Kitzelmaschinen", ""),
    2661 : ("Dösbartel", ""),
    2662 : ("Dr. B. Geistert", ""),
    2663 : ("Toontown Cinerama", ""),
    2664 : ("Die Lustigen Mimen", ""),
    2665 : ("Reisebüro Hin & Weg", ""),
    2666 : ("Lachtankstelle", ""),
    2667 : ("Glückliche Zeiten", ""),
    2669 : ("Maldons Hohle Ballone", ""),
    2670 : ("Suppengabeln", ""),
    2671 : ("", ""),
    # titles for: phase_5/dna/toontown_central_2200.dna
    2701 : ("", ""),
    2704 : ("Multiplex-Kino", ""),
    2705 : ("Weisackers Krachmacher", ""),
    2708 : ("Schleimleim", ""),
    2711 : ("Toontown Postamt", ""),
    2712 : ("Gluckscafé", ""),
    2713 : ("Café Lachtniezu", ""),
    2714 : ("Spinners Cineplex", ""),
    2716 : ("Suppen und Beknacktes", ""),
    2717 : ("Flaschendosen", ""),
    2720 : ("Autoreparaturen Zerschmeißdich", ""),
    2725 : ("", ""),
    2727 : ("Seltersflaschen und -dosen", ""),
    2728 : ("Verschwindcreme", ""),
    2729 : ("14-Karat-Goldfisch", ""),
    2730 : ("Nachrichten zum Aufrichten", ""),
    2731 : ("", ""),
    2732 : ("Spaghetti und Blödhammel", ""),
    2733 : ("Gußeisendrachen", ""),
    2734 : ("Saugnäpfe und -teller", ""),
    2735 : ("Die Kawummerei", ""),
    2739 : ("Kaputtlacher-Flickerei", ""),
    2740 : ("Gebrauchte Feuerwerkskörper", ""),
    2741 : ("", ""),
    2742 : ("", ""),
    2743 : ("Die fetzige Reinigung", ""),
    2744 : ("", ""),
    2747 : ("Sichtbare Tinte", ""),
    2748 : ("Du machst mir Spaß!", ""),
    # titles for: phase_5/dna/toontown_central_2300.dna
    2801 : ("Sofa-Rubbeldiekatz-Kissen", ""),
    2802 : ("Aufblasbare Abbruchkugeln", ""),
    2803 : ("Karneval Kid", ""),
    2804 : ("Dr. Verdreht, Chiropraktiker", ""),
    2805 : ("", ""),
    2809 : ("Sportstudio Schwitzeria", ""),
    2814 : ("Toontown Theater", ""),
    2818 : ("Die Fliegende Torte", ""),
    2821 : ("", ""),
    2822 : ("Gummiadler-Sandwiches", ""),
    2823 : ("Eiskrem zum fröhlichen Eisbechern", ""),
    2824 : ("Kinopalast Sparwitz", ""),
    2829 : ("Blödes Geschwafel", ""),
    2830 : ("Beppos Blödeleien", ""),
    2831 : ("Professor Krümmdichs Lachhaus", ""),
    2832 : ("", ""),
    2833 : ("", ""),
    2834 : ("Lachanfall Notaufnahme", ""),
    2836 : ("", ""),
    2837 : ("Hartmuts Haha-Seminare", ""),
    2839 : ("Ungenießbare Pasta", ""),
    2841 : ("", ""),
    # titles for: phase_6/dna/donalds_dock_sz.dna
    1506 : ("Gag-Laden", ""),
    1507 : ("Toontown Zentrale", ""),
    1508 : ("Bekleidungsgeschäft", ""),
    # titles for: phase_6/dna/donalds_dock_1100.dna
    1602 : ("Gebrauchte Rettungswesten", ""),
    1604 : ("Regenjacken-Trockenreinigung", ""),
    1606 : ("Hooks Uhrenreparaturen", ""),
    1608 : ("Steuerbord & Backröhre", ""),
    1609 : ("Jedermanns Köder", ""),
    1612 : ("Heller und Kreuzer Bank", ""),
    1613 : ("Quitt Pro Quo, Rechtsanwälte", ""),
    1614 : ("Streich die Nägel Boutique", ""),
    1615 : ("Yacht nix, Leute!", ""),
    1616 : ("Schwarzbarts Schönheitssalon", ""),
    1617 : ("Land-In-Sicht-Optik", ""),
    1619 : ("Baumchirurgie & Piratung", ""),
    1620 : ("Von Bug bis Heck", ""),
    1621 : ("Verpeildeck-Sporthalle", ""),
    1622 : ("Schalter und Strömlinge Elektrogeschäft", ""),
    1624 : ("Hechtledersohlen-Schnellreparatur", ""),
    1626 : ("Edelfeine Bekleidung für festliche Anlässe", ""),
    1627 : ("Kalle Kiels Kaufrausch-Kompasshaus", ""),
    1628 : ("Kaviarstimmer", ""),
    1629 : ("", ""),
    # titles for: phase_6/dna/donalds_dock_1200.dna
    1701 : ("Kindergarten ", ""),
    1703 : ("China-Imbiss Wok 8, Achtern Strom", ""),
    1705 : ("Gaumensegelverkauf", ""),
    1706 : ("Erdnussbutter und Quallengelee", ""),
    1707 : ("Geschenkideen mit Riff", ""),
    1709 : ("Karavellbonbons und Marzipan", ""),
    1710 : ("Bernikel-Billigschnäppchen", ""),
    1711 : ("Tiefsee-Kneipe", ""),
    1712 : ("Sporthalle Volle Kraft", ""),
    1713 : ("Adalberts Smarter Seekarten-Markt", ""),
    1714 : ("Hol-Sie-Inn", ""),
    1716 : ("Meerjungfrau-Badebekleidung", ""),
    1717 : ("Sei Stiller Ozean-Ansichten", ""),
    1718 : ("Taxiservice Gestrandet", ""),
    1719 : ("Ducks Stilles Wasser GmbH", ""),
    1720 : ("Angelruten-Rudi", ""),
    1721 : ("Nautisch um jeden Preis", ""),
    1723 : ("Kalmars Seetang", ""),
    1724 : ("Ritters Aalverkauf", ""),
    1725 : ("Achims Fabelhaftes Seekrabben-Center", ""),
    1726 : ("Flüssiggersteladungen", ""),
    1727 : ("Dies Ruder Das", ""),
    1728 : ("Pfiffige Pfeilschwanzkrebse", ""),
    1729 : ("", ""),
    # titles for: phase_6/dna/donalds_dock_1300.dna
    1802 : ("Nautisch, aber nett", ""),
    1804 : ("Muckibude", ""),
    1805 : ("Frühstück aus der Köderbüchse", ""),
    1806 : ("Hutgeschäft Fesche Schlagseite", ""),
    1807 : ("Kiel-Deals", ""),
    1808 : ("Knot am Mann!", ""),
    1809 : ("Rosteimer", ""),
    1810 : ("Anker-Management", ""),
    1811 : ("Nicht zu überbooten!", ""),
    1813 : ("Anlegestellenberatung", ""),
    1814 : ("Ahoi-Shop", ""),
    1815 : ("Is' Was, Dock?", ""),
    1818 : ("Café Sieben Meere", ""),
    1819 : ("Dockers-Kneipe", ""),
    1820 : ("Haken, Schnur und Senkbleischmuckladen", ""),
    1821 : ("König Neptuns Konservenfabrik", ""),
    1823 : ("Speiselokal Muschelauflauf", ""),
    1824 : ("Hundepaddel", ""),
    1825 : ("Fischmarkt Absolut Makrelig", ""),
    1826 : ("Gerts Gewebeleinstek-Gewänder", ""),
    1828 : ("Alices Ballastpalast", ""),
    1829 : ("Möwenstatuenmarkt", ""),
    1830 : ("Verloren und Geflundern", ""),
    1831 : ("Klar Schiff!", ""),
    1832 : ("Marks Massiv-Marssegel-Markt", ""),
    1833 : ("Maßanzüge Ein Mann wie ein Mastbaum", ""),
    1834 : ("Jollig lächerlich!", ""),
    1835 : ("", ""),
    # titles for: phase_6/dna/minnies_melody_land_sz.dna
    4503 : ("Gag-Laden", ""),
    4504 : ("Toontown Zentrale", ""),
    4506 : ("Bekleidungsgeschäft", ""),
    # titles for: phase_6/dna/minnies_melody_land_4100.dna
    4603 : ("Tom-Toms Trommeln", ""),
    4604 : ("Im Vier-Viertel-Takt", ""),
    4605 : ("Fifis Fiedeln", ""),
    4606 : ("Casa De Castanets", ""),
    4607 : ("Aparte Liedbekleidung", ""),
    4609 : ("Ta-Ke-Ti-Nasten-Pianotasten", ""),
    4610 : ("Bitte benimm' dich!", ""),
    4611 : ("Stimmgabeln und -löffel", ""),
    4612 : ("Dr. Karies Zahnarztpraxis", ""),
    4614 : ("Rasieren und Haarschneiden für ein Lied", ""),
    4615 : ("Piccolos Pizza", ""),
    4617 : ("Lustige Mandolinen", ""),
    4618 : ("Notendurft-Räume", ""),
    4619 : ("Mehr Punkte", ""),
    4622 : ("Kinnstütz-Kissen", ""),
    4623 : ("Entfernen von Kreuzen", ""),
    4625 : ("Zahnpasta in der Tuba", ""),
    4626 : ("Notationen", ""),
    4628 : ("Schlechte-Vorzeichen-Versicherung", ""),
    4629 : ("Buntlose Papierteller", ""),
    4630 : ("Musik ist unsere Lautstärke", ""),
    4631 : ("Canto mir helfen?", ""),
    4632 : ("Tanz rund um die Uhr-Macherei", ""),
    4635 : ("Tenor-Times", ""),
    4637 : ("Singende Schneiderei", ""),
    4638 : ("Hard Rock Shop", ""),
    4639 : ("Antiquitäten zum Viertel-Preis", ""),
    4641 : ("Blues News", ""),
    4642 : ("Die fetzige Reinigung", ""),
    4645 : ("Club 88", ""),
    4646 : ("", ""),
    4648 : ("Umzugsfirma Tonträger", ""),
    4649 : ("", ""),
    4652 : ("Große-Pause-Laden ", ""),
    4653 : ("", ""),
    4654 : ("Perfekte Ton-Dächer", ""),
    4655 : (" Kochschule des Notenschüssel-Kochs ", ""),
    4656 : ("", ""),
    4657 : ("Barbershop-Quartett", ""),
    4658 : ("Plumpsende Pianos", ""),
    4659 : ("", ""),
    # titles for: phase_6/dna/minnies_melody_land_4200.dna
    4701 : ("Die Schmalzwalzer-Tanzschule", ""),
    4702 : ("Holzmichelbedarf Singende Säge", ""),
    4703 : ("Ein Feines Händel für Gepäck", ""),
    4704 : ("Tinas Konzertinakonzerte", ""),
    4705 : ("Weder Klavier noch dort", ""),
    4707 : ("Dopplers Soundeffekt-Studio", ""),
    4709 : ("Hohes C Kletterbedarf", ""),
    4710 : ("Fahrschule Tempo, Kutscherpolka!", ""),
    4712 : ("Reparatur für punktierte Reifen", ""),
    4713 : ("Dissis Modische Herrenbekleidung", ""),
    4716 : ("Vier-Seiten-Mundharmonikas", ""),
    4717 : ("Auto-Rabattversicherung Schuld war der Andantere!", ""),
    4718 : ("Bachmaterial und anderes Küchenzubehör", ""),
    4719 : ("Madrigal Wohnmobile", ""),
    4720 : ("Der richtige Toon", ""),
    4722 : ("Ouvertüren-Untersuchungen", ""),
    4723 : ("Spielplatzbedarf Verspiel Dich", ""),
    4724 : ("Rauschen beim Anziehen und Plauschen", ""),
    4725 : ("Der Baritonbarbier", ""),
    4727 : ("Flechten von Stimmbändern", ""),
    4728 : ("Sing solo, wir hören Dich nicht", ""),
    4729 : ("Buchladen Leere Saite", ""),
    4730 : ("Törichte Texte", ""),
    4731 : ("Toon-Töne", ""),
    4732 : ("Theaterkompanie Etude Brute?", ""),
    4733 : ("", ""),
    4734 : ("", ""),
    4735 : ("Akkordeons, beim Eintreten nicht balgen!", ""),
    4736 : ("Hochzeitsplaner Auf in die Zitherwochen", ""),
    4737 : ("Harfenschoner", ""),
    4738 : ("Geschäft für Kunstmusik und Kunstgewerbe", ""),
    4739 : ("", ""),
    # titles for: phase_6/dna/minnies_melody_land_4300.dna
    4801 : ("Marshalls Plattenstapel", ""),
    4803 : ("Dienstmädchenschule Mezzoprächtig", ""),
    4804 : ("Mixolydische Schule für Barkeeper", ""),
    4807 : ("Entspann den Bach", ""),
    4809 : ("Ich Nix Verstanza!", ""),
    4812 : ("", ""),
    4817 : ("Tierhandlung Basstölpel", ""),
    4819 : ("Yukis Ukulelen", ""),
    4820 : ("", ""),
    4821 : ("Annas Kreuzfahrten", ""),
    4827 : ("Tabulatuhren", ""),
    4828 : ("Schumanns Schuhe für den Mann", ""),
    4829 : ("Pachelbels Kanonenkugeln", ""),
    4835 : ("Ursatz für Kool Katz", ""),
    4836 : ("Reggae-Regale", ""),
    4838 : ("Musikschule für Kazoologie", ""),
    4840 : ("Coda Pop musikalische Getränke", ""),
    4841 : ("Lyra, Lyra, nix berühra!", ""),
    4842 : ("Die Synkopenierung Unternehmung", ""),
    4843 : ("", ""),
    4844 : ("Con-Moto-Räder", ""),
    4845 : ("Katrins kunterbunte Klagelieder", ""),
    4848 : ("Massenhaft Noten Bausparkasse", ""),
    4849 : ("", ""),
    4850 : ("Pfandhaus Leihakkord", ""),
    4852 : ("Verblümtes Flötenvlies", ""),
    4853 : ("Leos Fender", ""),
    4854 : ("Wagners Wohlerdachte Violinen-Videos", ""),
    4855 : ("Das Tele-Caster-Netzwerk", ""),
    4856 : ("", ""),
    4862 : ("Quentins Quintessenzielle Quadrillen", ""),
    4867 : ("Mr. Costellos Fabulöse Cellos", ""),
    4868 : ("", ""),
    4870 : ("Ziggys Zoo der Zigeunermusik", ""),
    4871 : ("Harrys Haus der Harmonischen Humbucker", ""),
    4872 : ("Fast Freddies Verbundlose Fingergriffbretter", ""),
    4873 : ("", ""),
    # titles for: phase_8/dna/daisys_garden_sz.dna
    5501 : ("Gag-Laden", ""),
    5502 : ("Toontown Zentrale", ""),
    5503 : ("Bekleidungsgeschäft", ""),
    # titles for: phase_8/dna/daisys_garden_5100.dna
    5601 : ("Kartoffelauge Sehkraftprüfung", ""),
    5602 : ("Artie Schocks Krawatten", ""),
    5603 : ("Da haben wir den Salat", ""),
    5604 : ("Schleierkraut Hochzeitsausstatter", ""),
    5605 : ("Vege-stabile Tische und Stühle", ""),
    5606 : ("Blüten", ""),
    5607 : ("Kompostamt", ""),
    5608 : ("Rock und Pop Corn", ""),
    5609 : ("Verbirkene Schätze", ""),
    5610 : ("Susan Matschauges Boxunterricht", ""),
    5611 : ("Gophers Gags", ""),
    5613 : ("Kahlschlag-Barbiere", ""),
    5615 : ("Volkers Vogelfutter", ""),
    5616 : ("Zaungasthaus", ""),
    5617 : ("Schmetterdings Schmetterlinge", ""),
    5618 : ("Kletten und Etiketten", ""),
    5619 : ("Jacks Bohnenstangen", ""),
    5620 : ("Gasthaus Ohne Harken und Ösen", ""),
    5621 : ("Buchweizen für Leseratten", ""),
    5622 : (" Drahtesel für Grünlandfahrer    ", ""),
    5623 : ("Vogel-Schaumbäder", ""),
    5624 : ("Mund Halten!", ""),
    5625 : ("Lass es Wein!", ""),
    5626 : ("Fichtennadelarbeiten", ""),
    5627 : ("", ""),
    # titles for: phase_8/dna/daisys_garden_5200.dna
    5701 : ("Von Anfang bis Ernte", ""),
    5702 : ("Hakes Marken-Harken", ""),
    5703 : ("Foto-Erikas Kameraladen ", ""),
    5704 : ("Lisa Limones Gebrauchtwagen", ""),
    5705 : ("Giftefeu-Möbel", ""),
    5706 : ("14-Karotten-Juweliere", ""),
    5707 : ("Musikalische Früchtchen", ""),
    5708 : ("Reisebüro Wäre Weg", ""),
    5709 : ("Astroturf-Mäher", ""),
    5710 : ("Sportstudio Beerenstarke Jungs", ""),
    5711 : ("Glühstrumpfwaren", ""),
    5712 : ("Komische Statuen", ""),
    5713 : ("Lot und Leiden", ""),
    5714 : ("Springbrunnen-Seltersflaschen", ""),
    5715 : ("Scheunen-Nachrichten", ""),
    5716 : ("Pfandhaus Nimms oder Lassos", ""),
    5717 : ("Die Spritzblume", ""),
    5718 : ("Löwenzahn Exoten-Tierhandlung", ""),
    5719 : ("Privatdetektei Hermit die Wahrheit!", ""),
    5720 : ("Reben und Gecken Herrenbekleidung", ""),
    5721 : ("Rute 66 Speiserestaurant", ""),
    5725 : ("Gerste-, Hopfen- und Malzgeschäft", ""),
    5726 : ("Berts Dreck", ""),
    5727 : ("Vergissmeingeldnicht Bausparkasse", ""),
    5728 : ("", ""),
    # titles for: phase_8/dna/daisys_garden_5300.dna
    5802 : ("Toontown Zentrale ", ""),
    5804 : ("Glas mal Sehen", ""),
    5805 : ("Schneckenpost ", ""),
    5809 : ("Clownschule Tiefe Lache", ""),
    5810 : ("Männertreu ist hier neu ", ""),
    5811 : ("Gasthaus Freundliche Einsaladung ", ""),
    5815 : ("Graswurzel", ""),
    5817 : ("Äpfel und Birnen", ""),
    5819 : ("Flotte-Bienen-Jeans ", ""),
    5821 : ("Sporthalle Hauen und Flechten", ""),
    5826 : ("Ameisenzuchtzubehör ", ""),
    5827 : ("Hollunder Wunderangebote", ""),
    5828 : ("Faulpelz Möbel", ""),
    5830 : ("Spuck's Aus", ""),
    5833 : ("Die Salatbar", ""),
    5835 : ("Blumenbed & Breakfast", ""),
    5836 : ("Aprilregenwasserduschen", ""),
    5837 : ("Schule der blumigen Künste ", ""),
    # titles for: phase_8/dna/donalds_dreamland_sz.dna
    9501 : ("Schlafliedbibliothek", ""),
    9503 : ("Die Dämmer-Bar", ""),
    9504 : ("Gag-Laden", ""),
    9505 : ("Toontown Zentrale", ""),
    9506 : ("Bekleidungsgeschäft", ""),
    # titles for: phase_8/dna/donalds_dreamland_9100.dna
    9601 : ("Kuschel Dich 'Inn", ""),
    9602 : ("Vierzigmal Zwinkern zum Preis von zwanzig", ""),
    9604 : ("Eds Bettlaken", ""),
    9605 : ("Schlafliedgasse 323", ""),
    9607 : ("Big Mamas Bahama-Pyjama", ""),
    9608 : ("Katzenminz' für Katzenschlummer", ""),
    9609 : ("Tiefschlaf mit Schaf", ""),
    9613 : ("Die Uhrenreiniger", ""),
    9616 : ("Elektrofirma Licht Aus", ""),
    9617 : ("Schlafliedgasse 212", ""),
    9619 : ("Maximale Entspannung", ""),
    9620 : (" PJs Taxiservice", ""),
    9622 : ("Schlafens-Zeiteisen", ""),
    9625 : ("Schönheitssalon Roll Dich Ein", ""),
    9626 : ("Schlafliedgasse 818", ""),
    9627 : ("Das Schlaftipi", ""),
    9628 : ("Sis-Feierahmd-Kalender", ""),
    9629 : ("Schlafliedgasse 310", ""),
    9630 : ("Schlafen-wie-ein-Stein-Bruch", ""),
    9631 : ("Auszeit Uhrenreparaturen", ""),
    9633 : ("Traumland-Kinosaal", ""),
    9634 : ("Ratzematratze", ""),
    9636 : ("Schlaflos-Versicherung", ""),
    9639 : ("Haus des Winterschlafs", ""),
    9640 : ("Schlafliedgasse 805", ""),
    9642 : ("Säge-Schlummerbretter", ""),
    9643 : ("Augen-Zu Sehprüfung", ""),
    9644 : ("Kissenschlacht jede Nacht", ""),
    9645 : ("Gasthaus Zur Warmen Bettdecke", ""),
    9647 : ("Eisenwarenhandlung Mach dein Bett!", ""),
    9649 : ("Schnarchkapsel", ""),
    9650 : ("Schlafliedgasse 714", ""),
    9651 : ("Für Reicher und Schnarcher", ""),
    9652 : ("", ""),
    # titles for: phase_8/dna/the_burrrgh_sz.dna
    3507 : ("Gag-Laden", ""),
    3508 : ("Toontown Zentrale", ""),
    3509 : ("Bekleidungsgeschäft", ""),
    # titles for: phase_8/dna/the_burrrgh_3100.dna
    3601 : ("Elektrofirma Nordlicht ", ""),
    3602 : ("Nordoster-Hüte", ""),
    3605 : ("", ""),
    3607 : ("Der Schnee-Weise", ""),
    3608 : ("Nichts zu Rodeln", ""),
    3610 : ("Mikes Mordsmäßiger Mukluk-Mart", ""),
    3611 : ("Herrn Krugs Schneepflugs", ""),
    3612 : ("Iglu Design", ""),
    3613 : ("Blitzeisgefahrräder", ""),
    3614 : ("Schneeflocken-Müsli-Firma", ""),
    3615 : ("Gefrosteter Kalter Hund", ""),
    3617 : ("Kaltluftballonfahrten", ""),
    3618 : ("Kein Schneema! Krisenmanagement", ""),
    3620 : ("Schiklinik", ""),
    3621 : ("Schmelz-Eisbar", ""),
    3622 : ("", ""),
    3623 : ("Umtoste Toastbrot-Firma", ""),
    3624 : ("Unter Null Sandwichladen", ""),
    3625 : ("Tante Frostbeules Heizkörper", ""),
    3627 : ("Bernhardinerhüttenclub", ""),
    3629 : ("Café Dicke Suppe", ""),
    3630 : ("(R)Eis(e)büro London-Frost, Frost-Frankreich", ""),
    3634 : ("Schaukelstuhllifte", ""),
    3635 : ("Gebrauchtes Feuerholz", ""),
    3636 : ("Gänsehaut für Jedermann", ""),
    3637 : ("Kates Skates", ""),
    3638 : ("Ins Ungewisse Schlitten", ""),
    3641 : ("Freds Geschätzte Schlittenbetten", ""),
    3642 : ("Sturmauge Optik", ""),
    3643 : ("Schneeballsaal", ""),
    3644 : ("Geschmolzene Eiswürfel", ""),
    3647 : ("Smokinggeschäft Heiterer Pinguin", ""),
    3648 : ("Pulverisiertes Trockeneis", ""),
    3649 : ("Hambrrrger", ""),
    3650 : ("Antarktische Antiquitäten", ""),
    3651 : ("Feinfrost-Freddys Gefrostete Frankfurter", ""),
    3653 : ("Kühlhaus-Schmuck", ""),
    3654 : ("", ""),
    # titles for: phase_8/dna/the_burrrgh_3200.dna
    3702 : ("Winterlagerung", ""),
    3703 : ("", ""),
    3705 : ("Eisgefahrräder für zwei", ""),
    3706 : ("Schüttelfrost-Shakes", ""),
    3707 : ("Zu Hause ist es am schneesten", ""),
    3708 : ("Plutos Laden", ""),
    3710 : ("Speiserestaurant Fallende Grade ", ""),
    3711 : ("", ""),
    3712 : ("Schwimm mit dem Eisstrom", ""),
    3713 : ("Klappernde Zähne, Unter-Null-Zahnarzt", ""),
    3715 : ("Tante Arktis' Suppenküche", ""),
    3716 : ("Streusalz und -pfeffer", ""),
    3717 : ("Verschneen Sie, was ich meine??", ""),
    3718 : ("Designer-Schlauchseelen", ""),
    3719 : ("Eiswürfel am Stiel", ""),
    3721 : ("Schlitzauges Schlitten-Schnäppchen", ""),
    3722 : ("Schneehasen-Skigeschäft", ""),
    3723 : ("Schüttis Schneekugeln", ""),
    3724 : ("Die Bibberchronik", ""),
    3725 : ("Zu erschlittern", ""),
    3726 : ("Sonnenenergie-Bettdecken", ""),
    3728 : ("Müde Schneepflüge ", ""),
    3729 : ("", ""),
    3730 : ("Schneemänner An- und Verkauf", ""),
    3731 : ("Transportable Kamine", ""),
    3732 : ("Die Frostnase", ""),
    3734 : ("Sehkraftprüfungen Ich sehe was, was du nicht siehst ", ""),
    3735 : ("Polereiskappen", ""),
    3736 : ("Würfeleis zum Schleuderpreis", ""),
    3737 : ("Gasthof Bergab", ""),
    3738 : ("Hitze - Hol sie dir, solange sie heiß ist ", ""),
    3739 : ("", ""),
    }

# translate
# DistributedCloset.py
ClosetTimeoutMessage = "Entschuldige, deine\n Zeit ist abgelaufen."
ClosetNotOwnerMessage = "Das ist zwar nicht dein Schrank, aber du darfst die Sachen anprobieren."
ClosetPopupOK = lOK
ClosetPopupCancel = lCancel
ClosetDiscardButton = "Entfernen"
ClosetAreYouSureMessage = "Du hast einige Kleidungsstücke gelöscht. Möchtest du sie wirklich löschen?"
ClosetYes = lYes
ClosetNo = lNo
ClosetVerifyDelete = "%s wirklich löschen?"
ClosetShirt = "dieses Oberteil"
ClosetShorts = "diese Shorts"
ClosetSkirt = "diesen Rock"
ClosetDeleteShirt = "Oberteil\nlöschen"
ClosetDeleteShorts = "Shorts\nlöschen"
ClosetDeleteSkirt = "Rock\nlöschen"

# EstateLoader.py
EstateOwnerLeftMessage = "Leider ist der Eigentümer dieses Grundstückes nicht da. Du wirst in %s Sekunden zum Spielplatz zurück geschickt."
EstatePopupOK = lOK
EstateTeleportFailed = "Du konntest nicht nach Hause gehen. Versuche es nochmal!"
EstateTeleportFailedNotFriends = "Leider ist %s auf dem Grundstück eines Toons, mit dem du nicht befreundet bist."

# DistributedHouse.py
AvatarsHouse = "%s\n Haus"

# BankGui.py
BankGuiCancel = lCancel
BankGuiOk = lOK

# DistributedBank.py
DistributedBankNoOwner = "Entschuldige, das ist nicht deine Sparbüchse."
DistributedBankNotOwner = "Entschuldige, das ist nicht deine Sparbüchse."

# FishSellGui.py
FishGuiCancel = lCancel
FishGuiOk = "Alles verkaufen"
FishTankValue = "Hi, %(name)s! Du hast %(num)s Fische in deinem Eimer, die insgesamt %(value)s Jelly Beans wert sind. Möchtest du sie alle verkaufen?"

def GetPossesive(name):
    if name[-1:] == 's':
        possesive = name +" '"
    else:
        possesive = name + "s"
    return possesive

# end translate

# DistributedFireworkShow.py
FireworksInstructions = lToonHQ+": Drücke die Taste 'Bild Hoch', um besser zu sehen."

FireworksJuly4Beginning = lToonHQ+": Frohes Tag der deutschen Einheit Feuerwerk! Viel Spaß!"
FireworksJuly4Ending = lToonHQ+": Wir hoffen, es hat dir gefallen!"
FireworksNewYearsEveBeginning = lToonHQ+": Frohes neues Jahr! Viel Spaß beim Feuerwerk!"
FireworksNewYearsEveEnding = lToonHQ+": Wir hoffen, es hat dir gefallen! Ein frohes Jahr 2006!"

# ToontownLoadingScreen.py

TIP_NONE = 0
TIP_GENERAL = 1
TIP_STREET = 2
TIP_MINIGAME = 3
TIP_COGHQ = 4
TIP_ESTATE = 5

# As of 8/5/03, ToonTips shouldn't exceed 130 characters in length
TipTitle = "TOON-TIPP:"
TipDict = {
    TIP_NONE : (
    "",
    ),

    TIP_GENERAL : (
    "Wenn du deinen Spielstand bei den Toon-Aufgaben schnell kontrollieren willst, halte einfach die Taste 'Ende' gedrückt. ",
    "Wenn du deine Gag-Seite schnell kontrollieren willst, halte einfach Taste 'Pos1' gedrückt.",
    "Drücke die Taste 'F7', um deine Freunde-Liste zu öffnen.",
    "Drücke die Taste 'F8', um dein Sticker-Buch zu öffnen oder zu schließen. ",
    "Wenn du die Taste 'Bild Hoch' drückst, kannst du nach oben schauen, mit der Taste 'Bild Runter' nach unten.",
    "Wenn du springen willst, drücke die Taste 'Strg'.",
    "Drücke die Taste 'F9' um einen Screenshot, also eine Bildschirmansicht in deinem Toontown-Ordner auf deinem Computer zu speichern.",
    # This one makes me nervous without mentioning Parent Passwords - but that would be too long
    # "You can exchange Secret Friend Codes with somebody you know outside Toontown to enable open chat with them in Toontown.",
    "Auf der Seite Optionen in deinem Sticker-Buch kannst du die Bildschirmauflösung ändern sowie Audio und andere Optionen einstellen und steuern.",
    "Probiere die Kleidung deines Freundes vor dem Schrank in seinem Haus an.",
    "Mit der Schaltfläche 'Nach Hause gehen' auf deinem Stadtplan kommst du zu deinem Haus.",
    "Immer, wenn du eine gelöste Toon-Aufgabe abgibst, werden deine Lach-Punkte automatisch aufgefüllt.",
    "Im Angebot von Bekleidungsgeschäften kannst du auch ohne Kleidermarke stöbern.",
    "Die Belohnung für manche Toon-Aufgaben ermöglicht dir, mehr Gags und Jelly Beans bei dir zu tragen.",
    "Du kannst bis zu 50 Freunde auf deiner Freunde-Liste haben.",
    "Einige Belohnungen für erledigte Toon-Aufgaben ermöglichen dir, dich mit Hilfe der Stadtplanseite im Sticker-Buch zu Spielplätzen zu teleportieren.",
    "Erhöhe deine Lach-Punkte auf den Spielplätzen, indem du Schätze wie Sterne und Eistüten sammelst.",
    "Wenn du nach einem harten Kampf schnell heilen musst, geh zu deinem Grundstück und sammle Eistüten.",
    "Mit der Tab-Taste kannst du zwischen verschiedenen Ansichten deines Toons wechseln.",
    "Manchmal werden verschiedene Toon-Aufgaben für dieselbe Belohnung angeboten. Vergleiche die Angebote!",
    "Das Spiel kann noch mehr Spaß machen, wenn du dir Freunde mit ähnlichen Toon-Aufgaben suchst.",
    "Du brauchst deinen Spielstand nicht zu speichern. Die Toontown-Server speichern fortwährend alle notwendigen Informationen.",
    "Du kannst anderen Toons etwas zuflüstern, indem du sie entweder anklickst oder sie in deiner Freunde-Liste auswählst.",
    "Manche Schnell-Chat-Wendungen zeigen die Gefühle deines Toons als Animation.",
    "Wenn die Gegend, in der du dich befindest, überfüllt ist, versuche den Bezirk zu wechseln. Gehe zur Bezirksseite in deinem Sticker-Buch und wähle einen anderen.",
    "Wenn du aktiv Gebäude rettest, erhältst du einen Stern in Bronze, Silber oder Gold über deinem Toon.",
    "Wenn du so viele Gebäude rettest, dass du einen Stern über deinem Kopf erhältst, findest du deinen Name wahrscheinlich auf der Tafel in eine Toontown-Zentrale.",
    "Gerettete Gebäude werden manchmal von den Bots zurückerobert. Wenn du deinen Stern behalten willst, musst du loszuziehen und weitere Gebäude retten!",
    "Die Namen deiner Geheimen Freunde erscheinen in Blau.",
    # Fishing
    "Versuche, alle Fische in Toontown zu fangen!",
    "In verschiedenen Teichen schwimmen verschiedene Fische. Versuche es überall! ",
    "Wenn dein Fischeimer voll ist, verkaufe deine Fische an die Tierhandlungs- Angestellten auf den Spielplätzen.",
    "Du kannst deine Fische an die Tierhandlungen oder an die Tierhandlungs-Angestellten verkaufen.",
    "Stärkere Angelruten fangen schwerere Fische, ihre Benutzung kostet aber mehr Jelly Beans. ",
    "Du kannst stärkere Angelruten im Kuhtalog kaufen.",
    "Schwerere Fische sind in der Tierhandlung mehr Jelly Beans wert.",
    "Seltene Fische sind in der Tierhandlung mehr Jelly Beans wert.",
    "Manchmal kann man beim Fischen Beutel mit Jelly Beans finden.",
    "Bei manchen Toon-Aufgaben muss man Dinge aus den Teichen fischen.",
    "In den Fischteichen auf den Spielplätzen gibt es andere Fische als in Teichen an Straßen.",
    "Manche Fische sind überaus selten. Angle weiter, bis du alle gesammelt hast!",
    "In dem Teich bei deinem Grundstück gibt es Fische, die man nur dort findet.",
    "Für jeweils 10 Arten, die du fängst, erhältst du eine Angeltrophäe!",
    "In deinem Sticker-Buch kannst du sehen, welche Fische du gesammelt hast.",
    "Bei manchen Angeltrophäen bekommst du eine Lach-Spritze.",
    "Angeln ist eine gute Möglichkeit, sich noch mehr Jelly Beans zu verdienen.",
    ),

  TIP_STREET : (
    "Es gibt vier Arten von Bots: Gesetzomaten, Monetomaten, Schachermaten und Chefomaten.",
    "Jeder Gag-Ablauf hat einen anderen Grad an Genauigkeit und schädlicher Wirkung.",
    "Sound-Gags wirken auf alle Bots, wecken aber geköderter Bots auf.",
    "Bots in einer strategischen Folge zu bekämpfen erhöht die Chancen, Kämpfe zu gewinnen.",
    "Mit dem Gag-Ablauf Aufheitern kannst du andere Toons im Kampf heilen.",
    "Während einer Bot-Invasion verdoppeln sich die Gag-Erfahrungspunkte!",
    "Mehrere Toons können sich zusammenschließen und denselben Gag-Ablauf im Kampf verwenden, um zusätzlichen Schaden bei den Bots anzurichten.",
    "Im Kampf werden Gags von oben nach untern in der Reihenfolge benutzt, wie sie auf dem Gag-Menü erscheinen.",
    "Die Reihe runder Lichter über den Aufzügen in Bot-Gebäuden zeigt an, wie viele Stockwerke es drinnen gibt.",
    "Klicke auf einen Bot, um Einzelheiten zu sehen.",
    "Die Verwendung von Gags höherer Level gegen Bots niedrigerer Level bringt keine Erfahrungspunkte ein.",
    "Gags, die Erfahrungspunkte einbringen, haben im Kampf auf dem Gag-Menü einen blauen Hintergrund.",
    "Die Gag-Erfahrung multipliziert sich beim Einsatz des Gags im Inneren von Gebäuden. Höhere Stockwerke haben höhere Multiplikationsfaktoren.",
    "Wenn ein Bot besiegt wird, wird er nach dem Kampf jedem Toon in dieser Runde angerechnet.",
    "Jede Straße in Toontown hat verschiedene Bot-Level und -Arten.",
    "Fußwege sind frei von Bots.",
    "Auf den Straßen geben die Seitentüren lustige Sprüche von sich, wenn man sich ihnen nähert.",
    "Manche Toon-Aufgaben sind ein Training für neue Gag-Abläufe. Du darfst nur sechs der sieben Gag-Tracks auswählen. Wähle daher sorgfältig!",
    "Fallen Stellen sind nur nützlich, wenn du oder deine Freunde sich beim Einsatz von Ködern im Kampf koordiniert.",
    "Bei Köder-Gags höherer Level ist ein Versagen weniger wahrscheinlich.",
    "Gags niedrigerer Level haben gegen Bots höherer Level eine geringere Genauigkeit.",
    "Bots können nicht angreifen, wenn sie im Kampf geködert wurden.",
    "Wenn du mit deinen Freunden ein Bot-Gebäude erobert hast, dann werdet ihr mit Porträts im geretteten Toon-Gebäude belohnt.",
    "Die Anwendung eines Tooning-Gags auf einen Toon mit vollem Lach-O-Meter bringt keine Tooning-Erfahrung.",
    "Bots sind kurz betäubt, wenn sie von einem Gag getroffen werden. Das erhöht die Trefferwahrscheinlichkeit für andere Gags in derselben Runde.",
    "Fallen lassen-Gags haben eine geringe Trefferwahrscheinlichkeit, aber die Genauigkeit wird erhöht, wenn Bots in derselben Runde zuerst von einem anderen Gag getroffen werden.",
    "Wenn du genügend Bots besiegt hast, verwende den 'Bot-Radar', indem du die Bot-Symbole auf der Bot-Galerie-Seite in deinem Sticker-Buch anklickst.",
    "Während eines Kampfes kannst du an den Strichen (-) und X-en sehen, welchen Bot deine Teamkameraden gerade angreifen.",
    "Im Kampf zeigt bei den Bots ein Licht ihren Gesundheitszustand an: Grün bedeutet gesund, Rot bedeutet fast zerstört.",
    "Es können maximal vier Toons auf einmal kämpfen.",
    "Auf der Straße treten Bots eher in einen Kampf gegen mehrere Toons als gegen nur einen Toon ein.",
    "Die beiden schwierigsten Bot jeder Art findet man nur innerhalb von Gebäuden.",
    "Fallen lassen-Gags wirken niemals gegen geköderte Bots.",
    "Bots greifen meist den Toon an, der ihnen den größten Schaden zugefügt hat.",
    "Sound-Gags richten bei geköderten Bots keinen zusätzlichen Schaden an.",
    "Wenn du allzu lange mit dem Angriff auf einen geköderten Bot wartest, wacht er wieder auf. Der Köder wirkt auf höheren Leveln länger.",
    "Jede Straße in Toontown hat einen Fischteich. Manche Straßen haben einzigartige Fische, die es nur dort gibt.",
    ),

  TIP_MINIGAME : (
    "Wenn du dein Jelly Beans-Glas aufgefüllt hast, werden alle Jelly Beans, die du bei den kleinen Spielen des Toon-Expresses gewinnst, automatisch in deine Sparbüchse in deinem Haus transferiert.",
    "Im Spiel 'Minnies Tanzstunde' kannst du anstelle der Maus auch die Pfeiltasten benutzen.",
    "Im Kanonen-Spiel kannst du die Kanone mit den Pfeiltasten bewegen und mit der 'Strg'- Taste abfeuern.",
    "Im Ringspiel werden Bonuspunkte vergeben, wenn die ganze Gruppe erfolgreich durch ihre Ringe schwimmt.",
    "Ein fehlerloser Durchlauf von Minnies Tanzstunde verdoppelt deine Punkte.",
    "Beim Tauziehen erhältst du mehr Jelly Beans, wenn du gegen einen stärkeren Bot spielst.",
    "Der Schwierigkeitsgrad der Spiele, die man mit dem Toon-Express erreicht, hängt von der Gegend ab: Toontown Mitte hat die leichtesten und Donalds Traumland die schwersten.",
    "Bestimmte Spiele, die man mit dem Toon-Express erreicht, kann man nur in einer Gruppe spielen.",
    ),

  TIP_COGHQ : (
    "Du musst deine Bot-Verkleidung vervollständigen, bevor du ein Chef-Gebäude betrittst.",
    "Du kannst auf Bot-Schläger springen, um sie vorübergehend außer Gefecht zu setzen.",
    "Sammle Bot-Verdienste, indem du Bots im Kampf besiegst.",
    "Bots höherer Level bringen mehr Verdienste ein.",
    "Wenn du genügend Bot-Verdienste für eine Beförderung gesammelt hast, suche den Schachermat-VP auf!",
    "Wenn du deine Bot-Verkleidung trägst, kannst du wie ein Bot reden. ",
    "Bis zu acht Toons können sich zusammenschließen, um gegen den Schachermat-VP zu kämpfen.",
    "Der Schachermat-VP sitzt ganz oben im Bot-Hauptquartier.",
    "Folge in Bot-Fabriken den Treppen nach oben, um zum Vorarbeiter zu gelangen.",
    "Jedes Mal, wenn du dich durch die Fabrik durchkämpfst, erhältst du ein Stück deiner Bot-Verkleidung.",
    "Den aktuellen Stand deiner Bot-Verkleidung kannst du in deinem Sticker-Buch nachsehen.",
    "Den aktuellen Stand deiner Verdienste kannst du auf der Verkleidungsseite in deinem Sticker-Buch nachsehen.",
    "Achte darauf, dass du eine volle Ladung Gags und einen vollem Lach-O-Meter hast, bevor du zum VP gehst.",
    "Wenn du befördert wirst, wird deine Bot-Verkleidung auf den aktuellen Stand gebracht. ",
    "Du musst den Vorarbeiter der Fabrik besiegen, um ein Stück der Bot-Verkleidung zu erbeuten.",
    ),
    
  }

FishGenusNames = {
    0 : "Ballonfisch",
    2 : "Katzenfisch",
    4 : "Clownfisch",
    6 : "Gefrierfisch",
    8 : "Seestern",
    10 : "Löchrige Makrele",
    12 : "Hundshai",
    14 : "Amoraal",
    16 : "Ammenhai",
    18 : "Königskrabbe",
    20 : "Mondfisch",
    22 : "Seepferdchen",
    24 : "Beckenhai",
    26 : "Bäracuda",
    28 : "Mordforelle",
    30 : "Kaviarstimmer",
    32 : "Erdnussbutter & Geleequalle",
    34 : "Teufelsrochen",
    }

FishSpeciesNames = {
    0 : ( "Ballonfisch",
          "Heißluftballonfisch",
          "Wetterballonfisch",
          "Wasserballonfisch",
          "Roter Ballonfisch",
          ),
    2 : ( "Katzenfisch",
          "Siamesischer Katzenfisch",
          "Streunender Katzenfisch",
          "Tigerkatzenfisch",
          "Katerfisch",
          ),
    4 : ( "Clownfisch",
          "Trauriger Clownfisch",
          "Partyclownfisch",
          "Zirkusclownfisch",
          ),
    6 : ( "Gefrierfisch",
          ),
    8 : ( "Seestern",
          "Fünf-Stern",
          "Schlagersternchen",
          "Leuchtender Seestern",
          "Nord-Seestern",
          ),
    10 : ( "Löchrige Makrele",
           ),
    12 : ( "Hundshai",
           "Bulldoggenhai",
           "Hotdoghai",
           "Dalmatinerhai",
           "Welpenhai",
           ),
    14 : ( "Amoraal",
           "Elektrischer Amoraal",
           ),
    16 : ( "Ammenhai",
           "Hebammenhai",
           "Zündflammenhai",
           ),
    18 : ( "Königskrabbe",
           "Alaska-Königskrabbe",
           "Altkönigskrabbe",
           ),
    20 : ( "Mondfisch",
           "Vollmondfisch",
           "Halbmondfisch",
           "Neumondfisch",
           "Zunehmender Mondfisch",
           "Wonnemondfisch",
           ),
    22 : ( "Seepferdchen",
           "Schaukel-Seepferdchen",
           "Lipizzaner-Seepferdchen",
           "Araber-Seepferdchen",
           ),
    24 : ( "Beckenhai",
           "Planschbeckenhai",
           "Schwimmbeckenhai",
           "Olympiabeckenhai",
           ),
    26 : ( "Braunbäracuda",
           "Schwarzbäracuda",
           "Koalabäracuda",
           "Honigbäracuda",
           "Eisbäracuda",
           "Pandabäracuda",
           "Lippenbäracuda",
           "Grizzlybäracuda",
           ),
    28 : ( "Mordforelle",
           "Piratenkapitänforelle",
           "Gemeine Mordforelle",
           ),
    30 : ( "Klavierstint",
           "Konzertflügelstint",
           "Flügelstint",
           "Pianostint",
           "Mechanischer Klavierstint",
           ),
    32 : ( "Erdnussbutter & Geleequalle",
           "Erdnussbutter & Quittengeleequalle",
           "Grobe Erdnussbutter & Geleequalle",
           "Erdnussbutter & Erdbeergeleequalle",
           "Erdnussbutter & Traubengeleequalle",
           ),
    34 : ( "Teufelsrochen",
           ),
    }

FishFirstNames = (
    "",
    "Angelo",
    "Arktis",
    "Baby",
    "Bermuda",
    "Big",
    "Dorsch",
    "Bläschen",
    "Meister",
    "Zuckerle",
    "Käpt'n",
    "Winzig",
    "Döbel",
    "Korall",
    "Doktor",
    "Körnchen",
    "Kaiser",
    "Beißer",
    "Dick",
    "Forelli",
    "Flipper",
    "Flunder",
    "Tüpfel",
    "Schatzi",
    "Hans",
    "König",
    "Kleini",
    "Wels",
    "Fräulein",
    "Herr",
    "Pippi",
    "Rosa",
    "Prinz",
    "Prinzessin",
    "Professor",
    "Schnapp",
    "Königin",
    "Regenbogen",
    "Rochen",
    "Rosi",
    "Ruben",
    "Salzer",
    "Scholle",
    "Sandy",
    "Schupp",
    "Haichen",
    "Sir",
    "Hüpfer",
    "Schleicher",
    "Schnapper",
    "Pünktchen",
    "Stachel",
    "Schecki",
    "Star",
    "Sugar",
    "Super",
    "Tiger",
    "Winzling",
    "Bartel",
    )

FishLastPrefixNames = (
    "",
    "Strand",
    "Schwarz",
    "Blau",
    "Keiler",
    "Bulle",
    "Katze",
    "Tief",
    "Doppel",
    "Ost",
    "Fantasie",
    "Flockig",
    "Flach",
    "Frisch",
    "Riesen",
    "Gold",
    "Golden",
    "Grau",
    "Grün",
    "Schwein",
    "Geplapper",
    "Gelee",
    "Dame",
    "Leder",
    "Zitrone",
    "Lang",
    "Nord",
    "Ozean",
    "Okto",
    "Öl",
    "Perle",
    "Bausch",
    "Rot",
    "Band",
    "Fluss",
    "Fels",
    "Rubin",
    "Ruder",
    "Salz",
    "Meer",
    "Silber",
    "Schnorchel",
    "Seezunge",
    "Süd",
    "Spitz",
    "Gischt",
    "Schwert",
    "Tiger",
    "Dreifach",
    "Tropisch",
    "Tunfisch",
    "Welle",
    "Schwach",
    "West",
    "Weiß",
    "Gelb",
    )

FishLastSuffixNames = (
    "",
    "ball",
    "flussbarsch",
    "bauch",
    "wanze ",
    "dieb",
    "butter",
    "klaue",
    "pfuscher",
    "krabbe",
    "unker",
    "trommel",
    "finne",
    "fisch",
    "platscher",
    "flosse",
    "geist",
    "grunzer",
    "kopf",
    "schnorchler",
    "springer",
    "makrele",
    "mond",
    "maul ",
    "barbe",
    "hals",
    "nase",
    "barsch",
    "grobian",
    "läufer",
    "segel",
    "hai",
    "muschel",
    "seide",
    "schleim",
    "schnäpper",
    "gestank",
    "schwanz",
    "kröte",
    "forelle",
    "wasser",
    )


CogPartNames = (
    "Linker Oberschenkel", "Linker Unterschenkel", "Linker Fuß",
    "Rechter Oberschenkel", "Rechter Unterschenkel", "Rechter Fuß",
    "Linke Schulter",  "Rechte Schulter", "Brust", "Gesundheitsmesser", "Becken",
    "Linker Oberarm",  "Linker Unterarm", "Linke Hand",
    "Rechter Oberarm", "Rechter Unterarm", "Rechte Hand",
    )

CogPartNamesSimple = (
    "Oberkörper",
    )

# SellbotLegFactorySpec.py

SellbotLegFactorySpecMainEntrance = "Haupteingang"
SellbotLegFactorySpecLobby = "Lobby"
SellbotLegFactorySpecLobbyHallway = "Korridor Lobby"
SellbotLegFactorySpecGearRoom = "Getrieberaum"
SellbotLegFactorySpecBoilerRoom = "Kesselraum"
SellbotLegFactorySpecEastCatwalk = "Östlicher Laufsteg"
SellbotLegFactorySpecPaintMixer = "Farbmischer"
SellbotLegFactorySpecPaintMixerStorageRoom = "Farbmischer-Lagerraum"
SellbotLegFactorySpecWestSiloCatwalk = "Westsilo-Laufsteg"
SellbotLegFactorySpecPipeRoom = "Rohrleitungsraum"
SellbotLegFactorySpecDuctRoom = "Leitungskanalraum"
SellbotLegFactorySpecSideEntrance = "Seiteneingang"
SellbotLegFactorySpecStomperAlley = "Stampfer-Gang"
SellbotLegFactorySpecLavaRoomFoyer = "Foyer Lava-Raum "
SellbotLegFactorySpecLavaRoom = "Lava-Raum"
SellbotLegFactorySpecLavaStorageRoom = "Lava-Lagerraum"
SellbotLegFactorySpecWestCatwalk = "Westlicher Laufsteg"
SellbotLegFactorySpecOilRoom = "Ölraum"
SellbotLegFactorySpecLookout = "Beobachtungsstand"
SellbotLegFactorySpecWarehouse = "Lagerhaus"
SellbotLegFactorySpecOilRoomHallway = "Korridor Ölraum"
SellbotLegFactorySpecEastSiloControlRoom = "Ostsilo-Kontrollraum"
SellbotLegFactorySpecWestSiloControlRoom = "Westsilo-Kontrollraum"
SellbotLegFactorySpecCenterSiloControlRoom = "Mittelsilo-Kontrollraum"
SellbotLegFactorySpecEastSilo = "Ostsilo"
SellbotLegFactorySpecWestSilo = "Westsilo"
SellbotLegFactorySpecCenterSilo = "Mittelsilo"
SellbotLegFactorySpecEastSiloCatwalk = "Ostsilo-Laufsteg"
SellbotLegFactorySpecWestElevatorShaft = "West-Aufzugs-Schacht"
SellbotLegFactorySpecEastElevatorShaft = "Ost-Aufzugs-Schacht"
