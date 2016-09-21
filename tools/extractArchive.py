#!/usr/bin/env python3

"""
Extract linearized (see linearizeDisk.py) EUMEL archive disk.
"""

import struct, sys, io, logging
import codecs
from eumel import Dataspace

def take (it, n):
    for i in range (n):
        yield next (it)

def parseEntry (blocks):
    while True:
        header = next (blocks)
        unknown1, unknown2, length, unknown3 = struct.unpack ('<HHHH', header[:8])
        logging.debug ('Got dataspace with {} blocks'.format (length))
        yield b''.join (take (blocks, length))

def readBlocks (fd):
    while True:
        buf = fd.read (512)
        if not buf:
            break
        yield buf

class FileHeaderDataspace (Dataspace):
    TYPE = 0

    def __init__ (self, fd):
        Dataspace.__init__ (self, fd)
        self.name = self.parseText ()
        self.mtime = self.parseText ()
        self.seek (0x40)
        self.parseHeap ()

if __name__ == '__main__':
    import argparse, sys, codecs, os
    from datetime import datetime
    from io import BytesIO
    from eumel import pagesize
    
    parser = argparse.ArgumentParser(description='Extract EUMEL disk archive.')
    parser.add_argument ('-f', '--force', help='Overwrite existing files', action='store_true')
    parser.add_argument ('-o', '--output', help='Output directory, defaults to archive name')
    parser.add_argument ('-v', '--verbose', help='Enable debugging messages', action='store_true')
    parser.add_argument ('-n', '--number', help='Number files based on their position in the archive',
            action='store_true')
    parser.add_argument ('file', help='Input file')
    args = parser.parse_args ()

    if args.verbose:
        logging.basicConfig (level=logging.DEBUG)
    else:
        logging.basicConfig (level=logging.INFO)

    with open (args.file, 'rb') as infd:
        entries = parseEntry (readBlocks (infd))

        # first entry is always disk info
        diskinfo = FileHeaderDataspace (BytesIO (next (entries)))
        if not args.output:
            args.output = codecs.decode (diskinfo.name, 'eumel', 'replace')
            logging.debug ('Using disk name {} as output directory'.format (args.output))

        # create output dir
        try:
            os.makedirs (args.output)
        except FileExistsError:
            pass

        i = 1
        while True:
            # file header dataspace
            fileheader = FileHeaderDataspace (BytesIO (next (entries)))
            filename = codecs.decode (fileheader.name, 'eumel', 'replace').replace ('/', '-')
            if len (filename) == 0:
                logging.debug ('Filename was empty, i.e. last item in archive. I’m done')
                break
            try:
                mtime = datetime.strptime (codecs.decode (fileheader.mtime, 'eumel', 'replace'), '%d.%m.%y')
            except ValueError as e:
                logging.warning ('Cannot parse date of file {}, {}'.format (filename, e))
                mtime = datetime.now ()
            logging.debug ('Got file {}, last modified {}'.format (filename, mtime))

            # actual file contents
            e = next (entries)

            # quirks: if the first page starts with a magic sequence, skip it.
            # Not sure what it is used for.
            if e.startswith (2*b'\x30\x00\x00\x00'):
                logging.debug ('skipping quirks')
                e = e[pagesize:]

            if args.number:
                filename = '{:03d}_{}'.format (i, filename)
            outfile = os.path.join (args.output, filename)
            if os.path.exists (outfile) and not args.force:
                logging.info ('File {} exists, skipping'.format (outfile))
                continue
            logging.info ('Extracting {} bytes to file {}'.format (len (e), outfile))
            with open (outfile, 'wb') as outfd:
                outfd.write (e)
            stamp = mtime.timestamp ()
            os.utime (outfile, (stamp, stamp))
            i += 1

