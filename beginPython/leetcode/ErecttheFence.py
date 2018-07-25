class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
    def __str__(self):
        return "[x = " + str(self.x) + ", y = " + str(self.y) + "]"
class ErecttheFence(object):
    def outerTrees(self, points):
        """
        :type points: List[Point]
        :rtype: List[Point]
        """
        # 描述那么多，实质就是一个，求凸包，也就是计算几何里面最基础的问题了，这里首先要明确一个叫orientation的概念，
        # orientation的定义其实很简单，三个点A, B, C，如果线段AB的斜率小于线段BC，表示BC这个方向是往AB的内部拐弯了，
        # 大于则BC是往外拐弯了，相等则AB // BC或者ABC三点一线，有了这个概念，就可以引出求凸包的最直觉性的解法Jarvis
        # algorithm了，Jarvis算法的道理也很简单，就是在一堆点里面找到一个横坐标最小的点，由这个点起步，再找一个相邻
        # 的点，由这两点去扫描其他点，如果扫描的点导致orientation往外拐，则把这个点设为这一轮找到的备选点去替换掉之
        # 前找的那个相邻的点，一轮下来找到一个点把它加入结果中，如此往复循环直到有一轮找到一个点和刚开始我们起步定
        # 义的那个点一样就中断循环（java里面有do
        # while所以这个描述更好实现，Python稍稍有点麻烦），这时候结果里面的点就是所求的凸包，另外对于两线平行的情况，
        # 我们还要单独在外层循环里面再加入一个for循环去检查两线平行的时候这个当前点是不是正好构成三点一线，如果是三
        # 点一线那这个点也应该在凸包里（原因的话如果两个点都是凸包上的点，这个点又和当前这两个点一线那肯定也是在凸
        # 包上的）这个循环应该放在检查备选点的for循环之后，另外Jarvis的时间复杂度是求凸包的算法里面最高的O(nh)，h是
        # 凸包里点的个数，另外几种算法个人觉得不太可能会需要掌握了，面试出现计算几何已经是一个很震惊的事了，如果再考
        # 更高级的有点过分啊...
        points.sort(key=lambda a: a.x)
        start = 0
        res = set([])
        n = len(points)
        cur = start

        while True:
            res.add(points[cur])
            nxt = (cur + 1) % n
            for i in range(n):
                if self.ori(points[cur], points[nxt], points[i]) < 0:
                    nxt = i

            for i in range(n):
                if self.ori(points[cur], points[nxt], points[i]) == 0:
                    if self.inBetween(points[cur], points[nxt], points[i]):
                        res.add(points[i])

            cur = nxt
            if cur == start:
                break

        return list(res)

    def ori(self, a, b, c):
        return (b.y - a.y) * (c.x - b.x) - (c.y - b.y) * (b.x - a.x)

    def inBetween(self, a, b, c):
        if min(a.x, b.x) <= c.x <= max(a.x, b.x) and min(a.y, b.y) <= c.y <= max(a.y, b.y):
            return True
        return False


if __name__ == '__main__':
    a = ErecttheFence()
    t = a.outerTrees([Point(1, 1), Point(2, 2), Point(2, 0), Point(2, 4), Point(3, 3), Point(4, 2)])
    for i in t:
        print(i)

    # print(a.outerTrees([[1, 2], [2, 2], [4, 2]]))