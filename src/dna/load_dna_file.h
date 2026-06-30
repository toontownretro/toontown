// Filename: load_dna_file.h
// Created by:  shochet (24May00)
//
////////////////////////////////////////////////////////////////////

#ifndef LOAD_DNA_FILE_H
#define LOAD_DNA_FILE_H

#include "toontownbase.h"

#include "dnaData.h"
#include "dnaLoadRequest.h"

#include "asyncTaskManager.h"
#include "asyncTask.h"
#include "coordinateSystem.h"
#include "pandaNode.h"
#include "pointerTo.h"

class DNAStorage;
class DNALoader;

BEGIN_PUBLISH

/*
 * A convenience function; the primary interface to this
 * package.  Loads up the indicated dna file, and
 * returns the root of a scene graph.  Returns NULL if
 * the file cannot be read for some reason. 
 * 
 * Unlike load_egg_file(), this function *does* search
 * for the file along the model_path (as well as the
 * dna_path) if it is not already fully qualified.
 * Begin the filename with ./ to prevent this behavior.
 */
EXPCL_TOONTOWN_DNALOADER PT(PandaNode)
load_DNA_file(DNAStorage *dna_store,
              const string &filename,
              CoordinateSystem cs = CS_default,
              int editing = 0);

/*
 * Loads up the indicated dna file but does not create
 * any geometry from it. It simply creates the dna
 * structures that can then be accessed via the dnaStorage
 * Returns the DNAData object on success, or NULL if the
 * file cannot be read for some reason.
 */
EXPCL_TOONTOWN_DNALOADER PT(DNAData)
load_DNA_file_AI(DNAStorage *dna_store,
                 const string &filename,
                 CoordinateSystem cs = CS_default);

/*
 * Returns a new AsyncTask (DNALoadRequest) object suitable for adding to load_async() to start
 * an asynchronous dna file load.
 */
EXPCL_TOONTOWN_DNALOADER PT(DNALoadRequest)
make_async_load_DNA_request(const Filename &filename,
                            DNAStorage *dna_store,
                            CoordinateSystem cs = CS_default,
                            int editing = 0);

/*
 * Returns a new AsyncTask (DNALoadRequest) object suitable for adding to load_async() to start
 * an asynchronous dna AI file load.
 */
EXPCL_TOONTOWN_DNALOADER PT(DNALoadRequest)
make_async_load_DNA_AI_request(const Filename &filename,
                               DNAStorage *dna_store,
                               CoordinateSystem cs = CS_default);

/**
 * Stop any threads used for asynchronous loads for the DNA task chain.
 */
EXPCL_TOONTOWN_DNALOADER void
stop_async_DNA_requests(AsyncTaskManager *task_manager = AsyncTaskManager::get_global_ptr());
                               
/**
 * Begins an asynchronous load request.  To use this call, first call
 * make_async_load_dna_request() or make_async_load_dna_AI_request() 
 * to create a new DNALoadRequest object with the filename you wish to load, 
 * and then add that object to the DNALoader with load_async.
 * This function will return immediately, and the dna will be loaded in 
 * the background.
 *
 * To determine when the dna has completely loaded, you may poll
 * request->is_ready() from time to time, or set the done_event on the request
 * object and listen for that event.  When the dna is ready, you may
 * retrieve it via request->get_model() or the dna data via request->get_data()
 */
EXPCL_TOONTOWN_DNALOADER void
async_load_DNA_file(PT(AsyncTask) request,
                    AsyncTaskManager *task_manager = AsyncTaskManager::get_global_ptr());
 
END_PUBLISH

#endif
