import collections


class CustomSortString(object):
    def customSortString(self, S, T):
        c, s = collections.Counter(T), set(S)
        return ''.join(i * c[i] for i in S) + ''.join(i * c[i] for i in c if i not in s)

if __name__ == '__main__':
    a = CustomSortString()
    print(a.customSortString("cba", "abcd"))
    print(a.customSortString("cba", "aabbccdd"))