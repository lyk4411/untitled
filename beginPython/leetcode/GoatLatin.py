class GoatLation(object):
    def toGoatLatin(self, S):
        def convert(word):
            if word[0] not in 'aeiouAEIOU':
                word = word[1:] + word[:1]
            return word + 'ma'

        return " ".join(convert(word) + 'a' * i
                        for i, word in enumerate(S.split(), 1))

if __name__ == '__main__':
    a = GoatLation()
    print(a.toGoatLatin("I speak Goat Latin"))
    print(a.toGoatLatin("The quick brown fox jumped over the lazy dog"))