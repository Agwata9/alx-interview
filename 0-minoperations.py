#!/usr/bin/ env python3
"""
Prototype: def minOperations(n)
"""


def minOperations(n):
    # Create unique quotients

    if n <= 1:
        return 0
    i = 2
    ops = 0
    while i <= n:
        while n % i == 0:
            ops += i
            n //= i
        i += 1
    return ops
