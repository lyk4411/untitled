class UnivaluedBinaryTree(object):
    def isUnivalTree(self, root):
        vals = []

        def dfs(node):
            if node:
                vals.append(node.val)
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        return len(set(vals)) == 1


class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


if __name__ == '__main__':
    a = UnivaluedBinaryTree()
    t1 = TreeNode(1)
    t2 = TreeNode(1)
    t3 = TreeNode(1)
    t4 = TreeNode(1)
    t5 = TreeNode(1)
    t6 = TreeNode(1)
    t1.left = t2
    t1.right = t3
    t2.left = t4
    t2.right = t5
    print(a.isUnivalTree(t1))