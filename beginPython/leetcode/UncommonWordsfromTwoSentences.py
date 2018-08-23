class UncommonWordsfromTwoSentences(object):
    def uncommonFromSentences(self, A, B):
        count = {}
        for word in A.split():
            count[word] = count.get(word, 0) + 1
        for word in B.split():
            count[word] = count.get(word, 0) + 1

        # Alternatively:
        # count = collections.Counter(A.split())
        # count += collections.Counter(B.split())

        return [word for word in count if count[word] == 1]

if __name__ == '__main__':
    a = UncommonWordsfromTwoSentences()
    print(a.uncommonFromSentences(A = "this apple is sweet", B = "this apple is sour"))
    print(a.uncommonFromSentences(A = "apple apple", B = "banana"))