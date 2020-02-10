class Node(object):
    def __init__(self,elem,next=None):
        self.elem = elem
        self.next = next

def Merge(head1,head2):
    #递归
    if head1 is None and head2 is None:
        return None
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    if head1.elem <= head2.elem:
        head1.next = Merge(head1.next,head2)
        return head1
    else:
        head2.next = Merge(head1,head2.next)
        return head2
        
def Merge1(head1,head2):
    if head1 is None and head2 is None:
        return None
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    root = Node(0)
    first = root
    while head1 and head2:
        val1 = head1.elem
        val2 = head2.elem
        if val1 <= val2:
            root.next = Node(val1)
            head1 = head1.next
        else:
            root.next = Node(val2)
            head2 = head2.next
        root = root.next
    if head1:
        root.next = head1
    if head2:
        root.next = head2
    return first.next


if __name__ == "__main__":
    l1 = Node(1)
    l1.next = Node(3)
    l1.next.next = Node(5)

  
    l2 = Node(2)
    l2.next = Node(4)
    l2.next.next = Node(6)
  
    l3 = Merge(l1,l2)
    print(l3.elem,l3.next.elem,l3.next.next.elem,l3.next.next.next.elem,l3.next.next.next.next.elem,l3.next.next.next.next.next.elem)

    l1 = Node(1)
    l1.next = Node(3)
    l1.next.next = Node(5)

  
    l2 = Node(2)
    l2.next = Node(4)
    l2.next.next = Node(6)
  
    l3 = Merge1(l1,l2)
    print(l3.elem,l3.next.elem,l3.next.next.elem,l3.next.next.next.elem,l3.next.next.next.next.elem,l3.next.next.next.next.next.elem)

