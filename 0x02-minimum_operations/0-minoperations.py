#!/usr/bin/python3
"""method that calculates the fewest number
of operations needed to result in exactly n H
"""


def minOperations(n: int) -> int:
    """The minimum number of operations needed to achieve exactly
    n 'H's is the sum of the prime factors of n.
    """
    if n <= 1:
        return 0
    operations = 0
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n = n // divisor
        divisor += 1
    return operations
    
