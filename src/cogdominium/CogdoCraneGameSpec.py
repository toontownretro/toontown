from toontown.coghq.SpecImports import *

GlobalEntities = {
    # LEVELMGR
    1000: {
        'type': 'levelMgr',
        'name': 'LevelMgr',
        'comment': '',
        'parentEntId': 0,
        'modelFilename': 'phase_10/models/cogHQ/EndVault.bam',
        }, # end entity 1000
    # EDITMGR
    1001: {
        'type': 'editMgr',
        'name': 'EditMgr',
        'parentEntId': 0,
        'insertEntity': None,
        'removeEntity': None,
        'requestNewEntity': None,
        'requestSave': None,
        }, # end entity 1001
    # ZONE
    0: {
        'type': 'zone',
        'name': 'UberZone',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': '',
        'visibility': [],
        }, # end entity 0
    # COGDOCRANECOGSETTINGS
    10001: {
        'type': 'cogdoCraneCogSettings',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 0,
        'CogFlyAwayDuration': 4.0,
        'CogFlyAwayHeight': 50.0,
        'CogMachineInteractDuration': 2.0,
        'CogSpawnPeriod': 10.0,
        'CogWalkSpeed': 12.07161265369133
        },
    # COGDOCRANEGAMESETTINGS
    10000: {
        'type': 'cogdoCraneGameSettings',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 0,
        'EmptyFrictionCoef': 0.1,
        'GameDuration': 180.0,
        'Gravity': -32,
        'MagnetMass': 1.0,
        'MoneyBagGrabHeight': -4.1,
        'RopeLinkMass': 1.0
        }, # end entity 10000
    }

Scenario0 = {
    }

levelSpec = {
    'globalEntities': GlobalEntities,
    'scenarios': [
        Scenario0,
        ],
    }
