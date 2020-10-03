# You are given weights and values of N items, put these items in a knapsack of capacity W
# to get the maximum total value in the knapsack. Note that we have only one quantity of each item.

# Input:
# The first line of input contains an integer T denoting the number of test cases.
# Then T test cases follow. Each test case consists of four lines.
# The first line consists of N the number of items.
# The second line consists of W, the maximum capacity of the knapsack.
# In the next line are N space separated positive integers denoting the values of the N items,
# and in the fourth line are N space separated positive integers
# denoting the weights of the corresponding items.

# Output:
# For each testcase, in a new line, print the maximum possible value you can get with the given conditions
# that you can obtain for each test case in a new line.

# Constraints:
# 1 ≤ T ≤ 100
# 1 ≤ N ≤ 1000
# 1 ≤ W ≤ 1000
# 1 ≤ wt[i] ≤ 1000
# 1 ≤ v[i] ≤ 1000

# Example:
# Input:
# 2
# 3
# 4
# 1 2 3
# 4 5 1
# 3
# 3
# 1 2 3
# 4 5 6

# Output:
# 3
# 0

# Explanation:
# Test Case 1: With W = 4, you can either choose the 0th item or the 2nd item.
# Thus, the maximum value you can generate is the max of val[0] and val[2], which is equal to 3.
# Test Case 2: With W = 3, there is no item you can choose from the given list as all the items
# have weight greater than W. Thus, the maximum value you can generate is 0.


def knapsack(val, wt, n, W):

    if n == 0 or W == 0:
        return 0

    if M[n][W] != None:
        return M[n][W]

    if(wt[n-1] > W):
        M[n][W] = knapsack(val, wt, n-1, W)
    else:
        M[n][W] = max(knapsack(val, wt, n-1, W), (val[n-1] +
                                                  knapsack(val, wt, n-1, W-wt[n-1])))

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
    print(knapsack(val, wt, n, W))
