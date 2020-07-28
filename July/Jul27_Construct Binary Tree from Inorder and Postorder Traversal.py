"""
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right



    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder:
            return None
        # post的最后一个元素一定是根节点，在inorder中找出此根节点的位置序号
        ind = inorder.index(postorder.pop())
        root = TreeNode(inorder[ind])

        root.right = self.buildTree(inorder[ind + 1:], postorder)
        root.left = self.buildTree(inorder[:ind], postorder)
        return root

node = TreeNode()
print(node.buildTree([9,3,15,20,7], [9,15,7,20,3]))

# post 数组中每个元素和其坐标之间的映射，直接在 HashMap 中将其位置取出来无需查找
def buildTree2(self, inorder, postorder):
    map_inorder = {}
    for i, val in enumerate(inorder):
        map_inorder[val] = i

    def recur(low, high):
        if low > high:
            return None
        x = TreeNode(postorder.pop())
        mid = map_inorder[x.val]

        x.right = recur(mid + 1, high)
        x.left = recur(low, mid - 1)
        return x

    return recur(0, len(inorder) - 1)