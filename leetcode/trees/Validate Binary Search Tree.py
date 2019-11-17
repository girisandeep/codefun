
'''
Validate Binary Search Tree

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys

class Solution1(object):
    def isValidBST(self, root, mn=-sys.maxint - 1,  mx=sys.maxint):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            if root.val <= mn or root.val >= mx:
                return False
            
            if root.left:
                if not self.isValidBST(root.left, mn=mn, mx=min(root.val, mx)):
                    return False
            if root.right:
                if not self.isValidBST(root.right, mn=max(mn, root.val), mx=mx):
                    return False
        return True


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack = [(root, -sys.maxint - 1, sys.maxint)]
        
        while stack:
            root, mn, mx = stack.pop()
            if root:
                #print(root.val, mn, mx)
                if root.val <= mn or root.val >= mx:
                    return False
                
                if root.right:
                    stack.append((root.right, root.val, mx))
                if root.left:
                    stack.append((root.left, mn, root.val))
        return True

