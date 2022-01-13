"""
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        # creat a container to store the nodes that should be visited
        stack = [(root, 0)]
        ans = []
        while stack:
            node, level = stack.pop()
            if len(ans) == level:
                ans.append([])
            ans[level].append(node.val)
            if node.right:
                stack.append((node.right, level+1))
            if node.left:
                stack.append((node.left, level+1))
        return ans

    def levelOrder2(self, root):
        if not root:
            return []
        ans = []
        queue = deque()
        queue.append((root, 0))
        while queue:
            node, level = queue.popleft()
            if len(ans) == level:
                ans.append([])
            ans[level].append(node.val)
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        return ans