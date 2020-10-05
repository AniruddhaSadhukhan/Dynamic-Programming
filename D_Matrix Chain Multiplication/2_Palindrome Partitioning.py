# Given a string, a partitioning of the string is a palindrome partitioning if
# every substring of the partition is a palindrome.

# For example, “aba|b|bbabb|a|b|aba” is a palindrome partitioning of “ababbbabbababa”.

# Determine the fewest cuts needed for a palindrome partitioning of a given string.
# For example, minimum of 3 cuts are needed for “ababbbabbababa”.
# The three cuts are “a|babbbab|b|ababa”. If a string is a palindrome,
# then minimum 0 cuts are needed. If a string of length n containing all different
# characters, then minimum n-1 cuts are needed.

# Input : “geek”
# Output : 2
# We need to make minimum 2 cuts, i.e., “g ee k”

# Input : “aaaa”
# Output : 0
# The string is already a palindrome.

# Input : “abcde”
# Output : 4

# Input : “abbac”
# Output : 1

# Input : ababbbabbababa
# Output : 3

# Logic:  If the string is a palindrome, then we simply return 0.
# Else, like the Matrix Chain Multiplication problem, we try making cuts at all
# possible places, recursively calculate the cost for each cut and return the minimum value.

from sys import maxsize


def PalindromePartitioning(str, i, j):

    if M[i][j] != None:
        return M[i][j]

    minCost = maxsize

    if i >= j:
        minCost = 0

    elif isPalindrome(str[i:j+1]):
        minCost = 0

    else:
        for k in range(i, j):
            cost = PalindromePartitioning(
                str, i, k) + PalindromePartitioning(str, k+1, j) + 1
            minCost = min(minCost, cost)

    M[i][j] = minCost

    return minCost


def isPalindrome(str):
    return str == str[::-1]


def make2DMemory(n, m):
    global M
    M = [[None for i in range(m+1)] for j in range(n+1)]


T = int(input())
for _ in range(T):
    str = input().strip()
    n = len(str)

    make2DMemory(n, n)
    print(PalindromePartitioning(str, 0, n-1))

# 5
# geek
# aaaa
# abcde
# abbac
# ababbbabbababa
