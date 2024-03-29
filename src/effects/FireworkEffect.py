from toontown.toonbase.ToontownModules import *
from direct.interval.IntervalGlobal import *
import random

from toontown.effects.FireworkGlobals import *
from toontown.effects.Glow import Glow
from toontown.effects.GlowTrail import GlowTrail
from toontown.effects.SparksTrail import SparksTrail
from toontown.effects.SparksTrailLong import SparksTrailLong
from toontown.effects.PolyTrail import PolyTrail
from toontown.effects.FlashEffect import FlashEffect
from toontown.effects.BlastEffect import BlastEffect
from toontown.effects.FireworkSparkles import FireworkSparkles
from toontown.effects.SimpleSparkles import SimpleSparkles
from toontown.effects.PeonyEffect import PeonyEffect
from toontown.effects.RayBurst import RayBurst
from toontown.effects.StarBurst import StarBurst
from toontown.effects.ChrysanthemumEffect import ChrysanthemumEffect
from toontown.effects.RingEffect import RingEffect
from toontown.effects.NoiseSparkles import NoiseSparkles
from toontown.effects.SkullBurst import SkullBurst
from toontown.effects.SkullFlash import SkullFlash
from toontown.effects.TrailExplosion import TrailExplosion
from toontown.effects.IceCream import IceCream

trailSfxNames = ['phase_4/audio/sfx/firework_whistle_01.mp3',
                 'phase_4/audio/sfx/firework_whistle_02.mp3']
burstSfxNames = ['phase_4/audio/sfx/firework_explosion_01.mp3',
                 'phase_4/audio/sfx/firework_explosion_02.mp3',
                 'phase_4/audio/sfx/firework_explosion_03.mp3',
                 'phase_4/audio/sfx/firework_distance_01.mp3',
                 'phase_4/audio/sfx/firework_distance_02.mp3',
                 'phase_4/audio/sfx/firework_distance_03.mp3']

class FireworkEffect(NodePath):

    # initialize the firework effect and its attributes:
    # trailEffectId   - specifies the firework's trail effect type
    # burstEffectId   - specifies the firework's burst effect type
    # velocity        - initial velocity for shooting firework
    # scale           - scale of explosion
    # primaryColor    - firework's primary color
    # secondaryColor  - optional secondary firework's color
    # burstDelay      - delay until explosion (duration of trail)
    # --------------------------------------------------------------------
    def __init__(self, burstEffectId, trailEffectId=FireworkTrailType.Default,
                 velocity=Vec3(0,0,500), scale=1.0,
                 primaryColor=Vec4(1,1,1,1), secondaryColor=None,
                 burstDelay=1.25):
        NodePath.__init__(self, "FireworkEffect")

        self.burstTypeId = burstEffectId
        self.trailTypeId = trailEffectId

        self.velocity = velocity
        # Scale down for toontown
        self.scale = scale/7
        self.primaryColor = primaryColor
        self.secondaryColor = secondaryColor
        if not self.secondaryColor:
            self.secondaryColor = self.primaryColor
        self.burstDelay = burstDelay
        self.gravityMult = 1.0

        self.fireworkMainIval = None
        self.trailEffectsIval = None
        self.burstEffectsIval = None

        self.effectsNode = self.attachNewNode('fireworkEffectsNode')
        self.trailEffects = []
        self.burstEffects = []

        self.trailSfx = []
        for audio in trailSfxNames:
            audio = loader.loadSfx(audio)
            audio.setVolume(0.075)
            self.trailSfx.append(audio)
        self.burstSfx = []
        for audio in burstSfxNames:
            audio = loader.loadSfx(audio)
            audio.setVolume(0.8)
            self.burstSfx.append(audio)

    def play(self):
        self.getFireworkMainIval().start()

    def getFireworkMainIval(self):
        self.effectsNode.setPos(0,0,0)
        if not self.fireworkMainIval:
            self.fireworkMainIval = Parallel()
            self.fireworkMainIval.append(self.getTrailEffectsIval())
            self.fireworkMainIval.append(Sequence(Wait(self.burstDelay),
                                                  Func(self.cleanupTrailEffects),
                                                  self.getBurstEffectsIval(),
                                                  Func(self.cleanupBurstEffects),
                                                  Func(self.cleanupEffect)))
        return self.fireworkMainIval

    # TRAIL EFFECTS
    ######################################################################
    def getTrailEffectsIval(self):
        if not self.trailEffectsIval:

            if self.trailTypeId is None:
                # if trail is not needed, use velocity as explosion's position
                self.effectNode.setPos(self.velocity)
                self.trailEffectsIval = Wait(self.burstDelay)
                return self.trailEffectsIval

            self.trailEffectsIval = Parallel()

            self.trailEffectsIval.append(ProjectileInterval(self.effectsNode,
                                                            startVel = self.velocity,
                                                            duration = self.burstDelay,
                                                            gravityMult = self.gravityMult))
            if self.trailTypeId is None:
                return self.trailEffectsIval

            # Add trail Sound Interval
            self.trailEffectsIval.append(Func(random.choice(self.trailSfx).play))

            # For low effects settings do a simple trail
##            if base.options.getSpecialEffectsSetting() == base.options.SpecialEffectsLow:
            # Config variable toontown-sfx-setting 0 = Low Special Effect Setting
            # Config variable toontown-sfx-setting 1 = Medium Special Effect Setting
            # Config variable toontown-sfx-setting 2 = High Special Effect Setting
            if (ConfigVariableInt('toontown-sfx-setting', 1).getValue() == 0):
                if self.trailTypeId != FireworkTrailType.LongGlowSparkle:
                    self.trailTypeId = FireworkTrailType.Default

            # Default - basic glow
            # --------------------------------------------------------------------
            if (self.trailTypeId == FireworkTrailType.Default):
                glowEffect = Glow.getEffect()
                if glowEffect:
                    glowEffect.reparentTo(self.effectsNode)
                    glowEffect.setColorScale(Vec4(1,1,1,1))
                    glowEffect.setScale(10.0)
                    self.trailEffects.append(glowEffect)
                    self.trailEffectsIval.append(Func(glowEffect.startLoop))

            # Polygonal
            # --------------------------------------------------------------------
            elif (self.trailTypeId == FireworkTrailType.Polygonal):
                r = 0.75
                mColor = Vec4(1,1,1,1)
                vertex_list = [Vec4 (r, 0.0, r, 1.0),
                               Vec4 (r, 0.0, -r, 1.0),
                               Vec4 (-r, 0.0, -r, 1.0),
                               Vec4 (-r, 0.0, r, 1.0),
                               Vec4 (r, 0.0, r, 1.0)]
                motion_color = [mColor,mColor,mColor,mColor,mColor]
                trailEffect=PolyTrail(None, vertex_list, motion_color, .5)
                trailEffect.setUnmodifiedVertexColors(motion_color)
                trailEffect.reparentTo(self.effectsNode)
                trailEffect.motion_trail.geom_node_path.setTwoSided(False)
                trailEffect.setBlendModeOn()
                trailEffect.setLightOff()
                self.trailEffects.append(trailEffect)
                self.trailEffectsIval.append(Func(trailEffect.beginTrail))

            # Glow - glowing particle trail
            # --------------------------------------------------------------------
            elif (self.trailTypeId == FireworkTrailType.Glow):
                trailEffect=GlowTrail.getEffect()
                if trailEffect:
                    trailEffect.reparentTo(self.effectsNode)
                    trailEffect.setEffectScale(self.scale*0.75)
                    trailEffect.setEffectColor(Vec4(1,1,1,1))
                    trailEffect.setLifespan(0.25)
                    self.trailEffects.append(trailEffect)
                    self.trailEffectsIval.append(Func(trailEffect.startLoop))

            # Sparkle - sparkles
            # --------------------------------------------------------------------
            elif (self.trailTypeId == FireworkTrailType.Sparkle):
                trailEffect=SparksTrail.getEffect()
                if trailEffect:
                    trailEffect.reparentTo(self.effectsNode)
                    trailEffect.setEffectScale(self.scale)
                    trailEffect.setEffectColor(Vec4(1,1,1,1))
                    self.trailEffects.append(trailEffect)
                    self.trailEffectsIval.append(Func(trailEffect.startLoop))

            # GlowSparkle - basic glow and sparkles
            # --------------------------------------------------------------------
            elif (self.trailTypeId == FireworkTrailType.GlowSparkle):
                glowEffect = Glow.getEffect()
                if glowEffect:
                    glowEffect.reparentTo(self.effectsNode)
                    glowEffect.setColorScale(Vec4(1,1,1,1))
                    glowEffect.setScale(15.0)
                    self.trailEffects.append(glowEffect)
                    self.trailEffectsIval.append(Func(glowEffect.startLoop))
                trailEffect=SparksTrail.getEffect()
                if trailEffect:
                    trailEffect.reparentTo(self.effectsNode)
                    trailEffect.setEffectScale(self.scale)
                    trailEffect.setEffectColor(Vec4(1,1,1,1))
                    self.trailEffects.append(trailEffect)
                    self.trailEffectsIval.append(Func(trailEffect.startLoop))

            # LongSparkle
            # --------------------------------------------------------------------
            elif (self.trailTypeId == FireworkTrailType.LongSparkle):
                trailEffect=SparksTrailLong.getEffect()
                if trailEffect:
                    trailEffect.reparentTo(self.effectsNode)
                    trailEffect.setEffectScale(self.scale)
                    trailEffect.setEffectColor(Vec4(1,1,1,1))
                    trailEffect.setLifespan(4.0)
                    self.trailEffects.append(trailEffect)
                    self.trailEffectsIval.append(Func(trailEffect.startLoop))

            # LongGlowSparkle
            # --------------------------------------------------------------------
            elif (self.trailTypeId == FireworkTrailType.LongGlowSparkle):
                trailEffect=SparksTrailLong.getEffect()
                if trailEffect:
                    trailEffect.reparentTo(self.effectsNode)
                    trailEffect.setEffectScale(self.scale)
                    trailEffect.setEffectColor(self.secondaryColor)
                    trailEffect.setLifespan(3.5)
                    self.trailEffects.append(trailEffect)
                    self.trailEffectsIval.append(Func(trailEffect.startLoop))
                # Medium setting
                if (ConfigVariableInt('toontown-sfx-setting', 1).getValue() >= 1):
                    trailEffect=GlowTrail.getEffect()
                    if trailEffect:
                        trailEffect.reparentTo(self.effectsNode)
                        trailEffect.setEffectScale(self.scale)
                        trailEffect.setEffectColor(self.primaryColor)
                        trailEffect.setLifespan(1.0)
                        self.trailEffects.append(trailEffect)
                        self.trailEffectsIval.append(Func(trailEffect.startLoop))


        return self.trailEffectsIval

    # BURST EFFECTS
    ######################################################################
    def getBurstEffectsIval(self):
        if not self.burstEffectsIval:
            self.burstEffectsIval = Parallel()

            if self.burstTypeId is None:
                return self.burstEffectsIval

            # Add burst Sound Interval
            self.burstEffectsIval.append(Wait(0.5))
            self.burstEffectsIval.append(Func(random.choice(self.burstSfx).play))

            # basic flash effect
            flash = FlashEffect()
            flash.reparentTo(self.effectsNode)
            flash.setEffectColor(self.primaryColor)
            flash.setScale(1200*self.scale)
            flash.fadeTime = .5
            self.burstEffectsIval.append(flash.getTrack())
            self.burstEffects.append(flash)

            # inside light blasts
            primaryBlast = BlastEffect()
            primaryBlast.reparentTo(self.effectsNode)
            primaryBlast.setScale(100*self.scale)
            primaryBlast.setEffectColor(Vec4(1,1,1,1))
            primaryBlast.fadeTime = 0.75
            self.burstEffectsIval.append(primaryBlast.getTrack())
            self.burstEffects.append(primaryBlast)

            # Medium
            if (ConfigVariableInt('toontown-sfx-setting', 1).getValue() >= 1):
                secondaryBlast = BlastEffect()
                secondaryBlast.reparentTo(self.effectsNode)
                secondaryBlast.setScale(250*self.scale)
                secondaryBlast.setEffectColor(self.primaryColor)
                secondaryBlast.fadeTime = 0.3
                self.burstEffectsIval.append(secondaryBlast.getTrack())
                self.burstEffects.append(secondaryBlast)

            # TYPE SPECIFIC EFFECTS:

            # Sparkles - basic explosion of sparkles
            # --------------------------------------------------------------------
            if (self.burstTypeId == FireworkBurstType.Sparkles):
                sparkles = FireworkSparkles.getEffect()
                if sparkles:
                    sparkles.reparentTo(self.effectsNode)
                    sparkles.setEffectScale(self.scale)
                    sparkles.setRadius(100*self.scale)
                    sparkles.setEffectColor(self.primaryColor)
                    self.burstEffectsIval.append(sparkles.getTrack())
                    self.burstEffects.append(sparkles)

            # PeonyShell
            # --------------------------------------------------------------------
            elif (self.burstTypeId == FireworkBurstType.PeonyShell):
                explosion = PeonyEffect.getEffect()
                if explosion:
                    explosion.reparentTo(self.effectsNode)
                    explosion.setEffectScale(self.scale)
                    explosion.setEffectColor(self.primaryColor)
                    explosion.startDelay = 0.0
                    self.burstEffectsIval.append(explosion.getTrack())
                    self.burstEffects.append(explosion)

                # Medium
                if (ConfigVariableInt('toontown-sfx-setting', 1).getValue() >= 1):
                    rays = RayBurst()
                    rays.reparentTo(self.effectsNode)
                    rays.setEffectScale(self.scale)
                    rays.setEffectColor(self.primaryColor)
                    self.burstEffectsIval.append(rays.getTrack())
                    self.burstEffects.append(rays)

                # High
                if (ConfigVariableInt('toontown-sfx-setting', 1).getValue() >= 2):
                    sparkles = FireworkSparkles.getEffect()
                    if sparkles:
                        sparkles.reparentTo(self.effectsNode)
                        sparkles.setEffectScale(self.scale)
                        sparkles.setEffectColor(self.primaryColor)
                        sparkles.startDelay = 0.0
                        self.burstEffectsIval.append(sparkles.getTrack())
                        self.burstEffects.append(sparkles)

                # Medium
                if (ConfigVariableInt('toontown-sfx-setting', 1).getValue() >= 1):
                    explosion = PeonyEffect.getEffect()
                    if explosion:
                        explosion.reparentTo(self.effectsNode)
                        explosion.setEffectScale(self.scale *.8)
                        explosion.setEffectColor(self.primaryColor)
                        explosion.startDelay = 0.15
                        explosion.setR(220)
                        self.burstEffectsIval.append(explosion.getTrack())
                        self.burstEffects.append(explosion)

            # PeonyParticleShell
            # --------------------------------------------------------------------
            elif (self.burstTypeId == FireworkBurstType.PeonyParticleShell):
                explosion = StarBurst.getEffect()
                if explosion:
                    explosion.reparentTo(self.effectsNode)
                    explosion.setEffectScale(self.scale)
                    explosion.setEffectColor(self.primaryColor)
                    self.burstEffectsIval.append(explosion.getTrack())
                    self.burstEffects.append(explosion)

                # Medium
                if (ConfigVariableInt('toontown-sfx-setting', 1).getValue() >= 1):
                    rays = RayBurst()
                    rays.reparentTo(self.effectsNode)
                    rays.setEffectScale(self.scale*.75)
                    rays.setEffectColor(self.primaryColor)
                    self.burstEffectsIval.append(rays.getTrack())
                    self.burstEffects.append(rays)

            # PeonyDiademShell
            # --------------------------------------------------------------------
            elif (self.burstTypeId == FireworkBurstType.PeonyDiademShell):
                explosion = StarBurst.getEffect()
                if explosion:
                    explosion.reparentTo(self.effectsNode)
                    explosion.setEffectScale(self.scale)
                    explosion.setEffectColor(self.primaryColor)
                    self.burstEffectsIval.append(explosion.getTrack())
                    self.burstEffects.append(explosion)

                # Medium
                if (ConfigVariableInt('toontown-sfx-setting', 1).getValue() >= 1):
                    rays = RayBurst()
                    rays.reparentTo(self.effectsNode)
                    rays.setEffectScale(self.scale)
                    rays.setEffectColor(self.primaryColor)
                    self.burstEffectsIval.append(rays.getTrack())
                    self.burstEffects.append(rays)

                sparkles = SimpleSparkles.getEffect()
                if sparkles:
                    sparkles.reparentTo(self.effectsNode)
                    sparkles.setEffectScale(self.scale)
                    sparkles.setRadius(100*self.scale)
                    sparkles.setEffectColor(self.secondaryColor)
                    self.burstEffectsIval.append(sparkles.getTrack())
                    self.burstEffects.append(sparkles)

            # ChrysanthemumShell
            # --------------------------------------------------------------------
            elif (self.burstTypeId == FireworkBurstType.ChrysanthemumShell):
                explosion = ChrysanthemumEffect()
                explosion.reparentTo(self.effectsNode)
                explosion.setEffectScale(self.scale)
                explosion.setEffectColor(self.primaryColor)
                self.burstEffectsIval.append(explosion.getTrack())
                self.burstEffects.append(explosion)

                # Medium
                if (ConfigVariableInt('toontown-sfx-setting', 1).getValue() >= 2):
                    sparkles = FireworkSparkles.getEffect()
                    if sparkles:
                        sparkles.reparentTo(self.effectsNode)
                        sparkles.setEffectScale(self.scale*0.8)
                        sparkles.setEffectColor(self.primaryColor)
                        sparkles.startDelay = 0.2
                        self.burstEffectsIval.append(sparkles.getTrack())
                        self.burstEffects.append(sparkles)

            # ChrysanthemymDiademShell
            # --------------------------------------------------------------------
            elif (self.burstTypeId == FireworkBurstType.ChrysanthemumDiademShell):
                explosion = ChrysanthemumEffect()
                explosion.reparentTo(self.effectsNode)
                explosion.setEffectScale(self.scale)
                explosion.setEffectColor(self.primaryColor)
                self.burstEffectsIval.append(explosion.getTrack())
                self.burstEffects.append(explosion)

                sparkles = SimpleSparkles.getEffect()
                if sparkles:
                    sparkles.reparentTo(self.effectsNode)
                    sparkles.setEffectScale(self.scale)
                    sparkles.setRadius(100*self.scale)
                    sparkles.setEffectColor(self.secondaryColor)
                    self.burstEffectsIval.append(sparkles.getTrack())
                    self.burstEffects.append(sparkles)

            # RingShell
            # --------------------------------------------------------------------
            elif (self.burstTypeId == FireworkBurstType.RingShell):
                explosion = RingEffect.getEffect()
                if explosion:
                    explosion.reparentTo(self.effectsNode)
                    explosion.setEffectScale(self.scale)
                    explosion.setEffectColor(self.primaryColor)
                    self.burstEffectsIval.append(explosion.getTrack())
                    self.burstEffects.append(explosion)

            # SaturnShell
            # --------------------------------------------------------------------
            elif (self.burstTypeId == FireworkBurstType.SaturnShell):
                explosion = RingEffect.getEffect()
                if explosion:
                    explosion.reparentTo(self.effectsNode)
                    explosion.setEffectScale(self.scale)
                    explosion.setEffectColor(self.primaryColor)
                    self.burstEffectsIval.append(explosion.getTrack())
                    self.burstEffects.append(explosion)

                sparkles = SimpleSparkles.getEffect()
                if sparkles:
                    sparkles.reparentTo(self.effectsNode)
                    sparkles.setEffectScale(self.scale)
                    sparkles.setRadius(75*self.scale)
                    sparkles.setEffectColor(self.secondaryColor)
                    self.burstEffectsIval.append(sparkles.getTrack())
                    self.burstEffects.append(sparkles)

            # BeeShell
            # --------------------------------------------------------------------
            elif (self.burstTypeId == FireworkBurstType.BeeShell):
                explosion = NoiseSparkles.getEffect()
                if explosion:
                    explosion.reparentTo(self.effectsNode)
                    explosion.setEffectScale(self.scale)
                    explosion.setEffectColor(self.primaryColor)
                    self.burstEffectsIval.append(Sequence(Wait(0.1), explosion.getTrack()))
                    self.burstEffects.append(explosion)

                # Medium
                if (ConfigVariableInt('toontown-sfx-setting', 1).getValue() >= 1):
                    rays = RayBurst()
                    rays.reparentTo(self.effectsNode)
                    rays.setEffectScale(self.scale)
                    rays.setEffectColor(self.primaryColor)
                    self.burstEffectsIval.append(rays.getTrack())
                    self.burstEffects.append(rays)

            # SkullBlast - outward flash explosion in the shape of a skull
            # --------------------------------------------------------------------
            elif (self.burstTypeId == FireworkBurstType.SkullBlast):
                explosion = SkullBurst.getEffect()
                if explosion:
                    explosion.reparentTo(self.effectsNode)
                    explosion.setEffectScale(self.scale)
                    explosion.setEffectColor(self.primaryColor)
                    explosion.startDelay = 0.1
                    self.burstEffectsIval.append(explosion.getTrack())
                    self.burstEffects.append(explosion)

                skullFlash = SkullFlash.getEffect()
                if skullFlash:
                    skullFlash.reparentTo(self.effectsNode)
                    skullFlash.setScale(650*self.scale)
                    skullFlash.fadeTime = 0.75
                    skullFlash.startDelay = 0.08
                    self.burstEffectsIval.append(skullFlash.getTrack())
                    self.burstEffects.append(skullFlash)

                # Medium
                if (ConfigVariableInt('toontown-sfx-setting', 1).getValue() >= 1):
                    rays = RayBurst()
                    rays.reparentTo(self.effectsNode)
                    rays.setEffectScale(self.scale)
                    rays.setEffectColor(self.primaryColor)
                    self.burstEffectsIval.append(rays.getTrack())
                    self.burstEffects.append(rays)

                # High
                if (ConfigVariableInt('toontown-sfx-setting', 1).getValue() >= 2):
                    sparkles = FireworkSparkles.getEffect()
                    if sparkles:
                        sparkles.reparentTo(self.effectsNode)
                        sparkles.setEffectScale(self.scale)
                        sparkles.setRadius(400*self.scale)
                        sparkles.startDelay = 0.1
                        sparkles.setEffectColor(self.secondaryColor)
                        self.burstEffectsIval.append(sparkles.getTrack())
                        self.burstEffects.append(sparkles)

            # TrailExplosion - explosion of 3-5 trail effects
            # --------------------------------------------------------------------
            elif (self.burstTypeId == FireworkBurstType.TrailExplosion):
                explosion = TrailExplosion.getEffect()
                if explosion:
                    explosion.reparentTo(self.effectsNode)
                    explosion.setEffectScale(self.scale)
                    explosion.setEffectColor(self.primaryColor)
                    explosion.numTrails = 3 + ConfigVariableInt('toontown-sfx-setting', 1).getValue()
                    self.burstEffectsIval.append(explosion.getTrack())
                    self.burstEffects.append(explosion)

            elif self.burstTypeId == FireworkBurstType.IceCream:
                explosion = IceCream.getEffect()
                if explosion:
                    explosion.reparentTo(self.effectsNode)
                    explosion.setEffectScale(self.scale)
                    explosion.setEffectColor(self.primaryColor)
                    self.burstEffectsIval.append(explosion.getTrack())
                    self.burstEffects.append(explosion)

        return self.burstEffectsIval

    def cleanupTrailEffects(self):
        if self.trailEffectsIval:
            self.trailEffectsIval.pause()
            self.trailEffectsIval = None
        for effect in self.trailEffects:
            if isinstance(effect, PolyTrail):
                effect.destroy()
                effect = None
            else:
                effect.stopLoop()
                effect = None
        self.trailEffects = []

    def cleanupBurstEffects(self):
        if self.burstEffectsIval:
            self.burstEffectsIval.pause()
            self.burstEffectsIval = None
        for effect in self.burstEffects:
            effect.stop()
            effect = None
        self.burstEffects = []

    def cleanupEffect(self):
        if self.fireworkMainIval:
            self.fireworkMainIval.pause()
            self.fireworkMainIval = None
        self.cleanupTrailEffects()
        self.cleanupBurstEffects()
