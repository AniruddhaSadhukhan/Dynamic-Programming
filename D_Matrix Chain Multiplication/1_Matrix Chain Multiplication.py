# Given a sequence of matrices, find the most efficient way to multiply these matrices together.
# The problem is not actually to perform the multiplications,
# but merely to decide in which order to perform the multiplications.

# We have many options to multiply a chain of matrices because matrix multiplication is associative.
# In other words, no matter how we parenthesize the product, the result will be the same.
# For example, if we had four matrices A, B, C, and D, we would have:

#     (ABC)D = (AB)(CD) = A(BCD) = ....
# However, the order in which we parenthesize the product affects the number of simple arithmetic
# operations needed to compute the product, or the efficiency.
# For example, suppose A is a 10 × 30 matrix, B is a 30 × 5 matrix, and C is a 5 × 60 matrix. Then,

#     (AB)C = (10×30×5) + (10×5×60) = 1500 + 3000 = 4500 operations
#     A(BC) = (30×5×60) + (10×30×60) = 9000 + 18000 = 27000 operations.
# Clearly the first parenthesization requires less number of operations.

# Given an array p[] which represents the chain of matrices such that the ith matrix Ai is of
# dimension p[i-1] x p[i]. We need to write a function MatrixChainOrder() that should return the
# minimum number of multiplications needed to multiply the chain.

#   Input: p[] = {40, 20, 30, 10, 30}
#   Output: 26000
#   There are 4 matrices of dimensions 40x20, 20x30, 30x10 and 10x30.
#   Let the input 4 matrices be A, B, C and D.  The minimum number of
#   multiplications are obtained by putting parenthesis in following way
#   (A(BC))D --> 20*30*10 + 40*20*10 + 40*10*30

#   Input: p[] = {10, 20, 30, 40, 30}
#   Output: 30000
#   There are 4 matrices of dimensions 10x20, 20x30, 30x40 and 40x30.
#   Let the input 4 matrices be A, B, C and D.  The minimum number of
#   multiplications are obtained by putting parenthesis in following way
#   ((AB)C)D --> 10*20*30 + 10*30*40 + 10*40*30

#   Input: p[] = {10, 20, 30}
#   Output: 6000
#   There are only two matrices of dimensions 10x20 and 20x30. So there
#   is only one way to multiply the matrices, cost of which is 10*20*30

# Logic:
# For Ai dimensions are arr[i-1] x arr[i]
# So we will call MCM(arr, 1, len(arr)-1)
# If we devide into 2 halves arr[i]-arr[k] and arr[k+1]-arr[j]
# then k will run from k=i to k=j-1

from sys import maxsize


def MCM(arr, i, j):

    if M[i][j] != None:
        return M[i][j]

    minCost = maxsize

    if i >= j:
        minCost = 0

    else:
        for k in range(i, j):
            cost = MCM(arr, i, k) + MCM(arr, k+1, j) + \
                arr[i-1] * arr[k] * arr[j]
            minCost = min(minCost, cost)

    M[i][j] = minCost

    return minCost


def make2DMemory(n, m):
    global M
    M = [[None for i in range(m+1)] for j in range(n+1)]


T = int(input())
for _ in range(T):
    arr = list(map(int, input().split()))
    n = len(arr)

    make2DMemory(n, n)
    print(MCM(arr, 1, n-1))

# 3
# 40 20 30 10 30
# 10 20 30 40 30
# 10 20 30
