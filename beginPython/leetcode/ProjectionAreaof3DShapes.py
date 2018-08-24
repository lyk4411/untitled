class ProjectionAreaof3DShapes(object):
    def projectionArea(self, grid):
        N = len(grid)
        ans = 0

        for i in range(N):
            best_row = 0  # max of grid[i][j]
            best_col = 0  # max of grid[j][i]
            for j in range(N):
                if grid[i][j]: ans += 1  # top shadow
                best_row = max(best_row, grid[i][j])
                best_col = max(best_col, grid[j][i])

            ans += best_row + best_col

        return ans


if __name__ == '__main__':
    a = ProjectionAreaof3DShapes()
    print(a.projectionArea([[2]]))
    print(a.projectionArea([[1,2],[3,4]]))
    print(a.projectionArea([[1,0],[0,2]]))
