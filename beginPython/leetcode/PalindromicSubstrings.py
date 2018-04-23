


class PalindromicSubstrings(object):
    def countSubstrings(self, S):
        """
        :type s: str
        :rtype: int
        """
        N = len(S)
        ans = 0
        for center in range(2 * N - 1):
            left = center // 2
            right = left + center % 2
            while left >= 0 and right < N and S[left] == S[right]:
                ans += 1
                left -= 1
                right += 1
        return ans
if __name__ == '__main__':
     a = PalindromicSubstrings()
     print(a.countSubstrings("abc"))
     print(a.countSubstrings("aaa"))