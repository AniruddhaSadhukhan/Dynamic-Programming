# Given 2 string X & Y, output if X is a subsequence of Y

# X = AXY
# Y = ADXCPY
# Output : True

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


T = int(input())
for _ in range(T):
    X = input().strip()
    Y = input().strip()
    n = len(X)
    m = len(Y)

    make2DMemory(n, m)
    print(LCS(X, Y, n, m) == n)
