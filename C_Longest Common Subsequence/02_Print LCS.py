# LCS Problem Statement: Given two sequences, find the longest subsequence present in both of them.
# A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous.
# For example, “abc”, “abg”, “bdf”, “aeg”, ‘”acefg”, .. etc are subsequences of “abcdefg”.

# Examples:
# LCS for input Sequences “ABCDGH” and “AEDFHR” is “ADH”
# LCS for input Sequences “AGGTAB” and “GXTXAYB” is “GTAB”

# Logic:
# After calculating LCS and populating M, again recursively do the same with following change
# Instead of returning 0 for base case, return blank string
# Instead of adding 1 when matched, add the matched char at end
# During max calculation, do the max calculation on length (get longest string)


def LCS(X, Y, n, m):
    if M[n][m] != None:
        return M[n][m]

    elif n == 0 or m == 0:
        M[n][m] = 0

    elif X[n-1] == Y[m-1]:
        M[n][m] = LCS(X, Y, n-1, m-1) + 1
    else:
        M[n][m] = max(
            LCS(X, Y, n-1, m),
            LCS(X, Y, n, m-1)
        )

    return M[n][m]


def printLCS(X, Y, n, m):

    if n == 0:
        return ""
    elif m == 0:
        return ""

    if X[n-1] == Y[m-1]:
        return printLCS(X, Y, n-1, m-1) + X[n-1]
    else:
        if M[n-1][m] >= M[n][m-1]:
            return printLCS(X, Y, n-1, m)
        else:
            return printLCS(X, Y, n, m-1)


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
    LCS(X, Y, n, m)
    print(printLCS(X, Y, n, m))


# 2
# ABCDGH
# AEDFHR
# AGGTAB
# GXTXAYB
