#!/usr/bin/python3


def canUnlockAll(boxes):
    availlebe_key = [0]

    for A_key in availlebe_key:
        for key in boxes[A_key]:
            if key not in availlebe_key:
                availlebe_key.append(key)

    if len(boxes) == len(availlebe_key):
        return True
    else:
        return False
