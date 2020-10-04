# Given a sequence, print a longest palindromic subsequence of it.
# Examples :

# Input : BBABCBCAB
# Output : BABCBAB
# The above output is the longest
# palindromic subsequence of given
# sequence. "BBBBB" and "BBCBB" are
# also palindromic subsequences of
# the given sequence, but not the
# longest ones.

# Input : GEEKSFORGEEKS
# Output : Output can be either EEKEE
#          or EESEE or EEGEE, ..

# Logic: LPS will be LCS(str, reverse(str))

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


def LPS(X):
    Y = X[::-1]
    n = len(X)

    make2DMemory(n, n)
    return(LCS(X, Y, n, n))


T = int(input())
for _ in range(T):
    X = input().strip()
    Y = X[::-1]
    n = len(X)

    make2DMemory(n, n)
    print(LPS(X))

# 1
# GEEKSFORGEEKS
