import collections


class MaximumFrequencyStack(object):
    def __init__(self):
        self.freq = collections.Counter()
        self.group = collections.defaultdict(list)
        self.maxfreq = 0

    def push(self, x):
        f = self.freq[x] + 1
        self.freq[x] = f
        if f > self.maxfreq:
            self.maxfreq = f
        self.group[f].append(x)

    def pop(self):
        x = self.group[self.maxfreq].pop()
        self.freq[x] -= 1
        if not self.group[self.maxfreq]:
            self.maxfreq -= 1

        return x

if __name__ == '__main__':
    a = MaximumFrequencyStack()
    a.push(5)
    a.push(7)
    a.push(5)
    a.push(7)
    a.push(4)
    a.push(5)
    print(a.group)
    print(a.freq)
    print(a.pop())
    print(a.pop())
    print(a.pop())
    print(a.pop())