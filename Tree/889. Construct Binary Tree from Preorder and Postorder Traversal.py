"""
Given two integer arrays, preorder and postorder where preorder is the preorder traversal of a binary tree of distinct values and postorder is the postorder traversal of the same tree, reconstruct and return the binary tree.

If there exist multiple answers, you can return any of them.



Example 1:


Input: preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]
Example 2:

Input: preorder = [1], postorder = [1]
Output: [1]

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root
        i = postorder.index(preorder[1])
        root.left = self.constructFromPrePost(preorder[1:i+2], postorder[:i+1])
        root.right = self.constructFromPrePost(preorder[i+2:], postorder[i+1:-1])
        return root


class SolutionDemo:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def dfs(inorder, i_start, i_end, postorder, p_start, p_end):
            if i_start > i_end: return None
            if i_start == i_end: return TreeNode(inorder[i_start])
            node = TreeNode(postorder[p_end])
            i = inorder.index(postorder[p_end])
            node.left = dfs(inorder, i_start, i - 1, postorder, p_start, p_start + (i - 1 - i_start))
            node.right = dfs(inorder, i + 1, i_end, postorder, p_start + (i - 1 - i_start) + 1, p_end - 1)
            return node
        return dfs(inorder, 0, len(inorder) - 1, postorder, 0, len(postorder) - 1)