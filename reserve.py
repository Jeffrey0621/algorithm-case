class Node(object):
    def __init__(self, elem, next=None):
        self.elem = elem
        self.next = next
 
def reverseList(head):
    if head == None or head.next==None:  # 若链表为空或者仅一个数就直接返回
        return head 
    pre = None
    next = None
    while(head != None): 
        next = head.next
        head.next = pre
        pre = head
        head = next
    return pre

if __name__ == '__main__':
    l1 = Node(1)    # 建立链表1->2->3->4->None
    l1.next = Node(2)
    l1.next.next = Node(3)
    l1.next.next.next = Node(4)
    l = reverseList(l1)
    print (l.elem, l.next.elem, l.next.next.elem, l.next.next.next.elem)
