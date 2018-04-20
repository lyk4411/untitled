from pip._vendor.requests.packages.urllib3.connectionpool import xrange


class ValidPalindromeII(object):
    def validPalindrome(self, s):
        def is_pali_range(i, j):
            return all(s[k] == s[j - k + i] for k in range(i, j))

        for i in xrange(len(s) // 2):
            if s[i] != s[len(s) - 1 - i]:
                j = len(s) - 1 - i
                return is_pali_range(i + 1, j) or is_pali_range(i, j - 1)
        return True

if __name__ == '__main__':
    a = ValidPalindromeII()
    print(a.validPalindrome(r"aba"))
    print(a.validPalindrome(r"abca"))
    print(a.validPalindrome(r"abc"))

