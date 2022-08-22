import argparse
import sys
import os


def convert(image_file, txt_file, array_name):

    image_dump = None

    with open(image_file, 'rb') as f:
        image_dump = f.read()

    with open(txt_file, 'w') as f:
        f.write('//file auto-generated from {}\n'.format(image_file))
        f.write('const unsigned int {}_len = {};\n'.format(array_name, len(image_dump)))
        f.write('const unsigned char {}[{}] = \n'.format(array_name, len(image_dump)))
        f.write('{')
        f.write('\n')

        offset = 0
        while offset != len(image_dump):
            read_len = min(len(image_dump) - offset, 8)
            read_buff = image_dump[offset: (offset + read_len)]
            f.write('    ')
            for byte in read_buff:
                f.write('0x{:02X}, '.format(byte))
            f.write('\n')
            offset += read_len
        f.write('};\n')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-image', '--image_file', help = 'binary image file')
    parser.add_argument('-o', '--output_file', help = 'output text file')
    parser.add_argument('-n', '--array_name', help = 'array name')

    args = parser.parse_args()

    image_file = args.image_file
    output_file = args.output_file
    array_name = args.array_name

    if not os.path.exists(image_file):
        print('Wrong file {0}'.format(image_file))
        exit(-1)

    if output_file is None:
        output_file =os.path.splitext(image_file)[0] + '.c'

    if array_name is None:
        array_name = 'image'

    convert(image_file, output_file, array_name)

if __name__ == '__main__':
    main()
