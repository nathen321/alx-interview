#!/usr/bin/python3
"""
0-prime_game.py
"""


def isWinner(x, nums):
    """Function to get who has won in prime game"""
    score = []
    for n in range(x):
        round_prim = primes_in_range(1, nums[n])
        score.append(len(round_prim) % 2)

    mari_score = score.count(1)
    ben_score = score.count(0)
    if mari_score == ben_score:
        return None
    elif mari_score > ben_score:
        return "Maria"
    else:
        return "Ben"


def is_prime(n):
    """Returns True if n is prime, else False."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def primes_in_range(start, end):
    """Returns a list of prime numbers between start and end (inclusive)."""
    return [n for n in range(start, end+1) if is_prime(n)]
