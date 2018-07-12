class StrangePrinter(object):
    def strangePrinter(self, s):
        s = ''.join(a for a,b in zip(s, '#'+s) if a!=b)
        size = len(s)
        if size <= 1:
            return size
        dp = [[0 for j in range(size)] for i in range(size)]
        for i in range(size):
            for j in range(i, size):
                dp[i][j] = j - i + 1
        for i in range(1, size):
            for j in range(size - i):
                for k in range(j, j + i):
                    temp = dp[j][k] + dp[k + 1][j + i]
                    if s[k] == s[i + j]:
                        temp -= 1
                    dp[j][j + i] = min(dp[j][j + i], temp)
        return dp[0][size - 1]

if __name__ == '__main__':
    a = StrangePrinter()
    print(a.strangePrinter("aaa"))
    print(a.strangePrinter("aaabbbb"))
    print(a.strangePrinter("abc"))