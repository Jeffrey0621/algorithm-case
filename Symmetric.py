class Node(object):
    ## 
    # 节点类
    # 初始化节点
    # # 
    def __init__(self, val, lchild=None, rchild=None):
        self.val = val
        self.lchild = lchild
        self.rchild = rchild

                    
def isSymmetrical(root):
    head = root
    if head == None:
        return True
    if head.lchild == None and head.rchild == None:
        return True
    return judge(head.lchild,head.rchild)
    
        
def judge(left,right):
    if left == None and right == None:
        return True
    if left == None or right == None:
        return False
    if right.val == left.val:
        return judge(right.rchild,left.lchild) and judge(right.lchild,left.rchild)


if __name__ == "__main__":
    tree = Node(0, Node(1, Node(2), Node(3)), Node(1, Node(3),Node(2)))
    print(isSymmetrical(tree))

