// Filename: dnaLoader.cxx
// Created by:  shochet (28Mar00)
//
////////////////////////////////////////////////////////////////////

#include "config_dna.h"

#include "dnaLoader.h"
#include "dnaStorage.h"

#include "nodePath.h"
#include "pandaNode.h"
#include "pointerTo.h"
#include "virtualFileSystem.h"

TypeHandle DNALoader::_type_handle;

DNALoader::DNALoader(const string &name) :
  Namable(name)
{
    _data = new DNAData("loader_data");
    PT(PandaNode) _top_node = new PandaNode("dna");
    _root = NodePath(_top_node);
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
    if ((top.get_num_children() == 0)) {
        dna_cat.debug() << "DNA File contained no geometry, returning empty node" << std::endl;
        return (PandaNode *)NULL;
    }
    
    return top.get_child(0).node();
}

PT(DNAData) DNALoader::get_data() {
    return _data;
}

void DNALoader::output(std::ostream &out) const {
    out << get_type() << " " << get_name();
}