class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

class NaryTreePostorderTraversal(object):
    def postorder(self, root):
        ret, stack = [], [root]
        while any(stack):
            node = stack.pop()
            ret.append(node.val)
            stack += [child for child in node.children if child]
        return ret[::-1]

if __name__ == '__main__':
    a = NaryTreePostorderTraversal()
    n1 = Node(1, [])
    n2 = Node(3, [])
    n3 = Node(2, [])
    n4 = Node(4, [])
    n5 = Node(5, [])
    n6 = Node(6, [])
    n1.children.append(n2)
    n1.children.append(n3)
    n1.children.append(n4)
    n2.children.append(n5)
    n2.children.append(n6)

    print(a.postorder(n1))