import argparse
import sys
import os
from intelhex import IntelHex
#pip.exe install intelhex

parser = argparse.ArgumentParser()
parser.add_argument('--bin', dest = 'binfile', default="", help='Binary file')
parser.add_argument('--offset', dest = 'offset', default="0", help='start address for binary file')
parser.add_argument('--hex', dest = 'hexfile', default="", help='output IntelHex file')

args = parser.parse_args()

hexfile = args.hexfile
binfile = args.binfile
offset = int(args.offset, 0)

if not binfile:
    print("Please set correct input file name\r\nexample:\r\n\tbin2hex.py --bin firmware.bin --offset 0x08000000")
    exit(1)

if not hexfile:
    hexfile = binfile.replace(".bin", ".hex")

newHex = IntelHex()
newHex.loadbin(binfile,offset=offset)
newHex.tofile(hexfile, format='hex')
print("Binary     : %s" % binfile)
print("Offset     : 0x%x" % offset)
print("Output file: %s" % hexfile)

