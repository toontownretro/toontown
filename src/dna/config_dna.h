// Filename: config_dna.h
// Created by:  shochet (26Jun00)
//
////////////////////////////////////////////////////////////////////

#ifndef CONFIG_DNA_H
#define CONFIG_DNA_H

#include "toontownbase.h"

#include "notifyCategoryProxy.h"
#include "dconfig.h"
#include "configVariableList.h"
#include "configVariableSearchPath.h"

class DSearchPath;

NotifyCategoryDeclNoExport(dna);

extern EXPCL_TOONTOWN_DNALOADER ConfigVariableList dna_preload;
extern EXPCL_TOONTOWN_DNALOADER ConfigVariableSearchPath dna_path;

BEGIN_PUBLISH
EXPCL_TOONTOWN_DNALOADER const ConfigVariableSearchPath &get_dna_path();
END_PUBLISH

#endif
