# Unbounded Knapsack (Repetition of items allowed)
# You are given weights and values of N items, put these items in a knapsack
# of capacity W to get the maximum total value in the knapsack.
# This is different from classical Knapsack problem,
# here we are allowed to use unlimited number of instances of an item.
# Input : W = 100
#        val[]  = {1, 30}
#        wt[] = {1, 50}
# Output : 100
# There are many ways to fill knapsack.
# 1) 2 instances of 50 unit weight item.
# 2) 100 instances of 1 unit weight item.
# 3) 1 instance of 50 unit weight item and 50
#    instances of 1 unit weight items.
# We get maximum value with option 2.

# Input : W = 8
#        val[] = {10, 40, 50, 70}
#        wt[]  = {1, 3, 4, 5}
# Output : 110
# We get maximum value with one unit of
# weight 5 and one unit of weight 3.

# Logic: Its similar to 0/1 Knapsack, only change will be
# in O/1 Knapsack, whether we include or exclude a element, we take it as processed
# but in unbounded knapsack:
#     If item is included, its not marked as processed, as it can be again taken up later
#     If item is excluded, its marked as processed and will not be taken up later


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
