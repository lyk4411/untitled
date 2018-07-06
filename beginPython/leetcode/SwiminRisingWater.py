import heapq
from filecmp import cmp


class Node(object):
    def __init__(self, val, x, y):
        self.val = val
        self.x = x
        self.y = y
    def __cmp__(self, other):
        return cmp(self.val, other.val)
    def __lt__(self, other):
        return self.val < other.val
    def __str__(self):
        return "val:" + str(self.val) + " x:" + str(self.x) + " y:" + str(self.y)
class SwiminRisingWater(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        N = len(grid)
        M = len(grid[0])
        vis = set()
        node = Node(grid[0][0], 0, 0)
        q = []
        heapq.heappush(q, node)
        vis.add((0, 0))
        while q:
            t = heapq.heappop(q)
            if t.x == N -1 and t.y == M - 1:
                return t.val
            for d in (-1, 1):
                for ni, nj in [(t.x + d, t.y), (t.x, t.y + d)]:
                    if (ni, nj) not in vis and 0 <= ni < N and 0 <= nj < M:
                        grid[ni][nj] = max(grid[ni][nj], grid[t.x][t.y])
                        heapq.heappush(q, Node(grid[ni][nj], ni, nj))
                        vis.add((ni, nj))

        return 0




if __name__ == '__main__':
    a = SwiminRisingWater()
    print(a.swimInWater([[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]))
    print(a.swimInWater([[0,2],[1,3]]))