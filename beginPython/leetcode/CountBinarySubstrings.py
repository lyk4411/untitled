from pip._vendor.requests.packages.urllib3.connectionpool import xrange

class CountBinarySubstrings(object):
    def countBinarySubstrings(self, s):
        groups = [1]
        for i in xrange(1, len(s)):
            if s[i-1] != s[i]:
                groups.append(1)
            else:
                groups[-1] += 1

        ans = 0
        for i in xrange(1, len(groups)):
            ans += min(groups[i-1], groups[i])
        return ans

if __name__ == '__main__':
    a = CountBinarySubstrings()
    print(a.countBinarySubstrings("00110011"))
    print(a.countBinarySubstrings("10101"))
