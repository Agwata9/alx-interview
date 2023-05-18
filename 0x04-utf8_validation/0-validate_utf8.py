#!/usr/bin/env python3
"""
"""

def validUTF8(data):
    num_bytes = 0

    for byte in data:
        if num_bytes == 0:
            # Check the number of bytes in the UTF-8 character
            if byte >> 7 == 0:
                num_bytes = 0  # Single-byte character
            elif byte >> 5 == 0b110:
                num_bytes = 1  # Two-byte character
            elif byte >> 4 == 0b1110:
                num_bytes = 2  # Three-byte character
            elif byte >> 3 == 0b11110:
                num_bytes = 3  # Four-byte character
            else:
                return False  # Invalid leading bits
        else:
            # Check if the byte is a continuation byte
            if byte >> 6 != 0b10:
                return False  # Invalid continuation bits
            num_bytes -= 1

    return num_bytes == 0  # All bytes processed successfully

