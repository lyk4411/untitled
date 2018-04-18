from pip._vendor.requests.packages.urllib3.connectionpool import xrange


class PrimeNumberofSetBitsinBinaryRepresentation(object):
    def countPrimeSetBits(self, L, R):
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        return sum(bin(x).count('1') in primes
                   for x in xrange(L, R + 1))

if __name__ == '__main__':
    a = PrimeNumberofSetBitsinBinaryRepresentation()
    print(a.countPrimeSetBits(6, 10))
    print(a.countPrimeSetBits(10, 15))