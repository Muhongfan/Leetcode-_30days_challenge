def verticalTraversal(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    m = list()
    dfs(root, m, 0, 0)
    m.sort()
    res = [[m[0][2]]]
    for i in range(1, len(m)):
        if m[i][0] == m[i - 1][0]:
            res[-1].append(m[i][2])
        else:
            res.append([m[i][2]])
    return res
def dfs(root,m, x, y):
    if not root:
        return
    m.append((x, -y, root.val))
    dfs(root.left, x-1, y-1)
    dfs(root.right, x+1, y-1)


print(verticalTraversal([3,9,20,0,0,15,7]))
