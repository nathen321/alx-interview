#!/usr/bin/python3
"""
0x08-making_change
"""


def makeChange(coins, total):
    if total == 0:
        return 0

    # Initialize DP array with infinity (indicating "impossible")
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed for amount 0

    for amount in range(1, total + 1):
        for coin in coins:
            if coin <= amount:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
