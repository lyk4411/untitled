from time import sleep


class KnightProbabilityinChessboard(object):
    def knightProbability(self, N, K, r, c):
        dp0 = [[1 for i in range(N)] for i in range(N)]
        for i in range(0,K):
            dp1 = [[0 for i in range(N)] for i in range(N)]
            for j in range(0, N):
                for k in range(0, N):
                    for rd, cd in ((2, 1), (2, -1), (-2, 1), (-2, -1),
                                   (1, 2), (1, -2), (-1, 2), (-1, -2)):
                        row = j + rd
                        col = k + cd
                        if 0 <= row < N and 0 <= col < N:
                            dp1[row][col] += dp0[j][k]

            dp0 = dp1
        return dp0[r][c] / 8**K

if __name__ == '__main__':
    a = KnightProbabilityinChessboard()
    print(a.knightProbability(3, 2, 0, 0))