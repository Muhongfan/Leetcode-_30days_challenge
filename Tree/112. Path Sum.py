"""
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.



Example 1:


Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.
Example 2:


Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.
Example 3:

Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths.

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False
        stack = [(root, targetSum - root.val)]
        while stack:
            node, cursum = stack.pop()
            if not cursum and node.left and node.right:
                return True
            if node.left:
                stack.append(node.left, cursum - node.left.val)
            if node.right:
                stack.append(node.left, cursum - node.right.val)

        return False

    def hasPathSum2(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        stack = [(root, root.val)]

        while stack:
            curr, currsum = stack.pop()

            # if leaf and target value
            if not curr.right and not curr.left and currsum == targetSum:
                return True

            # else append right child
            if curr.right:
                stack.append((curr.right, currsum + curr.right.val))

            # append left child (which will be checked in next loop)
            if curr.left:
                stack.append((curr.left, currsum + curr.left.val))

        return False
