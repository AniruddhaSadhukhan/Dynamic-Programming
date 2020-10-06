# Given a boolean expression with following symbols.

# Symbols
#     'T' ---> true
#     'F' ---> false
# And following operators filled between symbols

# Operators
#     &   ---> boolean AND
#     |   ---> boolean OR
#     ^   ---> boolean XOR
# Count the number of ways we can parenthesize the expression so that
# the value of expression evaluates to true.

# Input 1:
#     A = "T|F"

# Output 1:
#     1

# Explanation 1:
#     The only way to evaluate the expression is:
#         => (T|F) = T

# Input 2:
#     A = "T^T^F"

# Output 2:
#     0


def boolParenthesizations(str, i, j, V):

    t = 0 if V == 'F' else 1

    if M[i][j][t] != None:
        return M[i][j][t]

    maxWays = 0

    if i == j:
        maxWays = 1 if (str[i] == V) else 0

    else:
        for k in range(i+1, j, 2):
            lT = boolParenthesizations(str, i, k-1, 'T')
            lF = boolParenthesizations(str, i, k-1, 'F')
            rT = boolParenthesizations(str, k+1, j, 'T')
            rF = boolParenthesizations(str, k+1, j, 'F')

            if (str[k] == '&'):
                if V == 'T':
                    maxWays = maxWays + lT*rT
                else:
                    maxWays = maxWays + lT*rF + lF*rT + lF*rF

            elif (str[k] == '|'):
                if V == 'T':
                    maxWays = maxWays + lT*rT + lT*rF + lF*rT
                else:
                    maxWays = maxWays + lF*rF

            elif (str[k] == '^'):
                if V == 'T':
                    maxWays = maxWays + lT*rF + lF*rT
                else:
                    maxWays = maxWays + lT*rT + lF*rF

    M[i][j][t] = maxWays

    return maxWays


def make3DMemory(a, b, c):
    global M
    M = [[[None for i in range(a)] for j in range(b+1)] for k in range(c+1)]


T = int(input())
for _ in range(T):
    str = input().strip()
    n = len(str)

    make3DMemory(2, n, n)
    print(boolParenthesizations(str, 0, n-1, 'T'))

# 3
# T|T&F^T
# T|F
# T^T^F
