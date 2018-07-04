class MaxIncreasetoKeepCitySkyline(object):
    def maxIncreaseKeepingSkyline(self, grid):
        row_maxes = [max(row) for row in grid]
        col_maxes = [max(col) for col in zip(*grid)]

        return sum(min(row_maxes[r], col_maxes[c]) - val
                   for r, row in enumerate(grid)
                   for c, val in enumerate(row))

if __name__ == '__main__':
    a = MaxIncreasetoKeepCitySkyline()
    print(a.maxIncreaseKeepingSkyline([[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]))