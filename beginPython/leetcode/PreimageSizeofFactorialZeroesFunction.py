import sys


class PreimageSizeofFactorialZeroesFunction(object):
    def preimageSizeFZF(self, K):
        """
        :type K: int
        :rtype: int
        """
        a = 0
        b = sys.maxsize
        while a < b:
            mid = a + (b - a) // 2
            k = self.trailingZeroes(mid)
            if k == K:
                return 5
            elif k < K:
                a = mid + 1
            else:
                b = mid - 1
        return 0

    def trailingZeroes(self, n):
        x = 5
        ans = 0
        while n >= x:
            ans += n // x
            x *= 5
        return ans

if __name__ == '__main__':
    a = PreimageSizeofFactorialZeroesFunction()
    print(a.preimageSizeFZF(5))
    print(a.preimageSizeFZF(0))
    print(a.preimageSizeFZF(15))
    print(a.preimageSizeFZF(1000000000))

