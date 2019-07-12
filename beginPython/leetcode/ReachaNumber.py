class ReachaNumber(object):
    def reachNumber(self, target):
        target = abs(target)
        k = 0
        while target > 0:
            k += 1
            target -= k

        return k if target % 2 == 0 else k + 1 + k % 2

if __name__ == '__main__':
    a = ReachaNumber()
    print(a.reachNumber(10))
    print(a.reachNumber(3))
