from pip._vendor.requests.packages.urllib3.connectionpool import xrange


class LongestWordinDictionary(object):
    def longestWord(self, words):
        ans = ""
        wordset = set(words)
        for word in words:
            if len(word) > len(ans) or len(word) == len(ans) and word < ans:
                if all(word[:k] in wordset for k in xrange(1, len(word))):
                    ans = word
        return ans

if __name__ == '__main__':
    a = LongestWordinDictionary()
    print(a.longestWord(["w", "wo", "wor", "worl", "world"]))
    print(a.longestWord(["a", "banana", "app", "appl", "ap", "apply", "apple"]))
