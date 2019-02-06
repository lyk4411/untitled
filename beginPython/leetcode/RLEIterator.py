class RLEIterator(object):
    def __init__(self, A):
        self.A = A
        self.i = 0
        self.q = 0

    def next(self, n):
        while self.i < len(self.A):
            if self.q + n > self.A[self.i]:
                n -= self.A[self.i] - self.q
                self.q = 0
                self.i += 2
            else:
                self.q += n
                return self.A[self.i + 1]
        return -1

if __name__ == '__main__':
    a = RLEIterator([3, 8, 0, 9, 2, 5])
    print(a.next(2))
    print(a.next(1))
    print(a.next(1))
    print(a.next(2))
