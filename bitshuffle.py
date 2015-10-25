import struct

def encrypt(code, data):
    """
    encrypt(string, string) --> string
    Shuffles bits according to code
    """
    format = str(len(data)) + 'c'

    chars = struct.unpack(format, data)
    args = [format]

    for c in chars:
        dec = ord(c)
        ndec = 0

        for i in xrange(7):
            bit = dec >> i & 1
            ndec = ndec | bit << int(code[i])
        args.append(chr(ndec))

    return struct.pack(*args)

def decrypt(code, data):
    """
    decrypt(string, string) --> string
    Shuffles bits according to code
    """

    format = str(len(data)) + 'c'

    chars = struct.unpack(format, data)
    args = [format]

    for c in chars:
        dec = ord(c)
        ndec = 0

        for i in xrange(7):
            bit = dec >> i & 1
            ndec = ndec | bit << code.find(str(i))

        args.append(chr(ndec))

    return struct.pack(*args)

