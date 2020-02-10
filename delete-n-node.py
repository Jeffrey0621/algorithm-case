class Node(object):
    def __init__(self,elem,next=None):
        self.elem = elem
        self.next = next

def delete_last_n_node(head,n):
    #快慢指针法
    #使用前后指针。前指针先走n步，
    #然后前、后指针同时走，当前指针走到节点尾时，后指针刚好走到要删除的节点。
    if head == None or n == 0:
        return head
    before_head = head
    back_head = head
    for i in range(n+1):
        before_head = before_head.next
    while before_head != None:
        before_head = before_head.next
        back_head = back_head.next
    back_head.next = back_head.next.next
    return head

def delete_last_n_node_2(head,n):
    #先计算链表长度count，删除倒数第n个，相当于删除正数count-n+1=5-2+1=4个
    #（开头从1开始计），所以要找它前面的那个节点，也就是第3个,在上面的例子中是
    #找到节点3，记为p，将p.next=p.next.next，就相当于删除了p.next
    if head == None or n == 0:
        return head
    p = head
    count = 0
    while p != None:
        count += 1
        p = p.next
    n = count - n
    p = head
    while n>1:
        p = p.next
        n -= 1
    p.next = p.next.next
    return head

if __name__ == "__main__":
    l1 = Node(1)
    l1.next = Node(2)
    l1.next.next = Node(3)
    l1.next.next.next = Node(4)
    l1.next.next.next.next = Node(5)
    l2 = delete_last_n_node(l1,3)
    print(l2.elem,l2.next.elem,l2.next.next.elem,l2.next.next.next.elem)
    l1 = Node(1)
    l1.next = Node(2)
    l1.next.next = Node(3)
    l1.next.next.next = Node(4)
    l1.next.next.next.next = Node(5)
    l3 = delete_last_n_node_2(l1,3)
    print(l3.elem,l3.next.elem,l3.next.next.elem,l3.next.next.next.elem)

