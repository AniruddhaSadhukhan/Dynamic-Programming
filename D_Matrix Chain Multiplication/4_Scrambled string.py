# Given string str, we can represent it as a binary tree by partitioning it to two non-empty substrings recursively.

# Note: Srambled string is not same as an Anagram

# Below is one possible representation of str = “coder”:

#     coder
#    /    \
#   co    der
#  / \    /  \
# c   o  d   er
#            / \
#           e   r
# To scramble the string, we may choose any non-leaf node and swap its two children.
# Suppose, we choose the node “co” and swap its two children, it produces a scrambled string “ocder”.


#     ocder
#    /    \
#   oc    der
#  / \    /  \
# o   c  d   er
#            / \
#           e   r
# Thus, “ocder” is a scrambled string of “coder”.
# Similarly, if we continue to swap the children of nodes “der” and “er”, it produces a scrambled string “ocred”.


#     ocred
#    /    \
#   oc    red
#  / \    /  \
# o   c  re  d
#        / \
#       r   e
# Thus, “ocred” is a scrambled string of “coder”.
# Examples:
# Input: S1=”coder”, S2=”ocder”
# Output: Yes
# Explanation:
# “ocder” is a scrambled form of “coder”

# Input: S1=”abcde”, S2=”caebd”
# Output: No
# Explanation:
# “caebd” is not a scrambled form of “abcde”

# Input: s1 = "great", s2 = "rgeat"
# Output: true

# Logic:
# Given two strings of equal length (say n+1), S1[0…n] and S2[0…n].
# If S2 is a scrambled form of S1, then there must exist an index i such that at least
# one of the following conditions is true:

# S2[0…i] is a scrambled string of S1[0…i] and S2[i+1…n] is a scrambled string of S1[i+1…n].
# S2[0…i] is a scrambled string of S1[n-i…n] and S2[i+1…n] is a scrambled string of S1[0…n-i-1].
# Note: An optimization step to consider here is to check beforehand if the two strings are anagrams
# of each other. If not, it indicates that the strings contain different characters
# and can’t be a scrambled form of each other.
from collections import Counter


def scrambledStrings(X, Y):
    if (X, Y) in M:
        return M[(X, Y)]

    if len(X) != len(Y):
        M[(X, Y)] = False
        return M[(X, Y)]

    if X == Y:
        M[(X, Y)] = True
        return M[(X, Y)]

    if Counter(X) != Counter(Y):
        M[(X, Y)] = False
        return M[(X, Y)]

    # This must be after counter check, anagrams of length 3 or less are always scrambled
    # a - a
    # ab - ba 
    # abc - bca - cab - bac - cba and so on...
    if len(X) <= 3:
        M[(X, Y)] = True
        return M[(X, Y)]

    M[(X, Y)] = False
    for i in range(1, len(X)):
        if (
            (scrambledStrings(X[:i], Y[-i:])
             and scrambledStrings(X[i:], Y[:-i]))
            or
            (scrambledStrings(X[:i], Y[:i]) and scrambledStrings(X[i:], Y[i:]))
        ):
            M[(X, Y)] = True
            break
    return M[(X, Y)]


def makeMapMemory():
    global M
    M = {}


T = int(input())
for _ in range(T):
    X = input().strip()
    Y = input().strip()

    makeMapMemory()
    print(scrambledStrings(X, Y))


# 3
# coder
# ocder
# abcde
# caebd
# great
# rgeat
