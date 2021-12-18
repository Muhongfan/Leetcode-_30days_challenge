"""
Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.



Example 1:


Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: inorder = [-1], postorder = [-1]
Output: [-1]

"""
class TreeNode:
    def __init__(self,val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder, postorder):
        if not inorder:
            return None
        root = TreeNode(postorder[-1])
        i = inorder.index(root.val)
        root.left = self.buildTree(inorder[0:i], postorder[0:i])
        root.right = self.buildTree((inorder[i+1:], postorder[i+i:-1]))

        return root

"""
时间复杂度：由于每次递归 inorder 和 postorder 的总数都会减 1，因此递归 N 次，故时间复杂度为 $O(N)$，其中 N 为节点个数。
空间复杂度：递归借助额外的栈空间完成， 由于栈的深度为 N，因此总的空间复杂度为 $O(N)$，其中 N 为节点个数。
"""