import collections

# 解题思路：本题需要用到一个数学规律，如果a%c = b%c，那么(a-b)%c=0。我的解法就是从后往前遍历数组，
# 依次累加每个元素的值并记为sum，同时用字典保存sum%K作为key值出现的次数。同时每累加一个元素，只要
# 去字典中查找历史sum%K出现的次数，这个次数就是从以这个元素作为起点满足条件的子数组的个数。特别注
# 意的是，如果sum%K=0，那么表示这个元素本身就满足条件，次数要+1。
class SubarraySumsDivisiblebyK(object):
    def subarraysDivByK(self, A, K):
        P = [0]
        for x in A:
            P.append((P[-1] + x) % K)
        print(P)
        count = collections.Counter(P)
        print(count)
        print(count.values())
        return sum(v * (v - 1) // 2 for v in count.values())

if __name__ == '__main__':
    a = SubarraySumsDivisiblebyK()
    A = [4, 5, 0, -2, -3, 1]
    K = 5
    print(a.subarraysDivByK(A, K))
    A = [1, 2, 3]
    print(a.subarraysDivByK(A, K))
