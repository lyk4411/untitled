class SplitLinkedListinParts(object):
    def splitListToParts(self, root, k):
        cur = root
        for N in range(1001):
            if not cur: break
            cur = cur.next
        width, remainder = divmod(N, k)

        ans = []
        cur = root
        for i in range(k):
            head = write = ListNode(None)
            for j in range(width + (i < remainder)):
                write.next = write = ListNode(cur.val)
                if cur: cur = cur.next
            ans.append(head.next)
        return ans

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

if __name__ == '__main__':
    a = SplitLinkedListinParts()
    ln1 = ListNode(1)
    ln2 = ListNode(2)
    ln3 = ListNode(3)
    ln1.next = ln2
    ln2.next = ln3
    lns = a.splitListToParts(ln1, 5)
    for ln in lns:
        if ln is not None:
            print(ln.val)
        else:
            print("null")
