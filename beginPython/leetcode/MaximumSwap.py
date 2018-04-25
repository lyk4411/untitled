


class MaximumSwap(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        A = map(int, str(num))
        last = {x: i for i, x in enumerate(A)}
        for i, x in enumerate(A):
            for d in range(9, x, -1):
                if last.get(d, None) > i:
                    A[i], A[last[d]] = A[last[d]], A[i]
                    return int("".join(map(str, A)))
        return num

if __name__ == '__main__':
    a = MaximumSwap()
    print(a.maximumSwap(789))
    print(a.maximumSwap(987654))
    print(a.maximumSwap(789452))
