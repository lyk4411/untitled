class DSU:
    def __init__(self, N):
        self.p = list(range(N))


    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]


    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        self.p[xr] = yr
class RegionsCutBySlashes(object):
    def regionsBySlashes(self, grid):
        N = len(grid)
        dsu = DSU(4 * N * N)
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                root = 4 * (r * N + c)
                if val in '/':
                    dsu.union(root + 0, root + 3)
                    dsu.union(root + 1, root + 2)
                if val in '\\':
                    dsu.union(root + 0, root + 1)
                    dsu.union(root + 2, root + 3)
                if val in ' ':
                    dsu.union(root + 0, root + 1)
                    dsu.union(root + 1, root + 2)
                    dsu.union(root + 2, root + 3)

                if c + 1 < N:
                    dsu.union(root + 1, (root + 4) + 3)
                if r + 1 < N:
                    dsu.union(root + 2, (root + 4 * N) + 0)

        return sum(dsu.find(x) == x for x in range(4 * N * N))

if __name__ == '__main__':
    a = RegionsCutBySlashes()
    print(a.regionsBySlashes([" /", "/ "]))
    print(a.regionsBySlashes([" /", "  "]))
    print(a.regionsBySlashes(["\\/", "/\\"]))
    print(a.regionsBySlashes(["/\\", "\\/"]))
    print(a.regionsBySlashes(["//", "/ "]))