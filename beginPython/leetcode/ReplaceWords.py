
class ReplaceWords(object):
    def replaceWords(self, roots, sentence):
        rootset = set(roots)

        def replace(word):
            for i in range(1, len(word)):
                if word[:i] in rootset:
                    return word[:i]
            return word

        return " ".join(map(replace, sentence.split()))

if __name__ == '__main__':
    a = ReplaceWords()
    roots = ["cat", "bat", "rat"]
    print(a.replaceWords(roots, "the cattle was rattled by the battery"))