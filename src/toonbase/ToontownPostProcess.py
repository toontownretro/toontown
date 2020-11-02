from panda3d.core import Shader, PTA_LVecBase3f, Vec3
from panda3d.core import PostProcess, PostProcessPass, PostProcessEffect, HDREffect, \
    BloomEffect, FXAA_Effect, SSAO_Effect, MotionBlur

#
# Draw world
# Image-space motion blur
# Draw view models
# Post process

class ToontownPostProcess(PostProcess):

    def __init__(self):
        PostProcess.__init__(self)

        self.hdr = None
        self.bloom = None
        self.fxaa = None
        self.ssao = None
        self.mb = None

        self.enableHDR = False
        self.enableBloom = True
        self.enableSSAO = False
        self.enableFXAA = False
        self.enableMB = True

        self.flashEnabled = False
        self.flashColor = PTA_LVecBase3f.emptyArray(1)
        self.setFlashColor(Vec3(0))

    def update(self):
        PostProcess.update(self)
        if self.mb:
            self.mb.update()

    def enableFlash(self, color = Vec3(0)):
        self.flashEnabled = True
        self.setFlashColor(color)

    def setFlashColor(self, color):
        self.flashColor.setElement(0, color)

    def disableFlash(self):
        self.flashEnabled = False
        self.setFlashColor(Vec3(0))

    def cleanup(self):
        if self.hdr:
            self.hdr.shutdown()
            self.removeEffect(self.hdr)
        self.hdr = None

        if self.bloom:
            self.bloom.shutdown()
            self.removeEffect(self.bloom)
        self.bloom = None

        if self.fxaa:
            self.fxaa.shutdown()
            self.removeEffect(self.fxaa)
        self.fxaa = None

        if self.ssao:
            self.ssao.shutdown()
            self.removeEffect(self.ssao)
        self.ssao = None

        if self.mb:
            self.mb.shutdown()
        self.mb = None

    def setup(self):
        self.cleanup()

        textures = {"sceneColorSampler": self.getSceneColorTexture()}

        if self.enableHDR:
            self.hdr = HDREffect(self)
            self.hdr.getHdrPass().setExposureOutput(base.shaderGenerator.getExposureAdjustment())
            self.addEffect(self.hdr)
            #textures["hdrDebug"] = self.hdr.getFinalTexture()

        if self.enableBloom:
            self.bloom = BloomEffect(self)
            self.addEffect(self.bloom)
            textures["bloomSampler"] = self.bloom.getFinalTexture()

        if self.enableFXAA:
            self.fxaa = FXAA_Effect(self)
            self.addEffect(self.fxaa)
            # Replace scene color with FXAA'ed version
            textures["sceneColorSampler"] = self.fxaa.getFinalTexture()

        if self.enableSSAO:
            self.ssao = SSAO_Effect(self)
            self.addEffect(self.ssao)
            textures["aoSampler"] = self.ssao.getFinalTexture()

        if self.enableMB:
            self.mb = MotionBlur(self.getOutput())
            self.mb.setSceneCamera(base.cam)
            self.mb.setup()
            # sort value of 2 to do motion blur *after* the main scene,
            # which is sort 1
            self.addCamera(self.mb.getCamera(), 1)

        finalQuad = self.getScenePass().getQuad()

        vtext = "#version 330\n"
        vtext += "uniform mat4 p3d_ModelViewProjectionMatrix;\n"
        vtext += "in vec4 p3d_Vertex;\n"
        vtext += "in vec4 texcoord;\n"
        vtext += "out vec2 l_texcoord;\n"
        vtext += "void main()\n"
        vtext += "{\n"
        vtext += "  gl_Position = p3d_ModelViewProjectionMatrix * p3d_Vertex;\n"
        vtext += "  l_texcoord = texcoord.xy;\n"
        vtext += "}\n"

        ptext = "#version 330\n"
        ptext += "out vec4 outputColor;\n"
        ptext += "in vec2 l_texcoord;\n"

        for sampler in textures.keys():
            ptext += "uniform sampler2D " + sampler + ";\n"

        if self.flashEnabled:
            ptext += "uniform vec3 flashColor[1];\n"

        ptext += "void main()\n"
        ptext += "{\n"
        ptext += "  outputColor = texture(sceneColorSampler, l_texcoord);\n"
        if self.enableSSAO:
            ptext += "  outputColor.rgb *= texture(aoSampler, l_texcoord).rgb;\n"
        if self.enableBloom:
            ptext += "  outputColor.rgb += texture(bloomSampler, l_texcoord).rgb;\n"
        if self.flashEnabled:
            ptext += "  outputColor.rgb += pow(flashColor[0], vec3(2.2));\n"
        if self.enableSSAO:
            ptext += "  outputColor.rgb = texture(aoSampler, l_texcoord).rgb;\n"
        ptext += "}\n"

        shader = Shader.make(Shader.SL_GLSL, vtext, ptext)
        if not shader:
            return

        finalQuad.setShader(shader)

        for sampler, texture in textures.items():
            finalQuad.setShaderInput(sampler, texture)

        if self.flashEnabled:
            finalQuad.setShaderInput("flashColor", self.flashColor)
