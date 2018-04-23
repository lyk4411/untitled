

class MaximumLengthofRepeatedSubarray(object):
    def findLength(self, A, B):
        memo = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
        for i in range(len(A) - 1, -1, -1):
            for j in range(len(B) - 1, -1, -1):
                if A[i] == B[j]:
                    memo[i][j] = memo[i+1][j+1]+1
        return max(max(row) for row in memo)

if __name__ == '__main__':
    a = MaximumLengthofRepeatedSubarray()
    print(a.findLength([1,2,3,2,1], [3,2,1,4,7]))
    print(a.findLength([1,2,3,2,1], [1,3,2,1,4,7]))
