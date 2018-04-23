import collections


class TopKFrequentWords:
    def topKFrequent(self, words, k):
        count = collections.Counter(words)
        candidates = count.keys()
        ans = sorted(candidates, key=lambda w: (-count[w], w))
        return ans[:k]
if __name__ == '__main__':
    a = TopKFrequentWords()
    words1 = [r"i", r"love", r"leetcode", r"i", r"love", r"coding"]
    words2 = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
    print(a.topKFrequent(words1, 2))
    print(a.topKFrequent(words2, 4))
