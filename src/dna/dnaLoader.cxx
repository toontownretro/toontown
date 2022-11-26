// Filename: dnaLoader.cxx
// Created by:  shochet (28Mar00)
//
////////////////////////////////////////////////////////////////////

#include "config_dna.h"

#include "dnaLoader.h"
#include "dnaStorage.h"
#include "dnaLoadRequest.h"
#include "pandaNode.h"
#include "nodePath.h"
#include "pointerTo.h"
#include "virtualFileSystem.h"

TypeHandle DNALoader::_type_handle;

DNALoader::DNALoader(const string &name) :
  Namable(name)
{
    _data = new DNAData("loader_data");
    PT(PandaNode) _top_node = new PandaNode("dna");
    _root = NodePath(_top_node);
    
    _task_manager = AsyncTaskManager::get_global_ptr();
    _task_chain = name;

    if (_task_manager->find_task_chain(_task_chain) == nullptr) {
        PT(AsyncTaskChain) chain = _task_manager->make_task_chain(_task_chain);

        ConfigVariableInt dna_loader_num_threads
          ("dna-loader-num-threads", 1,
           PRC_DESC("The number of threads that will be started by the DNALoader class "
                    "to load models asynchronously.  These threads will only be "
                    "started if the asynchronous interface is used, and if threading "
                    "support is compiled into Panda.  The default is one thread, "
                    "which allows models to be loaded one at a time in a single "
                    "asychronous thread.  You can set this higher, particularly if "
                    "you have many CPU's available, to allow loading multiple models "
                    "simultaneously."));
        chain->set_num_threads(dna_loader_num_threads);

        ConfigVariableEnum<ThreadPriority> dna_loader_thread_priority
          ("dna-loader-thread-priority", TP_low,
           PRC_DESC("The default thread priority to assign to the threads created "
                    "for asynchronous loading.  The default is 'low'; you may "
                    "also specify 'normal', 'high', or 'urgent'."));
        chain->set_thread_priority(dna_loader_thread_priority);
    }
}

/*
 * Returns a new AsyncTask object suitable for adding to load_async() to start
 * an asynchronous dna file load.
 */
PT(AsyncTask) DNALoader::make_async_request(const Filename &filename, DNAStorage *dna_store, CoordinateSystem cs, bool is_AI, int editing) {
    return new DNALoadRequest(std::string("dna:") + filename.get_basename(), filename, dna_store, cs, is_AI, editing, this);
}

/**
 * Loads a single dna file, if possible.  Returns the Node that is the
 * root of the file, or NULL if the file cannot be loaded.
 */
PT(PandaNode) DNALoader::load_file(const Filename &filename, 
                                   DNAStorage *dna_store, 
                                   CoordinateSystem cs, 
                                   int editing) {
    // We use binary mode to avoid Windows' end-of-line convention.
    Filename dna_filename = Filename::binary_filename(filename);
    if (!dna_filename.is_fully_qualified()) {
        if (!DNAData::resolve_dna_filename(dna_filename)) {
            dna_cat.error() << "load_file could not find " << filename
                          <<"\n    in dna_path: "<<get_dna_path()
                          <<"\n    or model_path: "<<get_model_path()<<"\n";
            return (PandaNode *)NULL;
        }
    }

    dna_cat.info() << "Reading " << dna_filename << "\n";

    _data->set_dna_filename(dna_filename);
    _data->set_dna_storage(dna_store);
    if (cs != CS_default) {
        _data->set_coordinate_system(cs);
    }

    VirtualFileSystem *vfs = VirtualFileSystem::get_global_ptr();
    istream *istr = vfs->open_read_file(dna_filename, true);
    if (istr == (istream *)NULL) {
        dna_cat.error() << "Could not open " << dna_filename << " for reading.\n";
        return (PandaNode *)NULL;
    }
    
    bool ok_flag = _data->read(*istr);
    vfs->close_read_file(istr);

    if (!ok_flag) {
    dna_cat.error() << "Error reading " << dna_filename << "\n";
        return (PandaNode *)NULL;
    }

    dna_cat.debug() << "About to call build_graph.\n";
    return build_graph(dna_store, editing);
}

/**
 * Loads a single dna file, if possible.  Returns the Node that is the
 * root of the file, or NULL if the file cannot be loaded.
 */
PT(DNAData) DNALoader::load_file_AI(const Filename &filename,
                                    DNAStorage *dna_store,
                                    CoordinateSystem cs) const {
    Filename dna_filename = Filename::text_filename(filename);
    if (!DNAData::resolve_dna_filename(dna_filename)) {
        dna_cat.error() << "load_file_AI could not find " << filename
                        <<"\n    in dna_path: "<<get_dna_path()
                        <<"\n    or model_path: "<<get_model_path()<<"\n";
        return NULL;
    }

    dna_cat.info() << "Reading " << dna_filename << "\n";

    _data->set_dna_filename(dna_filename);
    _data->set_dna_storage(dna_store);
    if (cs != CS_default) {
        _data->set_coordinate_system(cs);
    }

    VirtualFileSystem *vfs = VirtualFileSystem::get_global_ptr();
    istream *istr = vfs->open_read_file(dna_filename, true);
    if (istr == (istream *)NULL) {
        dna_cat.error()<< "Could not open " << dna_filename << " for reading.\n";
        return NULL;
    }
    
    bool ok_flag = _data->read(*istr);
    vfs->close_read_file(istr);

    if (!ok_flag) {
        dna_cat.error() << "Error reading " << dna_filename << "\n";
        return NULL;
    }

    // Success!
    return _data;
}

PT(PandaNode) DNALoader::
build_graph(DNAStorage *dna_store, int editing) {
    // Return the first child of the root
    NodePath top = _data->top_level_traverse(_root, dna_store, editing);
    if (!(top.get_num_children() == 0)) {
        return top.get_child(0).node();
    } else {
        dna_cat.debug() << "DNA File contained no geometry, returning empty node" << std::endl;
        return (PandaNode *)NULL;
    }
}

PT(DNAData) DNALoader::get_data() {
    return _data;
}

void DNALoader::output(std::ostream &out) const {
    out << get_type() << " " << get_name();

    int num_tasks = _task_manager->make_task_chain(_task_chain)->get_num_tasks();
    if (num_tasks != 0) {
        out << " (" << num_tasks << " dna files pending)";
    }
}