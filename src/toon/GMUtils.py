from toontown.toonbase import TTLocalizer


def testGMIdentity(name=''):
    if name.find('$')!=-1:
        return True
    else:
        return False
        
def handleGMName(name=''):
    """ Parse the name for symbols that will get replaced by prefixes and icons """
    if name.find('$000')!=-1:
        prefix = TTLocalizer.GM_1
    elif name.find('$001')!=-1:
        prefix = TTLocalizer.GM_2
    elif name.find('$002')!=-1:
        prefix = TTLocalizer.GM_3
    elif name.find('$003')!=-1:
        prefix = TTLocalizer.GM_4
    else:
        # This is suspicious
        prefix = ''
            
    gmName = prefix + ' ' + name.lstrip('$0123456789')
    
    return gmName
    
def getGMType(name=''):
    if (name.find('$000')!=-1) or (name.find(TTLocalizer.GM_1)==0):
        return TTLocalizer.GM_1
    elif (name.find('$001')!=-1) or (name.find(TTLocalizer.GM_2)==0):
        return TTLocalizer.GM_2
    elif (name.find('$002')!=-1) or (name.find(TTLocalizer.GM_3)==0):
        return TTLocalizer.GM_3
    elif (name.find('$003')!=-1) or (name.find(TTLocalizer.GM_4)==0):
        return TTLocalizer.GM_4
    else:
        # This is suspicious
        return ''