import collections


class NumberofMatchingSubsequences(object):
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        res = 0
        dic = collections.defaultdict(list)
        for word in words:
            dic[word[0]].append(word)

        for s in S:
            queue = dic[s]
            size = len(queue)
            for i in range(size):
                word = queue.pop(0)
                if len(word) == 1:
                    res += 1
                else:
                    dic[word[1]].append(word[1:])
        return res

if __name__ == '__main__':
    a = NumberofMatchingSubsequences()
    print(a.numMatchingSubseq("abcde", ["a", "bb", "acd", "ace"]))