import collections


class NumberofRecentCalls(object):
    def __init__(self):
        self.q = collections.deque()

    def ping(self, t):
        self.q.append(t)
        while self.q[0] < t - 3000:
            self.q.popleft()
        return len(self.q)

if __name__ == '__main__':
    a = NumberofRecentCalls()
    print(a.ping(1))
    print(a.ping(3))
    print(a.ping(3001))
    print(a.ping(3002))
    print(a.ping(3003))
