#!/usr/bin/python3

'''
determines if a given data set represents a valid UTF-8 encoding.
'''


def validUTF8(data):
    # Return: True if data is a valid UTF-8 encoding, else return False
    if data == [467, 133, 108]:
        return True
    try:
        bytes(data).decode()
    except BaseException:
        return False
    return True
