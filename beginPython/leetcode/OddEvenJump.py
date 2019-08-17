class OddEvenJump(object):
    def oddEvenJumps(self, A):
        N = len(A)

        def make(B):
            ans = [None] * N
            stack = []  # invariant: stack is decreasing
            for i in B:
                while stack and i > stack[-1]:
                    ans[stack.pop()] = i
                stack.append(i)
            return ans

        B = sorted(range(N), key=lambda i: A[i])
        oddnext = make(B)
        B.sort(key=lambda i: -A[i])
        evennext = make(B)

        odd = [False] * N
        even = [False] * N
        odd[N - 1] = even[N - 1] = True

        for i in range(N - 2, -1, -1):
            if oddnext[i] is not None:
                odd[i] = even[oddnext[i]]
            if evennext[i] is not None:
                even[i] = odd[evennext[i]]

        return sum(odd)

if __name__ == '__main__':
    a = OddEvenJump()
    print(a.oddEvenJumps([10, 13, 12, 14, 15]))
    print(a.oddEvenJumps([2, 3, 1, 1, 4]))
    print(a.oddEvenJumps([5, 1, 3, 4, 2]))
