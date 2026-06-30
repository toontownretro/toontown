// Filename: load_dna_file.cxx
// Created by:  shochet (24May00)
//
////////////////////////////////////////////////////////////////////

#include "config_dna.h"

#include "load_dna_file.h"

#include "dnaData.h"
#include "dnaLoader.h"
#include "dnaStorage.h"

#include "config_putil.h"
#include "virtualFileSystem.h"

const std::string async_dna_task_chain("async_dna_loader_tasks");

PT(PandaNode)
load_DNA_file(DNAStorage *dna_store,
              const string &filename,
              CoordinateSystem cs,
              int editing) {
  nassertr(dna_store != nullptr, nullptr);
  DNALoader loader;
  return loader.load_file(filename, dna_store, cs, editing);
}

PT(DNAData)
load_DNA_file_AI(DNAStorage *dna_store,
              const string &filename,
              CoordinateSystem cs) {
  nassertr(dna_store != nullptr, nullptr);
  DNALoader loader;
  return loader.load_file_AI(filename, dna_store, cs);
}

PT(DNALoadRequest)
make_async_load_DNA_request(const Filename &filename,
                            DNAStorage *dna_store,
                            CoordinateSystem cs,
                            int editing) {
  nassertr(dna_store != nullptr, nullptr);
  return new DNALoadRequest(std::string("dna:") + filename.get_basename(), filename, dna_store, cs, false, editing);
}

PT(DNALoadRequest)
make_async_load_DNA_AI_request(const Filename &filename,
                               DNAStorage *dna_store,
                               CoordinateSystem cs) {
  nassertr(dna_store != nullptr, nullptr);
  return new DNALoadRequest(std::string("dna:") + filename.get_basename(), filename, dna_store, cs, true, 0);
}

void stop_async_DNA_requests(AsyncTaskManager *task_manager) {
    nassertv(task_manager != nullptr);
    
    PT(AsyncTaskChain) task_chain = task_manager->find_task_chain(async_dna_task_chain);
    if (task_chain == nullptr) { return; }
    
    task_chain->stop_threads();
}

void async_load_DNA_file(PT(AsyncTask) request,
                         AsyncTaskManager *task_manager) {
    nassertv(task_manager != nullptr);
    nassertv(request != nullptr);
  
    PT(AsyncTaskChain) task_chain = task_manager->find_task_chain(async_dna_task_chain);
    if (task_chain == nullptr) {
        task_chain = task_manager->make_task_chain(async_dna_task_chain);
        task_chain->set_num_threads(dna_async_num_threads);
        task_chain->set_thread_priority(dna_async_thread_priority);
    }

    request->set_task_chain(async_dna_task_chain);
    task_manager->add(request);
}