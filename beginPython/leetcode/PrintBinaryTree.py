


class PrintBinaryTree(object):
    def getHeight(self, node):
        if not node:
            return 0
        return max(1 + self.getHeight(node.left), 1 + self.getHeight(node.right))

    def helper(self, root, d, pos):
        self.res[-d - 1][pos] = str(root.val)
        if root.left: self.helper(root.left, d - 1, pos - 2 ** (d - 1))
        if root.right: self.helper(root.right, d - 1, pos + 2 ** (d - 1))
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        if not root: return [""]
        d = self.getHeight(root)
        cols = 2 ** d - 1
        self.res = [["" for i in range(cols)] for j in range(d)]
        self.helper(root, d - 1, 2 ** (d - 1) - 1)
        return self.res



class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

if __name__ == '__main__':
    a = PrintBinaryTree()
    t1 = TreeNode(1);
    t2 = TreeNode(2);
    t1.left = t2;
    print(a.printTree(t1))