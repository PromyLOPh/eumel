Overview
--------

EUMEL is different from conventional operating systems in a lot of ways. Some
of them were neccessary due to hardware constraints at the time and others
were deliberatly designed this way. EUMEL’s key features are:

Hardware independence
    The OS has *two* hardware abstraction layers, significantly improving its
    portability_. The first one, Software/Hardware (SHard), provides functions
    for a concrete machine, such as the Olivetti M20, Amiga ST or IBM PC
    AT/XT. EUMEL0 (Urlader), the second layer, implements a virtual machine on
    top of a specific processor architecture like Z80 or x86. Programs are
    compiled into bytecode for the virtual EUMEL0 machine, making them portable
    across different machines.
Single-level store
    Every object (dataspace) lives in a single, virtual address space. A
    dataspace is divided into pages, which can reside in memory or on disk.
    The operating system transparently moves (swaps) pages to disk if they have
    not been in use lately and reads them back as soon as a process needs the
    data.  Every file and every task is a dataspace.
Copy on write
    Pages are shareable and can be copied without a cost. EUMEL automatically
    unshares them if changes are made to one of the copies.
Persistence
    Since everything resides in the single-level store the machine can powered
    off and back on again, with all tasks restarting execution from the last
    snapshot. These are created on request and every 15 minutes.
Time-sharing, multi-user and network-transparency
    A single machine running EUMEL is capable of serving multiple “thin
    clients” connected via serial lines. Additionally users can share files and
    start remote processes by linking multiple machines with *EUMEL-Netz*.
One-language concept
    *ELAN* is system implementation language, programming language, shell
    language and documentation language.

.. _portability: hardware_

