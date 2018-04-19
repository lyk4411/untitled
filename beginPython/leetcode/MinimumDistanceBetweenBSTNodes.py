class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class MinimumDistanceBetweenBSTNodes(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        vals = []

        def inOrder(root):
            if not root:
                return
            inOrder(root.left)
            vals.append(root.val)
            inOrder(root.right)

        inOrder(root)
        return min([vals[i + 1] - vals[i] for i in range(len(vals) - 1)])

if __name__ == '__main__':
    a = MinimumDistanceBetweenBSTNodes()
    t1 = TreeNode(4)
    t2 = TreeNode(2)
    t3 = TreeNode(6)
    t4 = TreeNode(1)
    t5 = TreeNode(3)
    t1.left = t2
    t1.right = t3
    t2.left = t4
    t2.right = t5
    print(a.minDiffInBST(t1))
