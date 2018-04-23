

class MaxChunksToMakeSorted(object):
    def maxChunksToSorted(self, arr):
        ans = ma = 0
        for i, x in enumerate(arr):
            ma = max(ma, x)
            if ma == i: ans += 1
        return ans

if __name__ == '__main__':
    a = MaxChunksToMakeSorted()
    print(a.maxChunksToSorted([4,3,2,1,0]))
    print(a.maxChunksToSorted([1,0,2,3,4]))
    print(a.maxChunksToSorted([1,2,0,3]))


