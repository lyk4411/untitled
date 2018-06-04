class ShortEncodingofWords(object):
    def minimumLengthEncoding(self, words):
        good = set(words)
        for word in words:
            for k in range(1, len(word)):
                good.discard(word[k:])
        return sum(len(word) + 1 for word in good)

if __name__ == '__main__':
    a = ShortEncodingofWords()
    words = ["time", "me", "bell"]
    print(a.minimumLengthEncoding(words))