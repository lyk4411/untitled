from pip._vendor.requests.packages.urllib3.connectionpool import xrange


class BinaryNumberwithAlternatingBits(object):
    def hasAlternatingBits(self, n):
        bits = bin(n)
        return all(bits[i] != bits[i+1]
                   for i in xrange(len(bits) - 1))

if __name__ == '__main__':
    a = BinaryNumberwithAlternatingBits()
    print(a.hasAlternatingBits(5))
    print(a.hasAlternatingBits(6))
    print(a.hasAlternatingBits(7))
    print(a.hasAlternatingBits(8))
    print(a.hasAlternatingBits(9))