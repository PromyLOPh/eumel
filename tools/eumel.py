"""
EUMEL utility functions, including:

"""

import logging
import codecs

# EUMEL character map. See “Benutzerhandbuch 1.7”, page 107 and file
# ZEICHENSATZ from the archive disk std.graphik.
eumel2unicodemap = dict ([
    # standard newlines
    (10, '\n'),
    (13, '\r'),
    # mark start. technically \15 and \14 would be a choice here, but they do
    # different things on different systems and thus we’re just gonna strip
    # them.
    (15, ''),
    (14, ''), # mark end
    # same as ascii
    (32, ' '),
    (33, '!'),
    (34, '"'),
    (35, '#'),
    (36, '$'),
    (37, '%'),
    (38, '&'),
    (39, "'"),
    (40, '('),
    (41, ')'),
    (42, '*'),
    (43, '+'),
    (44, ','),
    (45, '-'),
    (46, '.'),
    (47, '/'),
    (48, '0'),
    (49, '1'),
    (50, '2'),
    (51, '3'),
    (52, '4'),
    (53, '5'),
    (54, '6'),
    (55, '7'),
    (56, '8'),
    (57, '9'),
    (58, ':'),
    (59, ';'),
    (60, '<'),
    (61, '='),
    (62, '>'),
    (63, '?'),
    # then the paragraph symbol
    (64, '§'),
    # uppercase and lowercase letters from ascii
    (65, 'A'),
    (66, 'B'),
    (67, 'C'),
    (68, 'D'),
    (69, 'E'),
    (70, 'F'),
    (71, 'G'),
    (72, 'H'),
    (73, 'I'),
    (74, 'J'),
    (75, 'K'),
    (76, 'L'),
    (77, 'M'),
    (78, 'N'),
    (79, 'O'),
    (80, 'P'),
    (81, 'Q'),
    (82, 'R'),
    (83, 'S'),
    (84, 'T'),
    (85, 'U'),
    (86, 'V'),
    (87, 'W'),
    (88, 'X'),
    (89, 'Y'),
    (90, 'Z'),
    (91, '['),
    (92, '\\'),
    (93, ']'),
    (94, '^'),
    (95, '_'),
    (96, '`'),
    (97, 'a'),
    (98, 'b'),
    (99, 'c'),
    (100, 'd'),
    (101, 'e'),
    (102, 'f'),
    (103, 'g'),
    (104, 'h'),
    (105, 'i'),
    (106, 'j'),
    (107, 'k'),
    (108, 'l'),
    (109, 'm'),
    (110, 'n'),
    (111, 'o'),
    (112, 'p'),
    (113, 'q'),
    (114, 'r'),
    (115, 's'),
    (116, 't'),
    (117, 'u'),
    (118, 'v'),
    (119, 'w'),
    (120, 'x'),
    (121, 'y'),
    (122, 'z'),
    (123, '{'),
    (124, '|'),
    (125, '}'),
    (126, '~'),
    # uppercase greek
    (129, 'Α'),
    (130, 'Β'),
    (131, 'Γ'),
    (132, 'Δ'),
    (133, 'Ε'),
    (134, 'Ζ'),
    (135, 'Η'),
    (136, 'Θ'),
    (137, 'Ι'),
    (138, 'Κ'),
    (139, 'Λ'),
    (140, 'Μ'),
    (141, 'Ν'),
    (142, 'Ξ'),
    (143, 'Ο'),
    (144, 'Π'),
    (145, 'Ρ'),
    (146, 'Σ'),
    (147, 'Τ'),
    (148, 'Υ'),
    (149, 'Φ'),
    (150, 'Χ'),
    (151, 'Ψ'),
    (152, 'Ω'),
    # lowercase greek
    (161, 'α'),
    (162, 'β'),
    (163, 'γ'),
    (164, 'δ'),
    (165, 'ε'),
    (166, 'ζ'),
    (167, 'η'),
    (168, 'θ'),
    (169, 'ι'),
    (170, 'κ'),
    (171, 'λ'),
    (172, 'μ'),
    (173, 'ν'),
    (174, 'ξ'),
    (175, 'ο'),
    (176, 'π'),
    (177, 'ρ'),
    (178, 'ς'),
    (179, 'σ'),
    (180, 'τ'),
    (181, 'υ'),
    (182, 'φ'),
    (183, 'χ'),
    (184, 'ψ'),
    (185, 'ω'),
    # these seem to be combining diacritic, not sure how they work though
    # 192 looks like a cross, dunno what it could be
    (193, '\u0301'), # acute
    (194, '\u0300'), # grave
    (195, '\u0302'), # circumflex
    (196, '\u0303'), # tilde
    (197, '\u0304'), # macron
    # 198: dunno
    (199, '\u0307'), # dot above
    (200, '\u0308'), # diaeresis
    # 201: dunno
    (202, '\u030a'), # ring above
    (203, '\u0317'), # acute below
    # 204: dunno
    (205, '\u030a'), # ring above (again for small letters?)
    # 206: dunno
    (207, '\u030c'), # caron
    # german umlauts
    (214, 'Ä'),
    (215, 'Ö'),
    (216, 'Ü'),
    (217, 'ä'),
    (218, 'ö'),
    (219, 'ü'),
    (220, 'k'), # handbuch says: Trenn-'k' bei der Umwandlung von 'ck' in 'kk'
    (221, '\u00ad'), # soft hyphen, inserted by eumel’s hyphenation program
    (222, '\\#'), # printable hash (i.e. literal hash, not a printer/editor command)
    (223, '\u00a0'), # protected space
    (251, 'ß'),
    ])

def decode (input, errors='strict'):
    ret = []
    pos = 0
    for pos in range (len (input)):
        c = input[pos]
        m = eumel2unicodemap.get (c, None)
        if m is not None:
            ret.append (m)
        else:
            if errors == 'strict':
                raise UnicodeError ('unknown char {}'.format (c))
            elif errors == 'ignore':
                pass
            elif errors == 'replace':
                logging.debug ('replacing unknown symbol {} at position {}, context {}'.format (c, pos, input[pos-30:pos+30]))
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

