class LeafSimilarTrees(object):
    def leafSimilar(self, root1, root2):
        def dfs(node):
            if node:
                if not node.left and not node.right:
                    yield node.val
                yield from dfs(node.left)
                yield from dfs(node.right)

        return list(dfs(root1)) == list(dfs(root2))

class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
if __name__ == '__main__':
    a = LeafSimilarTrees()
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t4 = TreeNode(4)
    t5 = TreeNode(5)
    t6 = TreeNode(6)
    t1.left = t2
    t1.right = t3
    t2.left = t4
    t2.right = t5
    t3.left = t6
    print(a.leafSimilar(t1, t1))
    print(a.leafSimilar(t1, t2))
