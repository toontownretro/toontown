#begin lib_target
  #define TARGET suit
  #define LOCAL_LIBS dnaLoader toontownbase
  #define OTHER_LIBS \
    panda:m pandaexpress:m \
    p3interrogatedb \
    p3dtoolutil:c p3dtoolbase:c p3dtool:m \
    p3prc

  #define SOURCES \
    suitLeg.I suitLeg.h \
    suitLegList.I suitLegList.h

  #define COMPOSITE_SOURCES  \
    suitLeg.cxx suitLegList.cxx

  #define IGATESCAN all

#end lib_target
