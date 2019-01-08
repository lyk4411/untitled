class NaryTreeLevelOrderTraversal(object):
    def levelOrder(self, root):
        """
            :type root: Node
            :rtype: List[List[int]]
            """
        ans = []
        if root:
            q = [root]

            while q:
                n = len(q)
                ansforlevel = []
                for i in range(n):
                    qtop = q.pop(0)
                    ansforlevel.append(qtop.val)
                    for c in qtop.children:
                        q.append(c)

                ans.append(ansforlevel)

        return ans
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

if __name__ == '__main__':
    a = NaryTreeLevelOrderTraversal()
    ch1 = []
    ch2 = []
    ch3 = []
    ch4 = []
    ch5 = []
    ch6 = []
    n1 = Node(1, ch1)
    n2 = Node(2, ch2)
    n3 = Node(3, ch3)
    n4 = Node(4, ch4)
    n5 = Node(5, ch5)
    n6 = Node(6, ch6)
    ch1.append(n2)
    ch1.append(n3)
    ch1.append(n4)
    ch2.append(n5)
    ch2.append(n6)
    print(a.levelOrder(n1))