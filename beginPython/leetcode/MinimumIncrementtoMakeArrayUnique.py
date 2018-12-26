import collections


class MinimumIncrementtoMakeArrayUnique(object):
    def minIncrementForUnique(self, A):
        count = collections.Counter(A)
        taken = []

        ans = 0
        for x in range(100000):
            if count[x] >= 2:
                taken.extend([x] * (count[x] - 1))
            elif taken and count[x] == 0:
                ans += x - taken.pop()
        return ans

if __name__ == '__main__':
    a = MinimumIncrementtoMakeArrayUnique()
    print(a.minIncrementForUnique([1, 2, 2]))
    print(a.minIncrementForUnique([1, 2, 2, 4, 5, 5, 4]))
