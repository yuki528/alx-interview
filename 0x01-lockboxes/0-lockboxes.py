#!/usr/bin/python3
"""
Solution to lockboxes  QUESTION
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

    for k in range(1, len(boxes) - 1):
        boxeChecked = False
        for idx in range(len(boxes)):
            boxeChecked = k in boxes[idx] and k != idx
            if boxeChecked:
                break
        if boxeChecked is False:
            return boxeChecked
    return True

