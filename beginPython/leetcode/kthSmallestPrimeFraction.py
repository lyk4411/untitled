import heapq


class kthSmallestPrimeFraction(object):
    def kthSmallestPrimeFraction(self, A, K):
        l = len(A) - 1
        h = []
        for i in range(l):  # 先往把每个元素的最小值加入heapq中，heapq中的每个元素第一位表示p/q的值，第二个表示p在A中的索引，第三位表示q在A中的索引
            heapq.heappush(h, (A[i] / float(A[l]), i, l)) # 一个个查找
        while K > 0: # 输出最小的一个
            min_one = heapq.heappop(h) # 添加保持min_one的p不变，q选择的索引 + 1，并且保证p<q
            if min_one[2] - 1 > min_one[1]:
                new_l = min_one[2] - 1
                heapq.heappush(h, (A[min_one[1]] / float(A[new_l]), min_one[1], new_l))
            K -= 1
        return [A[min_one[1]], A[min_one[2]]]


if __name__ == '__main__':
    a = kthSmallestPrimeFraction()
    print(a.kthSmallestPrimeFraction([1, 2, 3], 2))
    print(a.kthSmallestPrimeFraction( A = [1, 2, 3, 5], K = 3))
    print(a.kthSmallestPrimeFraction( A = [1, 7], K = 1))


