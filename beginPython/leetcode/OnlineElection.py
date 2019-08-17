import bisect
import collections

class OnlineElection(object):
    def __init__(self, persons, times):
        maxCount = 0
        d = collections.defaultdict(int)
        self.Q = {}
        self.cache = {}
        for i in range(len(persons)):
            d[persons[i]] += 1
            if d[persons[i]] >= maxCount:
                maxCount = d[persons[i]]
                self.Q[times[i]] = persons[i]
        self.res = sorted(self.Q.keys())

    def q(self, t):
        if t not in self.cache:
            index = bisect.bisect_right(self.res, t)
            self.cache[t] = self.Q[self.res[index - 1]]
        return self.cache[t]

if __name__ == '__main__':
    a = OnlineElection([0,1,1,0,0,1,0],[0,5,10,15,20,25,30])
    print(a.q(3))
    print(a.q(12))
    print(a.q(25))
    print(a.q(15))
    print(a.q(24))
    print(a.q(8))