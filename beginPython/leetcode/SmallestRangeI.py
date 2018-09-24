class SmallestRangeI(object):
    def smallestRangeI(self, A, K):
        return max(0, max(A) - min(A) - 2 * K)

if __name__ == '__main__':
    a = SmallestRangeI()
    print(a.smallestRangeI([0, 10], 2))