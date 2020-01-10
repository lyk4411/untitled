class NumberofClosedIslands():
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def helper(grid, i, j, h, w):
            if i < 0 or j < 0 or i >= h or j >= w:
                return 1
            if grid[i][j] != 0:
                return 0
            grid[i][j] = -1
            # return helper(grid, i - 1, j, h, w) or helper(grid, i + 1, j, h, w) or helper(grid, i, j - 1, h, w) or helper(grid, i, j + 1, h, w)  ## in this case, if the first return value is 1, the left functions won't be called.
            up = helper(grid, i - 1, j, h, w)
            down = helper(grid, i + 1, j, h, w)
            left = helper(grid, i, j - 1, h, w)
            right = helper(grid, i, j + 1, h, w)
            return up or down or left or right

        h = len(grid)
        w = len(grid[0])
        res = 0
        for i in range(h):
            for j in range(w):
                if grid[i][j] != 0:
                    continue
                if helper(grid, i, j, h, w) == 0:
                    res += 1
        return res

if __name__ == '__main__':
    a = NumberofClosedIslands()
    grid1 = [[1, 1, 1, 1, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 0]]
    grid2 = [[0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0]]
    grid3 = [[1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1]]
    print(a.closedIsland(grid1))
    print(a.closedIsland(grid2))
    print(a.closedIsland(grid3))