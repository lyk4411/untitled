import itertools


class LargestTriangleArea(object):
    def largestTriangleArea(self, points):
        def area(p, q, r):
            return .5 * abs(p[0 ] *q[1 ] +q[0 ] *r[1 ] +r[0 ] *p[1] -p[1]*q[0]-q[1]*r[0]-r[1]*p[0 ] )
        return max(area(*triangle)
                    for triangle in itertools.combinations(points, 3))

if __name__ == '__main__':
    points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
    a = LargestTriangleArea
    print(a.largestTriangleArea(0,points))