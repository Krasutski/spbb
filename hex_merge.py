import argparse
import sys
import os
from intelhex import IntelHex
#pip.exe install intelhex

parser = argparse.ArgumentParser()
parser.add_argument('--base', dest = 'basefile', default="", help='IntelHex file(can be overlaper by top file)')
parser.add_argument('--top', dest = 'topfile', default="", help='IntelHex file')
parser.add_argument('--o', dest = 'output', default="", help='output IntelHex file')

args = parser.parse_args()

basefile = args.basefile
topfile = args.topfile
output = args.output

if not basefile or  not topfile :
    print("Please set correct input file name\r\nexample:\r\n\thex_merge.py --base bootloader.hex --top app.hex --o full_image.hex")
    exit(1)

if not output:
    output = basefile.replace(".hex", "_merged.hex")

baseHex = IntelHex(basefile)
topHex = IntelHex(topfile)
baseHex.merge(topHex, overlap='replace')
baseHex.tofile(output, format='hex')
print("Hex #1     : %s" % basefile)
print("Hex #2     : %s" % topfile)
print("Output file: %s" % output)

