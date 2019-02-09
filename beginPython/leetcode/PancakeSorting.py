


class PancakeSorting(object):
    def re(self, A, l, r):
        while l < r:
            tmp = A[l]
            A[l] = A[r]
            A[r] = tmp
            l += 1
            r -= 1

    def pancakeSort(self, A):
        ans = []
        backup = sorted(A[:])

        for i in range(len(A) - 1, -1, -1):
            j = len(backup) - 1
            while j >= 0:
                if A[j] == backup[i]:
                    break
                j -= 1

            if i == j:
                continue
            if j != 0:
                ans.append(j + 1)
                self.re(A, 0, j)
            ans.append(i + 1)
            self.re(A, 0, i)
        return ans

if __name__ == '__main__':
    a = PancakeSorting()
    print(a.pancakeSort([3, 2, 4, 1]))
    print(a.pancakeSort([1, 2, 3, 4]))