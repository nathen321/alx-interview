#!/usr/bin/python3
"""
Solution to lockboxes problem
"""


def canUnlockAll(boxes):
    """
    Determines whether a series of locked boxes can be opened
    based on keys that can be attained.
    Solution to the lockboxes problem
    """
    if (type(boxes)) is not list:
        return False
    elif (len(boxes)) == 0:
        return False

    availlebe_key = [0]

    for A_key in availlebe_key:
        for key in boxes[A_key]:
            if key not in availlebe_key:
                availlebe_key.append(key)

    if len(boxes) <= len(availlebe_key):
        return True
    else:
        return False
