class LargestPerimeterTriangle(object):
    def largestPerimeter(self, A):
        A.sort()
        for i in range(len(A) - 3, -1, -1):
            if A[i] + A[i + 1] > A[i + 2]:
                return A[i] + A[i + 1] + A[i + 2]
        return 0

if __name__ == '__main__':
    a = LargestPerimeterTriangle()
    print(a.largestPerimeter([2, 1, 2]))
    print(a.largestPerimeter([2, 1, 1]))
    print(a.largestPerimeter([3, 1, 5, 3]))
