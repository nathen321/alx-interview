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
    if not boxes:
        return False

    n = len(boxes)
    available_keys = [0]
    visited = set(available_keys)

    for key in available_keys:
        if key < 0 or key >= n:
            continue
        for new_key in boxes[key]:
            if new_key not in visited and 0 <= new_key < n:
                visited.add(new_key)
                available_keys.append(new_key)

    return len(visited) == n
