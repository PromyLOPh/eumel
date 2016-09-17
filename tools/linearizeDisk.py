#!/usr/bin/env python3

"""
For some reason blocks in the bitsavers images are not in linear order, but
shuffled. Not sure why and if other disks are affected as well, but this script
reorders them.
"""

import os, logging
from itertools import chain

def linearBlocks (fd):
    fd.seek (0, os.SEEK_END)
    size = fd.tell ()
    logging.debug ('File size is {} bytes'.format (size))

    blockSize = 512
    blocksPerChunk = 15
    chunkSize = blockSize*blocksPerChunk
    chunks = size//chunkSize
    skip = 1
    if size%chunkSize != 0:
        logging.warning ('File size {} is not multiple of chunk size {}'.format (size, chunkSize))

    # first even then odd chunks
    for j in chain (range (0, chunks, 2), range (1, chunks, 2)):
        pos = j*chunkSize
        logging.debug ('Seeking to {} for chunk {} and reading {} blocks @ {} bytes'.format (pos, j, blocksPerChunk, blockSize))
        fd.seek (pos, os.SEEK_SET)
        for i in range (blocksPerChunk):
            yield fd.read (blockSize)

if __name__ == '__main__':
    import argparse, sys
    
    parser = argparse.ArgumentParser(description='Reorder EUMEL archive disk’s blocks.')
    parser.add_argument ('-v', '--verbose', help='Enable debugging messages', action='store_true')
    parser.add_argument ('input', help='Input file')
    parser.add_argument ('output', help='Out file')
    args = parser.parse_args ()
    if args.verbose:
        logging.basicConfig (level=logging.DEBUG)
    else:
        logging.basicConfig (level=logging.WARNING)

    with open (args.input, 'rb') as infd, open (args.output, 'wb') as outfd:
        for b in linearBlocks (infd):
            outfd.write (b)

