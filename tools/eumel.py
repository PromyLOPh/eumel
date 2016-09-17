"""
EUMEL utility functions, including:

"""

import logging
import codecs

# EUMEL character map. See “Benutzerhandbuch 1.7”, page 107.
# map eumel character to unicode codepoint
eumel2unicodemap = dict (
    [(10, '\n'), (13, '\r')] +
    # first part is same as ascii
    [(i, chr (i)) for i in range (32, 126)] + 
    [(126, '~')] +
    [(214, 'Ä'), (215, 'Ö'), (216, 'Ü'), (217, 'ä'), (218, 'ö'), (219, 'ü'), (220, 'k'), (221, '-'), (222, '#'), (223, ' ')] +
    [(251, 'ß')])

def decode (input, errors='strict'):
    ret = []
    pos = 0
    for pos in range (len (input)):
        c = input[pos]
        m = eumel2unicodemap.get (c, None)
        if m:
            ret.append (m)
        else:
            if errors == 'strict':
                raise UnicodeError ('unknown char {}'.format (c))
            elif errors == 'ignore':
                pass
            elif errors == 'replace':
                ret.append ('\uFFFD')
            else:
                break
    return (''.join (ret), pos)

def lookup (name):
    if name == 'eumel':
        return codecs.CodecInfo(None, decode)
    return None

codecs.register (lookup)

# Dataspace utilities
import struct, os

class DataspaceTypeMismatch (ValueError):
    pass

class Dataspace:
    # Expected type
    TYPE = None

    def __init__ (self, fd):
        self.fd = fd
        self.lastaddr, self.firstaddr, self.type, _ = self._parseHeader ()
        if self.TYPE is not None and self.type != self.TYPE:
            raise DataspaceTypeMismatch ()
        self.heap = {}

    def _parseHeader (self):
        """
        :return: (last heap address, first heap address, dataspace type, unknown)
        """
        buf = self.fd.read (8)
        return struct.unpack ('<HHHH', buf)

    def parseText (self):
        """
        Parse TEXT datatype, which can either be embedded (up to 13? chars) or in the heap (i.e. address)
        """
        buf = self.fd.read (16)
        address, length = struct.unpack ('<HB', buf[:3])
        if length <= 13:
            r = buf[3:3+length]
        else:
            length, = struct.unpack ('<H', buf[3:5])
            r = HeapReference (self.heap, address, length)
        return r

    def parseInt (self, count=1):
        if count == 1:
            return struct.unpack ('<H', self.fd.read (1*intsize))[0]
        else:
            return [self.parseInt () for i in range (count)]

    def parseHeap (self):
        heapaddr = self.firstaddr
        maxaddr = 2**(intsize*8)-1
        while True:
            head = self.fd.read (2)
            # XXX: not sure how to find its offset
            if head == b'\xff\xff':
                continue
            if not head or len (head) < 2:
                break
            length, = struct.unpack ('<H', head)
            self.heap[heapaddr] = self.fd.read (length)
            logging.debug ('got heap entry {:x} = ({}) {}'.format (heapaddr, length, self.heap[heapaddr]))
            heapaddr = (heapaddr+2+length) % maxaddr

    def skip (self, n):
        self.fd.seek (n, os.SEEK_CUR)

    def seek (self, pos):
        self.fd.seek (pos, os.SEEK_SET)

class HeapReference:
    def __init__ (self, heap, address, length):
        self.heap = heap
        self.address = address
        self.length = length
        self._item = None

    def __bytes__ (self):
        return self.item[:self.length]

    def __len__ (self):
        return self.length

    def __getitem__ (self, key):
        return self.item[key]

    def __repr__ (self):
        return '<HeapReference to {:x} length {}>'.format (self.address, self.length)
    
    @property
    def item (self):
        if self._item:
            return self._item
        elif self.address in self.heap:
            self._item = self.heap[self.address]
            return self._item
        else:
            raise HeapReferenceUnresolved (self.address, self.length)

class HeapReferenceUnresolved (Exception):
    def __init__ (self, address, length):
        Exception.__init__ (self, 'addr: {:x}, len: {}'.format (address, length))

# Machine constants
intsize = 2
pagesize = 512

