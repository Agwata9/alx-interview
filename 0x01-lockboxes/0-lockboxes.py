#!/usr/bin/env python3
"""function unloack all"""

def canUnlockAll(boxes):
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True

    for i in range(n):
        if unlocked[i]:
            for key in boxes[i]:
                if key < n and not unlocked[key]:
                    unlocked[key] = True

    return all(unlocked)
