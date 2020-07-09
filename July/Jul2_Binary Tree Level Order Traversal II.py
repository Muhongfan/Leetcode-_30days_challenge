"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
"""

'''
Binary Tree
'''


def levelOrderBottom(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    tree = []
    if not root:
        return tree
    curr_level = [root]
    # print(type(root), type(curr_level))  # (<class 'precompiled.treenode.TreeNode'>, <type 'list'>)
    # print(curr_level)  # 作为list，却并不能遍历整个树
    while curr_level:
        level_list = []
        next_level = []
        for temp in curr_level:
            level_list.append(temp.val)
            if temp.left:
                next_level.append(temp.left)
            if temp.right:
                next_level.append(temp.right)
        tree.append(level_list)
        curr_level = next_level
    tree.reverse()
    return tree
print(levelOrderBottom([3,9,20,0,0,15,7]))