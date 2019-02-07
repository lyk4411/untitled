class SquaresofaSortedArray(object):
    def sortedSquares(self, A):
        return sorted(x * x for x in A)

if __name__ == '__main__':
    a = SquaresofaSortedArray()
    print(a.sortedSquares([-4, -1, 0, 3, 10]))
