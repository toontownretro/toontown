// DIR_TYPE "metalib" indicates we are building a shared library that
// consists mostly of references to other shared libraries.  Under
// Windows, this directly produces a DLL (as opposed to the regular
// src libraries, which don't produce anything but a pile of OBJ files
// under Windows).

#define DIR_TYPE metalib

#begin metalib_target
  #define TARGET toontown
  #define COMPONENT_LIBS pets dnaLoader toontownbase suit
  #define SOURCES toontown.cxx
  #if $[BUILD_COMPONENTS]
    #define BUILDING_DLL BUILDING_TOONTOWN_STUB
  #else
    #define BUILDING_DLL BUILDING_TOONTOWN
  #endif
#end metalib_target
