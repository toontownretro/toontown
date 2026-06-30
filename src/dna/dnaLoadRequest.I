/**
 * Returns the filename associated with this asynchronous DNALoadRequest.
 */
INLINE const Filename &DNALoadRequest::
get_filename() const {
  return _filename;
}

/**
 * Returns the DNAStorage associated with this asynchronous
 * DNALoadRequest.
 */
INLINE DNAStorage *DNALoadRequest::
get_storage() const {
  return _storage;
}

INLINE const CoordinateSystem &DNALoadRequest::
get_coordinate_system() const {
  return _cs;
}

INLINE int DNALoadRequest::
get_editing() const {
  return _editing;
}

/**
 * Returns true if this request has completed, false if it is still pending or
 * if it has been cancelled.  When this returns true, you may retrieve the
 * model loaded by calling get_model() or the data by calling get_data() if it's for a AI.
 * Equivalent to `req.done() and not req.cancelled()`.
 * @see done()
 */
INLINE bool DNALoadRequest::
is_ready() const {
  return (FutureState)_future_state.load(std::memory_order_relaxed) == FS_finished;
}

/**
 * Returns the node that was loaded asynchronously, if any, or null if there
 * was an error.  It is an error to call this unless done() returns true.
 * @deprecated Use result() instead.
 */
INLINE PandaNode *DNALoadRequest::
get_model() const {
  nassertr_always(done(), nullptr);
  if (_is_AI == true) { return nullptr; }
  return (PandaNode *)_result;
}

/**
 * Returns the DNAData that was loaded asynchronously, if any, or null if there
 * was an error.  It is an error to call this unless done() returns true.
 * @deprecated Use result() instead.
 */
INLINE DNAData *DNALoadRequest::
get_data() const {
  nassertr_always(done(), nullptr);
  if (_is_AI != true) { return nullptr; }
  return (DNAData *)_result;
}
