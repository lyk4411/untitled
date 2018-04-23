
class MaxChunksToMakeSortedII:
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        sum1 = 0
        sum2 = 0
        ans = 0;
        arr1 = arr[:]
        arr2 = sorted(arr1)
        for i,v in enumerate(arr):
            sum1 += v
            sum2 += arr2[i]
            if sum1 == sum2:
                ans += 1
        return ans

if __name__ == '__main__':
    a = MaxChunksToMakeSortedII()
    print(a.maxChunksToSorted([4,3,2,1,0]))
    print(a.maxChunksToSorted([1,0,2,3,4]))
    print(a.maxChunksToSorted([1,2,0,3]))

