


class ShortestCompletingWord:
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        licence_plate = licensePlate.lower()
        d = dict()
        for c in licence_plate:
            if c.isalpha():
                if c not in d:
                    d[c] = 0
                d[c] += 1

        res = None
        length = 1111
        for word in words:
            freq = d.copy()
            for c in word:
                if c in freq:
                    freq[c] -= 1
                    if freq[c] == 0:
                        freq.pop(c)
                if not freq:
                    if len(word) < length:
                        res = word
                        length = len(word)

        return res

if __name__ == '__main__':
    a = ShortestCompletingWord()
    words1 = ["step", "steps", "stripe", "stepple"]
    words2 = ["looks", "pest", "stew", "show"]
    print(a.shortestCompletingWord("1s3 PST", words1))
    print(a.shortestCompletingWord("1s3 456", words2))

