class LongestContinuousIncreasingSubsequence(object):
    def findLengthOfLCIS(self, nums):
        ans = anchor = 0
        for i in range(len(nums)):
            if i and nums[ i -1] >= nums[i]:
                anchor = i
            ans = max(ans, i - anchor + 1)
        return ans


if __name__ == '__main__':
    lcis = LongestContinuousIncreasingSubsequence()
    print(lcis.findLengthOfLCIS(['a', 'b', 'c']))
    print(lcis.findLengthOfLCIS(['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']))
    print(lcis.findLengthOfLCIS(['a', 'a', 'b', 'a', 'a', 'b', 'a', 'a', 'b']))
    print(lcis.findLengthOfLCIS([2,2,2,2]))
    print(lcis.findLengthOfLCIS([1,2,3,4,5,2,4,6,1,8,9,7,4]))


