


class MaximumSwap(object):
    def maximumSwap(self, num):
        A = map(int, str(num))
        B = list(str(num))
        last = {x: i for i, x in enumerate(A)}
        for i in range(len(str(num))):
            for d in range(9, int(B[i]), -1):
                if last.get(d, 0) > i:
                    B[i], B[last[d]] = B[last[d]], B[i]
                    return int("".join(map(str, B)))
        return num

if __name__ == '__main__':
    a = MaximumSwap()
    print(a.maximumSwap(789))
    print(a.maximumSwap(2736))
    print(a.maximumSwap(21))
    print(a.maximumSwap(12))
    print(a.maximumSwap(987654))
    print(a.maximumSwap(789452))
