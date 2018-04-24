class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class SecondMinimumNodeInaBinaryTree(object):
    def findSecondMinimumValue(self, root):
        def dfs(node):
            if node:
                uniques.add(node.val)
                dfs(node.left)
                dfs(node.right)

        uniques = set()
        dfs(root)

        min1, ans = root.val, float('inf')
        for v in uniques:
            if min1 < v < ans:
                ans = v

        return ans if ans < float('inf') else -1

if __name__ == '__main__':
    a = SecondMinimumNodeInaBinaryTree()
    t1 = TreeNode(2)
    t2 = TreeNode(2)
    t3 = TreeNode(5)
    t4 = TreeNode(5)
    t5 = TreeNode(7)
    t1.left = t2;
    t1.right = t3;
    t3.left = t4;
    t3.right = t5;
    print(a.findSecondMinimumValue(t1))