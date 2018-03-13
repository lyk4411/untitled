
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class TrimaBinarySearchTree(object):
    def trimBST(self, root, L, R):
        def trim(node):
            if not node:
                return None
            elif node.val > R:
                return trim(node.left)
            elif node.val < L:
                return trim(node.right)
            else:
                node.left = trim(node.left)
                node.right = trim(node.right)
                return node
        return trim(root)

if __name__ == '__main__':
    tbsc = TrimaBinarySearchTree()
    a1 = TreeNode(1)
    a2 = TreeNode(2)
    a0 = TreeNode(0)
    a1.left = a0
    a1.right = a2

    print(a1)
    print(tbsc.trimBST(a1,1,2))
    print(a1)
