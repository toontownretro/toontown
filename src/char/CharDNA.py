"""AvatarDNA module: contains the methods and definitions for describing
multipart actors with a simple class"""

import random
from toontown.toonbase.ToontownModules import *
from direct.directnotify.DirectNotifyGlobal import *
import random
from direct.distributed.PyDatagram import PyDatagram
from direct.distributed.PyDatagramIterator import PyDatagramIterator
from otp.avatar import AvatarDNA

notify = directNotify.newCategory("CharDNA")

# char defines
charTypes = [ "mk", "vmk", "mn", "wmn", "g", "sg", "d", "fd", "dw", "p", "wp", "cl", "dd", "shdd", "ch", "da", "pch", "jda" ]
# ...mickey, vampire mickey, minnie, Witch minnie, goofy, donald, donald-wheel, pluto, Clarabelle, Daisy, Chip, Dale

class CharDNA(AvatarDNA.AvatarDNA):
    """CharDNA class: contains methods for describing avatars with a
    simple class. The CharDNA class may be converted to lists of strings
    for network transmission. Also, CharDNA objects can be constructed
    from lists of strings recieved over the network. Some examples are in
    order.

        # create a character's dna (defaults to Mickey)
        dna = AvatarDNA()
        dna.newChar()

        # create a specific char by passing in an identifier
        # string (see 'char types' above)
        dna = AvatarDNA()
        dna.newChar('mk')
        # mickey

    """
    # special methods

    def __init__(self, str=None, type=None, dna=None, r=None, b=None, g=None):
        """__init__(self, string=None, string=None, string()=None, float=None,
        float=None, float=None)
        CharDNA contructor - see class comment for usage
        """
        # have they passed in a stringified DNA object?
        if (str != None):
            self.makeFromNetString(str)
        # have they specified what type of DNA?
        elif (type != None):
            if (type == 'c'):  # Char
                self.newChar(dna)
            else:
                # Invalid type
                assert(0)
        else:
            # mark DNA as undefined
            self.type = 'u'

    def __str__(self):
        """__str__(self)
        Avatar DNA print method
        """
        if (self.type == 'c'):
            return "type = char, name = %s" % self._name
        else:
            return "type undefined"


    # stringification methods
    def makeNetString(self):
        dg = PyDatagram()
        dg.addFixedString(self.type, 1)
        if (self.type == 'c'):  # Char
            dg.addFixedString(self._name, 2)
        elif (self.type == 'u'):
            notify.error("undefined avatar")
        else:
            notify.error("unknown avatar type: ", self.type)

        return dg.getMessage()

    def makeFromNetString(self, string):
        dg=PyDatagram(string)
        dgi=PyDatagramIterator(dg)
        self.type = dgi.getFixedString(1)
        if (self.type == 'c'):  # Char
            self._name = sgi.getFixedString(2)
        else:
            notify.error("unknown avatar type: ", self.type)

        return None

    def __defaultChar(self):
        """__defaultChar(self)
        Make a default character dna
        """
        self.type = 'c'
        self._name = charTypes[0]

    def newChar(self, name = None):
        """newChar(self, string = None)
        Make the dna for the given character name,
        or Mickey if not specified
        """
        if (name == None):
            self.__defaultChar()
        else:
            self.type = 'c'
            if (name in  charTypes):
                self._name = name
            else:
                notify.error("unknown avatar type: %s" % (name))

    def getType(self):
        """getType(self)
        Return which type of actor this dna represents.
        """
        if (self.type == 'c'):
            #char type
            type = self.getCharName()
        else:
            notify.error("Invalid DNA type: ", self.type)

        return type

    # char helper funcs
    def getCharName(self):
        """getCharName(self)
        Return the type of the character as a string
        """
        if (self._name == "mk"):
            return("mickey")
        elif(self._name=="vmk"):
            return("vampire_mickey")
        elif (self._name == "mn"):
            return("minnie")
        elif (self._name == "wmn"):
            return("witch_minnie")
        elif (self._name == "g"):
            return("goofy")
        elif (self._name == "sg"):
            return("super_goofy")
        elif (self._name == "d"):
            return("donald")
        elif (self._name == "dw"):
            return("donald-wheel")
        elif (self._name == "fd"):
            return("franken_donald")
        elif (self._name == "dd"):
            return("daisy")
        elif (self._name == "shdd"):
            return("sockHop_daisy")
        elif (self._name == "p"):
            return("pluto")
        elif( self._name == "wp"):
            return("western_pluto")
        elif (self._name == "cl"):
            return("clarabelle")
        elif (self._name == "ch"):
            return("chip")
        elif (self._name == "da"):
            return("dale")
        elif (self._name == "pch"):
            return("police_chip")
        elif (self._name == "jda"):
            return("jailbird_dale")
        else:
            notify.error("unknown char type: ", self._name)
