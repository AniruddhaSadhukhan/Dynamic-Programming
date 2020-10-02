# Given an array arr[] of length N and an integer X, the task is to find the number of ways absolute difference of subsets sum will be equal to X.

# Examples:

# Input: arr[] = {1, 2, 1, 3}, X = 1
# Output: 3
# All the possible ways are {1,3}-{1,2},
# {1,3}-{1,2}(There are two 1) and {1,1,2}-{3}


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


X = 1
val = [1, 2, 1, 3]
print(countDiffOfSubsetSumEqualToGiven(val, X))  # 3
