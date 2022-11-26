#include "dnaLoadRequest.h"
#include "loader.h"
#include "config_pgraph.h"

TypeHandle DNALoadRequest::_type_handle;

/**
 * Create a new DNALoadRequest, and add it to the loader via load_async(),
 * to begin an asynchronous load.
 */
DNALoadRequest::
DNALoadRequest(const std::string &name,
               const Filename &filename,                            
               DNAStorage *dna_store,
               CoordinateSystem cs,
               int editing,
               bool is_AI,
               DNALoader *loader) :
  AsyncTask(name),
  _filename(filename),
  _storage(dna_store),
  _cs(cs),
  _editing(editing),
  _is_AI(is_AI),
  _loader(loader)
{
}

/**
 * Performs the task: that is, loads the one model.
 */
AsyncTask::DoneStatus DNALoadRequest::
do_task() {
    double delay = async_load_delay;
    if (delay != 0.0) {
        Thread::sleep(delay);
    }
    
    if (_is_AI) {
        PT(DNAData) data = _loader->load_sync_AI(_filename, _storage, _cs);
        set_result(data);
    } else {
        PT(PandaNode) model = _loader->load_sync(_filename, _storage, _cs, _editing);
        set_result(model);
    }

    // Don't continue the task; we're done.
    return DS_done;
}
