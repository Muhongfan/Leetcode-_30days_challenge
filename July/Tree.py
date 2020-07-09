class Node():
    def __init__(self, item, lchild = None, rchild = None):
        self.item = item
        self.lchild = lchild
        self.rchild = rchild

class Tree():
    # 先定义一个带默认值None的根节点
    def __init__(self, root = None):
        self.root = root
    # 定义添加元素的方法
    def add(self, item):
        node = Node(item)
        if self.root == None:
            self.root = node
        else:
            # 注意这里是用队列的方式来循环判断当前节点有没有可加入位置的
            queue = []
            queue.append(self.root)
            while queue:
                cur = queue.pop(0)
                if cur.lchild == None:
                    cur.lchild = node
                    return
                elif cur.rchild == None:
                    cur.rchild = node
                    return
                else:
                    queue.append(cur.lchild)
                    queue.append(cur.rchild)
    # 定义广度优先遍历(层次遍历)方法
    def breadth_travel(self):
        if self.root == None:
            return
        else:
            # 仍然是用队列的方式实现遍历，末端按遍历顺序逐个添加节点，首端逐个弹出先读到的节点
            queue = []
            queue.append(self.root)
            while queue:
                cur = queue.pop(0)
                print(cur.item, end=" ")
                if cur.lchild is not None:
                    queue.append(cur.lchild)
                if cur.rchild is not None:
                    queue.append(cur.rchild)

if __name__ == "__main__":
    t = Tree()
    t.add(0)
    t.add(1)
    t.add(2)
    t.add(3)
    t.add(4)
    t.add(5)
    t.add(6)
    t.add(7)
    t.add(8)
    t.add(9)
    t.breadth_travel()

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def levelOrder(root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        tmp = [[root]]
        if root == None:
            return res
        while tmp != []:
            s = tmp.pop(0)
            tmp1 = []
            tmp2 = []
            for i in range(len(s)):
                tmp1.append(s[i].val)
                if s[i].left != None:
                    tmp2.append(s[i].left)
                if s[i].right != None:
                    tmp2.append(s[i].right)
            if tmp2 != []:
                tmp.append(tmp2)
            res.append(tmp1)
        return res

print(levelOrder([3,9,20,0,0,15,7]))
