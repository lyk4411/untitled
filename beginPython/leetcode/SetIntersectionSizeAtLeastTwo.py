class SetIntersectionSizeAtLeastTwo(object):
    def intersectionSizeTwo(self, intervals):
        intervals.sort(key=lambda l: (l[1], -l[0]))
        print(intervals)
        ans, p1, p2 = 0, -1, -1
        for i in range(0,len(intervals)):
            if intervals[i][0] <= p1:
                continue
            elif intervals[i][0] > p2:
                ans += 2
                p2 = intervals[i][1]
                p1 = p2 - 1
            else:
                ans += 1
                p1 = p2
                p2 = intervals[i][1]
        return ans

if __name__ == '__main__':
    a = SetIntersectionSizeAtLeastTwo()
    print(a.intersectionSizeTwo([[1, 3], [1, 4], [2, 5], [3, 5]]))
    print(a.intersectionSizeTwo([[1, 2], [2, 3], [2, 4], [4, 5]]))
    print(a.intersectionSizeTwo([[1, 3], [5, 6]]))
    print(a.intersectionSizeTwo([[1, 3], [1, 2], [0, 1]]))
    print(a.intersectionSizeTwo([[16,18],[11,18],[15,23],[1,16],[10,16],[6,19],[18,20],
                [7,19],[10,11],[11,23],[6,7],[23,25],[1,3],[7,12],[1,13],
                [23,25],[10,22],[23,25],[0,19],[0,13],[7,12],[14,19],
                [8,17],[7,23],[4,24]]))


