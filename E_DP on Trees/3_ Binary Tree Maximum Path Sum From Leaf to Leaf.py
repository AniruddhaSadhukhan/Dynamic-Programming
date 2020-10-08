# Given a binary tree in which each node element contains a number.
# Find the maximum possible sum from one leaf node to another.
# The maximum sum path may or may not go through root.
# Example 1:

# Input :
#            3
#          /    \
#        4       5
#       /  \
#     -10   4

# Output: 16

# Explanation :
# Maximum Sum lies between leaf node 4 and 5.
# 4 + 4 + 3 + 5 = 16.

# Example 2:

# Input :
#             -15
#          /      \
#         5         6
#       /  \       / \
#     -8    1     3   9
#    /  \              \
#   2   -3              0
#                      / \
#                     4  -1
#                        /
#                      10

# Output :  27

# Explanation:
# The maximum possible sum from one leaf node
# to another is (3 + 6 + 9 + 0 + -1 + 10 = 27)

from collections import deque
import sys
sys.setrecursionlimit(50000)

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
res = 0

# This returns the max no of nodes if it is part of Diameter


def calcMaxPathSum(root):
    if root == None:
        return 0

    l = calcMaxPathSum(root.left)
    r = calcMaxPathSum(root.right)

    nodesIfPartOfMaxPath = 0

    if(root.left == None and root.right == None):
        nodesIfPartOfMaxPath = root.data

    elif(root.left == None):
        nodesIfPartOfMaxPath = root.data + r

    elif(root.right == None):
        nodesIfPartOfMaxPath = root.data + l

    else:
        nodesIfPartOfMaxPath = root.data + max(l, r)

        # Only if it have left and right sub tree
        nodesIfRootOfMaxPath = root.data + l + r

        global res
        res = max(res, nodesIfRootOfMaxPath)

    return nodesIfPartOfMaxPath


def maxPathSum(root):
    global res
    res = float('-inf')
    calcMaxPathSum(root)

    return res


# Tree Node


class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

    def __str__(self):
        return "{ V: "+str(self.data) + ", L: " + str(self.left) + ", R: " + str(self.right) + " }"


# Function to Build Tree
def buildTree(s):
    # Corner Case
    if(len(s) == 0 or s[0] == "N"):
        return None

    # Creating list of strings from input
    # string after spliting by space
    ip = list(map(str, s.split()))

    # Create the root of the tree
    root = Node(int(ip[0]))
    size = 0
    q = deque()

    # Push the root to the queue
    q.append(root)
    size = size+1

    # Starting from the second element
    i = 1
    while(size > 0 and i < len(ip)):
        # Get and remove the front of the queue
        currNode = q[0]
        q.popleft()
        size = size-1

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if(currVal != "N"):

            # Create the left child for the current node
            currNode.left = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size = size+1
        # For the right child
        i = i+1
        if(i >= len(ip)):
            break
        currVal = ip[i]

        # If the right child is not null
        if(currVal != "N"):

            # Create the right child for the current node
            currNode.right = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size = size+1
        i = i+1
    return root


t = int(input())
for _ in range(0, t):
    s = input()
    root = buildTree(s)
    k = maxPathSum(root)
    print(k)


# 2
# 3 4 5 -10 4
# -15 5 6 -8 1 3 9 2 -3 N N N N N 0 N N N N 4 -1 N N 10
