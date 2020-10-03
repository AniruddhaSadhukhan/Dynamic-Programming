# LCS Problem Statement: Given two sequences, find the longest subsequence present in both of them.
# A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous.
# For example, “abc”, “abg”, “bdf”, “aeg”, ‘”acefg”, .. etc are subsequences of “abcdefg”.

# Examples:
# LCS for input Sequences “ABCDGH” and “AEDFHR” is “ADH”
# LCS for input Sequences “AGGTAB” and “GXTXAYB” is “GTAB”

# Logic:
# Instead of storing length, store the string itself
# So instead of returning 0 for base case, return blank string
# Instead of adding 1 when matched, add the matched char at end
# During max calculation, do the max calculation on length (get longest string)

def LCS(X, Y, n, m):
    if M[n][m] != None:
        return M[n][m]

    if n == 0 or m == 0:
        return ""

    if X[n-1] == Y[m-1]:
        M[n][m] = LCS(X, Y, n-1, m-1) + X[n-1]
    else:
        M[n][m] = max(
            LCS(X, Y, n-1, m),
            LCS(X, Y, n, m-1),
            key=len
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