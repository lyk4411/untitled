class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class MaximumWidthofBinaryTree(object):
    def widthOfBinaryTree(self, root):
        self.ans = 0
        left = {}
        def dfs(node, depth = 0, pos = 0):
            if node:
                left.setdefault(depth, pos)
                self.ans = max(self.ans, pos - left[depth] + 1)
                dfs(node.left, depth + 1, pos * 2)
                dfs(node.right, depth + 1, pos * 2 + 1)

        dfs(root)
        return self.ans

if __name__ == '__main__':
    a = MaximumWidthofBinaryTree()
    t1 = TreeNode(1)
    t2 = TreeNode(3)
    t3 = TreeNode(2)
    t4 = TreeNode(5)
    t5 = TreeNode(9)
    t6 = TreeNode(6)
    t7 = TreeNode(7)
    t1.left = t2
    t1.right = t3
    t2.left = t4
    t3.right = t5
    t4.left = t6
    t5.right = t7
    print(a.widthOfBinaryTree(t1))