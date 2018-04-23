from pip._vendor.requests.packages.urllib3.connectionpool import xrange


class MinimumASCIIDeleteSumforTwoStrings(object):
    def minimumDeleteSum(self, s1, s2):
        dp = [[0] * (len(s2) + 1) for _ in xrange(len(s1) + 1)]

        for i in xrange(len(s1) - 1, -1, -1):
            dp[i][len(s2)] = dp[i+1][len(s2)] + ord(s1[i])
        for j in xrange(len(s2) - 1, -1, -1):
            dp[len(s1)][j] = dp[len(s1)][j+1] + ord(s2[j])

        for i in xrange(len(s1) - 1, -1, -1):
            for j in xrange(len(s2) - 1, -1, -1):
                if s1[i] == s2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = min(dp[i+1][j] + ord(s1[i]),
                                   dp[i][j+1] + ord(s2[j]))

        return dp[0][0]

if __name__ == '__main__':
    a = MinimumASCIIDeleteSumforTwoStrings()
    print(a.minimumDeleteSum("sea","eat"))
    print(a.minimumDeleteSum("delete","leet"))

