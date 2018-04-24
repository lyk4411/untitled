


class NonnegativeIntegerswithoutConsecutiveOnes:
    def findIntegers(self, num):
        """
        :type num: int
        :rtype: int
        """
        f = [0 for n in range(32)]
        f[0] = 1
        f[1] = 2
        for i in range(2,len(f)):
            f[i] = f[i -1] + f[i - 2]
        i = 30
        sum = 0
        prev_bit = 0
        while i >= 0:
            if (num & 1<<i) !=0:
                sum += f[i]
                if prev_bit == 1:
                    return sum
                prev_bit = 1
            else:
                prev_bit = 0
            i -= 1
        return sum + 1


if __name__ == '__main__':
    a = NonnegativeIntegerswithoutConsecutiveOnes()
    print(a.findIntegers(12))
    print(a.findIntegers(14))
    print(a.findIntegers(10))



