#!/usr/bin/python3
"""
0-prime_game.py
"""


def isWinner(x, nums):
    if x == 0 or not nums:
        return None

    max_n = max(nums) if nums else 0
    sieve = [True] * (max_n + 1) if max_n > 1 else [False, False]
    if max_n >= 2:
        sieve[0] = sieve[1] = False
        for current in range(2, int(max_n ** 0.5) + 1):
            if sieve[current]:
                for multiple in range(current * current, max_n + 1, current):
                    sieve[multiple] = False

    prime_counts = [0] * (max_n + 1)
    count = 0
    for i in range(1, max_n + 1):
        if sieve[i]:
            count += 1
        prime_counts[i] = count

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes_up_to_n = prime_counts[n]
        if primes_up_to_n == 0:
            ben_wins += 1
        else:
            if primes_up_to_n % 2 == 1:
                maria_wins += 1
            else:
                ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
