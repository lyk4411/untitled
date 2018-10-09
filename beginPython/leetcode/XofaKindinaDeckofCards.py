import collections
from functools import reduce


class XofaKindinaDeckofCards(object):
    def hasGroupsSizeX(self, deck):

        from fractions import gcd
        vals = collections.Counter(deck).values()
        return reduce(gcd, vals) >= 2

if __name__ == '__main__':
    a = XofaKindinaDeckofCards()
    print(a.hasGroupsSizeX([1, 2, 3, 4, 4, 3, 2, 1]))
    print(a.hasGroupsSizeX([1, 1, 1, 2, 2, 2, 3, 3]))