class DominoandTrominoTiling(object):
    def numTilings(self, N):
        MOD = 1000000007
        if N == 1: return 1
        if N == 2: return 2
        if N == 3: return 5
        dp = [0, 0, 0, 0]
        dp[1] = 1
        dp[2] = 2
        dp[3] = 5
        for i in range(4, N + 1, 1):
            dp[i % 4] = (2 * dp[(i - 1) % 4] % MOD + dp[(i - 3) % 4]) % MOD
        return dp[N % 4]

if __name__ == '__main__':
    a = DominoandTrominoTiling()
    print(a.numTilings(4))
    print(a.numTilings(10))
    print(a.numTilings(20))