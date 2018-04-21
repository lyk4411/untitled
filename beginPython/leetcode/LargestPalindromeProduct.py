from PIL.WmfImagePlugin import long


class LargestPalindromeProduct:
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        def createPalindrome(i):
            temp = str(i) + str(i)[::-1]
            return long(temp);
        if n == 1 :
            return 9
        high = 10**n - 1
        low = high // 10
        for i in range(high,low, -1):
            # print("i:" + str(i))
            palindrome = createPalindrome(i);
            for j in range(high, low, -1):
                if palindrome // j > high:
                    break
                if palindrome % j == 0:
                    return int(palindrome % 1337)
        return -1;



if __name__ == '__main__':
    a = LargestPalindromeProduct()
    print(a.largestPalindrome(9))
    print(a.largestPalindrome(8))
    print(a.largestPalindrome(7))
    print(a.largestPalindrome(6))
    print(a.largestPalindrome(5))
    print(a.largestPalindrome(4))
    print(a.largestPalindrome(3))
    print(a.largestPalindrome(2))
    print(a.largestPalindrome(1))