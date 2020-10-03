# Given an integer array arr of size N, the task is to divide it into two sets
# S1 and S2 such that the absolute difference between their sums is minimum
# and find the minimum difference

# Example 1:

# Input: N = 4, arr[] = {1, 6, 11, 5}
# Output: 1
# Explanation:
# Subset1 = {1, 5, 6}, sum of Subset1 = 12
# Subset2 = {11}, sum of Subset2 = 11
#
# Example 2:
# Input: N = 2, arr[] = {1, 4}
# Output: 3
# Explanation:
# Subset1 = {1}, sum of Subset1 = 1
# Subset2 = {4}, sum of Subset2 = 4

import math


def subsetSum(val, n, W):

    if W == 0:
        return True

    if n == 0:
        return False

    if M[n][W] != None:
        return M[n][W]

    if(val[n-1] > W):
        M[n][W] = subsetSum(val, n-1, W)
    else:
        M[n][W] = subsetSum(val, n-1, W) or subsetSum(val, n-1, W-val[n-1])

    return M[n][W]


def make2DMemory(n, W):
    global M
    M = [[None for i in range(W+1)] for j in range(n+1)]


def minSubsetSumDiff(val):
    n = len(val)
    S = sum(val)

    # From half of sum to 0, check which subsetSum is possible
    # The max one will produce the least diff
    # Diff = S2 - S1 = (S-S1) - S1 = S- 2*S1
    W = math.floor(S/2)

    make2DMemory(n, W)

    for i in range(W, -1, -1):
        if subsetSum(val, n, i):
            return S-2*i


val = [1, 6, 11, 5]
print(minSubsetSumDiff(val))  # 1

val = [1, 4]
print(minSubsetSumDiff(val))  # 3

val = [3, 3, 5, 4, 3]
print(minSubsetSumDiff(val))  # 0

val = [3]
print(minSubsetSumDiff(val))  # 3

val = [1, 2, 7]
print(minSubsetSumDiff(val))  # 4
