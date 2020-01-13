class CountServersthatCommunicate(object):
    def countServers(self, grid) -> int:
        R, C, res = len(grid), len(grid[0]), 0
        for r in range(R):
            for c in range(C):
                if grid[r][c]:
                    res += any(grid[i][c] for i in range(R) if i != r) or any(grid[r][j] for j in range(C) if j != c)
        return res

if __name__ == '__main__':
    a = CountServersthatCommunicate()
    print(a.countServers([[1, 0], [0, 1]]))
    print(a.countServers([[1, 0], [1, 1]]))
    print(a.countServers([[1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]]))
