import collections


class UniqueLetterString(object):
    def uniqueLetterString(self, S):
        letterIdx = collections.defaultdict(list)
        for i, v in enumerate(S):
            letterIdx[v].append(i)
        ans = 0
        for letter, idx in letterIdx.items():
            idx = [-1] + idx + [len(S)]
            for x in range(1, len(idx) - 1):
                ans += (idx[x] - idx[x - 1]) * (idx[x + 1] - idx[x])
        return ans
if __name__ == '__main__':
    a = UniqueLetterString()
    print(a.uniqueLetterString("ABC"))
    print(a.uniqueLetterString("ABA"))
    print(a.uniqueLetterString("ABAC"))


