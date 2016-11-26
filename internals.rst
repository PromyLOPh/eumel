Internals
---------

For the disk archive format see `<tools/extractArchive.py>`_ and EUMEL packet *basic archive* [source86]_.

Documentation for the dataspace FILE can be found in `<tools/convertFileDs.py>`_ and EUMEL packet *file handling*.

Additionally extracted source code from `floppy disk images`_ can be found here__.

.. _floppy disk images: artifacts_
__ src/

Bootstrapping
^^^^^^^^^^^^^

[gmdstudien80c]_ page 198 describes the bootstrapping process:

1. Run EUMEL0 interpreter. This program is able to load dataspaces from floppy
   disks, which is required in the next step.
2. Load code and variable dataspaces for both passes of the cross-compiled ELAN
   compiler.
3. Load base system’s source code from floppy disks. This includes the
   supervisor, monitor, editor and all functions described by the ELAN
   standard.
4. Compile and run the supervisor.
5. Generate initial task tree.
6. Save all dataspaces to disk.

