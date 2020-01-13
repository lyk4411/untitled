class RemoveCoveredIntervals(object):
    def removeCoveredIntervals(self, A) -> int:
        res = right = 0
        A.sort(key=lambda a: (a[0], -a[1]))
        print(A)
        for i, j in A:
            res += j > right
            right = max(right, j)
        return res

if __name__ == '__main__':
    a = RemoveCoveredIntervals()
    intervals = [[1,4],[3,6],[2,8]]
    print(a.removeCoveredIntervals(intervals))