from pip._vendor.requests.packages.urllib3.connectionpool import xrange


class RotateString(object):
    def rotateString(self, A, B):
        if len(A) != len(B):
            return False
        if len(A) == 0:
            return True

        for s in xrange(len(A)):
            if all(A[(s+i) % len(A)] == B[i] for i in xrange(len(A))):
                return True
        return False

if __name__ == '__main__':
    a = RotateString()
    a1 = "abcde"
    b1 = "bcdea"
    print(a.rotateString(a1,b1))