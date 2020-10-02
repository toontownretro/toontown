#define USE_PACKAGES cg  // from gobj.

#begin lib_target
  #define TARGET toontownbase

  #define OTHER_LIBS \
      p3dtool:m \
      p3prc p3dtoolutil:c p3dtoolbase:c

  #define SOURCES \
    toontownbase.cxx toontownbase.h toontownsymbols.h \

  #define INSTALL_HEADERS \
    toontownbase.h toontownsymbols.h

#end lib_target
