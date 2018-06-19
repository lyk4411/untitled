class PeakIndexinaMountainArray(object):
    def peakIndexInMountainArray(self, A):
        lo, hi = 0, len(A) - 1
        while lo < hi:
            mi = (lo + hi) // 2
            if A[mi] < A[mi + 1]:
                lo = mi + 1
            else:
                hi = mi
        return lo

if __name__ == '__main__':
    a = PeakIndexinaMountainArray()
    print(a.peakIndexInMountainArray([1, 2, 1]))
    print(a.peakIndexInMountainArray([1, 2, 1, 0]))