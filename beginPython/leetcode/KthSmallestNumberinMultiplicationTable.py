class KthSmallestNumberinMultiplicationTable(object):
    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        left, right = 1, m * n
        while left < right:
            mid = left + (right - left) // 2
            cnt = 0
            for i in range(1, m + 1):
                cnt += n if mid > n * i else (mid // i)
            if cnt < k:
                left = mid + 1
            else:
                right = mid
        return right

if __name__ == '__main__':
    a = KthSmallestNumberinMultiplicationTable()
    print(a.findKthNumber(3, 3, 5))
    print(a.findKthNumber(2, 3, 6))