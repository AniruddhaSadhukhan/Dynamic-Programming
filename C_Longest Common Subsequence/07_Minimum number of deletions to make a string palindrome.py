# Given a string of size ‘n’. The task is to remove or delete minimum number of
# characters from the string so that the resultant string is palindrome.

# Note: The order of characters should be maintained.

# Examples:

# Input: aebcbda
# Output: 2
# Remove characters 'e' and 'd'
# Resultant string will be 'abcba'
# which is a palindromic string

# Input: geeksforgeeks
# Output: 8

# Logic: Same as previous question (Longest Palindromic Subsequence)
# Answer = len(X) - LPS(X)

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


def minDelToPalindrome(X):
    Y = X[::-1]
    n = len(X)

    make2DMemory(n, n)
    return(n - LCS(X, Y, n, n))


T = int(input())
for _ in range(T):
    X = input().strip()
    Y = X[::-1]
    n = len(X)

    make2DMemory(n, n)
    print(minDelToPalindrome(X))
