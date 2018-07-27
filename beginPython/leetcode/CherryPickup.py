


class CherryPickup(object):
    def cherryPickup(self, grid):
        n = len(grid)
        memo = [[[-99 for i in range(n)] for j in range(n)] for k in range(n)]
        def dp(x1, y1, x2):
            y2 = x1 + y1 - x2
            if x1 < 0 or y1 < 0 or x2 < 0 or y2 < 0: return -1
            if grid[y1][x1] < 0 or grid[y2][x2] < 0: return -1
            if x1 == 0 and y1 == 0: return grid[y1][x1]
            if memo[x1][y1][x2] != -99: return memo[x1][y1][x2]
            ans = max( dp(x1 - 1, y1, x2 - 1), dp(x1, y1 - 1, x2),dp(x1, y1 - 1, x2 - 1), dp(x1 - 1, y1, x2))
            if ans < 0:
                memo[x1][y1][x2] = -1
                return memo[x1][y1][x2]
            ans += grid[y1][x1]
            if x1 != x2: ans += grid[y2][x2]
            memo[x1][y1][x2] = ans
            return memo[x1][y1][x2]
        return max(0, dp(n - 1, n - 1, n - 1))


if __name__ == '__main__':
    a = CherryPickup()
    print(a.cherryPickup([[1, 1], [1, 1]]))
    print(a.cherryPickup([[0, 1, -1], [1, 0, -1], [1, 1, 1]]))
