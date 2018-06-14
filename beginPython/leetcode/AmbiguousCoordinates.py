import itertools


class AmbiguousCoordinates(object):
    def ambiguousCoordinates(self, S):
        def make(frag):
            N = len(frag)
            for d in range(1, N + 1):
                left = frag[:d]
                right = frag[d:]
                if ((not left.startswith('0') or left == '0')
                    and (not right.endswith('0'))):
                    yield left + ('.' if d != N else '') + right

        S = S[1:-1]
        return ["({}, {})".format(*cand)
                for i in range(1, len(S))
                for cand in itertools.product(make(S[:i]), make(S[i:]))]

if __name__ == '__main__':
    a = AmbiguousCoordinates()
    print(a.ambiguousCoordinates("(123)"))
    print(a.ambiguousCoordinates("(00111)"))
    print(a.ambiguousCoordinates("(0123)"))
    print(a.ambiguousCoordinates("(100)"))