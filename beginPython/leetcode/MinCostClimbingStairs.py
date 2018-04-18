class MinCostClimbingStairs(object):
    def minCostClimbingStairs(self, cost):
        length = cost.__len__()
        dp = [0] * (length + 1)
        for index in range(2,length + 1):
            dp[index] = min(dp[index - 2] + cost[index - 2], dp[index - 1] + cost[index - 1])
        return dp[length]

if __name__ == '__main__':
    a = MinCostClimbingStairs()
    cost1 = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    cost2 = [10, 15, 20]
    print(a.minCostClimbingStairs(cost1))
    print(a.minCostClimbingStairs(cost2))
