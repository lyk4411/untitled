class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class LongestUnivaluePath(object):
    def longestUnivaluePath(self, root):
        self.ans = 0

        def arrow_length(node):
            if not node: return 0
            left_length = arrow_length(node.left)
            right_length = arrow_length(node.right)
            left_arrow = right_arrow = 0
            if node.left and node.left.val == node.val:
                left_arrow = left_length + 1
            if node.right and node.right.val == node.val:
                right_arrow = right_length + 1
            self.ans = max(self.ans, left_arrow + right_arrow)
            return max(left_arrow, right_arrow)

        arrow_length(root)
        return self.ans

if __name__ == '__main__':
    t1 = TreeNode(5)
    t2 = TreeNode(4)
    t3 = TreeNode(5)
    t4 = TreeNode(1)
    t5 = TreeNode(1)
    t6 = TreeNode(5)
    t1.left = t2;
    t1.right = t3;
    t2.left = t4;
    t2.right = t5;
    t3.right = t6;
    a = LongestUnivaluePath()
    print(a.longestUnivaluePath(t1))