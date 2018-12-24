class MirrorReflection(object):
    def mirrorReflection(self, p, q):
        """
            :type p: int
            :type q: int
            :rtype: int
            """

        m, n = q, p
        while m % 2 == 0 and n % 2 == 0:
            m, n = m / 2, n / 2
        if m % 2 == 0 and n % 2 == 1:
            return 0
        elif m % 2 == 1 and n % 2 == 1:
            return 1
        elif m % 2 == 1 and n % 2 == 0:
            return 2
if __name__ == '__main__':
    a = MirrorReflection()
    print(a.mirrorReflection(12, 1))
    print(a.mirrorReflection(12, 11))
    print(a.mirrorReflection(11, 1))
    print(a.mirrorReflection(11, 4))