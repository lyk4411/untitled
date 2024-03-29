class FindandReplacePattern(object):
    def findAndReplacePattern(self, words, pattern):
        def match(word):
            m1, m2 = {}, {}
            for w, p in zip(word, pattern):
                if w not in m1: m1[w] = p
                if p not in m2: m2[p] = w
                if (m1[w], m2[p]) != (p, w):
                    return False
            return True

        return filter(match, words)

if __name__ == '__main__':
    a = FindandReplacePattern()
    print(list(a.findAndReplacePattern(["abc", "deq", "mee", "aqq", "dkd", "ccc"], "abb")))
    print(list(a.findAndReplacePattern(["abc", "deq", "mee", "aqq", "dkd", "ccc"], "aaa")))