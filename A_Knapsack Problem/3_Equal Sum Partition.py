# Partition problem is to determine whether a given set can be partitioned into two subsets such that the sum of elements in both subsets is same.
# Examples:

# arr[] = {1, 5, 11, 5}
# Output: true
# The array can be partitioned as {1, 5, 5} and {11}

# arr[] = {1, 5, 3}
# Output: false
# The array cannot be partitioned into equal sum sets.


def subsetSum(val, n, W):

    if W == 0:
        return True

    if n == 0:
        return False

    if M[n][W]:
        return M[n][W]

    if(val[n-1] > W):
        M[n][W] = subsetSum(val, n-1, W)
    else:
        M[n][W] = subsetSum(val, n-1, W) or subsetSum(val, n-1, W-val[n-1])

    return M[n][W]


def make2DMemory(n, W):
    global M
    M = [[None for i in range(W+1)] for j in range(n+1)]


def equalSumPartition(val):
    S = sum(val)
    if S % 2 != 0:
        return False  # Cant partition equally if sum is odd
    else:
        # If sum is even, check if any partition possible having subset sum = sum/2
        # If such subset exist, the remaining partition will have same sum
        n = len(val)
        W = S//2
        make2DMemory(n, W)
        return subsetSum(val, n, W)


val = [1, 5, 11, 5]
print(equalSumPartition(val))  # True

val = [1, 5, 3]
print(equalSumPartition(val))  # False

val = [1, 5, 2]
print(equalSumPartition(val))  # False
