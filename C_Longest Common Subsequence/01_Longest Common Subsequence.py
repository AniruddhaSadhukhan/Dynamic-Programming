# LCS Problem Statement: Given two sequences, find the length of longest subsequence present in both of them.
# A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous.
# For example, “abc”, “abg”, “bdf”, “aeg”, ‘”acefg”, .. etc are subsequences of “abcdefg”.

# Examples:
# LCS for input Sequences “ABCDGH” and “AEDFHR” is “ADH” of length 3.
# LCS for input Sequences “AGGTAB” and “GXTXAYB” is “GTAB” of length 4.

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

# Top Down approach
# Use a double loop and replace n with i and m with j


def LCS_TopDown(X, Y, n, m):
    for i in range(n+1):
        for j in range(m+1):
            if i == 0 or j == 0:
                M[i][j] = 0

    for i in range(1, n+1):
        for j in range(1, m+1):
            if X[i-1] == Y[j-1]:
                M[i][j] = LCS(X, Y, i-1, j-1) + 1
            else:
                M[i][j] = max(
                    LCS(X, Y, i-1, j),
                    LCS(X, Y, i, j-1)
                )

    return M[n][m]


def make2DMemory(n, W):
    global M
    M = [[None for i in range(W+1)] for j in range(n+1)]


T = int(input())
for _ in range(T):
    X = input().strip()
    Y = input().strip()
    n = len(X)
    m = len(Y)

    make2DMemory(n, m)
    print(LCS(X, Y, n, m))


# 2
# ABCDGH
# AEDFHR
# AGGTAB
# GXTXAYB
