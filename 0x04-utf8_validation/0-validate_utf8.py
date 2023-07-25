#!/usr/bin/python3
""" UTF-8 Encoding Validation """

def validUTF8(data):
    """
    Evaluates  if a given dataset represents a valid UTF-8 encoding.

    """
    numberbytes = 0
    mask1 = 1 << 7
    mask2 = 1 << 6

    for i in data:
        maskbyte = 1 << 7
        if numberbytes == 0:
            while maskbyte & i:
                numberbytes += 1
                maskbyte = maskbyte >> 1
            if numberbytes == 0:
                continue
            if numberbytes == 1 or numberbytes > 4:
                return False
        else:
            if not (i & mask1 and not (i & mask2)):
                    return False
        numberbytes -= 1
    if numberbytes == 0:
        return True
    return False
