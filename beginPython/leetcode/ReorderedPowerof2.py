import itertools


class ReorderedPowerof2(object):
    def reorderedPowerOf2(self, N):
        """
        Let's work through an example like N = 128.
        In the last line, 'for cand in itertools.permutations(str(N))' will
        iterate through the six possibilities cand = ('1', '2', '8'),
        cand = ('1', '8', '2'), cand = ('2', '1', '8'), and so on.

        The check cand[0] != '0' is a check that the candidate permutation
        does not have a leading zero.

        The check bin(int("".join(cand))).count('1') == 1 is a check that cand
        represents a power of 2: namely, that the number of ones in its binary
        representation is 1.
        """
        # 搜索遍历所有排列的可能性，然后将其转换为二进制数，如果转换的二进制数只有一个1则是二的倍数。
        return any(cand[0] != '0' and bin(int("".join(cand))).count('1') == 1
                   for cand in itertools.permutations(str(N)))

if __name__ == '__main__':
    a = ReorderedPowerof2()
    print(a.reorderedPowerOf2(1))
    print(a.reorderedPowerOf2(16))
    print(a.reorderedPowerOf2(8))
    print(a.reorderedPowerOf2(22))
    print(a.reorderedPowerOf2(61))
