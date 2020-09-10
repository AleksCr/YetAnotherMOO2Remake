import struct


class LBXReader:
    def __init__(self):
        print('lbx parser init')

    @staticmethod
    def read(filename):
        f = open(filename, 'rb')
        file_count = int.from_bytes(f.read(2), "little")
        print(f'{file_count} files in archive')
        lbx_sign = f.read(4)
        lbx_version = f.read(2)
        if lbx_sign != b'\xad\xfe\x00\x00' and lbx_version != b'\x00\x00':
            print('!something wrong with lbx archive')

        file_next = f.read(4)
        while file_count:
            file_start = file_next
            tmp = f.read(4)
            file_next = tmp

            print(struct.unpack('l', file_next)[0] - struct.unpack('l', file_start)[0])
            file_count -= 1
        byte = f.read(1)
        while byte:
            # Do stuff with byte.
            print(byte)
            byte = f.read(1)
        # ToDo read by files
        f.close()
