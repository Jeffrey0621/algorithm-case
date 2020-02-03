class Node():
    def __init__(self,item,lchild = None,rchild = None):
        self.item = item
        self.lchild = lchild
        self.rchild = rchild
        
class Tree():
    def __init__(self,root = None):
        self.root = root

    #  定义添加元素的方法
    def add(self,item):
        node = Node(item)
        if self.root == None:
            self.root = node
        else:
            # 用队列来循环判断当前节点有没有课加入的位置
            queue = []
            queue.append(self.root)
            while queue:
                current = queue.pop(0)
                if current.lchild == None:
                    current.lchild = node
                    return
                elif current.rchild == None:
                    current.rchild = node
                    return
                else:
                    queue.append(current.lchild)
                    queue.append(current.rchild)

    def breadth_travel(self):
        if self.root == None:
            return
        else:
            queue = []
            queue.append(self.root)
            while queue:
                cur = queue.pop(0)
                print(cur.item,end = " ")
                if cur.lchild is not None:
                    queue.append(cur.lchild)
                if cur.rchild is not None:
                    queue.append(cur.rchild)

    #先序遍历
    def preorder(self,node):
        if node == None:
            return
        else:
            print(node.item,end = " ")
            self.preorder(node.lchild)
            self.preorder(node.rchild)

    #中序遍历
    def inorder(self,node):
        if node == None:
            return
        else:
            self.inorder(node.lchild)
            print(node.item,end = " ")
            self.inorder(node.rchild)

    #后序遍历
    def postorder(self,node):
        if node == None:
            return
        else:
            self.postorder(node.lchild)
            self.postorder(node.rchild)
            print(node.item,end = " ")

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
    print("")
    t.breadth_travel()
    print("")
    t.preorder(t.root)
    print("")
    t.inorder(t.root)
    print("")
    t.postorder(t.root)

