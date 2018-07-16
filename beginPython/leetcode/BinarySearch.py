class BinarySearch(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1
        return -1

if __name__ == '__main__':
    a = BinarySearch()
    print(a.search([-1, 0, 3, 7, 9], 7))
    print(a.search([-1, 0, 3, 7, 9], 2))
