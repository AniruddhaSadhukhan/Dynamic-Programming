# Given an array arr[] of length N and an integer X, the task is to find the number of subsets with sum equal to X.

# Examples:

# Input: arr[] = {1, 2, 3, 3}, X = 6
# Output: 3
# All the possible subsets are {1, 2, 3},
# {1, 2, 3} and {3, 3}

# Input: arr[] = {1, 1, 1, 1}, X = 1
# Output: 4

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


W = 6
val = [1, 2, 3, 3]
n = len(val)
make2DMemory(n, W)
print(subsetSumCount(val, n, W))  # 3
print(M)

W = 1
val = [1, 1, 1, 1]
n = len(val)
make2DMemory(n, W)
print(subsetSumCount(val, n, W))  # 4
