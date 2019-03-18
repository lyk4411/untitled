class SmallestStringStartingFromLeaf(object):
    def smallestFromLeaf(self, root):
        self.ans = "~"

        def dfs(node, A):
            if node:
                A.append(chr(node.val + ord('a')))
                if not node.left and not node.right:
                    self.ans = min(self.ans, "".join(reversed(A)))

                dfs(node.left, A)
                dfs(node.right, A)
                A.pop()

        dfs(root, [])
        return self.ans
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

if __name__ == '__main__':
    a = SmallestStringStartingFromLeaf()
    t1 = TreeNode(0)
    t2 = TreeNode(1)
    t3 = TreeNode(2)
    t4 = TreeNode(3)
    t5 = TreeNode(4)
    t6 = TreeNode(3)
    t7 = TreeNode(4)
    t1.left = t2
    t1.right = t3
    t2.left = t4
    t2.right = t5
    t3.left = t6
    t3.right = t7
    a1 = TreeNode(25)
    a2 = TreeNode(1)
    a3 = TreeNode(3)
    a4 = TreeNode(1)
    a5 = TreeNode(3)
    a6 = TreeNode(0)
    a7 = TreeNode(2)
    a1.left = a2
    a1.right = a3
    a2.left = a4
    a2.right = a5
    a3.left = a6
    a3.right = a7
    print(a.smallestFromLeaf(t1))
    print(a.smallestFromLeaf(a1))