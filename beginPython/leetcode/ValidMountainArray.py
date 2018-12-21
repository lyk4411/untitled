class ValidMountainArray(object):
    def validMountainArray(self, A):
        N = len(A)
        i = 0

        # walk up
        while i + 1 < N and A[i] < A[i + 1]:
            i += 1

        # peak can't be first or last
        if i == 0 or i == N - 1:
            return False

        # walk down
        while i + 1 < N and A[i] > A[i + 1]:
            i += 1

        return i == N - 1

if __name__ == '__main__':
    a = ValidMountainArray()
    print(a.validMountainArray([1, 2, 4]))
    print(a.validMountainArray([1, 2]))
    print(a.validMountainArray([1, 2, 4, 7, 4, 3]))