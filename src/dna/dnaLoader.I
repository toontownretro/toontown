
/**
 * Specifies the task manager that is used for asynchronous loads.  The
 * default is the global task manager.
 */
INLINE void DNALoader::
set_task_manager(AsyncTaskManager *task_manager) {
    _task_manager = task_manager;
}

/**
 * Returns the task manager that is used for asynchronous loads.
 */
INLINE AsyncTaskManager *DNALoader::
get_task_manager() const {
    return _task_manager;
}

/**
 * Specifies the task chain that is used for asynchronous loads.  The default
 * is the initial name of the DNALoader object.
 */
INLINE void DNALoader::
set_task_chain(const std::string &task_chain) {
    _task_chain = task_chain;
}

/**
 * Returns the task chain that is used for asynchronous loads.
 */
INLINE const std::string &DNALoader::
get_task_chain() const {
    return _task_chain;
}

/**
 * Stop any threads used for asynchronous loads.
 */
INLINE void DNALoader::
stop_threads() {
    PT(AsyncTaskChain) chain = _task_manager->find_task_chain(_task_chain);
    if (chain != nullptr) {
        chain->stop_threads();
    }
}

/**
 * Removes a pending asynchronous load request.  Returns true if successful,
 * false otherwise.
 * @deprecated use task.cancel() to cancel the request instead.
 */
INLINE bool DNALoader::
remove(AsyncTask *task) {
    return _task_manager->remove(task);
}

/**
 * Loads the file immediately, waiting for it to complete.
 *
 * If search is true, the file is searched for along the dna path;
 * otherwise, only the exact filename is loaded.
 */
INLINE PT(PandaNode) DNALoader::
load_sync(const Filename &filename, DNAStorage *dna_store, CoordinateSystem cs, int editing) {
    return load_file(filename, dna_store, cs, editing);
}

/**
 * Loads the file immediately, waiting for it to complete.
 *
 * If search is true, the file is searched for along the dna path;
 * otherwise, only the exact filename is loaded.
 */
INLINE PT(DNAData) DNALoader::
load_sync_AI(const Filename &filename, DNAStorage *dna_store, CoordinateSystem cs) const {
    return load_file_AI(filename, dna_store, cs);
}

/**
 * Begins an asynchronous load request.  To use this call, first call
 * make_async_request() to create a new DNALoadRequest object with the
 * filename you wish to load, and then add that object to the DNALoader with
 * load_async.  This function will return immediately, and the dna will be
 * loaded in the background.
 *
 * To determine when the dna has completely loaded, you may poll
 * request->is_ready() from time to time, or set the done_event on the request
 * object and listen for that event.  When the dna is ready, you may
 * retrieve it via request->get_model().
 */
INLINE void DNALoader::
load_async(AsyncTask *request) {
    request->set_task_chain(_task_chain);
    _task_manager->add(request);
}