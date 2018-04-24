


class TwoKeysKeyboard(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        d = 2
        while n > 1:
            while n % d == 0:
                ans += d
                n /= d
            d += 1
        return ans

if __name__ == '__main__':
    a = TwoKeysKeyboard()
    print(a.minSteps(1))
    print(a.minSteps(2))
    print(a.minSteps(3))
    print(a.minSteps(4))
    print(a.minSteps(5))
    print(a.minSteps(6))
    print(a.minSteps(7))
    print(a.minSteps(8))
    print(a.minSteps(9))
