from toontown.toonbase.ToontownModules import Point3
from toontown.toonbase.ToontownModules import Vec3
import copy
from toontown.toonbase import TTLocalizer

__mickeyPaths = {
    # for each node:
    # (
    #   pos, # position of node
    #   (
    #    adjacent node,
    #    adjacent node,
    #    ...
    #   )
    # )
    # TODO: redo these when the safe zone is final
    'a' : (Point3(17, -17, 4.025),
          ('b','e')
           ),
    'b' : (Point3(17.5, 7.6, 4.025),
           ('c','e')
           ),
    'c' : (Point3(85, 11.5, 4.025),
           ('d',)
           ),
    'd' : (Point3(85, -13, 4.025),
           ('a',)
           ),
    'e' : (Point3(-27.5, -5.25, 0.0), # bottom of central steps
           ('a','b','f')
           ),
    'f' : (Point3(-106.15, -4.0, -2.5), # end of bridge (opposite gazebo)
           ('e','g','h','i',)
           ),
    'g' : (Point3(-89.5, 93.5, 0.5), # sidewalk just South of Punchline Pl.
           ('f','h'),
           ),
    'h' : (Point3(-139.95, 1.69, 0.5), # sidewalk in front of Loopy Ln.
           ('f','g','i',)
           ),
    'i' : (Point3(-110.95, -68.57, 0.5), # sidewalk in front of Loopy Ln.
           ('f','h',)
           ),
    }

# note to self: singleton tuple requires comma: (item,)
# this table holds the waypoints between walk nodes,
# if any, the 3 value in for each edge is 0 if raycast
# is not needed, 1 if raycast is needed
__mickeyWaypoints = (
    # from, to, waypoints
    ('a','e',1,[]),
    ('b','e',1,[]),
    ('e','f',1,[Point3(-76.87, -7.85, -1.85),
                Point3(-80.57, -4.0, -1.85),
                ]),
    ('f','g',1,[Point3(-106.62, 28.65, -1.5),]),
    ('g','h',1,[Point3(-128.38, 60.27, 0.5),]),
    #('g','h',1,[Point3(-134.96, 60.34, 0.5),]),
    ('h','f',1,[]),
    ('h','i',1,[Point3(-137.13, -42.79, 0.5),]),
    ('i','f',1,[]),
    )

__minniePaths = {
    # for each node:
    # (
    #   pos, # position of node
    #   (
    #    adjacent node,
    #    adjacent node,
    #    ...
    #   )
    # )
    'a' : (Point3(53.334,71.057,6.525), # in front of horn, near TTCentral entrance
           ('b','r')
           ),
    'b' : (Point3(127.756,58.665,-11.75), # on other side of horn
           ('a','s','c')
           ),
    'c' : (Point3(130.325,15.174,-2.003), # on piano keys
           ('b','d')
           ),
    'd' : (Point3(126.173,7.057,0.522), # higher on piano keys
           ('c','e')
           ),
    'e' : (Point3(133.843,-6.618,4.710), # higher on piano keys
           ('d','f','g','h')
           ),
    'f' : (Point3(116.876,1.119,3.304), # on drum
           ('e')
           ),
    'g' : (Point3(116.271,-41.568,3.304), # on middle drum
           ('e','h')
           ),
    'h' : (Point3(128.983,-49.656,-0.231), # on piano keys
           ('e','g','i','j')
           ),
    'i' : (Point3(106.024,-75.249,-4.498), # on other drum
           ('h')
           ),
    'j' : (Point3(135.016,-93.072,-13.376), # on ground by 2nd horn
           ('h','k','z')
           ),
    'k' : (Point3(123.966,-100.242,-10.879), # on keys for 2nd horn
           ('j','l')
           ),
    'l' : (Point3(52.859,-109.081,6.525), # on other side of 2nd horn
           ('k','m')
           ),
    'm' : (Point3(-32.071,-107.049,6.525), # on other side of Dreamland entrance
           ('l','n')
           ),
    'n' : (Point3(-40.519,-99.685,6.525), # stop at record player
           ('m','o')
           ),
    'o' : (Point3(-40.245,  -88.634,  6.525 ), # further around upper area of safezone
           ('n','p')
           ),
    'p' : (Point3(-66.300,  -62.192,  6.525 ), # near party gatefurther around upper area of safezone
           ('o','q')
           ),
    'q' : (Point3(-66.212,  23.069,  6.525), # further around upper area of safezone
           ('p','r')
           ),
    'r' : (Point3(-18.344,69.532,6.525), # at last turn on upper area of safezone
           ('q','a')
           ),
    's' : (Point3(91.357,44.546,-13.475), # on ground between piano and center area
           ('b','t')
           ),
    't' : (Point3(90.355, 6.279, -13.475), # in center area near piano
           ('s','u')
           ),
    'u' : (Point3(-13.765,42.362,-14.553), # in center area
           ('t','v')
           ),
    'v' : (Point3(-52.627,7.428,-14.553), # in center area opposite piano
           ('u','w')
           ),
    'w' : (Point3(-50.654,-54.879,-14.553), # in center area opposite piano
           ('v','x')
           ),
    'x' : (Point3(-3.711,-81.819,-14.553), # in center area
           ('w','y')
           ),
    'y' : (Point3(90.777, -49.714, -13.475),
           ('z','x')
           ),
    'z' : (Point3(90.059, -79.426, -13.475),
           ('j','y')
           ),
    }

__minnieWaypoints = (
    ('a','b',1,[]),
    ('k','l',1,[]),
    ('b','c',1,[]),
    ('c','d',1,[]),
    ('d','e',1,[]),
    ('e','f',1,[]),
    ('e','g',1,[]),
    ('e','h',1,[]),
    ('g','h',1,[]),
    ('h','i',1,[]),
    ('h','j',1,[]),
    ('s','b',1,[]),
    ('t','u',1,[]), # curb down
    ('x','y',1,[]), # curb up
    )

__goofyPaths = {
    # for each node:
    # (
    #   pos, # position of node
    #   (
    #    adjacent node,
    #    adjacent node,
    #    ...
    #   )
    # )
    'a' : (Point3(64.995,169.665,10.027), # in front of TTCentral entrance
           ('b','q')
           ),
    'b' : (Point3(48.893,208.912,10.027), # by flowers
           ('a','c')
           ),
    'c' : (Point3(5.482,210.479,10.030), # in front of trolley
           ('b','d')
           ),
    'd' : (Point3(-34.153,203.284,10.029), # near construction zone entrance
           ('c','e')
           ),
    'e' : (Point3(-66.656,174.334,10.026), # front construction zone entrance
           ('d','f')
           ),
    'f' : (Point3(-55.994,162.330,10.026), # top of ramp
           ('e','g')
           ),
    'g' : (Point3(-84.554,142.099,0.027), # down below ramp
           ('f','h')
           ),
    'h' : (Point3(-92.215,96.446,0.027), # toward flower bed
           ('g','i')
           ),
    'i' : (Point3(-63.168,60.055,0.027), # in front of flower bed
           ('h','j')
           ),
    'j' : (Point3(-37.637,69.974,0.027), # next to bush
           ('i','k')
           ),
    'k' : (Point3(-3.018,26.157,0.027), # front of Cog HQ entrance
           ('j','l','m')
           ),
    'l' : (Point3(-0.711,46.843,0.027), # next to fountain
           ('k')
           ),
    'm' : (Point3(26.071,46.401,0.027), # next to pond
           ('k','n')
           ),
    'n' : (Point3(30.870,67.432,0.027), # next to bush
           ('m','o')
           ),
    'o' : (Point3(93.903,90.685,0.027), # toward ramp
           ('n','p')
           ),
    'p' : (Point3(88.129,140.575,0.027), # below ramp
           ('o','q')
           ),
    'q' : (Point3(53.988,158.232,10.027), # top of ramp
           ('p','a')
           ),
    }

__goofyWaypoints = (
    # from, to, waypoints
    ('f','g',1,[]),
    ('p','q',1,[])
    )

__goofySpeedwayPaths = {
    # for each node:
    # (
    #   pos, # position of node
    #   (
    #    adjacent node,
    #    adjacent node,
    #    ...
    #   )
    # )
    'a' : (Point3(-9.0,-19.517,-0.323), # near store rear entrance
           ('b','k')
           ),
    'b' : (Point3(-30.047,-1.578,-0.373), # by giant wrenches
           ('a','c')
           ),
    'c' : (Point3(-10.367,49.042,-0.373), # in front of TTC entrance
           ('b','d')
           ),
    'd' : (Point3(38.439,44.348,-0.373), # near car showoff platform
           ('c','e')
           ),
    'e' : (Point3(25.527,-2.395,-0.373), # near giant tires
           ('d','f')
           ),
    'f' : (Point3(-4.043,-59.865,-0.003), # in tunnel to track area
           ('e','g')
           ),
    'g' : (Point3(0.390,-99.475,-0.009), # in front of leaderboard
           ('f','h')
           ),
    'h' : (Point3(21.147,-109.127,-0.013), # near city race track
           ('g','i')
           ),
    'i' : (Point3(5.981,-147.606,-0.013), # near stadium race track
           ('h','j')
           ),
    'j' : (Point3(-24.898,-120.618,-0.013), # near rural race track
           ('i','k')
           ),
    'k' : (Point3(-2.710,-90.315,-0.011), # near tunnel to kart shop
           ('j','a')
           ),
    }

__goofySpeedwayWaypoints = (
    # from, to, waypoints
    ('a','k',1,[]),
    ('k','a',1,[])
    )

__donaldPaths = {
    # for each node:
    # (
    #   pos, # position of node
    #   (
    #    adjacent node,
    #    adjacent node,
    #    ...
    #   )
    # )
    'a' : (Point3(-94.883,-94.024,0.025), # corner near melodyland entrance
           ('b')
           ),
    'b' : (Point3(-13.962,-92.233,0.025), # front of melodyland entrance
           ('a','h')
           ),
    'c' : (Point3(68.417,-91.929,0.025), # by trolley
           ('m','g')
           ),
    'd' : (Point3(68.745,91.227,0.025), # across bed from trolley
           ('k','i')
           ),
    'e' : (Point3(4.047,94.260,0.025), # front of cog hq. entrance
           ('i','j')
           ),
    'f' : (Point3(-91.271,90.987,0.025), # corner near cog hq. entrance
           ('j')
           ),
    'g' : (Point3(43.824,-94.129,0.025), # in front of trolley
           ('c','h')
           ),
    'h' : (Point3(13.905,-91.334,0.025), # near melodyland entrance
           ('b','g')
           ),
    'i' : (Point3(43.062,88.152,0.025), # near cog hq. entrance
           ('d','e')
           ),
    'j' : (Point3(-48.960,88.565,0.025), # near cog hq. entrance
           ('e','f')
           ),
    'k' : (Point3(75.118,  52.840,  -16.620), # north of party gate
           ('d','l')
           ),
    'l' : (Point3(44.677,  27.091,  -15.385 ), # west of party gate
           ('k','m')
           ),
    'm' : (Point3(77.009,  -16.022,  -14.975 ), # south of party gate
           ('l','c')
           ),
    }

__donaldWaypoints = (
    # from, to, waypoints
    ('d','k',1,[]),
    ('k','l',1,[]),
    ('l','m',1,[]),
    ('m', 'c', 1, []),
    ('b','a',1,[Point3(-55.883,-89.0,0.025),]),
    )

__plutoPaths = {
    # for each node:
    # (
    #   pos, # position of node
    #   (
    #    adjacent node,
    #    adjacent node,
    #    ...
    #   )
    # )
    'a' : (Point3(-110.0,-37.8,8.6), # on mound near 'North Pole'
           ('b','c')
           ),
    'b' : (Point3(-11.9,-128.2,6.2), # near entrance to sleet street
           ('a','c')
           ),
    'c' : (Point3(48.9,-14.4,6.2), # near entrance to walrus way
           ('b','a','d')
           ),
    'd' : (Point3(0.25,80.5,6.2), # near entrance to Cog HQ
           ('c','e')
           ),
    'e' : (Point3(-83.3,36.1,6.2), # near the Toon HQ igloo
           ('d','a')
           ),
    }

__plutoWaypoints = (
    ('a','b',1,[Point3(-90.4,-57.2,3.0),
                Point3(-63.6,-79.8,3.0),
                Point3(-50.1,-89.1,6.2),]),
    ('c','a',1,[Point3(-15.6,-25.6,6.2),
                Point3(-37.5,-38.5,3.0),
                Point3(-55.0,-55.0,3.0),
                Point3(-85.0,-46.4,3.0)]),
    ('d','e',0,[Point3(-25.8,60.,6.2),
                Point3(-61.9,64.5,6.2)]),
    ('e','a',1,[Point3(-77.2,28.5,6.2),
                Point3(-76.4,12.0,3.0),
                Point3(-93.2,-21.2,3.0),]),

    )


__daisyPaths = {
    # for each node:
    # (
    #   pos, # position of node
    #   (
    #    adjacent node,
    #    adjacent node,
    #    ...
    #   )
    # )
    'a' : (Point3(64.995,169.665,10.027), # in front of TTCentral entrance
           ('b','q')
           ),
    'b' : (Point3(48.893,208.912,10.027), # by flowers
           ('a','c')
           ),
    'c' : (Point3(5.482,210.479,10.030), # in front of trolley
           ('b','d')
           ),
    'd' : (Point3(-34.153,203.284,10.029), # near construction zone entrance
           ('c','e')
           ),
    'e' : (Point3(-66.656,174.334,10.026), # front construction zone entrance
           ('d','f')
           ),
    'f' : (Point3(-55.994,162.330,10.026), # top of ramp
           ('e','g')
           ),
    'g' : (Point3(-84.554,142.099,0.027), # down below ramp
           ('f','h')
           ),
    'h' : (Point3(-92.215,96.446,0.027), # toward flower bed
           ('g','i')
           ),
    'i' : (Point3(-63.168,60.055,0.027), # in front of flower bed
           ('h','j')
           ),
    'j' : (Point3(-37.637,69.974,0.027), # next to bush
           ('i','k')
           ),
    'k' : (Point3(-3.018,26.157,0.027), # front of Cog HQ entrance
           ('j','l','m')
           ),
    'l' : (Point3(-0.711,46.843,0.027), # next to fountain
           ('k')
           ),
    'm' : (Point3(26.071,46.401,0.027), # next to pond
           ('k','n')
           ),
    'n' : (Point3(30.870,67.432,0.027), # next to bush
           ('m','o')
           ),
    'o' : (Point3(93.903,90.685,0.027), # toward ramp
           ('n','p')
           ),
    'p' : (Point3(88.129,140.575,0.027), # below ramp
           ('o','q')
           ),
    'q' : (Point3(53.988,158.232,10.027), # top of ramp
           ('p','a')
           ),
    }

__daisyWaypoints = (
    # from, to, waypoints
    ('f','g',1,[]),
    ('p','q',1,[])
    )

__chipPaths = {
    # for each node:
    # (
    #   pos, # position of node
    #   (
    #    adjacent node,
    #    adjacent node,
    #    ...
    #   )
    # )
    'a' : (Point3(50.004, 102.725,  0.6), # in front of log tunnel
           ('b','k')),
    'b' : (Point3(-29.552, 112.531,  0.6), # north bridge inner side
           ('c','a')),
    'c' : (Point3(-51.941, 146.155,  0.025), # north bridge outer side
           ('d','b')),
    'd' : (Point3(-212.334, -3.639,  0.025), # in front of golf tunnel
           ('e','c')),
    'e' : (Point3(-143.466, -67.526,  0.025), # west bridge outer side
           ('f','d','i')),
    'f' : (Point3(-107.556, -62.257,  0.025), # west bridge inner side
           ('g','e','j')),
    'g' : (Point3(-43.103, -71.518,  0.2734), # south bridge inner side
           ('h','f','j')),
    'h' : (Point3(-40.605, -125.124,  0.025), # south bridge outer side
           ('i','g')),
    'i' : (Point3(-123.05, -124.542,  0.025), # between south & west bridge
           ('h','e')),
    'j' : (Point3(-40.092, 2.784,  1.268), # SW of gazebo
           ('k','b','f','g')),
    'k' : (Point3(75.295, 26.715,  1.4), # SE of gazebo
           ('a','j')),
    }

__chipWaypoints = (
    ('a','b',1,[]),
    ('a','k',1,[]),
    ('b','c',1,[]),
    ('b','j',1,[]),
    ('c','d',1,[]),
    ('d','e',1,[]),
    ('e','f',1,[]),
    ('e','i',1,[]),
    ('f','g',1,[]),
    ('f','j',1,[]),
    ('g','h',1,[]),
    ('g','j',1,[]),
    ('h','i',1,[]),
    ('j','k',1,[]),
    )

# when Dale is going over a bridge, have him orbit closer
DaleOrbitDistanceOverride = {
    ('b','c') : 2.5,
    ('e','f') : 2.5,
    }

startNode = 'a'

def getPaths(charName, location = 0):
    charName = charName.lower()
    if charName==TTLocalizer.Mickey.lower():
        return __mickeyPaths
    elif charName==TTLocalizer.VampireMickey.lower():
        return __mickeyPaths
    elif charName==TTLocalizer.Minnie.lower():
        return __minniePaths
    elif charName == TTLocalizer.WitchMinnie.lower():
        return __minniePaths
    elif charName==TTLocalizer.Daisy.lower() or charName == TTLocalizer.SockHopDaisy.lower():
        return __daisyPaths
    elif charName==TTLocalizer.Goofy.lower():
        if location == 0:
            return __goofyPaths
        else:
            return __goofySpeedwayPaths
    elif charName==TTLocalizer.SuperGoofy.lower():
        return __goofySpeedwayPaths
    elif charName==TTLocalizer.Donald.lower() or charName == TTLocalizer.FrankenDonald.lower():
        return __donaldPaths
    elif charName==TTLocalizer.Pluto.lower():
        return __plutoPaths
    elif charName==TTLocalizer.WesternPluto.lower():
        return __plutoPaths
    elif charName==TTLocalizer.Chip.lower() or charName == TTLocalizer.PoliceChip.lower():
        return __chipPaths
    elif charName==TTLocalizer.Dale.lower() or charName == TTLocalizer.JailbirdDale.lower():
        return __chipPaths
    elif charName==TTLocalizer.DonaldDock.lower():
        return {'a':(Point3(0,0,0),'a')}
    else:
        #assert 0, "Unknown path information"
        return

def __getWaypointList(paths):
    if paths==__mickeyPaths:
        return __mickeyWaypoints
    elif paths==__minniePaths:
        return __minnieWaypoints
    elif paths==__daisyPaths:
        return __daisyWaypoints
    elif paths==__goofyPaths:
        return __goofyWaypoints
    elif paths==__goofySpeedwayPaths:
        return __goofySpeedwayWaypoints
    elif paths==__donaldPaths:
        return __donaldWaypoints
    elif paths==__plutoPaths:
        return __plutoWaypoints
    elif paths==__chipPaths:
        return __chipWaypoints
    elif paths==__dalePaths:
        return __chipWaypoints
    else:
        assert 0, "Unknown waypoint information"
        
def getNodePos(node, paths):
    assert node in paths
    return paths[node][0]

def getAdjacentNodes(node, paths):
    assert node in paths
    return paths[node][1]

def getWayPoints(fromNode, toNode, paths, wpts = None):
    list = []

    if (fromNode != toNode):
        if wpts == None:
            wpts = __getWaypointList(paths)
        for path in wpts:
            if path[0] == fromNode and path[1] == toNode:
                for point in path[3]:
                    list.append(Point3(point))
                break
            elif path[0] == toNode and path[1] == fromNode:
                # reverse the order of the list
                for point in path[3]:
                    list = [Point3(point)] + list
                break
    return list

def getRaycastFlag(fromNode, toNode, paths):
    result = 0
    if (fromNode != toNode):
        wpts = __getWaypointList(paths)
        for path in wpts:
            if path[0] == fromNode and path[1] == toNode:
                if path[2]:
                    result = 1
                    break
            elif path[0] == toNode and path[1] == fromNode:
                # reverse the order of the list
                if path[2]:
                    result = 1
                    break
    return result

def getPointsFromTo(fromNode, toNode, paths):
    startPoint = Point3(getNodePos(fromNode,paths))
    endPoint = Point3(getNodePos(toNode,paths))
    return [startPoint] + getWayPoints(fromNode, toNode, paths) + [endPoint]

def getWalkDuration(fromNode, toNode, velocity, paths):

    posPoints = getPointsFromTo(fromNode, toNode, paths)

    duration = 0
    for pointIndex in range(len(posPoints) - 1):
        startPoint = posPoints[pointIndex]
        endPoint = posPoints[pointIndex + 1]

        # Calculate the amount of time it will take to walk
        distance = Vec3(endPoint - startPoint).length()
        duration += distance / velocity

    return duration


def getWalkDistance(fromNode, toNode, velocity, paths):
    posPoints = getPointsFromTo(fromNode, toNode, paths)

    retval = 0
    for pointIndex in range(len(posPoints) - 1):
        startPoint = posPoints[pointIndex]
        endPoint = posPoints[pointIndex + 1]

        # Calculate the amount of time it will take to walk
        distance = Vec3(endPoint - startPoint).length()
        retval += distance

    return retval
