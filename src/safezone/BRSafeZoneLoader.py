from toontown.toonbase.ToontownModules import *
from direct.interval.IntervalGlobal import *

from . import SafeZoneLoader
from . import BRPlayground
from toontown.battle import BattleParticles

class BRSafeZoneLoader(SafeZoneLoader.SafeZoneLoader):

    # How quickly does the snow alpha fade in and out when we run
    # inside the igloo?
    SnowFadeLerpTime = 2.0

    def __init__(self, hood, parentFSM, doneEvent):
        SafeZoneLoader.SafeZoneLoader.__init__(self, hood, parentFSM, doneEvent)
        self.playgroundClass = BRPlayground.BRPlayground
        self.musicFile = "phase_8/audio/bgm/TB_nbrhood.mid"
        self.activityMusicFile = "phase_8/audio/bgm/TB_SZ_activity.mid"
        self.dnaFile = "phase_8/dna/the_burrrgh_sz.dna"
        self.safeZoneStorageDNAFile = "phase_8/dna/storage_BR_sz.dna"

    def load(self):
        SafeZoneLoader.SafeZoneLoader.load(self)
        self.wind1Sound = base.loader.loadSfx('phase_8/audio/sfx/SZ_TB_wind_1.mp3')
        self.wind2Sound = base.loader.loadSfx('phase_8/audio/sfx/SZ_TB_wind_2.mp3')
        self.wind3Sound = base.loader.loadSfx('phase_8/audio/sfx/SZ_TB_wind_3.mp3')
        self.snow = BattleParticles.loadParticleFile('snowdisk.ptf')
        self.snow.setPos(0, 0, 5)  # start the snow slightly above the camera
        self.snowRender = self.geom.attachNewNode('snowRender')
        self.snowRender.setDepthWrite(0)
        self.snowRender.setBin('fixed', 1)
        self.snowFade = None

    def unload(self):
        del self.wind1Sound
        del self.wind2Sound
        del self.wind3Sound
        del self.snow
        del self.snowRender
        SafeZoneLoader.SafeZoneLoader.unload(self)

    def enter(self, requestStatus):
        SafeZoneLoader.SafeZoneLoader.enter(self, requestStatus)
        self.snow.start(camera, self.snowRender)
        self.accept('enterigloo-interior', self.enterIgloo)
        self.accept('exitigloo-interior', self.exitIgloo)

    def exit(self):
        self.ignore('enterigloo-interior')
        self.ignore('exitigloo-interior')
        self.resetSnowLerp()
        self.snow.cleanup()
        SafeZoneLoader.SafeZoneLoader.exit(self)

    def enterIgloo(self, entry):
        # This would have been called when we ran inside the igloo,
        # but we don't have an igloo any more.  So this never gets
        # called, but the code is allowed to remain in case we do
        # eventually have an indoor area like the igloo again.
        self.fadeOutSnow()

    def exitIgloo(self, entry):
        self.fadeInSnow()

    def resetSnowLerp(self):
        if self.snowFade != None:
            self.snowFade.stop()
            self.snowFade = None

    def fadeInSnow(self):
        # Gradually lerp the snow's alpha back to full.
        self.resetSnowLerp()

        currentScale = self.snowRender.getColorScale()[3]
        ivals = [LerpFunctionInterval(
            self.snowRender.setAlphaScale,
            fromData = currentScale, toData = 1.0,
            duration = self.SnowFadeLerpTime),
                 FunctionInterval(self.snowRender.clearColorScale)]
        self.snowFade = Track(ivals, 'snow-fade')
        self.snowFade.play()

    def fadeOutSnow(self):
        # Gradually lerp the snow's alpha out to nothing.
        self.resetSnowLerp()

        currentScale = self.snowRender.getColorScale()[3]
        ivals = [LerpFunctionInterval(
            self.snowRender.setAlphaScale,
            fromData = currentScale, toData = 0.0,
            duration = self.SnowFadeLerpTime)]
        self.snowFade = Track(ivals, 'snow-fade')
        self.snowFade.play()
