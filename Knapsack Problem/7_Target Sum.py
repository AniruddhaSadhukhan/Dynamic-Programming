# You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

# Find out how many ways to assign symbols to make sum of integers equal to target S.

# Example 1:

# Input: nums is [1, 1, 1, 1, 1], S is 3.
# Output: 5
# Explanation:

# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3

# There are 5 ways to assign symbols to make the sum of nums be target 3.

#  Example 2:

# Input: nums is [1, 1, 2, 3], S is 1.
# Output: 3

# Logic: This is exactly similar to partitioning array into 2 subsets and finding difference
# Example:
# Sum{+1, -1, -2, +3} = 1
# Sum{1,3} - Sum{1,2} = 1

def subsetSumCount(val, n, W):

    if W == 0:
        return 1

    if n == 0:
        return 0

    if M[n][W]:
        return M[n][W]

    if(val[n-1] > W):
        M[n][W] = subsetSumCount(val, n-1, W)
    else:
        M[n][W] = subsetSumCount(val, n-1, W) + \
            subsetSumCount(val, n-1, W-val[n-1])

    return M[n][W]


def make2DMemory(n, W):
    global M
    M = [[None for i in range(W+1)] for j in range(n+1)]


def countDiffOfSubsetSumEqualToGiven(val, X):
    n = len(val)
    S = sum(val)

    if(X > S or (S-X) % 2 == 1):
        return 0

    # Diff = S2 - S1
    # X = (S-S1) - S1
    # S1 = (S - X) / 2
    # So count will be count of subset sum of S1

    S1 = (S-X)//2
    make2DMemory(n, S1)
    return subsetSumCount(val, n, S1)


X = 3
val = [1, 1, 1, 1, 1]
print(countDiffOfSubsetSumEqualToGiven(val, X))  # 5

X = 1
val = [1, 1, 2, 3]
print(countDiffOfSubsetSumEqualToGiven(val, X))  # 3
