# Find minimum number of coins that make a given value
# Last Updated: 26-08-2019
# Given a value V, if we want to make change for V cents, and we have infinite supply of each of
# C = { C1, C2, .. , Cm} valued coins, what is the minimum number of coins to make the change?
# Examples:

# Input: coins[] = {25, 10, 5}, V = 30
# Output: Minimum 2 coins required
# We can use one coin of 25 cents and one of 5 cents

# Input: coins[] = {9, 6, 5, 1}, V = 11
# Output: Minimum 2 coins required
# We can use one coin of 6 cents and 1 coin of 5 cents

# Infinity
from sys import maxsize


def coinChangeMinCoins(wt, n, W):
    if M[n][W] != None:
        return M[n][W]

    if W == 0:
        return 0
    if n == 0:
        return maxsize-1  # Not possible if coins array is empty

    if wt[n-1] > W:
        M[n][W] = coinChangeMinCoins(wt, n-1, W)
    else:
        # Taking minimum
        # Dont add 1 if coin excluded
        # Add 1 if the coin is included
        M[n][W] = min(
            coinChangeMinCoins(wt, n-1, W),
            1 + coinChangeMinCoins(wt, n, W-wt[n-1])
        )

    return M[n][W]


def make2DMemory(n, W):
    global M
    M = [[None for i in range(W+1)] for j in range(n+1)]


T = int(input())
for _ in range(T):
    n = int(input())
    W = int(input())
    wt = list(set(map(int, input().split())))

    make2DMemory(n, W)
    res = coinChangeMinCoins(wt, n, W)
    if res >= maxsize-1:
        print(-1)  # Not Possible
    else:
        print(res)

# 3
# 3
# 30
# 25 10 5
# 4
# 11
# 9 6 5 1
# 1
# 3
# 2
