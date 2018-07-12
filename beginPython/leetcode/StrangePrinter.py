class StrangePrinter(object):
    def strangePrinter(self, s):
        size = len(s)
        if size <= 1:
            return size
        dp = [[0 for j in range(100)] for i in range(100)]
        for i in range(size):
            for j in range(i, size):
                dp[i][j] = j - i + 1
        for i in range(1, size):
            j = 0
            while j + i < size:
                k = j
                while k < j + i:
                    temp = dp[j][k] + dp[k + 1][j + i]
                    if s[k] == s[i + j]:
                        temp -= 1
                    dp[j][j + i] = min(dp[j][j + i], temp)
                    k += 1
                j += 1
        return dp[0][size - 1]

if __name__ == '__main__':
    a = StrangePrinter()
    print(a.strangePrinter("aaa"))
    print(a.strangePrinter("aaabbbb"))
    print(a.strangePrinter("abc"))