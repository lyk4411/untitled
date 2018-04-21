import collections


class ImplementMagicDictionary(object):
    def __init__(self):
        self.buckets = collections.defaultdict(list)

    def buildDict(self, words):
        for word in words:
            self.buckets[len(word)].append(word)

    def search(self, word):
        return any(sum(a!=b for a,b in zip(word, candidate)) == 1
                   for candidate in self.buckets[len(word)])

if __name__ == '__main__':
    a = ImplementMagicDictionary()
    a.buildDict(["hello","world","leetcode"])
    print(a.search("hello"))
    print(a.search("hell"))
    print(a.search("hella"))
    print(a.search("leetcodd"))