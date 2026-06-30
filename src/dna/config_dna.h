// Filename: config_dna.h
// Created by:  shochet (26Jun00)
//
////////////////////////////////////////////////////////////////////

#ifndef CONFIG_DNA_H
#define CONFIG_DNA_H

#include "toontownbase.h"

#include "dconfig.h"
#include "configVariableEnum.h"
#include "configVariableInt.h"
#include "configVariableList.h"
#include "configVariableSearchPath.h"
#include "notifyCategoryProxy.h"
#include "threadPriority.h"

class DSearchPath;

NotifyCategoryDeclNoExport(dna);

extern EXPCL_TOONTOWN_DNALOADER ConfigVariableList dna_preload;
extern EXPCL_TOONTOWN_DNALOADER ConfigVariableSearchPath dna_path;

extern EXPCL_TOONTOWN_DNALOADER ConfigVariableInt dna_async_num_threads;
extern EXPCL_TOONTOWN_DNALOADER ConfigVariableEnum<ThreadPriority> dna_async_thread_priority;

BEGIN_PUBLISH
EXPCL_TOONTOWN_DNALOADER const ConfigVariableSearchPath &get_dna_path();
END_PUBLISH

extern EXPCL_TOONTOWN_DNALOADER void init_libdna();

#endif
