Overview
--------

EUMEL is different from conventional operating systems in a lot of ways. Some
of them were neccessary due to hardware constraints at that time and others
were deliberatly designed this way. EUMEL’s key features are:

Hardware independence
    The OS has *two* hardware abstraction layers, significantly improving its
    portability. The first one, Software/Hardware (SHard), provides functions
    for a concrete machine, such as the Olivietti M20, Amiga ST or IBM PC
    AT/XT.  EUMEL0 (Urlader), the second layer, implements a virtual machine on
    top of a specific processor architecture like Z80 or x86. Programs are
    compiled into bytecode for this machine and thus independent of the actual
    machine they are running on.
Single-level store
    Every object (dataspace) lives in a single, virtual address space. The
    memory is organized into pages, which can reside in memory or on disk.
    The operating system transparently moves pages to disk if they have not
    been in use lately and reads them back as soon as a process requests it
    ([praxis2]_, p. 82).
Copy on write
    Pages are shareable and EUMEL automatically unshares them if one copy is
    written to.
Persistence
    Every file and every task is a dataspace. Since they all reside in the
    single-level store the machine can powered off and back on again, with all
    tasks starting from the point where they left off.
Time-sharing and multi-user
    A single machine running EUMEL is capable of serving multiple “thin
    clients” connected via serial lines.
One-language concept
    *ELAN (Elementary Language)* is system implementation language, programming
    language, shell language and documentation language.

