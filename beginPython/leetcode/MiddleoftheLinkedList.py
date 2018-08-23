class MiddleoftheLinkedList(object):
    def middleNode(self, head):
        A = [head]
        while A[-1].next:
            A.append(A[-1].next)
        return A[len(A) // 2]

class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None
if __name__ == '__main__':
    a = MiddleoftheLinkedList()
    h1 = ListNode(1)
    h2 = ListNode(2)
    h3 = ListNode(3)
    h4 = ListNode(4)
    h5 = ListNode(5)
    h6 = ListNode(6)
    h1.next = h2
    h2.next = h3
    h3.next = h4
    h4.next = h5
    h5.next = h6
    print(a.middleNode(h1).val)
    print(a.middleNode(h2).val)
    print(a.middleNode(h3).val)
    print(a.middleNode(h4).val)

