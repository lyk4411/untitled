import bisect
import collections


class TimeBasedKeyValueStore(object):
    def __init__(self):
        self.M = collections.defaultdict(list)

    def set(self, key, value, timestamp):
        self.M[key].append((timestamp, value))

    def get(self, key, timestamp):
        A = self.M.get(key, None)
        if A is None: return ""
        i = bisect.bisect(A, (timestamp, chr(127)))
        return A[i - 1][1] if i else ""

if __name__ == '__main__':
    a = TimeBasedKeyValueStore()
    a.set("foo", "bar", 1)
    print(a.get("foo", 1))
    print(a.get("foo", 3))
    a.set("foo", "bar2", 4)
    print(a.get("foo", 4))
    print(a.get("foo", 5))

    a.set("love", "high", 10)
    a.set("love", "low", 20)
    print(a.get("love", 5))
    print(a.get("love", 10))
    print(a.get("love", 15))
    print(a.get("love", 20))


