class IntervalListIntersections(object):
    def intervalIntersection(self, A, B):
        ans = []
        i = j = 0

        while i < len(A) and j < len(B):
            # Let's check if A[i] intersects B[j].
            # lo - the startpoint of the intersection
            # hi - the endpoint of the intersection
            lo = max(A[i].start, B[j].start)
            hi = min(A[i].end, B[j].end)
            if lo <= hi:
                ans.append(Interval(lo, hi))

            # Remove the interval with the smallest endpoint
            if A[i].end < B[j].end:
                i += 1
            else:
                j += 1

        return ans

class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
    def __str__(self):
        return "start:" + str(self.start) + "  -  end:" + str(self.end)

if __name__ == '__main__':
    ili = IntervalListIntersections()
    a1 = Interval(0, 2)
    a2 = Interval(5, 10)
    a3 = Interval(13, 23)
    a4 = Interval(24, 25)

    b1 = Interval(1, 5)
    b2 = Interval(8, 12)
    b3 = Interval(15, 24)
    b4 = Interval(25, 26)

    A = [a1, a2, a3, a4]
    B = [b1, b2, b3, b4]

    C = ili.intervalIntersection(A, B)
    for i in range(len(C)):
        print(C[i])
