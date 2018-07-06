class SwiminRisingWater(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        N = len(grid)

        def go(i, j, mid, vis):
            if i == N - 1 and j == N - 1: return True
            vis.add((i, j))
            for d in (-1, 1):
                for ni, nj in [(i + d, j), (i, j + d)]:
                    if 0 <= ni < N and 0 <= nj < N and (ni, nj) not in vis and max(mid, grid[i][j]) == max(mid,
                                                                                                           grid[ni][
                                                                                                               nj]):
                        if go(ni, nj, mid, vis): return True
            return False

        lf = 0
        rt = N * N
        while lf < rt:
            mid = (lf + rt) // 2
            if go(0, 0, mid, set()):
                rt = mid
            else:
                lf = mid + 1
        return rt

if __name__ == '__main__':
    a = SwiminRisingWater()
    print(a.swimInWater([[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]))
    print(a.swimInWater([[0,2],[1,3]]))