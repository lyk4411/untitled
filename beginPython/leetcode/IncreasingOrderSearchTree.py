class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class IncreasingOrderSearchTree(object):
    def increasingBST(self, root):
        def inorder(node):
            if node:
                yield from inorder(node.left)
                yield node.val
                yield from inorder(node.right)

        ans = cur = TreeNode(None)
        for v in inorder(root):
            cur.right = cur = TreeNode(v)
        return ans.right

if __name__ == '__main__':
    a = IncreasingOrderSearchTree()
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t4 = TreeNode(4)
    t5 = TreeNode(5)
    t3.left = t2
    t3.right = t4
    t2.left = t1
    t4.right = t5
    print(t3)
    print(a.increasingBST(t3))

