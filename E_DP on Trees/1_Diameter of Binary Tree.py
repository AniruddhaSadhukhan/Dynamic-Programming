# Given a binary tree, you need to compute the length of the diameter of the tree.
# The diameter of a binary tree is the length of the longest path between any two
# nodes in a tree. This path may or may not pass through the root.

# Example:
# Given a binary tree
#           1
#          / \
#         2   3
#        / \
#       4   5
# Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

# Note: The length of path between two nodes is represented by the number of edges
# between them.


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


def calcDiameter(root):
    if root == None:
        return 0

    l = calcDiameter(root.left)
    r = calcDiameter(root.right)

    nodesIfRootOfDiameter = 1 + l + r

    global res
    res = max(res, nodesIfRootOfDiameter)

    nodesIfPartOfDiameter = 1 + max(l, r)

    return nodesIfPartOfDiameter


def diameter(root):
    global res
    res = 0
    calcDiameter(root)

    # Return res as it will contain the max nodes in diameter
    # return res

    # If max path is asked, return max(res-1 , 0) [0 when no nodes]
    return max(res-1, 0)

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
    k = diameter(root)
    print(k)


# 2
# 1 2 N 3 4 N 5 6 N 7 8 N 9
# 1 2 3 4 5
