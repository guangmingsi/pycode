# 创建节点类
class Node(object):
    def __init__(self,item):
        self.elem = item
        self.lchild = None
        self.rchild = None

#创建二叉树类
class Tree(object):
    # 构造根节点
    def __init__(self):
        self.root = None
    # 增加节点方法
    def add(self,item):
        node = Node(item)
        # 特殊情况，没有根节点
        if self.root == None:
            self.root = node
            return
        # 创建一个列表，放入root节点
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            if cur_node.lchild is None:
                cur_node.lchild = node
                return
            else:
                queue.append(cur_node.lchild)
            if cur_node.rchild is None:
                cur_node.rchild = node
                return
            else:
                queue.append(cur_node.rchild)
    # 广度优先遍历二叉树
    def breadth_travel(self):
        # 判断树是不是为空
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.elem,end = " ")
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)
    def preoder(self,node):
        """先序遍历"""
        # 递归结束条件
        if node is None:
            return
        print(node.elem,end = " ")
        self.preoder(node.lchild)
        self.preoder(node.rchild)
    def inorder(self,node):
        if node is None:
            return
        self.inorder(node.lchild)
        print(node.elem,end =" ")
        self.inorder(node.rchild)
    def postorder(self,node):
        if node is None:
            return
        self.postorder(node.lchild)
        self.postorder(node.rchild)
        print(node.elem,end = " ")



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
    print("")
    t.preoder(t.root)
    print("")
    t.inorder(t.root)
    print("")
    t.postorder(t.root)