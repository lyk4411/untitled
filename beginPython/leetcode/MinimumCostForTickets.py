from functools import lru_cache

class MinimumCostForTickets(object):
    def mincostTickets(self, days, costs):
        N = len(days)
        durations = [1, 7, 30]

        @lru_cache(None)
        def dp(i):  # How much money to do days[i]+
            if i >= N: return 0

            ans = float('inf')
            j = i
            for c, d in zip(costs, durations):
                while j < N and days[j] < days[i] + d:
                    j += 1
                ans = min(ans, dp(j) + c)

            return ans

        return dp(0)

if __name__ == '__main__':
    a = MinimumCostForTickets()
    days = [1, 4, 6, 7, 8, 20]
    costs = [2, 7, 15]
    print(a.mincostTickets(days, costs))
    days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31]
    costs = [2, 7, 15]
    print(a.mincostTickets(days, costs))