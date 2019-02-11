class AddtoArrayFormofInteger(object):
    def addToArrayForm(self, A, K):
        ans = []
        N = len(A)
        cur = K
        i = N - 1
        while i >= 0 or cur > 0:
            if i >= 0:
                cur += A[i]
            cur, temp = divmod(cur, 10)
            ans.append(temp)
            i -= 1

        ans.reverse()
        return ans

if __name__ == '__main__':
    a = AddtoArrayFormofInteger()
    print(a.addToArrayForm([1, 1, 1], 123))
    print(a.addToArrayForm([1, 1, 1], 11123))