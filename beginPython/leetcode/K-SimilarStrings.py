import collections


class KSimilarStrings(object):
    def kSimilarity(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        self.memo = {}
        return self.solve(A, B)

    def solve(self, A, B):
        diff = [A[i] != B[i] for i in range(len(A))]
        simplify = lambda S: ''.join(c * d for c, d in zip(S, diff))
        # print(list(c * d for c, d in zip(A, diff)))
        A, B = simplify(A), simplify(B)
        if not A: return 0
        if (A, B) in self.memo: return self.memo[(A, B)]
        ans = 0x7FFFFFFF
        for i, x in enumerate(A):
            if A[i] == B[0]:
                C = A[1:i] + A[0] + A[i + 1:]
                ans = min(ans, self.solve(C, B[1:]))
        self.memo[(A, B)] = ans + 1
        return ans + 1
    # def kSimilarity(self, A, B):
    #     def neighbors(S):
    #         for i, c in enumerate(S):
    #             if c != B[i]:
    #                 break
    #
    #         T = list(S)
    #         for j in range(i + 1, len(S)):
    #             if S[j] == B[i]:
    #                 T[i], T[j] = T[j], T[i]
    #                 # print("".join(T))
    #                 yield "".join(T)
    #                 T[j], T[i] = T[i], T[j]
    #
    #     queue = collections.deque([A])
    #     seen = {A: 0}
    #     while queue:
    #         S = queue.popleft()
    #         if S == B: return seen[S]
    #         for T in neighbors(S):
    #             if T not in seen:
    #                 seen[T] = seen[S] + 1
    #                 queue.append(T)

if __name__ == '__main__':
    a = KSimilarStrings()
    # print(a.kSimilarity('ab', 'ba'))
    print(a.kSimilarity('abcdefg', 'bagfedc'))
    print(a.kSimilarity('aabc', 'abca'))