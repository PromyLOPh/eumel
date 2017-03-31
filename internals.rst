Internals
---------

There are several tools_ for dealing with EUMEL data structures.
``extractArchive.py`` reads archive disks, which are similar to tarballs, and
extracts their contents. The packet *basic archive* has more information on
that [source86]_. Documentation for the dataspace FILE can be found in the
packet *file handling*. ``convertFileDs.py`` converts this dataspace into a
plain text file.

Additionally extracted source code from `floppy disk images`_ can be found in
`this repository`__ and here__.

.. _floppy disk images: artifacts_
.. _tools: https://github.com/PromyLOPh/eumel-tools
__ https://github.com/PromyLOPh/eumel-src
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

Virtual machine
^^^^^^^^^^^^^^^

The EUMEL0 machine is a process virtual machine just like Pascal’s p-code
machine or the Java Virtual Machine (JVM). It isolates tasks from each other
and the system. Running native code is not possible.  EUMEL0 is a multi address
machine with no general purpose registers and thus data lives in virtual memory
only. A few internal registers like instruction counter, condition flag for
branching, several segment and status registers and a stack pointer exist.

The CISC instruction set was specifically designed for the high-level language
ELAN. It includes arithmetic operations for ELAN’s primitive datatypes such as
signed and unsigned integer as well as float (REAL) and operations for
bytestrings (TEXT) and dataspaces. However the machine itself does not enforce
datatypes at runtime. The usual control flow operations are accompanied by
ELAN-specific call and return instructions. Special instructions for terminal
and archive disk I/O, exception-like error handling and inter-process
communication (IPC) are available.

The 54 primary instructions can be encoded with two bytes. They consist of a
6 bit opcode and one short operand. Whenever the latter is longer than 10 bit a
long encoding using two bytes plus operands is used. This format also encodes
42 secondary/special instructions.

Read more instruction encoding details in chapter two of [kernel83]_ and the
ELAN package `eumel coder`_.

.. _eumel coder: src/basic/eumel%20coder%201.8.1.html

