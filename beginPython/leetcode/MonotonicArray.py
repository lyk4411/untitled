class MonotonicArray(object):
    def isMonotonic(self, A):
        return (all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or
                all(A[i] >= A[i + 1] for i in range(len(A) - 1)))

if __name__ == '__main__':
    a = MonotonicArray()

    print(a.isMonotonic([1, 2, 3, 4]))
    print(a.isMonotonic([1, 2, 3, 4, 1]))
