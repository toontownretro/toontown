#define LOCAL_LIBS \
  dnaLoader
#define OTHER_LIBS \
  p3event:c p3mathutil:c p3linmath:c p3putil:c p3parametrics:c panda:m \
  p3express:c pandaexpress:m \
  p3dtoolutil:c p3dtoolbase:c p3prc p3dtool:m \
  p3pipeline:c p3pstatclient:c p3cull:c \
  p3prc p3interrogatedb p3express:c p3pandabase:c p3downloader:c p3pgraph:c \
  p3pgraphnodes:c p3gobj:c p3pnmimage:c p3gsgbase:c p3text:c p3display:c \
  $[if $[HAVE_NET],p3net:c] $[if $[WANT_NATIVE_NET],p3nativenet:c]

#if $[HAVE_FREETYPE]
    #define OTHER_LIBS $[OTHER_LIBS] p3pnmtext:c
  #endif

#define UNIX_SYS_LIBS m

#begin bin_target
  #define TARGET dna-trans

  #define SOURCES \
    dnaTrans.cxx

#end bin_target
