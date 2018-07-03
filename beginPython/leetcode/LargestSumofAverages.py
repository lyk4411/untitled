class LargestSumofAverages(object):
    def largestSumOfAverages(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: float
        """
        N = len(A)
        S = [0] * (N + 1)
        for x, a in enumerate(A):
            S[x + 1] += S[x] + a

        dp = [1.0 * S[x] / x for x in range(1, N + 1)]
        for x in range(K - 1):
            dp0 = [0] * N
            for y in range(x, N):
                for z in range(x, y):
                    dp0[y] = max(dp0[y], dp[z] + 1.0 * (S[y + 1] - S[z + 1]) / (y - z))
            dp = dp0
        return dp[-1]

if __name__ == '__main__':
    a = LargestSumofAverages()
    print(a.largestSumOfAverages([9, 1, 2, 3, 9], 3))
