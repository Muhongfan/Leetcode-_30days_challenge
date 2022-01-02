"""
94. Binary Tree Inorder Traversal

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root) :
        if (root == None):
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

    def inorderTraversal2(self, root) :
        traversal = []
        def traverse(tree, depth):

            if tree:
                depth +=1
                traverse(tree.left, depth)
                traversal.append(tree.val)
                traverse(tree.right, depth)
            else:
                depth -= 1

            traverse(root, 0)
            return traversal

    def inorderTraversal3(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        if root:
            output = output + self.inorderTraversal(root.left)
            output.append(root.val)
            output = output + self.inorderTraversal(root.right)
        return output


