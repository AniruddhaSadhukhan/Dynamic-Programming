# Given a string, find length of the longest repeating subseequence such that
# the two subsequence don’t have same string character at same position,
# i.e., any i’th character in the two subsequences shouldn’t have the same
# index in the original string.

# Input: str = "abc"
# Output: 0
# There is no repeating subsequence

# Input: str = "aab"
# Output: 1
# The two subssequence are 'a'(first) and 'a'(second).
# Note that 'b' cannot be considered as part of subsequence
# as it would be at same index in both.

# Input: str = "aabb"
# Output: 2

# Input: str = "axxxy"
# Output: 2

# Logic: This problem is just the modification of Longest Common Subsequence problem.
# The idea is to find the LCS(str, str)where str is the input string with the restriction
# that when both the characters are same, they shouldn’t be on the same index in the two strings.

def LRS(X, Y, n, m):
    if M[n][m] != None:
        return M[n][m]

    elif n == 0 or m == 0:
        M[n][m] = 0

    elif X[n-1] == Y[m-1] and n != m:
        M[n][m] = LRS(X, Y, n-1, m-1) + 1
    else:
        M[n][m] = max(
            LRS(X, Y, n-1, m),
            LRS(X, Y, n, m-1)
        )

    return M[n][m]


def make2DMemory(n, W):
    global M
    M = [[None for i in range(W+1)] for j in range(n+1)]


T = int(input())
for _ in range(T):
    X = input().strip()
    Y = X
    n = len(X)
    m = len(Y)

    make2DMemory(n, m)
    print(LRS(X, Y, n, m))


# 4
# abc
# aab
# aabb
# axxxy
