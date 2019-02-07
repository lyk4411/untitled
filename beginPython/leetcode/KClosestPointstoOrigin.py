class KClosestPointstoOrigin(object):
    def kClosest(self, points, K):
        points.sort(key=lambda P: P[0] ** 2 + P[1] ** 2)
        return points[:K]

if __name__ == '__main__':
    a = KClosestPointstoOrigin()
    print(a.kClosest(points=[[3, 3], [5, -1], [-2, 4]], K=2))
    print(a.kClosest(points=[[1, 3], [-2, 2]], K=1))