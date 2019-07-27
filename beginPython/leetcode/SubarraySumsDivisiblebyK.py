import collections


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
