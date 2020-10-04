# Given two strings ‘X’ and ‘Y’, find the length of the longest common substring.
# Examples :

# Input : X = “GeeksforGeeks”, y = “GeeksQuiz”
# Output : 5
# The longest common substring is “Geeks” and is of length 5.

# Input : X = “abcdxyz”, y = “xyzabcd”
# Output : 4
# The longest common substring is “abcd” and is of length 4.

# Input : X = “zxabcdezy”, y = “yzabcdezx”
# Output : 6
# The longest common substring is “abcdez” and is of length 6.

# Logic: This is similar to LCS with a few change
# Substring has to be continuous while subsequence can be discontinuous
# So, if the last characters dont match, we will store 0 in memory
# Also we have to get the max value in the array for the answer

def LongestCommonSubstring(X, Y, n, m):
    if M[n][m] != None:
        return M[n][m]

    elif n == 0 or m == 0:
        M[n][m] = 0

    elif X[n-1] == Y[m-1]:
        M[n][m] = LongestCommonSubstring(X, Y, n-1, m-1) + 1
    else:
        LongestCommonSubstring(X, Y, n, m-1)
        LongestCommonSubstring(X, Y, n-1, m)
        M[n][m] = 0

    global res
    res = max(res, M[n][m])

    return M[n][m]


def make2DMemory(n, W):
    global M
    M = [[None for i in range(W+1)] for j in range(n+1)]


res = -1
T = int(input())
for _ in range(T):
    X = input().strip()
    Y = input().strip()
    n = len(X)
    m = len(Y)

    res = -1
    make2DMemory(n, m)
    LongestCommonSubstring(X, Y, n, m)
    print(res)


# 3
# GeeksforGeeks
# GeeksQuiz
# abcdxyz
# xyzabcd
# zxabcdezy
# yzabcdezx
