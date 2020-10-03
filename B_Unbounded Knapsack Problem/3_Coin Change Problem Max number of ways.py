# Given a value N, if we want to make change for N cents, 
# and we have infinite supply of each of S = { S1, S2, .. , Sm} valued coins,
# how many ways can we make the change? The order of coins doesn’t matter.

# For example, for N = 4 and S = {1,2,3}, there are four solutions: 
# {1,1,1,1},{1,1,2},{2,2},{1,3}. So output should be 4.
# For N = 10 and S = {2, 5, 3, 6}, there are five solutions: 
# {2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5} and {5,5}.
# So the output should be 5.

# Logic: Similar to Count of Subset with given sum problem but for unbounded Knapsack


def coinChangeMaxWays(wt, n, W):
    if M[n][W] != None:
        return M[n][W]

    if W == 0:
        return 1
    if n == 0:
        return 0

    if wt[n-1] > W:
        M[n][W] = coinChangeMaxWays(wt, n-1, W)
    else:
        M[n][W] = coinChangeMaxWays(wt, n-1, W) + \
            coinChangeMaxWays(wt, n, W-wt[n-1])

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
    print(coinChangeMaxWays(wt, n, W))

# 2
# 3
# 4
# 1 2 3
# 4
# 10
# 2 5 3 6
