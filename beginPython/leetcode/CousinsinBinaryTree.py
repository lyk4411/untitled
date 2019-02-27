class CousinsinBinaryTree(object):
    def isCousins(self, root, x, y):
        parent = {}
        depth = {}

        def dfs(node, par=None):
            if node:
                depth[node.val] = 1 + depth[par.val] if par else 0
                parent[node.val] = par
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root)
        return depth[x] == depth[y] and parent[x] != parent[y]

class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

if __name__ == '__main__':
    a = CousinsinBinaryTree()
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t4 = TreeNode(4)
    t5 = TreeNode(5)
    t1.left = t2
    t1.right = t3
    t2.left = t4
    t3.right = t5
    print(a.isCousins(t1, 2, 3))
    print(a.isCousins(t1, 4, 5))