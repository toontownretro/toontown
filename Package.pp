//
// Package.pp
//
// This file defines certain configuration variables that are to be
// written into the various make scripts.  It is processed by ppremake
// (along with the Sources.pp files in each of the various
// directories) to generate build scripts appropriate to each
// environment.
//
// This is the package-specific file, which should be at the top of
// every source hierarchy.  It generally gets the ball rolling, and is
// responsible for explicitly including all of the relevent Config.pp
// files.



// What is the name and version of this source tree?
#if $[eq $[PACKAGE],]
  #define PACKAGE toontown
  #define VERSION 0.80
#endif


// Where should we find the OTP source directory?
#if $[OTP_SOURCE]
  #define OTP_SOURCE $[unixfilename $[OTP_SOURCE]]
#elif $[or $[CTPROJS],$[OTP]]
  // If we are presently attached, use the environment variable.
  #define OTP_SOURCE $[unixfilename $[OTP]]
  #if $[eq $[OTP],]
    #error You seem to be attached to some trees, but not OTP!
  #endif
#else
  // Otherwise, if we are not attached, we guess that the source is a
  // sibling directory to this source root.
  #define OTP_SOURCE $[standardize $[TOPDIR]/../otp]
#endif

// Where should we install TOONTOWN?
#if $[TOONTOWN_INSTALL]
  #define TOONTOWN_INSTALL $[unixfilename $[TOONTOWN_INSTALL]]
#elif $[CTPROJS]
  #set TOONTOWN $[unixfilename $[TOONTOWN]]
  #define TOONTOWN_INSTALL $[TOONTOWN]/built
  #if $[eq $[TOONTOWN],]
    #error You seem to be attached to some trees, but not TOONTOWN!
  #endif
#else
  #defer TOONTOWN_INSTALL $[unixfilename $[INSTALL_DIR]]
#endif


// Also get the OTP Package file and everything that includes.
#if $[not $[isfile $[OTP_SOURCE]/Package.pp]]
  #printvar OTP_SOURCE
  #error OTP source directory not found from toontown!  Are you attached properly?
#endif

#include $[OTP_SOURCE]/Package.pp

// Define the inter-tree dependencies.
#define NEEDS_TREES otp $[NEEDS_TREES]
#define DEPENDABLE_HEADER_DIRS $[DEPENDABLE_HEADER_DIRS] $[OTP_INSTALL]/include
