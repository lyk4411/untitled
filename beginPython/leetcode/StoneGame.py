class StoneGame(object):
    def stoneGame(self, piles):
        N = len(piles)

        def dp(i, j):
            # The value of the game [piles[i], piles[i+1], ..., piles[j]].
            if i > j: return 0
            parity = (j - i + N) % 2
            if parity == 1:  # first player
                return max(piles[i] + dp(i + 1, j), piles[j] + dp(i, j - 1))
            else:
                return min(-piles[i] + dp(i + 1, j), -piles[j] + dp(i, j - 1))

        return dp(0, N - 1) > 0

if __name__ == '__main__':
    a = StoneGame()
    print(a.stoneGame([5, 3, 4, 5]))
    print(a.stoneGame([5, 3, 4, 100, 5]))
    print(a.stoneGame([5, 5, 5, 5, 5]))
