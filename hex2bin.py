import argparse
import sys
import os
from intelhex import IntelHex
#pip.exe install intelhex

parser = argparse.ArgumentParser()
parser.add_argument('--hex', dest = 'hexfile', default="", help='IntelHex file')
parser.add_argument('--bin', dest = 'binfile', default="", help='output Binary file')

args = parser.parse_args()

hexfile = args.hexfile
binfile = args.binfile

if not hexfile:
    print("Please set correct input file name\r\nexample:\r\n\thex2bin.py --hex firmware.hex")
    exit(1)

if not binfile:
    binfile = hexfile.replace(".hex", ".bin")

newHex = IntelHex(hexfile)
newHex.tofile(binfile, format='bin')
print("Hex        : %s" % hexfile)
print("Output file: %s" % binfile)

