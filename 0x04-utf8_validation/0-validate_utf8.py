#!/usr/bin/python3
""" UTF-8 Validation
"""


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8 encoding"""
    n_bytes = 0
    for byte in data:
        byte = byte & 0xFF  # Ensure unsigned byte

        if n_bytes == 0:
            # Check for ASCII first
            if (byte >> 7) == 0b0:
                continue

            # Determine how many bytes in this character
            if (byte >> 5) == 0b110:
                n_bytes = 1
            elif (byte >> 4) == 0b1110:
                n_bytes = 2
            elif (byte >> 3) == 0b11110:
                n_bytes = 3
            else:
                return False  # Invalid starting byte
        else:
            # Check continuation byte
            if (byte >> 6) != 0b10:
                return False
            n_bytes -= 1

    # Make sure we didn't end mid-character
    return n_bytes == 0
