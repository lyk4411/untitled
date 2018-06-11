import collections


class MyCalendarIII(object):
    def __init__(self):
        self.delta = collections.Counter()

    def book(self, start, end):
        self.delta[start] += 1
        self.delta[end] -= 1

        active = ans = 0
        for x in sorted(self.delta):
            active += self.delta[x]
            if active > ans: ans = active

        return ans

if __name__ == '__main__':
    a = MyCalendarIII()
    print(a.book(10, 20))
    print(a.book(50, 60))
    print(a.book(10, 40))
    print(a.book(5, 15))
    print(a.book(5, 10))
    print(a.book(25, 55))