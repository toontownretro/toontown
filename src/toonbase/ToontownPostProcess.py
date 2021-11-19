from panda3d.core import Shader, PTA_LVecBase3f, Vec3, loadPrcFileData, TextNode
from panda3d.core import PostProcess, PostProcessPass, PostProcessEffect, HDREffect, \
    BloomEffect, FXAA_Effect, SSAO_Effect, MotionBlur, PTA_LVecBase2f, AUXTEXTUREBITS_NORMAL, AUXTEXTURE_NORMAL

from direct.gui.DirectGui import *

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

        self.hbaoControls = []
        self.hbaoControlZ = -0.2

        self.camDebugs = []
        self.camDebugZ = -0.2

        self.enableHDR = ConfigVariableBool("hdr-enable", True).getValue()
        self.enableBloom = ConfigVariableBool("bloom-enable", True).getValue()
        self.enableSSAO = ConfigVariableBool("ssao-enable", True).getValue()
        self.enableFXAA = ConfigVariableBool("fxaa-enable", True).getValue()
        self.enableMB = ConfigVariableBool("motion-blur-enable", False).getValue()

        self.flashEnabled = False
        self.flashColor = PTA_LVecBase3f.emptyArray(1)
        self.setFlashColor(Vec3(0))

        self.exposureBias = PTA_LVecBase3f.emptyArray(1)
        self.setExposureBias(1)

        base.accept('f1', self.decExposureBias)
        base.accept('f2', self.incExposureBias)

        #self.setupHBAOControls()
        if self.enableHDR:
            self.setupCamDebugs()
            taskMgr.add(self.updateCamDebugs, "updateCamDebugs")

    def addCamDebug(self):
        self.camDebugs.append(OnscreenText("", align = TextNode.ALeft, scale = 0.1, pos = (0.05, self.camDebugZ), parent=base.a2dTopLeft, fg = (1, 1, 1, 1), shadow=(0, 0, 0, 1)))
        self.camDebugZ -= 0.1

    def setupCamDebugs(self):
        for i in range(8):
            # Auto method, Shutter speed, aperature, ISO, exposure, luminance, lum max
            self.addCamDebug()

    def updateCamDebugs(self, task):
        method = self.camDebugs[0]
        methodVal = ConfigVariableInt("hdr-exposure-auto-method").getValue()
        if methodVal == 0:
            method.setText("Program AE")
        elif methodVal == 1:
            method.setText("Shutter priority AE")
        elif methodVal == 2:
            method.setText("Aperture priority AE")

        shutter = self.camDebugs[1]
        denom = self.hdr.getHdrPass().getShutterSpeed()
        if denom >= 1:
            shutter.setText(f"Shutter Speed: {int(denom)}\"")
        else:
            shutter.setText(f"Shutter Speed: 1/{int(1 / denom)}")

        apSize = self.hdr.getHdrPass().getAperature()
        aperature = self.camDebugs[2]
        aperature.setText(f"Aperture: f{round(apSize * 2) / 2}")

        isoVal = self.hdr.getHdrPass().getIso()
        iso = self.camDebugs[3]
        iso.setText(f"ISO: {int(isoVal)}")

        expVal = self.hdr.getHdrPass().getExposure()
        exp = self.camDebugs[4]
        exp.setText(f"EV: {format(expVal, '.2f')}")

        lumVal = self.hdr.getHdrPass().getLuminance()
        lum = self.camDebugs[5]
        lum.setText(f"L Avg: {format(lumVal, '.2f')}")

        lMaxVal = self.hdr.getHdrPass().getMaxLuminance()
        lMax = self.camDebugs[6]
        lMax.setText(f"L Max: {format(lMaxVal, '.2f')}")

        fVal = base.camLens.getFocalLength() * 25.4
        f = self.camDebugs[7]
        f.setText(f"Focal Length: {int(fVal)} mm")

        task.delayTime = 1.0
        return task.again

    def titleSliderBar(self, title, min, max, varname):
        def __updateVarValue(slider, title, text, varname):
            loadPrcFileData("", "{0} {1}".format(varname, slider['value']))
            text.setText("{0}: {1}".format(title, slider['value']))

        value = ConfigVariableDouble(varname, min).getValue()
        frame = DirectFrame(parent = base.a2dTopLeft, pos = (0.3, 0, self.hbaoControlZ), scale = 0.3)
        titleText = OnscreenText("{0}: {1}".format(title, value), parent = frame, scale = 0.1)
        slider = DirectSlider(
            range = (min, max),
            value = value,
            command = __updateVarValue,
            pos = (0.1, 0, -0.1),
            parent = frame
        )
        slider['extraArgs'] = [slider, title, titleText, varname]

        self.hbaoControlZ -= 0.1

    def setupHBAOControls(self):
        self.titleSliderBar("Falloff", 0.05, 20, "hbao-falloff")
        self.titleSliderBar("Max sample dist", 0.05, 20, "hbao-max-sample-distance")
        self.titleSliderBar("Sample radius", 0.05, 20, "hbao-sample-radius")
        self.titleSliderBar("Angle bias", 0, 1, "hbao-angle-bias")
        self.titleSliderBar("Strength", 0, 75, "hbao-strength")

    def setExposureBias(self, bias):
        self.exposureBias[0] = bias

    def getExposureBias(self):
        return self.exposureBias[0]

    def incExposureBias(self):
        self.exposureBias[0] += 0.05
        print(self.exposureBias[0])

    def decExposureBias(self):
        self.exposureBias[0] -= 0.05
        print(self.exposureBias[0])

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
            self.ssao = SSAO_Effect(self, SSAO_Effect.M_HBAO)
            self.addEffect(self.ssao)
            textures["aoSampler"] = self.ssao.getFinalTexture()

        if self.enableMB:
            self.mb = MotionBlur(self.getOutput())
            self.mb.setSceneCamera(base.cam)
            self.mb.setup()
            # sort value of 2 to do motion blur *after* the main scene,
            # which is sort 1
            self.addCamera(self.mb.getCamera(), 0, 1)

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

        ptext += "vec3 AccurateLinearToSRGB(vec3 linearCol) {\n"
        ptext += "  vec3 sRGBLo = linearCol * 12.92;\n"
        ptext += "  vec3 sRGBHi = (pow(abs(linearCol), vec3(1.0/2.4)) * 1.055) - 0.055;\n"
        ptext += "  vec3 sRGB = (length(linearCol) <= 0.0031308) ? sRGBLo : sRGBHi;\n"
        ptext += "  return sRGB;\n"
        ptext += "}\n"

        for sampler in textures.keys():
            ptext += "uniform sampler2D " + sampler + ";\n"

        if self.flashEnabled:
            ptext += "uniform vec3 flashColor[1];\n"

        if self.enableHDR:
            ptext += "const mat3 aces_input_mat = mat3(\n"
            ptext += "  vec3(0.59719, 0.35458, 0.04823),\n"
            ptext += "  vec3(0.07600, 0.90834, 0.01566),\n"
            ptext += "  vec3(0.02840, 0.13383, 0.83777)\n"
            ptext += ");\n"
            ptext += "const mat3 aces_output_mat = mat3(\n"
            ptext += "  vec3(1.60475, -0.53108, -0.07367),\n"
            ptext += "  vec3(-0.10208,  1.10813, -0.00605),\n"
            ptext += "  vec3(-0.00327, -0.07276,  1.07602)\n"
            ptext += ");\n"
            ptext += "vec3 rtt_and_odt_fit(vec3 v) {\n"
            ptext += "  vec3 a = v * (v + 0.0245786f) - 0.000090537f;\n"
            ptext += "  vec3 b = v * (0.983729f * v + 0.4329510f) + 0.238081f;\n"
            ptext += "  return a / b;\n"
            ptext += "}\n"
            ptext += "vec3 uncharted2TonemapPartial(vec3 x) {\n"
            ptext += "  float A = 0.15;\n"
            ptext += "  float B = 0.50;\n"
            ptext += "  float C = 0.10;\n"
            ptext += "  float D = 0.20;\n"
            ptext += "  float E = 0.02;\n"
            ptext += "  float F = 0.30;\n"
            ptext += "  return ((x*(A*x+C*B)+D*E)/(x*(A*x+B)+D*F))-E/F;\n"
            ptext += "}\n"

            ptext += "uniform float p3d_ExposureScale;\n"

        ptext += "void main()\n"
        ptext += "{\n"
        ptext += "  outputColor = texture(sceneColorSampler, l_texcoord);\n"
        if self.enableSSAO:
            ptext += "  outputColor.rgb *= texture(aoSampler, l_texcoord).r;\n"
        if self.enableBloom:
            ptext += "  vec3 bloomSample = texture(bloomSampler, l_texcoord).rgb;\n"
            ptext += "  outputColor.rgb += bloomSample;\n"
        if self.flashEnabled:
            ptext += "  outputColor.rgb += pow(flashColor[0], vec3(2.2));\n"
        if self.enableHDR:
            #ptext += "  outputColor.rgb *= p3d_ExposureScale;\n"
            #ptext += "  outputColor.rgb = aces_input_mat * outputColor.rgb;\n"
            #ptext += "  outputColor.rgb = rtt_and_odt_fit(outputColor.rgb);\n"
            #ptext += "  outputColor.rgb = aces_output_mat * outputColor.rgb;\n"
            #ptext += "  float exposureBias = p3d_ExposureScale * 2.0;\n"
            #ptext += "  vec3 curr = uncharted2TonemapPartial(outputColor.rgb * exposureBias);\n"
            #ptext += "  vec3 W = vec3(11.2);\n"
            #ptext += "  vec3 whiteScale = vec3(1.0) / uncharted2TonemapPartial(W);\n"
            # Raise the final color to a slight power to increase contrast
            #ptext += "  outputColor.rgb = curr * whiteScale;\n"
        #ptext += "  outputColor.rgb = clamp(outputColor.rgb, 0, 1);\n"
            #ptext += "  outputColor.rgb = outputColor.rgb / (outputColor.rgb + vec3(0.155)) * 1.019;\n"
        #if self.enableHDR:
            ptext += "  outputColor.rgb = vec3(1.0) - exp(-outputColor.rgb * p3d_ExposureScale);\n"
        #ptext += "  outputColor.rgb = AccurateLinearToSRGB(outputColor.rgb);\n"
            #ptext += "  float targetEV = ComputeTargetEV(p3d_ExposureScale);\n"
            #ptext += "  float aperature = 0.0;\n"
            #ptext += "  float shutterSpeed = 0.0;\n"
            #ptext += "  float iso = 0.0;\n"
            #ptext += "  ApplyProgramAuto(1.0, targetEV, aperature, shutterSpeed, iso);\n"
            #ptext += "  outputColor.rgb *= GetSaturationBasedExposure(aperature, shutterSpeed, iso);\n"
            #ptext += "  outputColor.rgb *= p3d_ExposureScale;\n"
        if self.enableSSAO and ConfigVariableBool("ao-debug", False).getValue():
            ptext += "  outputColor.rgb = vec3(texture(aoSampler, l_texcoord).x);\n"
        ptext += "}\n"

        shader = Shader.make(Shader.SL_GLSL, vtext, ptext)
        if not shader:
            return

        finalQuad.setShader(shader)

        for sampler, texture in textures.items():
            finalQuad.setShaderInput(sampler, texture)

        if self.flashEnabled:
            finalQuad.setShaderInput("flashColor", self.flashColor)

        #if self.enableHDR:
        #    finalQuad.setShaderInput("k_contrast", self.exposureBias)
