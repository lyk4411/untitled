import heapq


class MinimumCosttoHireKWorkers(object):
    def mincostToHireWorkers(self, quality, wage, K):
        from fractions import Fraction
        workers = sorted((Fraction(w, q), q, w)
                         for q, w in zip(quality, wage))

        ans = float('inf')
        pool = []
        sumq = 0
        for ratio, q, w in workers:
            heapq.heappush(pool, -q)
            sumq += q

            if len(pool) > K:
                sumq += heapq.heappop(pool)

            if len(pool) == K:
                ans = min(ans, ratio * sumq)

        return float(ans)

if __name__ == '__main__':
    a = MinimumCosttoHireKWorkers()
    print(a.mincostToHireWorkers(quality = [10,20,5], wage = [70,50,30], K = 2))
    print(a.mincostToHireWorkers(quality = [3,1,10,10,1], wage = [4,8,2,2,7], K = 3))