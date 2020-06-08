from typing import List


class LuckyNumbersinaMatrix:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        rmin = [min(x) for x in matrix]
        cmax = [max(x) for x in zip(*matrix)]
        return [matrix[i][j] for i in range(len(matrix)) for j in range(len(matrix[0])) if rmin[i] == cmax[j]]

if __name__ == '__main__':
    a = LuckyNumbersinaMatrix()
    matrix = [[3, 7, 8], [9, 11, 13], [15, 16, 17]]
    print(a.luckyNumbers(matrix))
    matrix = [[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]]
    print(a.luckyNumbers(matrix))
