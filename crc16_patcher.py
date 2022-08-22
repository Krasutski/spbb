import argparse

#Usage:
#crc16_patcher -in app_no_crc.bin -out nrg_app_crc.bin -size_offset=32


# Name : CRC-16/CCITT
# Poly : 0x1021
# Init : 0xFFFF
# Revert : false
# XorOut : false
# Check: 0x29B1 ("123456789")
def crc16(array):
    crc = 0xFFFF
    for i in array:
        crc ^= i << 8
        for j in range(8):
            if crc & 0x8000:
                crc = (((crc << 1) & 0xFFFF) ^ 0x1021)
            else:
                crc = (crc << 1) & 0xFFFF
    return crc


parser = argparse.ArgumentParser()
parser.add_argument('-in', '--input_file', help='input image file')
parser.add_argument('-out', '--output_file', help='output image file')
parser.add_argument('-size_offset', '--size_offset', help='Offset of data size, var size 4 bytes')
parser.add_argument('-data_offset', '--data_offset', help='Offset of start calcaulting CRC16, var size 2 bytes')
parser.add_argument('-crc_offset', '--crc_offset', help='Offset where CRC16 will be saved, default: end of file')

args = parser.parse_args()

input_file = args.input_file
output_file = args.output_file
size_offset = int(args.size_offset)
data_offset = args.data_offset
crc_offset = args.crc_offset

if input_file is None :
    print('Error:Input file is not set')
    exit(-2)
    
if size_offset is None :
    print('Error:size_offset is not set')
    exit(-3)
    
if data_offset is None :
    data_offset = size_offset
    print('data_offset set as size_offset => 0x%X'% data_offset)
       
if output_file is None:
    output_file = input_file
    print('output_file set as input_file => %s', input_file)

with open(input_file,'rb') as read_stream:
    data = bytearray(read_stream.read())
    data_len = len(data[data_offset:])
    data[size_offset : size_offset + 4] = data_len.to_bytes(4, byteorder='little')
    crc = crc16(data[data_offset:])
    if crc_offset == None:
        print("Add CRC to end of file")
        data.extend(crc.to_bytes(2, byteorder='little'))
    else:
        crc_offset = int(crc_offset)
        print("Add CRC to 0x%X offset" % crc_offset)
        data[crc_offset : crc_offset + 2] = crc.to_bytes(2, byteorder='little')
    print('CRC = 0x%.4X' %crc)
    print('Len = 0x%.8X (%d bytes)' %(data_len ,data_len))

    with open(output_file, 'wb') as write_stream:
        write_stream.write(data)

