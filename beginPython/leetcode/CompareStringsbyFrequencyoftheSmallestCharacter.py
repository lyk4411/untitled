import bisect

class CompareStringsbyFrequencyoftheSmallestCharacter:
    def numSmallerByFrequency(self, queries, words):
        f = sorted(w.count(min(w)) for w in words)
        print("f:", f)

        return [len(f) - bisect.bisect(f, q.count(min(q))) for q in queries]

if __name__ == '__main__':
    a = CompareStringsbyFrequencyoftheSmallestCharacter()
    print(a.numSmallerByFrequency(queries = ["cbd"], words = ["zaaaz"]))
    print(a.numSmallerByFrequency(queries = ["bbb","cc","ddddddd","e"], words = ["a","aa","aaa","aaaa"]))
