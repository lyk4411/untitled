class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class SearchinaBinarySearchTree(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """

        if not root:
            return None
        if root.val == val:
            return root
        elif root.val < val:
            return self.searchBST(root.right, val)
        else:
            return self.searchBST(root.left, val)
if __name__ == '__main__':
    a = SearchinaBinarySearchTree()
    t1 = TreeNode(4)
    t2 = TreeNode(2)
    t3 = TreeNode(7)
    t4 = TreeNode(1)
    t5 = TreeNode(3)
    t1.left = t2
    t1.right = t3
    t2.left = t4
    t2.right = t5
    print(a.searchBST(t1, 2).val)
    print(a.searchBST(t1, 5))