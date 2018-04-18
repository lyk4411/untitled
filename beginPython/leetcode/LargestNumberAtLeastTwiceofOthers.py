
class LargestNumberAtLeastTwiceofOthers(object):
    def dominantIndex(self, nums):
        m = max(nums)
        if all(m >= 2 * x for x in nums if x != m):
            return nums.index(m)
        return -1


if __name__ == '__main__':
    a = LargestNumberAtLeastTwiceofOthers()
    nums1 = [3, 6, 1, 0]
    nums2 = [1, 2, 3, 4]
    print(a.dominantIndex(nums1))
    print(a.dominantIndex(nums2))

