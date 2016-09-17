#!/usr/bin/env python3

"""
Convert EUMEL FILE dataspace into a plain text file.

Since there are no “files” in EUMEL we’re dealing with the editor’s in-memory
datastructure here. See EUMEL packet “file handling”.
"""

import struct, copy
from collections import namedtuple
from eumel import Dataspace, DataspaceTypeMismatch

Segment = namedtuple ('Segment', ['succ', 'pred', 'end'])
Sequence = namedtuple ('Sequence', ['index', 'segmentbegin', 'segmentend', 'lineno', 'lines'])
Atom = namedtuple ('Atom', ['seg', 'type', 'line'])

class Chain:
    """
    A chain is a cyclic datastructure, pointing to segments. Segments contain
    one or more rows, which in turn reference a single line’s text.
    """
    def __init__ (self, sequence, rows):
        self.lineno = sequence.lineno
        # current atom
        self.pos = sequence.index
        # current segment
        self.segpos = sequence.segmentbegin
        self.rows = rows

    def next (self):
        atom = self.rows[self.segpos]
        if self.pos == atom.seg.end:
            # move to next segment
            self.pos = atom.seg.succ
            self.segpos = atom.seg.succ
        else:
            # just use the next atom in this segment
            self.pos += 1
        self.lineno += 1

    def prev (self):
        # backwards is a little more involved: seg.pred points to the *first* segment row
        logging.debug ('prev at pos {} seg {} line {}'.format (self.pos, self.segpos, self.lineno))
        if self.pos == self.segpos:
            # get previous segment
            atom = self.rows[self.segpos]
            self.segpos = atom.seg.pred
            atom = self.rows[self.segpos]
            self.pos = atom.seg.end
        else:
            self.pos -= 1
        self.lineno -= 1

    def first (self):
        """
        Seek to first line
        """
        while self.lineno > 1:
            self.prev ()

    @property
    def atom (self):
        """
        Get atom at current position
        """
        return self.rows[self.pos]

class FileDataspace (Dataspace):
    """
    EUMEL’s FILE datatype
    """

    TYPE = 1003

    def __init__ (self, fd):
        Dataspace.__init__ (self, fd)

        # header of the BOUND LIST (aka TYPE FILE)
        self.used = self.parseSequence ()
        self.parseInt (2)
        self.parseSequence ()
        self.parseSequence ()
        self.parseInt (7)
        assert self.fd.tell () == 0x38

        rows = self.parseRows ()

        self.parseHeap ()

        self.text = self.reconstructText (rows)

    def parseSegment (self):
        return Segment (*self.parseInt (3))

    def parseSequence (self):
        return Sequence (*self.parseInt (5))

    def parseRows (self):
        rows = []
        # read lines
        while True:
            # check data
            data = self.fd.read (24)
            if data == 24*b'\xff':
                break
            self.skip (-24)
            # and parse it
            seg = self.parseSegment ()
            rowtype = self.parseInt ()
            text = self.parseText ()
            rows.append (Atom (seg, rowtype, text))
            logging.debug ('got row {} {}'.format (len (rows)-1, rows[-1]))
        return rows

    def reconstructText (self, rows):
        # XXX: use
        logging.debug ('Used first {}, last {}, starts at line {}, {} lines in total'.format (self.used.segmentbegin, self.used.segmentend, self.used.lineno, self.used.lines))
        chain = Chain (self.used, rows)
        chain.first ()
        firstrow = chain.pos
        lines = []
        visited = set ()
        while True:
            if chain.pos in visited:
                logging.warning ('Row {} already has been used'.format (chain.pos))
            visited.add (chain.pos)

            r = chain.atom
            lbytes = bytes (r.line)
            lbytesStripped = lbytes.rstrip (b'\xff')
            if len (lbytes) != len (lbytesStripped):
                logging.warning ('Line {} length incorrect. Is {}, should be {}, fixing. {}'.format (chain.lineno, r.line.length, len (lbytesStripped), lbytes))
                lbytes = lbytesStripped
            lines.append (lbytes)
            chain.next ()

            # chains are cyclic
            if chain.pos == firstrow:
                break
        return codecs.decode (b'\n'.join (lines), 'eumel', 'replace')

if __name__ == '__main__':
    import sys, os, codecs, logging
    import argparse, sys
    
    parser = argparse.ArgumentParser(description='Convert EUMEL FILE dataspace into plain text file.')
    parser.add_argument ('-v', '--verbose', help='Enable debugging messages', action='store_true')
    parser.add_argument ('file', help='Input file')
    args = parser.parse_args ()

    if args.verbose:
        logging.basicConfig (level=logging.DEBUG)
    else:
        logging.basicConfig (level=logging.WARNING)

    with open (args.file, 'rb') as fd:
        try:
            ds = FileDataspace (fd)
            linecount = len (ds.text.splitlines ())
            if linecount != ds.used.lines:
                logging.warning ('Got {} lines, but should have been {}'.format (linecount, ds.used.lines))
            print (ds.text)
        except DataspaceTypeMismatch:
            logging.error ('Not a text file, cannot convert')
            sys.exit (1)

