class SurfaceAreaof3DShapes(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        area = 0
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if grid[i][j]: area += grid[i][j] * 4 + 2
                if i: area -= min(grid[i][j], grid[i - 1][j]) * 2
                if j: area -= min(grid[i][j], grid[i][j - 1]) * 2
        return area

if __name__ == '__main__':
    a = SurfaceAreaof3DShapes()
    print(a.surfaceArea([[2]]))
    print(a.surfaceArea([[1,2],[3,4]]))
    print(a.surfaceArea([[1,0],[0,2]]))
    print(a.surfaceArea([[1,1,1],[1,0,1],[1,1,1]]))
    print(a.surfaceArea([[2,2,2],[2,1,2],[2,2,2]]))