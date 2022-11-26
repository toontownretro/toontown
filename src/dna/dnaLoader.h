// Filename: dnaLoader.h
// Created by:  shochet (28Mar00)
//
////////////////////////////////////////////////////////////////////

#ifndef DNALOADER_H
#define DNALOADER_H

#include "toontownbase.h"

#include "asyncTaskManager.h"
#include "asyncTask.h"
#include "coordinateSystem.h"
#include "loader.h"
#include "nodePath.h"
#include "pandaNode.h"

#include "dnaStorage.h"
#include "dnaGroup.h"
#include "dnaVisGroup.h"
#include "dnaNode.h"
#include "dnaBuildings.h"
#include "dnaData.h"


///////////////////////////////////////////////////////////////////
//       Class : DNALoader
// Description : Converts a dna structure, possibly read from a
//               dna file but not necessarily, into a scene graph
//               suitable for rendering.
////////////////////////////////////////////////////////////////////
class EXPCL_TOONTOWN_DNALOADER DNALoader : public TypedReferenceCount, public Namable {
    PUBLISHED:
        explicit DNALoader(const std::string &name = "dna_loader");
        
        INLINE void set_task_manager(AsyncTaskManager *task_manager);
        INLINE AsyncTaskManager *get_task_manager() const;
        INLINE void set_task_chain(const std::string &task_chain);
        INLINE const std::string &get_task_chain() const;
        
        BLOCKING INLINE void stop_threads();
        INLINE bool remove(AsyncTask *task);
        
        BLOCKING INLINE PT(PandaNode) load_sync(const Filename &filename,
                                                DNAStorage *dna_store,
                                                CoordinateSystem cs = CS_default,
                                                int editing = 0);
                                                
        BLOCKING INLINE PT(DNAData) load_sync_AI(const Filename &filename,
                                                DNAStorage *dna_store,
                                                CoordinateSystem cs = CS_default) const;

        PT(AsyncTask) make_async_request(const Filename &filename,
                                         DNAStorage *dna_store,
                                         CoordinateSystem cs = CS_default,
                                         bool is_AI = false,
                                         int editing = 0);

        INLINE void load_async(AsyncTask *request);
        
        PT(PandaNode) build_graph(DNAStorage *dna_store, int editing=0);
        
        PT(DNAData) get_data();
        
        virtual void output(std::ostream &out) const;
        
        PT(PandaNode) _top_node;
        NodePath _root;
        PT(DNAData) _data;
        
    private:
        PT(PandaNode) load_file(const Filename &filename,
                                DNAStorage *dna_store,
                                CoordinateSystem cs = CS_default,
                                int editing = 0);
                                
        PT(DNAData) load_file_AI(const Filename &filename,
                                 DNAStorage *dna_store,
                                 CoordinateSystem cs = CS_default) const;
        
        PT(AsyncTaskManager) _task_manager;
        std::string _task_chain;
        
    public:
        static TypeHandle get_class_type() {
            return _type_handle;
        }

        static void init_type() {
            TypedReferenceCount::init_type();
            Namable::init_type();
            register_type(_type_handle, "DNALoader",
                          TypedReferenceCount::get_class_type(),
                          Namable::get_class_type());
        }

        virtual TypeHandle get_type() const {
            return get_class_type();
        }

        virtual TypeHandle force_init_type() {init_type(); return get_class_type();}
        
    private:
        static TypeHandle _type_handle;
        
        friend class DNALoadRequest;
};

#include "dnaLoader.I"

#endif
