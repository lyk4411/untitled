import collections


class NRepeatedElementinSize2NArray(object):
    def repeatedNTimes(self, A):
        count = collections.Counter(A)
        for k in count:
            if count[k] > 1:
                return k


if __name__ == '__main__':
    a = NRepeatedElementinSize2NArray()
    print(a.repeatedNTimes([1, 2, 3, 4, 4, 4]))