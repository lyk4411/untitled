class LongestMountaininArray(object):
    def longestMountain(self, A):
        N = len(A)
        ans = base = 0

        while base < N:
            end = base
            if end + 1 < N and A[end] < A[end + 1]:  # if base is a left-boundary
                # set end to the peak of this potential mountain
                while end + 1 < N and A[end] < A[end + 1]:
                    end += 1

                if end + 1 < N and A[end] > A[end + 1]:  # if end is really a peak..
                    # set 'end' to right-boundary of mountain
                    while end + 1 < N and A[end] > A[end + 1]:
                        end += 1
                    # record candidate answer
                    ans = max(ans, end - base + 1)

            base = max(end, base + 1)

        return ans
if __name__ == '__main__':
    a = LongestMountaininArray()
    A1 = [2, 1, 4, 7, 3, 2, 5]
    A2 = [2, 2, 2]
    print(a.longestMountain(A1))
    print(a.longestMountain(A2))