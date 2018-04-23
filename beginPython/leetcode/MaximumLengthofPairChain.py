import operator


class MaximumLengthofPairChain(object):
    # def findLongestChain(self, pairs):  #Time Limit Exceeded
    #     pairs.sort()
    #     dp = [1] * len(pairs)
    #
    #     for j in range(len(pairs)):
    #         for i in range(j):
    #             if pairs[i][1] < pairs[j][0]:
    #                 dp[j] = max(dp[j], dp[i] + 1)
    #
    #     return max(dp)
    def findLongestChain(self, pairs):
        cur, ans = float('-inf'), 0
        for x, y in sorted(pairs, key=operator.itemgetter(1)):
            print(x,y)
            if cur < x:
                cur = y
                ans += 1
        return ans

if __name__ == '__main__':
    a = MaximumLengthofPairChain()
    print(a.findLongestChain([[1,2], [3,4], [2,3]]))