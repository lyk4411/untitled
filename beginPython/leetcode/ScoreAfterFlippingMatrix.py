

class ScoreAfterFlippingMatrix(object):
    def matrixScore(self, A):
        def moveLine(A):
            for i in range(len(A)):
                if A[i][0] == 0:
                    for j in range(len(A[0])):
                        A[i][j] = A[i][j] ^ 1

        def moveColumn(A):
            for j in range(len(A[0])):
                zeroCount = 0
                oneCount = 0
                for i in range(len(A)):
                    if A[i][j] == 1:
                        oneCount += 1
                    else:
                        zeroCount += 1

                if zeroCount > oneCount:
                    for k in range(len(A)):
                        A[k][j] = A[k][j] ^ 1


        def countResult(A, score):
            # print(list(enumerate(A[0])))
            for r in range(len(A)):
                score += sum(x * (1 << (len(A[0]) - 1 - c))
                            for c, x in enumerate(A[r]))
            return score
        score = 0
        moveLine(A)
        moveColumn(A)
        return countResult(A, score)


if __name__ == '__main__':
    a = ScoreAfterFlippingMatrix()
    print(a.matrixScore([[0,0,1,1],[1,0,1,0],[1,1,0,0]]))
