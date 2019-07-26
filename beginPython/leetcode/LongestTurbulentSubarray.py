


class LongestTurbulentSubarray(object):
    def cmp(self, param, param1):
        if param < param1:
            return -1
        elif param1 == param:
            return 0
        else:
            return 1
    def maxTurbulenceSize(self, A):
        N = len(A)
        ans = 1
        anchor = 0

        for i in range(1, N):
            c = self.cmp(A[i - 1], A[i])
            if c == 0:
                anchor = i
            elif i == N - 1 or c * self.cmp(A[i], A[i + 1]) != -1:
                ans = max(ans, i - anchor + 1)
                anchor = i
        return ans

if __name__ == '__main__':
    a  = LongestTurbulentSubarray()
    print(a.maxTurbulenceSize([9, 4, 2, 10, 7, 8, 8, 1, 9]))
    print(a.maxTurbulenceSize([1, 2, 3, 4]))
    print(a.maxTurbulenceSize([100]))
