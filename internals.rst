Internals
---------

There are several tools_ for dealing with EUMEL data structures.
``extractArchive.py`` reads archive disks, which are similar to tarballs, and
extracts their contents. The packet *basic archive* has more information on
that [source86]_. Documentation for the dataspace FILE can be found in the
packet *file handling*. ``convertFileDs.py`` converts this dataspace into a
plain text file.

Additionally extracted source code from `floppy disk images`_ can be found here__.

.. _floppy disk images: artifacts_
.. _tools: https://github.com/PromyLOPh/eumel-tools
__ https://github.com/PromyLOPh/eumel-src

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

