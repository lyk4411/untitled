import collections

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class FindDuplicateSubtrees(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        count = collections.Counter()
        ans = []

        def collect(node):
            if not node: return "#"
            serial = "{},{},{}".format(node.val, collect(node.left), collect(node.right))
            count[serial] += 1
            if count[serial] == 2:
                ans.append(node)
            return serial

        collect(root)
        return ans

if __name__ == '__main__':
    a = FindDuplicateSubtrees()
    t1 = TreeNode(1)
    t2 = TreeNode(1)
    t3 = TreeNode(1)
    t4 = TreeNode(1)
    t5 = TreeNode(1)
    t6 = TreeNode(1)
    t7 = TreeNode(1)

    t1.left = t2;
    t1.right = t3;
    t2.left = t4;
    t3.left = t5;
    t3.right = t6;
    t5.left = t7;
    print(list(a.findDuplicateSubtrees(t1)))
    # def findDuplicateSubtrees(self, root):
    #     trees = collections.defaultdict()
    #     trees.default_factory = trees.__len__
    #     count = collections.Counter()
    #     ans = []
    #
    #     def lookup(node):
    #         if node:
    #             uid = trees[node.val, lookup(node.left), lookup(node.right)]
    #             count[uid] += 1
    #             if count[uid] == 2:
    #                 ans.append(node)
    #             return uid
    #
    #     lookup(root)
    #     return ans
