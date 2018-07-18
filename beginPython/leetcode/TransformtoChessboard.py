class TransformtoChessboard(object):
    def movesToChessboard(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        N = len(board)
        colToMove = 0
        rowToMove = 0
        rowOneCnt = 0
        colOneCnt = 0
        for i in range(N):
            for j in range(N):
                if board[0][0] ^ board[i][0] ^ board[i][j] ^ board[0][j] == 1:
                    return -1

        for i in range(N):
            rowOneCnt += board[0][i];
            colOneCnt += board[i][0];
            if board[i][0] == i % 2:
                rowToMove += 1
            if board[0][i] == i % 2:
                colToMove += 1

        if rowOneCnt < N / 2 or rowOneCnt > (N + 1) / 2:
            return -1
        if colOneCnt < N / 2 or colOneCnt > (N + 1) / 2:
            return -1
        if N % 2 == 1:
            if colToMove % 2 == 1:
                colToMove = N - colToMove
            if rowToMove % 2 == 1:
                rowToMove = N - rowToMove
        else:
            colToMove = min(colToMove, N - colToMove)
            rowToMove = min(rowToMove, N - rowToMove)

        return (colToMove + rowToMove) // 2
if __name__ == '__main__':
    a = TransformtoChessboard()
    print(a.movesToChessboard([[0, 1, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1]]))