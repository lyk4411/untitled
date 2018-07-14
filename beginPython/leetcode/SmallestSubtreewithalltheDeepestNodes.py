import collections
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class SmallestSubtreewithalltheDeepestNodes(object):
    def subtreeWithAllDeepest(self, root):
        # The result of a subtree is:
        # Result.node: the largest depth node that is equal to or
        #              an ancestor of all the deepest nodes of this subtree.
        # Result.dist: the number of nodes in the path from the root
        #              of this subtree, to the deepest node in this subtree.
        Result = collections.namedtuple("Result", ("node", "dist"))

        def dfs(node):
            # Return the result of the subtree at this node.
            if not node: return Result(None, 0)
            L, R = dfs(node.left), dfs(node.right)
            if L.dist > R.dist: return Result(L.node, L.dist + 1)
            if L.dist < R.dist: return Result(R.node, R.dist + 1)
            return Result(node, L.dist + 1)

        return dfs(root).node

if __name__ == '__main__':
    a = SmallestSubtreewithalltheDeepestNodes()
    t1 = TreeNode(3)
    t2 = TreeNode(5)
    t3 = TreeNode(1)
    t4 = TreeNode(6)
    t5 = TreeNode(2)
    t6 = TreeNode(0)
    t7 = TreeNode(8)
    t8 = TreeNode(7)
    t9 = TreeNode(4)
    t1.left = t2
    t1.right = t3
    t2.left = t4
    t2.right = t5
    t3.left = t6
    t3.right = t7
    t5.left = t8
    t5.right = t9
    print(a.subtreeWithAllDeepest(t1).val)