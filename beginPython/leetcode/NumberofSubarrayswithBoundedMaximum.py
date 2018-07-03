class NumberofSubarrayswithBoundedMaximum(object):
    def numSubarrayBoundedMax(self, A, L, R):
        left = 0
        count = 0
        res = 0
        for right in range(0, len(A)):
            if A[right] >= L and A[right] <= R:
                res += right - left + 1
                count = right - left +1
            elif A[right] < L:
                res += count
            else:
                left = right + 1
                count = 0
        return res

if __name__ == '__main__':
    a = NumberofSubarrayswithBoundedMaximum()
    print(a.numSubarrayBoundedMax([2, 1, 4, 3], 2, 3))

