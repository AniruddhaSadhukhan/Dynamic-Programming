# You are given K eggs, and you have access to a building with N floors from 1 to N.

# Each egg is identical in function, and if an egg breaks, you cannot drop it again.

# You know that there exists a floor F with 0 <= F <= N such that any egg dropped at
# a floor higher than F will break, and any egg dropped at or below floor F will not break.

# Each move, you may take an egg (if you have an unbroken one) and drop it from any
# floor X (with 1 <= X <= N).

# Your goal is to know with certainty what the value of F is.

# What is the minimum number of moves that you need to know with certainty what F is,
# regardless of the initial value of F?

# Example 1:

# Input: K = 1, N = 2
# Output: 2
# Explanation:
# Drop the egg from floor 1.  If it breaks, we know with certainty that F = 0.
# Otherwise, drop the egg from floor 2.  If it breaks, we know with certainty that F = 1.
# If it didn't break, then we know with certainty F = 2.
# Hence, we needed 2 moves in the worst case to know what F is with certainty.
# Example 2:

# Input: K = 2, N = 6
# Output: 3
# Example 3:

# Input: K = 3, N = 14
# Output: 4

# Explanation :
# Drop from all floors ( recursion guess approach, try everything )

# From all floors we "max" the recursion call since we want the worst case or the case
# that reaches the base case and not a case where we were lucky (drop from first floor).
# We need a solution that COVERS ALL FLOORS ( a.k.a reaches the base case) and works in
# the given scenario perfectly, no matter where the threshold floor is.

# Minimum tries means MINIMUM wherever the threshold floor is, that is why maximum is
# taken from break vs not break.

# But min from all tries since we want the call which took minimum tries to reach the base case.


from sys import maxsize


def eggDrop(e, f):

    if M[e][f] != None:
        return M[e][f]

    minMoves = maxsize

    if e == 1 or f <= 1:
        minMoves = f

    else:
        for k in range(1, f+1):
            moves = 1 + max(eggDrop(e, f-k), eggDrop(e-1, k-1))
            minMoves = min(minMoves, moves)

    M[e][f] = minMoves

    return minMoves


def make2DMemory(n, m):
    global M
    M = [[None for i in range(m+1)] for j in range(n+1)]


T = int(input())
for _ in range(T):
    egg = int(input())
    floor = int(input())

    make2DMemory(egg, floor)
    print(eggDrop(egg, floor))

# 3
# 1
# 2
# 2
# 6
# 3
# 14
