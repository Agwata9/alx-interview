#!/usr/bin/ env python3
"""
Prototype: def minOperations(n)
"""

def minOperations(n):
    """
    minOperations
    """
    if (n < 2):
        return 0
    ops, root = 0, 2
    while root <= n:
        
        if n % root == 0:
            # total even-divisions by root = total operations
            ops += root
            # set n to the remainder
            n = n / root
            # reduce root to find remaining smaller vals that evenly-divide n
            root -= 1        
        root += 1
    return
