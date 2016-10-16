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

