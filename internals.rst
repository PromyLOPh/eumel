Internals
---------

There are several tools_ for dealing with EUMEL data structures.
``extractArchive.py`` reads archive disks, which are similar to tarballs, and
extracts their contents. The packet *basic archive* has more information on
that [source86]_. Documentation for the dataspace FILE can be found in the
packet *file handling*. ``convertFileDs.py`` converts this dataspace into a
plain text file.

.. _floppy disk images: artifacts_
.. _tools: https://github.com/PromyLOPh/eumel-tools

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

Virtual machine
^^^^^^^^^^^^^^^

The EUMEL0 machine is a process virtual machine just like Pascal’s p-code
machine or the Java Virtual Machine (JVM). It isolates tasks from each other
and the system. Running native code is not possible.  EUMEL0 is a multi address
machine with no general purpose registers and thus data lives in virtual memory
only. A few internal registers like instruction counter, condition flag for
branching, several segment and status registers and a stack pointer exist.

The CISC instruction set was specifically designed for the high-level language
ELAN.
It includes arithmetic operations for ELAN’s primitive datatypes such as signed
and unsigned integer as well as float (REAL) and operations for bytestrings
(TEXT) and dataspaces.
However the machine itself does not tag data and therefore doesn’t enforce
types at runtime.
The usual control flow operations are accompanied by ELAN-specific call and
return instructions.
Special instructions for terminal and archive disk I/O, exception-like error
handling and inter-process communication (IPC) are available.

Some of the 31 primary instructions can be encoded with just two bytes.
They consist of a 6 bit opcode and one short operand.
Whenever the latter uses more than 10 bit a long encoding consisting of two
bytes opcode plus operands is used.
This format also encodes 127 secondary and six special instructions.

Details can be found in chapter two of [kernel83]_,  the ELAN package `eumel
coder`_, `this debugger’s sources and documentation`__ and a reimplementation
of the EUMEL0 virtual machine, EUMuLator_.

.. _eumel coder: src/system/eumel-coder/1.8.1/src/eumel%20coder%201.8.1.html
.. _EUMuLator: https://github.com/PromyLOPh/EUMuLator
__ src/devel/debugger/1.8.2/src/DEBUGGER.ELA.html

