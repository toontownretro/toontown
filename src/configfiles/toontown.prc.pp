//
// _toontown.prc.pp
//
// This file defines the script to auto-generate _toontown.prc at
// ppremake time.
//

#output 60_toontown.prc notouch
#### Generated automatically by $[PPREMAKE] $[PPREMAKE_VERSION] from $[SOURCEFILE].
################################# DO NOT EDIT ###########################

#if $[CTPROJS]
// If we are using the ctattach tools, append "built"--this is a VR
// Studio convention.
model-path      $TTMODELS/built
sound-path      $TTMODELS/built
#else
// Dave Schuyler sees this.
model-path      $TTMODELS
sound-path      $TTMODELS
#endif

plugin-path $TOONTOWN/built/lib

# remove this when we integrate Toontown with the Uberdog
want-uberdog #f

dc-file $TOONTOWN/src/configfiles/toon.dc

### Window Options ###
window-title Toontown
win-origin -2 -2
#if $[WINDOWS_PLATFORM]
icon-filename phase_3/models/gui/toontown.ico
#else
icon-filename phase_3/models/gui/toontown_mac_icon.rgb
#endif

# Set your game server and port to be localhost
game-server http://localhost:6667

### SSL Config ###
ssl-certificates $OTP/src/configfiles/certificates.txt
ssl-certificates $OTP/src/configfiles/gameserver.txt

# Itemize the SSL certificates we might expect to encounter on our
# account servers.  This protects us from an imposter who happens to
# have his own VeriSign certificate (the imposter's certificate won't
# be from "Disney").
expected-ssl-server /O=Disney Enterprises/OU=WDIG/CN=account.toontown.com
expected-ssl-server /O=Disney Enterprises/OU=WDIG/CN=gameserver.toontown.com

# These two let us also accept the ttown2 certificate.
# This is only in the dev environment; it doesn't get published.
ssl-certificates $TOONTOWN/src/configfiles/ttown2.txt
expected-ssl-server /O=Disney Enterprises/OU=WDIG/CN=ttown2.online.disney.com

# check that the quests are internally consistent
quest-sanity-check #t

# this causes pupils, etc. to be generated as separate geometry under
# their exposed joints, instead of combined with the rest of the head.
egg-rigid-geometry #t

# Toontown is designed for 4/3 aspect ratio, so let's force it to be so
# aspect-ratio 1.333333

# This keeps the joint hierarchies for the different LOD's of an Actor separate.
# Seems to be necessary for the Toons--some of the naked Toons seem to have slightly different skeletons
# for the different LOD's.
merge-lod-bundles #f

### Game Options ###
# Need to turn on this option to support our broken door triggers.
early-event-sphere #t

# Need to turn this on to avoid jerky movement, pirates copes with it differently
accept-clock-skew #t

# A local directory to store cached news information in dev.  (In
# production, this is set to a subdirectory within the current directory).
news-stage-dir /tmp/news

# But devs don't need to be hitting the news server every time.
news-over-http #f
news-index-filename news_index.txt

# --- Custom Values --- #

### Shader Config ###
want-lighting-effects 0
# Ambient Occlusion
ao-debug #f
ao-blur-normal-factor 0
ao-blur-depth-factor 0
#
# Horizon Based Ambient Occlusion:
hbao-falloff 2.0
hbao-max-sample-distance 20.0
hbao-sample-radius 3.5
hbao-angle-bias 0.564
hbao-strength 5.0
#
# Cascaded Shadow Maps:
csm-distance 200
csm-sun-distance 400
csm-fixed-film-size #t
#
# Postprocess Shaders:
hdr-enable #t
bloom-enable #t
fxaa-enable #t
ssao-enable #f
#
# Shadows:
shadow-depth-bits 24

### Development and Debugging ###
tt-specific-login #t
want-magic-words #t

pstats-gpu-timing #f

# Display
cursor-filename phase_3/etc/toonmono.cur
show-frame-rate-meter #t
frame-rate-meter-update-interval 0.01

### Video Options ###
sync-video #f
assert-abort #f
framebuffer-srgb #t
textures-power-2 none

### Animation Config ###
hardware-animated-vertices #t
interpolate-frames #t

#end 60_toontown.prc
