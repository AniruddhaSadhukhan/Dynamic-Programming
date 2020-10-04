# Given a string str, the task is to find the minimum number of characters
# to be inserted to convert it to palindrome.

# ab: Number of insertions required is 1 i.e. bab
# aa: Number of insertions required is 0 i.e. aa
# abcd: Number of insertions required is 3 i.e. dcbabcd
# abcda: Number of insertions required is 2 i.e. adcbcda
# abcde: Number of insertions required is 4 i.e. edcbabcde

# Logic:
# Min # of insertion = Min # of deletion
#                    = String Length - Length of Longest Palindromic Subsequence

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
    print(n - LPS(X))

# 6
# ab
# aa
# abcd
# abcda
# abcde
# aebcbda
