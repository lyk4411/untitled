
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class FindElementsinaContaminatedBinaryTree(object):
    def __init__(self, root: TreeNode):
        self.seen = set()

        def dfs(node: TreeNode, v: int) -> None:
            if node:
                node.val = v
                self.seen.add(v)
                dfs(node.left, 2 * v + 1)
                dfs(node.right, 2 * v + 2)

        dfs(root, 0)

    def find(self, target: int) -> bool:
        return target in self.seen


if __name__ == '__main__':
    t1 = TreeNode(-1)
    t3 = TreeNode(-1)
    t1.right = t3
    a = FindElementsinaContaminatedBinaryTree(t1)
    print(a.find(1))
    print(a.find(2))
    b1 = TreeNode(-1)
    b2 = TreeNode(-1)
    b3 = TreeNode(-1)
    b4 = TreeNode(-1)
    b1.right = b2
    b2.left = b3
    b3.left = b4
    b = FindElementsinaContaminatedBinaryTree(b1)
    print("==================================================================================================")
    print(b.find(2))
    print(b.find(3))
    print(b.find(4))
    print(b.find(5))
