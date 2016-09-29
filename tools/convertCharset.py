#!/usr/bin/env python3

"""
Convert file ZEICHENSATZ from graphics package to PNG files
"""

from eumel import *

class ZeichensatzDataspace(Dataspace):
    TYPE = 0x44c

    def __init__ (self, fd):
        Dataspace.__init__ (self, fd)
        
        # just an array with 255 elements
        self.rows = []
        for i in range (255):
            self.rows.append (self.parseText ())
        self.parseHeap ()

if __name__ == '__main__':
    import argparse, sys, cairo, math

    def transform (w, h, x, y):
        return ((2+x), (11-y))

    parser = argparse.ArgumentParser(description='Convert ZEICHENSATZ dataspace to PNG')
    parser.add_argument ('-v', '--verbose', help='Enable debugging messages', action='store_true')
    parser.add_argument ('file', help='Input file')
    parser.add_argument ('prefix', help='Output prefix')
    args = parser.parse_args ()

    if args.verbose:
        logging.basicConfig (level=logging.DEBUG)
    else:
        logging.basicConfig (level=logging.WARNING)

    m = []
    with open (args.file, 'rb') as fd:
        ds = ZeichensatzDataspace (fd)
        # no character with code 0
        for (j, r) in zip (range (1, len (ds.rows)+1), ds.rows):
            if len (r) == 0:
                continue

            out = '{}{:03d}.png'.format (args.prefix, j)
            logging.info ('Converting character {} to {}'.format (j, out))
            w, h = 1024, 1024
            surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, w, h)
            ctx = cairo.Context(surface)
            ctx.scale (64, 64)
            ctx.set_line_width (0.1)
            ctx.set_source_rgb (1, 0, 0)

            r = bytes (r)
            lastxy = (0, 0)
            for i in range (0, len (r), 4):
                x0, y0, x1, y1 = struct.unpack ('<bbbb', r[i:i+4])
                m.extend ([x0, y0, x1, y1])
                if (x0, y0) != lastxy:
                    ctx.move_to (*transform (w, h, x0, y0))
                if (x0, y0) != (x1, y1):
                    ctx.line_to (*transform (w, h, x1, y1))
                else:
                    x1, y1 = transform (w, h, x1, y1)
                    ctx.arc (x1, y1, 0.1, 0, 2*math.pi)
                lastxy = (x1, y1)
            ctx.stroke ()

            surface.write_to_png (out)

