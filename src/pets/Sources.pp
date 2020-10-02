#begin lib_target
  #define TARGET pets
  #define LOCAL_LIBS \
    toontownbase

  #define OTHER_LIBS \
    otp:m otpbase:c movement:c \
    panda:m p3downloader:c p3express:c p3pandabase:c p3recorder:c \
    p3pgraph:c p3pgraphnodes:c p3pipeline:c p3grutil:c p3chan:c p3pstatclient:c \
    p3char:c p3collide:c p3cull:c p3device:c p3dgraph:c p3display:c \
    p3event:c p3gobj:c p3gsgbase:c p3linmath:c p3mathutil:c p3parametrics:c \
    p3pnmimagetypes:c p3pnmimage:c p3tform:c p3text:c \
    p3putil:c p3audio:c p3pgui:c p3interrogatedb \
    $[if $[HAVE_NET],p3net:c] $[if $[WANT_NATIVE_NET],p3nativenet:c] \
    $[if $[HAVE_FREETYPE],p3pnmtext:c] \
    p3dtoolutil:c p3dtoolbase:c p3prc

  #define SOURCES \
    config_pets.h config_pets.cxx \
    cPetBrain.h cPetBrain.cxx cPetChase.h cPetChase.I cPetChase.cxx \
    cPetFlee.h cPetFlee.I cPetFlee.cxx

  #define INSTALL_HEADERS \
    config_pets.h \
    cPetBrain.h cPetChase.h cPetChase.I cPetFlee.h cPetFlee.I

  #define IGATESCAN all
#end lib_target
