"""
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.



Example 1:


Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]

"""
#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder:  #same condition as inorder
            return None
        root = TreeNode(preorder[0])

        i = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:i+1], inorder[0:i])
        root.right = self.buildTree(preorder[i+1:], inorder[i+1:])

        return root
"""
时间复杂度：由于每次递归 inorder 和 preorder 的总数都会减 1，因此递归 N 次，故时间复杂度为 $O(N)$，其中 N 为节点个数。
空间复杂度：使用了递归，也就是借助额外栈空间来完成， 由于栈的深度为 N，因此总的空间复杂度为 $O(N)$，其中 N 为节点个数。
"""