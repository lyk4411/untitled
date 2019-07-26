class LengthofLongestFibonacciSubsequence(object):
    def lenLongestFibSubseq(self, A):
        S = set(A)
        ans = 0
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                """
                With the starting pair (A[i], A[j]),
                y represents the future expected value in
                the fibonacci subsequence, and x represents
                the most current value found.
                """
                x, y = A[j], A[i] + A[j]
                length = 2
                while y in S:
                    x, y = y, x + y
                    length += 1
                ans = max(ans, length)
        return ans if ans >= 3 else 0

if __name__ == '__main__':
    a = LengthofLongestFibonacciSubsequence()
    print(a.lenLongestFibSubseq([1, 3, 7, 11, 12, 14, 18]))
    print(a.lenLongestFibSubseq([1, 2, 3, 4, 5, 6, 7, 8]))
