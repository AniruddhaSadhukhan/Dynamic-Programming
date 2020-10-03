# Given a rod of length n inches and an array of prices that contains 
# prices of all pieces of size smaller than n. Determine the maximum value 
# obtainable by cutting up the rod and selling the pieces. 

# For example, if length of the rod is 8 and the values of different pieces
#  are given as following, then the maximum obtainable value is 22 
# (by cutting in two pieces of lengths 2 and 6)


# length   | 1   2   3   4   5   6   7   8
# --------------------------------------------
# price    | 1   5   8   9  10  17  17  20
# And if the prices are as following, then the maximum obtainable value is 
# 24 (by cutting in eight pieces of length 1)

# length   | 1   2   3   4   5   6   7   8
# --------------------------------------------
# price    | 3   5   8   9  10  17  17  20

# Logic: Exactly same as Unbounded Knapsack Problem.No Code change
# Length[]    <= Weight[]
# Price[]     <= Val[]
# Size        <= Knapsack Capacity (W)


# ==Use this to increase recursion limit in case of large input==
import sys
sys.setrecursionlimit(10**6)
# =====================================


def unboundedKnapsack(val, wt, n, W):
    if M[n][W] != None:
        return M[n][W]

    if n == 0 or W == 0:
        return 0

    if wt[n-1] > W:
        M[n][W] = unboundedKnapsack(val, wt, n-1, W)
    else:
        M[n][W] = max(
            unboundedKnapsack(val, wt, n-1, W),
            # Only change is here: n-1 -> n
            val[n-1] + unboundedKnapsack(val, wt, n, W-wt[n-1])
        )

    return M[n][W]


def make2DMemory(n, W):
    global M
    M = [[None for i in range(W+1)] for j in range(n+1)]


M = None
T = int(input())
for _ in range(T):
    n = int(input())
    W = int(input())
    val = list(map(int, input().split()))
    wt = list(map(int, input().split()))

    make2DMemory(n, W)
    print(unboundedKnapsack(val, wt, n, W))

# Input
# 2
# 8
# 8
# 1   5   8   9  10  17  17  20
# 1   2   3   4   5   6   7   8
# 8
# 8
# 3   5   8   9  10  17  17  20
# 1   2   3   4   5   6   7   8

# Output:
# 22
# 24
