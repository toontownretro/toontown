// Filename: config_dna.cxx
// Created by:  shochet (26Jun00)
//
////////////////////////////////////////////////////////////////////

#include "config_dna.h"

#include "dnaGroup.h"
#include "dnaVisGroup.h"
#include "dnaBuildings.h"
#include "dnaWindow.h"
#include "dnaStreet.h"
#include "dnaCornice.h"
#include "dnaProp.h"
#include "dnaAnimProp.h"
#include "dnaInteractiveProp.h"
#include "dnaAnimBuilding.h"
#include "dnaData.h"
#include "dnaNode.h"
#include "dnaDoor.h"
#include "dnaSign.h"
#include "dnaSignBaseline.h"
#include "dnaSignGraphic.h"
#include "dnaSignText.h"
#include "dnaSuitPoint.h"
#include "dnaSuitEdge.h"
#include "dnaSuitPath.h"
#include "dnaBattleCell.h"
#include "dnaLoader.h"
#include "dnaLoadRequest.h"
#include "loaderFileTypeDNA.h"

#include "dconfig.h"
#include "loaderFileTypeRegistry.h"

Configure(config_dna);
NotifyCategoryDef(dna, "");

ConfigVariableList dna_preload
("dna-preload");

ConfigVariableSearchPath dna_path
("dna-path");

ConfigVariableInt dna_async_num_threads
("dna-async-num-threads", 1,
 PRC_DESC("The number of threads that will be started by the task manager "
          "to load DNA files asynchronously.  These threads will only be "
          "started if the asynchronous interface is used, and if threading "
          "support is compiled into Panda.  The default is one thread, "
          "which allows DNA files to be loaded one at a time in a single "
          "asychronous thread.  You can set this higher, particularly if "
          "you have many CPU's available, to allow loading multiple DNA files "
          "simultaneously."));
          
ConfigVariableEnum<ThreadPriority> dna_async_thread_priority
("dna-async-thread-priority", TP_low,
 PRC_DESC("The default thread priority to assign to the threads created "
          "for asynchronous loading.  The default is 'low'; you may "
          "also specify 'normal', 'high', or 'urgent'."));

ConfigureFn(config_dna) {
  init_libdna();
}

const ConfigVariableSearchPath &
get_dna_path() {
  return dna_path;
}

/**
 *
 */
void
init_libdna() {
  static bool initialized = false;
  if (initialized) {
    return;
  }
  initialized = true;

  DNAGroup::init_type();
  DNAVisGroup::init_type();
  DNAData::init_type();
  DNANode::init_type();
  DNAWindows::init_type();
  DNAStreet::init_type();
  DNAWall::init_type();
  DNAFlatBuilding::init_type();
  DNALandmarkBuilding::init_type();
  DNACornice::init_type();
  DNAProp::init_type();
  DNAAnimProp::init_type();
  DNAInteractiveProp::init_type();
  DNAAnimBuilding::init_type();
  DNADoor::init_type();
  DNAFlatDoor::init_type();
  DNASign::init_type();
  DNASignBaseline::init_type();
  DNASignGraphic::init_type();
  DNASignText::init_type();
  DNASuitPoint::init_type();
  DNASuitEdge::init_type();
  DNASuitPath::init_type();
  DNABattleCell::init_type();
  DNALoader::init_type();
  DNALoadRequest::init_type();
  
  LoaderFileTypeDNA::init_type();

  LoaderFileTypeRegistry *reg = LoaderFileTypeRegistry::get_global_ptr();
  reg->register_type(new LoaderFileTypeDNA);
}
