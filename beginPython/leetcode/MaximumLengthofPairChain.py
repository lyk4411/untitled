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

    # 这道题给了我们一些链对，规定了如果后面链对的首元素大于前链对的末元素，
    # 那么这两个链对就可以链起来，问我们最大能链多少个。那么我们想，由于规
    # 定了链对的首元素一定小于尾元素，我们需要比较的是某个链表的首元素和另
    # 一个链表的尾元素之间的关系，如果整个链对数组是无序的，那么就很麻烦，
    # 所以我们需要做的是首先对链对数组进行排序，按链对的尾元素进行排序，小
    # 的放前面。这样我们就可以利用Greedy算法进行求解了。
    #
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