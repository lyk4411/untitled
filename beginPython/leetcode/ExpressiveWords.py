import itertools


class ExpressiveWords(object):
    def expressiveWords(self, S, words):
        def RLE(S):
            return zip(*[(k, len(list(grp)))
                         for k, grp in itertools.groupby(S)])

        R, count = RLE(S)
        ans = 0
        for word in words:
            R2, count2 = RLE(word)
            if R2 != R: continue
            ans += all(c1 >= max(c2, 3) or c1 == c2
                       for c1, c2 in zip(count, count2))

        return ans

if __name__ == '__main__':
    a = ExpressiveWords()
    S = "heeellooo"
    words = ["hello", "hi", "helo"]
    print(a.expressiveWords(S, words))