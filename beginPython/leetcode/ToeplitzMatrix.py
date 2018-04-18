
class ToeplitzMatrix(object):
    def isToeplitzMatrix(self, matrix):
        groups = {}
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                if r-c not in groups:
                    groups[r-c] = val
                elif groups[r-c] != val:
                    return False
        return True

if __name__ == '__main__':
    a = ToeplitzMatrix()
    matrix1 = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
    matrix2 = [[1,2],[2,2]]
    print(a.isToeplitzMatrix(matrix1))
    print(a.isToeplitzMatrix(matrix2))