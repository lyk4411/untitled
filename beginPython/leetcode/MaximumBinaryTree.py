from wx.lib.masked.numctrl import MININT


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class MaximumBinaryTree(object):
    def construct(self, root, nums, left, right):
        index = nums.index(max(nums[left:right]))
        root.val = nums[index]
        if nums[left:index]:
            root.left = self.construct(TreeNode(None), nums,left,index)
        if nums[index + 1:right]:
            root.right = self.construct(TreeNode(None), nums, index + 1, right)
        return root

    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        root = TreeNode(None)

        self.construct(root, nums, 0, len(nums))
        return root

if __name__ == '__main__':
    a = MaximumBinaryTree()

    print(a.constructMaximumBinaryTree([3,2,1,6,0,5]))

