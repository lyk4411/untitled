import math
from urllib3.connectionpool import xrange

class ImageSmoother(object):
    def imageSmoother(self,M):
        R, C = len(M), len(M[0])
        ans = [[0] * C for _ in M]

        for r in xrange(R):
            for c in xrange(C):
                count = 0
                for nr in (r - 1, r, r + 1):
                    for nc in (c - 1, c, c + 1):
                        if 0 <= nr < R and 0 <= nc < C:
                            ans[r][c] += M[nr][nc]
                            count += 1
                ans[r][c] = math.floor(ans[r][c]/count)
        return ans

if __name__ == '__main__':
    M = [[1,1,1],[1,0,1],[1,1,1]]
    result = ImageSmoother.imageSmoother(0,M)
    for r in xrange(len(result)):
        for c in xrange(len(result[0])):
            print(result[r][c])
        print('\n')
