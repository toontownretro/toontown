from toontown.coghq.SpecImports import *

GlobalEntities = {
    # LEVELMGR
    1000: {'type': 'levelMgr',
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
    # COGDOBOARDROOMGAMESETTINGS
    10000: {
        'type': 'cogdoBoardroomGameSettings',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 0,
        'TimerScale': 0.5028702719683693
        }, # end entity 10000
    }

Scenario0 = {
    }

levelSpec = {
    'globalEntities': GlobalEntities,
    'scenarios': [
        Scenario0
        ],
    }
