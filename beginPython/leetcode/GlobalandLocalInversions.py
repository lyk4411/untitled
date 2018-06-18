import sys


class GlobalandLocalInversions(object):
    def isIdealPermutation(self, A):
        n = len(A)

        temp = sys.maxsize
        for i in range(n - 1, 1, -1):
            temp = min(temp, A[i])
            if A[i - 2] > temp:
                return False
        return True

if __name__ == '__main__':
    a = GlobalandLocalInversions()
    print(a.isIdealPermutation([1, 0, 2]))
    print(a.isIdealPermutation([1, 2, 0]))
