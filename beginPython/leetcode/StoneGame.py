class StoneGame(object):
    def stoneGame(self, piles):
        N = len(piles)
        dp = [[0 for _ in range(len(piles) + 2)] for _ in range(len(piles) + 2)]

        for size in range(1, len(piles) + 1):
            for i in range(0, len(piles) - size + 1):
                j = i + size - 1
                if ((j + i + N) % 2 == 1):
                    dp[i + 1][j + 1] = max(piles[i] + dp[i + 2][j + 1], piles[j] + dp[i + 1][j])
                    print("dp[" + str(i + 1) + "][" + str(j + 1) + "]:" + str(dp[i + 1][j + 1]))
                else:
                    dp[i + 1][j + 1] = min(-piles[i] + dp[i + 2][j + 1], -piles[j] + dp[i + 1][j])
                    print("dp[" + str(i + 1) + "][" + str(j + 1) + "]:" + str(dp[i + 1][j + 1]))

        return dp[1][len(piles)] > 0

if __name__ == '__main__':
    a = StoneGame()
    print(a.stoneGame([5, 3, 4, 5]))
    print(a.stoneGame([5, 3, 4, 100, 5]))
    print(a.stoneGame([5, 5, 5, 5, 5]))
