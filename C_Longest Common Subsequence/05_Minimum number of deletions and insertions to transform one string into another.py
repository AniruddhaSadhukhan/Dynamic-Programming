# Given two strings ‘str1’ and ‘str2’ of size m and n respectively.
# The task is to remove/delete and insert the minimum number of characters
# from/in str1 to transform it into str2. It could be possible that the same
# character needs to be removed/deleted from one point of str1 and inserted
# to some another point.

# Example 1:

# Input:
# str1 = "heap", str2 = "pea"
# Output:
# Minimum Deletion = 2 and
# Minimum Insertion = 1
# Explanation:
# p and h deleted from heap
# Then, p is inserted at the beginning
# One thing to note, though p was required yet
# it was removed/deleted first from its position and
# then it is inserted to some other position.
# Thus, p contributes one to the deletion_count
# and one to the insertion_count.

# Logic: To convert X to Y, first we need to convert it to LCS(X, Y).
# So Deletion = lex(X) - LCS(X, Y)
# Then we need to convert the LCS(X, Y) to Y
# So Deletion = lex(Y) - LCS(X, Y)

def LCS(X, Y, n, m):
    if M[n][m] != None:
        return M[n][m]

    if n == 0 or m == 0:
        return 0

    if X[n-1] == Y[m-1]:
        M[n][m] = LCS(X, Y, n-1, m-1) + 1
    else:
        M[n][m] = max(
            LCS(X, Y, n-1, m),
            LCS(X, Y, n, m-1)
        )

    return M[n][m]


def make2DMemory(n, W):
    global M
    M = [[None for i in range(W+1)] for j in range(n+1)]


def minInsDel(X, Y, n, m):
    make2DMemory(n, m)
    lcs = LCS(X, Y, n, m)
    return n - lcs, m - lcs  # Deletion,Insertion


T = int(input())
for _ in range(T):
    X = input().strip()
    Y = input().strip()
    n = len(X)
    m = len(Y)

    print(minInsDel(X, Y, n, m))


# 1
# geek
# eke
# AGGTAB
# GXTXAYB
