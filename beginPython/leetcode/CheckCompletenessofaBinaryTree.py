class CheckCompletenessofaBinaryTree(object):
    def isCompleteTree(self, root):
        nodes = [(root, 1)]
        i = 0
        while i < len(nodes):
            node, v = nodes[i]
            i += 1
            if node:
                nodes.append((node.left, 2 * v))
                nodes.append((node.right, 2 * v + 1))

        return nodes[-1][1] == len(nodes)

class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

if __name__ == '__main__':
    a = CheckCompletenessofaBinaryTree()
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t4 = TreeNode(4)
    t5 = TreeNode(5)
    t6 = TreeNode(6)
    t7 = TreeNode(7)
    t1.left = t2
    t1.right = t3
    t2.left = t4
    t2.right = t5
    t2.left = t6
    print(a.isCompleteTree(t1))
    t2.right = t7
    print(a.isCompleteTree(t1))
    t2.left = None
    print(a.isCompleteTree(t1))

