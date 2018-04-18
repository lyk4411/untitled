
class RotatedDigits(object):
    def rotatedDigits(self, N):
        s1 = set([1, 8, 0])
        s2 = set([1, 2, 5, 8, 6, 9, 0])
        def isGood(n):
            s = set([int(i) for i in str(n)])
            return s.issubset(s2) and not s.issubset(s1)
        return sum(isGood(i) for i in range(N + 1))

if __name__ == '__main__':
    a = RotatedDigits()
    print(a.rotatedDigits(123))
    print(a.rotatedDigits(456))
    print(a.rotatedDigits(10))