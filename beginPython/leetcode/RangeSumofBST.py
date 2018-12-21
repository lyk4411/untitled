class RangeSumofBST(object):
    def rangeSumBST(self, root, L, R):
        def dfs(node):
            if node:
                if L <= node.val <= R:
                    self.ans += node.val
                if L < node.val:
                    dfs(node.left)
                if node.val < R:
                    dfs(node.right)

        self.ans = 0
        dfs(root)
        return self.ans

class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

if __name__ == '__main__':
    a = RangeSumofBST()
    t1 = TreeNode(10)
    t2 = TreeNode(5)
    t3 = TreeNode(15)
    t4 = TreeNode(3)
    t5 = TreeNode(7)
    t6 = TreeNode(18)
    t1.left = t2
    t1.right = t3
    t2.left = t4
    t2.right = t5
    t3.right = t6
    print(a.rangeSumBST(t1, 7, 15))
