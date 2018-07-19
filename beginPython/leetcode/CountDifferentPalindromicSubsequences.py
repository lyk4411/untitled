class CountDifferentPalindromicSubsequences(object):
    def countPalindromicSubsequences(self, S):
        """
        :type S: str
        :rtype: int
        """
        length = len(S)
        dp = [[0 for i in range(length)] for j in range(length)]
        for i in range(length):
            dp[i][i] = 1

        for distance in range(1, length):
            for i in range(length - distance):
                j = i + distance
                if S[i] == S[j]:
                    low = i + 1
                    high = j - 1

                    while low <= high and S[low] != S[j]:
                        low += 1
                    while low <= high and S[high] != S[j]:
                        high -= 1

                    if low > high:
                        dp[i][j] = dp[i + 1][j - 1] * 2 + 2
                    elif low == high:
                        dp[i][j] = dp[i + 1][j - 1] * 2 + 1
                    else:
                        dp[i][j] = dp[i + 1][j - 1] * 2 - dp[low + 1][high - 1]
                else:
                    dp[i][j] = dp[i][j - 1] + dp[i + 1][j] - dp[i + 1][j - 1]
            dp[i][j] =  dp[i][j] + 1000000007 if dp[i][j] < 0 else dp[i][j] % 1000000007
        return dp[0][length - 1]

if __name__ == '__main__':
    a = CountDifferentPalindromicSubsequences()
    print(a.countPalindromicSubsequences('bccb'))
    print(a.countPalindromicSubsequences('abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba'))