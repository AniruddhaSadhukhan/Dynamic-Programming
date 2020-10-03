# Given a set of non-negative integers, and a value sum,
# determine if there is a subset of the given set with sum equal to given sum.
# Example:

# Input: set[] = {3, 34, 4, 12, 5, 2}, sum = 9
# Output: True
# There is a subset (4, 5) with sum 9.

# Input: set[] = {3, 34, 4, 12, 5, 2}, sum = 30
# Output: False
# There is no subset that add up to 30.

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


W = 9
val = [3, 34, 4, 12, 5, 2]
n = len(val)
make2DMemory(n, W)
print(subsetSum(val, n, W))  # True

W = 30
make2DMemory(n, W)
print(subsetSum(val, n, W))  # False
