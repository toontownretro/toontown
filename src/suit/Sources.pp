#begin lib_target
  #define TARGET suit
  #define LOCAL_LIBS dnaLoader toontownbase
  #define OTHER_LIBS \
    panda:m pandaexpress:m \
    interrogatedb \
    dtoolutil:c dtoolbase:c dtool:m \
    prc

  #define SOURCES \
    suitLeg.I suitLeg.h \
    suitLegList.I suitLegList.h

  #define COMPOSITE_SOURCES  \
    suitLeg.cxx suitLegList.cxx

  #define IGATESCAN all

#end lib_target
