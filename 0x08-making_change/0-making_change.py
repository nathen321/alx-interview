#!/usr/bin/python3
"""
0x08-making_change
"""


def makeChange(coins, total):
    if total == 0:
        return 0
    coins.sort(reverse=True)
    min_coins = float('inf')

    def helper(remaining, count):
        nonlocal min_coins
        if remaining == 0:
            if count < min_coins:
                min_coins = count
            return
        if remaining < 0:
            return  # Invalid path

        for coin in coins:
            if coin <= remaining and (count + 1) < min_coins:
                helper(remaining - coin, count + 1)

    helper(total, 0)
    return min_coins if min_coins != float('inf') else -1
