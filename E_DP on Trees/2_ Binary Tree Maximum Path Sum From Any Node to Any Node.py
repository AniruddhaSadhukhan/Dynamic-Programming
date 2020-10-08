# Given a non-empty binary tree, find the maximum path sum.

# For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

# Example 1:

# Input: [1,2,3]

#        1
#       / \
#      2   3

# Output: 6
# Example 2:

# Input: [-10,9,20,null,null,15,7]

#    -10
#    / \
#   9  20
#     /  \
#    15   7

# Output: 42


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

    nodesIfPartOfMaxPath = max(root.data + max(l, r), root.data)

    nodesIfRootOfMaxPath = max(nodesIfPartOfMaxPath, root.data + l + r)

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
# 1 2 3
# -10 9 20 N N 15 7
