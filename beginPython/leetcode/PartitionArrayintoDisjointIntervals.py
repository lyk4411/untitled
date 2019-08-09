class PartitionArrayintoDisjointIntervals(object):
    def partitionDisjoint(self, A):
        N = len(A)
        maxleft = [None] * N
        minright = [None] * N

        m = A[0]
        for i in range(N):
            m = max(m, A[i])
            maxleft[i] = m

        m = A[-1]
        for i in range(N - 1, -1, -1):
            m = min(m, A[i])
            minright[i] = m

        for i in range(1, N):
            if maxleft[i - 1] <= minright[i]:
                return i

if __name__ == '__main__':
    a = PartitionArrayintoDisjointIntervals()
    print(a.partitionDisjoint([5, 0, 3, 8, 6]))
    print(a.partitionDisjoint([1, 1, 1, 0, 6, 12]))