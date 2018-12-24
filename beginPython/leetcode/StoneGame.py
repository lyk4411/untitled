class StoneGame(object):
    def stoneGame(self, piles):
        N = len(piles)
        dp = [[0 for _ in range(len(piles) + 1)] for _ in range(len(piles) + 1)]

        for size in range(1, len(piles) + 1):
            for i in range(0, len(piles) - size + 1):
                j = i + size - 1
                if ((j + i + N) % 2 == 1):
                    dp[i][j] = max(piles[i] + dp[i + 1][j], piles[j] + dp[i][j - 1])
                    print("dp[" + str(i) + "][" + str(j) + "]:" + str(dp[i][j]))
                else:
                    dp[i][j] = min(-piles[i] + dp[i + 1][j], -piles[j] + dp[i][j - 1])
                    print("dp[" + str(i) + "][" + str(j) + "]:" + str(dp[i][j]))

        return dp[0][len(piles) - 1] > 0

if __name__ == '__main__':
    a = StoneGame()
    print(a.stoneGame([5, 3, 4, 5]))
    print(a.stoneGame([5, 3, 4, 100, 5]))
    print(a.stoneGame([5, 5, 5, 5, 5]))
