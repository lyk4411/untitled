class BinaryGap(object):
    def binaryGap(self, N):
        A = [i for i in range(32) if (N >> i) & 1]
        if len(A) < 2: return 0
        return max(A[i + 1] - A[i] for i in range(len(A) - 1))

if __name__ == '__main__':
    a = BinaryGap()
    print(a.binaryGap(5))
    print(a.binaryGap(6))
    print(a.binaryGap(8))