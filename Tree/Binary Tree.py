# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return
        ans = []
        stack = [root]
        while stack:
            root = stack.pop()
            if root:
                ans.append(root.val)
                if root.right:
                    stack.append(root.right)
                if root.left:
                    stack.append(root.right)
        return ans


    def postorderTraversal(self, root):
        if not root:
            return []

        ans = []
        stack = []
        while stack:
            root = stack.pop()
            if root:
                if root.left:
                    stack.append(root.left)
                if root.right:
                    stack.append(root.right)
                ans.append(root.val)

        return ans[::-1]

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return

        ans = []
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            ans.append(root.val)
            root = root.right
        return ans


