class LinkedListComponents(object):
    def numComponents(self, head, G):
        Gset = set(G)
        cur = head
        ans = 0
        while cur:
            if (cur.val in Gset and
                        getattr(cur.next, 'val', None) not in Gset):
                ans += 1
            cur = cur.next

        return ans

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

if __name__ == '__main__':
    a = LinkedListComponents()
    l1 = ListNode(0)
    l2 = ListNode(1)
    l3 = ListNode(2)
    l4 = ListNode(3)
    l1.next = l2
    l2.next = l3
    l3.next = l4
    print(a.numComponents(l1,(0,1,3)))