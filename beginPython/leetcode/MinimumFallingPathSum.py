class MinimumFallingPathSum(object):
    def minFallingPathSum(self, A):
        while len(A) >= 2:
            row = A.pop()
            for i in range(len(row)):
                A[-1][i] += min(row[max(0, i - 1): min(len(row), i + 2)])
        return min(A[0])

if __name__ == '__main__':
    a = MinimumFallingPathSum()
    print(a.minFallingPathSum([[1,2,3],[4,5,6],[7,8,9]]))
