// Filename: load_dna_file.cxx
// Created by:  shochet (24May00)
//
////////////////////////////////////////////////////////////////////

#include "config_dna.h"
#include "load_dna_file.h"
#include "dnaLoader.h"
#include "dnaData.h"
#include "dnaStorage.h"
#include "config_putil.h"
#include "virtualFileSystem.h"

////////////////////////////////////////////////////////////////////
//     Function: load_dna_file
//  Description: A convenience function.  Loads up the indicated dna
//               file, and returns the root of a scene graph.  Returns
//               NULL if the file cannot be read for some reason.
//
//               Unlike load_egg_file(), this function *does* search
//               for the file along the model_path (as well as the
//               dna_path) if it is not already fully qualified.
//               Begin the filename with ./ to prevent this behavior.
////////////////////////////////////////////////////////////////////
PT(PandaNode)
load_DNA_file(DNAStorage *dna_store,
              const string &filename,
              CoordinateSystem cs,
              int editing) {
  DNALoader loader;
  return loader.load_sync(filename, dna_store, cs, editing);
}



////////////////////////////////////////////////////////////////////
//     Function: load_dna_file_AI
//  Description: Loads up the indicated dna file but does not create
//               geometry.  Returns the DNAData loaded, or NULL.
////////////////////////////////////////////////////////////////////
PT(DNAData)
load_DNA_file_AI(DNAStorage *dna_store,
              const string &filename,
              CoordinateSystem cs) {
  DNALoader loader;
  return loader.load_sync_AI(filename, dna_store, cs);
}
