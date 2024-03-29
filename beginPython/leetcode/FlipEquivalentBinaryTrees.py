import itertools

class FlipEquivalentBinaryTrees(object):
    def flipEquiv(self, root1, root2):
        def dfs(node):
            if node:
                yield node.val
                L = node.left.val if node.left else -1
                R = node.right.val if node.right else -1
                if L < R:
                    yield from dfs(node.left)
                    yield from dfs(node.right)
                else:
                    yield from dfs(node.right)
                    yield from dfs(node.left)
                yield '#'

        return all(x == y for x, y in itertools.zip_longest(
            dfs(root1), dfs(root2)))


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

if __name__ == '__main__':
    a = FlipEquivalentBinaryTrees()
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    a1 = TreeNode(1)
    a2 = TreeNode(3)
    a3 = TreeNode(2)
    t1.left = t2
    t1.right = t3
    a1.left = a2
    a1.right = a3

    print(a.flipEquiv(t1, a1))