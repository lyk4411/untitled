import unittest

from pip._vendor.requests.packages.urllib3.connectionpool import xrange


def product(x, y):
    return x * y


class ProductTestCase(unittest.TestCase):
    def testIntegers(self):
        for x in xrange(-10,10):
            for y in xrange(-10, 10):
                p = product(x,y)
                self.assertEqual(p, x*y,'Integer multiplication failed.')

    def testFloats(self):
        for x in xrange(-10,10):
            for y in xrange(-10, 10):
                x = x / 10
                y = y / 10
                p = product(x,y)
            self.failUnless(p == x*y, 'Float multiplication failed.')

if __name__ == '__main__':
    unittest.main()
