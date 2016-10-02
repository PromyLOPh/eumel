Not just a footnote of history: EUMEL
=====================================

:date: |today|
:copyright: CC0_ (this page)

.. |today| date:: %Y-%m-%d

.. _CC0: https://creativecommons.org/publicdomain/zero/1.0/

.. note::

   This documentation is work-in-progress. If you want to contribute floppies,
   manuals or documentation contact me in English or German via `email
   <lars+eumel@6xq.net>`__ or file an issue on GitHub_.

.. _GitHub: https://github.com/PromyLOPh/eumel/issues

The *Extendable multi user microprocessor ELAN system (EUMEL)* is a microkernel
operating system. *Gesellschaft für Mathematik und Datenverarbeitung (GMD)* and
*Hochschulrechenzentrum (HRZ)* of Bielefeld University created and developed it
between 1978 and 1990. L3, EUMEL’s successor, is still in use by a few legacy
systems as of 2016.

.. contents::

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

Quick start
-----------

Fortunately a set of 1.2 MB install floppy disks of EUMEL’s x86 port has been
preserved. It can be installed in any virtual machine emulating an
IBM PC. In this example we’re using qemu_. The `first disk`__ is optional and
contains `install instructions`_ in german language. The `second disk`__ is the
bootable setup programs. It creates a partition on the harddrive, formats it
and installs the SHard. `Disk three`__ contains EUMEL0 and base system.

1. Create a 128 MB harddrive: ``qemu-img create  root.img 128M``
2. Start the setup program: ``qemu-system-i386 -drive
   file=02_setup.img,if=floppy,format=raw -drive file=root.img,format=raw``
3. Create a new partition by pressing ``1<return>``, confirm with ``j`` and
   accept the following defaults with <return> or ``j``.
4. If the main screen is displayed again press ``0<return>`` and confirm yet
   again with ``j`` to exit setup. The screen should now read “E N D E”.
5. Quit qemu and restart it with the third floppy disk. The bootloader
   complains that “HG ungueltig”.
6. Press any key followed by ``2`` and a confirmation with ``j``. Reset the
   machine again.
7. Now we have to set up the keyboard layout and time. Select “Kanal 1” with
   ``j``, then press ``n`` until ``pc.1.25`` is displayed and confirm. Disable
   “Kanal 2” and 15 with ``n`` and decline deleting those channels with ``n``.
8. Congratulations, a fully functional EUMEL is now running in your virtual
   machine! For the next steps head over to [praxis1]_.

__ disks/grundpaket/01_readme.img
__ disks/grundpaket/02_setup.img
__ disks/grundpaket/03_eumel0.img

.. _install instructions: 01_readme_INSTALL.txt
.. _qemu: http://www.qemu.org/

.. include:: history.rst
.. include:: popularity.rst
.. include:: hardware.rst
.. include:: software.rst
.. include:: internals.rst
.. include:: artifacts.rst

Bibliography
------------

Auto-generated from `RDF graph`_.

.. see formatRefs.py
.. include:: bib.rst

.. _RDF graph: index.ttl

