# Given two strings str1 and str2, find the length of shortest string
# that has both str1 and str2 as subsequences.

# Examples :

# Input:   str1 = "geek",  str2 = "eke"
# Output: 5 ("geeke")

# Input:   str1 = "AGGTAB",  str2 = "GXTXAYB"
# Output:  9 ("AGXGTXAYB")

# Logic: We need to find a string that has both strings as subsequences
# and is shortest such string. If both strings have all characters different,
# then result is sum of lengths of two given strings. If there are common characters,
# then we don’t want them multiple times as the task is to minimize length.
# Therefore, we fist find the longest common subsequence, take one occurrence
# of this subsequence and add extra characters.


# Length of the shortest supersequence  = (Sum of lengths of given two strings) -
#                                         (Length of LCS of two given strings)

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


def shortestCommonSuperSequence(X, Y, n, m):
    make2DMemory(n, m)
    return m + n - LCS(X, Y, n, m)


T = int(input())
for _ in range(T):
    X = input().strip()
    Y = input().strip()
    n = len(X)
    m = len(Y)

    print(shortestCommonSuperSequence(X, Y, n, m))


# 2
# geek
# eke
# AGGTAB
# GXTXAYB
