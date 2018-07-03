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

        dp = [[0 for x in range(N)] for y in range(K)]
        for k in range(K):
            for i in range(0, N):
                if k == 0:
                    dp[k][i] = S[i + 1]/(i + 1)
                else:
                    dp[k][i] = dp[k - 1][i]
                if k > 0:
                    for j in range(i - 1, -1, -1):
                        dp[k][i] = max(dp[k][i], dp[k - 1][j] + (S[i + 1] - S[j + 1]) / (i - j))
        return dp[K - 1][N - 1]

if __name__ == '__main__':
    a = LargestSumofAverages()
    print(a.largestSumOfAverages([9, 1, 2, 3, 9], 3))
