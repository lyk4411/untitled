class TransposeMatrix(object):
    def transpose(self, A):
        R = len(A)
        C = len(A[0])
        ans = [[0 for i in range(R)] for j in range(C)]
        print(ans)
        for i in range(R):
            for j in range(C):
                ans[j][i] = A[i][j]
        return ans

if __name__ == '__main__':
    a = TransposeMatrix()
    print(a.transpose([[1,2,3],[4,5,6],[7,8,9]]))
    print(a.transpose([[1,2,3],[4,5,6]]))
