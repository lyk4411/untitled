class DistributeCoinsinBinaryTree(object):
    def distributeCoins(self, root):
        self.ans = 0

        def dfs(node):
            if not node: return 0
            L, R = dfs(node.left), dfs(node.right)
            self.ans += abs(L) + abs(R)
            return node.val + L + R - 1

        dfs(root)
        return self.ans
class TreeNode:
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
if __name__ == '__main__':
    a = DistributeCoinsinBinaryTree()
    t1 = TreeNode(3)
    t2 = TreeNode(0)
    t3 = TreeNode(0)
    t1.left = t2
    t1.right = t3
    print(a.distributeCoins(t1))

