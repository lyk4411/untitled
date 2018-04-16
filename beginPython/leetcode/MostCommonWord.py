import collections

class MostCommonWord(object):
    def mostCommonWord(self, paragraph, banned):
        banset = set(banned)
        count = collections.Counter(
            word.strip("!?',;.") for word in paragraph.lower().split())

        ans, best = '', 0
        for word in count:
            if count[word] > best and word not in banset:
                ans, best = word, count[word]

        return ans

if __name__ == '__main__':
    paragraph = r"Bob hit a ball, the hit BALL flew far after it was hit."
    banned = set("ball")
    print(MostCommonWord.mostCommonWord(0,paragraph,banned))