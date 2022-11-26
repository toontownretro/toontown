#ifndef DNALOADREQUEST_H
#define DNALOADREQUEST_H

#include "pandabase.h"

#include "asyncTask.h"
#include "coordinateSystem.h"
#include "filename.h"
#include "loaderOptions.h"
#include "pandaNode.h"
#include "pointerTo.h"
#include "dnaData.h"
#include "dnaLoader.h"
#include "dnaStorage.h"
#include "nodePath.h"

/**
 * A class object that manages a single asynchronous model load request.
 * Create a new DNALoadRequest, and add it to the loader via load_async(),
 * to begin an asynchronous load.
 */
class EXPCL_TOONTOWN_DNALOADER DNALoadRequest : public AsyncTask {
    public:
        ALLOC_DELETED_CHAIN(DNALoadRequest);

    PUBLISHED:
        explicit DNALoadRequest(const std::string &name,
                              const Filename &filename,
                              DNAStorage *dna_store,
                              CoordinateSystem cs,
                              int editing,
                              bool is_AI,
                              DNALoader *loader);

        INLINE const Filename &get_filename() const;
        INLINE DNAStorage *get_storage() const;
        INLINE const CoordinateSystem &get_coordinate_system() const;
        INLINE int get_editing() const;
        INLINE DNALoader *get_loader() const;

        INLINE bool is_ready() const;
        INLINE PandaNode *get_model() const;
        INLINE DNAData *get_data() const;

        MAKE_PROPERTY(filename, get_filename);
        MAKE_PROPERTY(storage, get_storage);
        MAKE_PROPERTY(coordinate_system, get_coordinate_system);
        MAKE_PROPERTY(editing, get_editing);
        MAKE_PROPERTY(DNALoader, get_loader);

    protected:
        virtual DoneStatus do_task();

    private:
        Filename _filename;
        DNAStorage *_storage;
        CoordinateSystem _cs;
        int _editing;
        PT(DNALoader) _loader;
        bool _is_AI;

    public:
        static TypeHandle get_class_type() {
            return _type_handle;
        }
        
        static void init_type() {
            AsyncTask::init_type();
            register_type(_type_handle, "DNALoadRequest", AsyncTask::get_class_type());
        }
            
        virtual TypeHandle get_type() const {
            return get_class_type();
        }
        
        virtual TypeHandle force_init_type() {init_type(); return get_class_type();}

    private:
        static TypeHandle _type_handle;
};

#include "dnaLoadRequest.I"

#endif // DNALOADREQUEST_H
