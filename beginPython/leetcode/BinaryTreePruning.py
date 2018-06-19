class BinaryTreePruning(object):
    def pruneTree(self, root):
        def containsOne(node):
            if not node: return False
            a1 = containsOne(node.left)
            a2 = containsOne(node.right)
            if not a1: node.left = None
            if not a2: node.right = None
            return node.val == 1 or a1 or a2

        return root if containsOne(root) else None


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.left.__str__() if self.left != None else None) + " : " + str(self.val) + " : " + str(self.right.__str__() if self.right != None else None)



if __name__ == '__main__':
    t1 = TreeNode(1)
    t2 = TreeNode(0)
    t3 = TreeNode(0)
    t4 = TreeNode(1)
    t1.right = t2
    t2.left = t3
    t2.right = t4
    a = BinaryTreePruning()
    print(t1)
    print(a.pruneTree(t1))
