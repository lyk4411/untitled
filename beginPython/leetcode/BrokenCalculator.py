class BrokenCalculator(object):
    def brokenCalc(self, X, Y):
        ans = 0
        while Y > X:
            ans += 1
            if Y % 2:
                Y += 1
            else:
                Y //= 2

        return ans + X - Y

if __name__ == '__main__':
    a = BrokenCalculator()
    print(a.brokenCalc(2, 100))
    print(a.brokenCalc(2, 3))
    print(a.brokenCalc(2, 4))