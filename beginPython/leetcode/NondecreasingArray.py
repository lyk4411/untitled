from pip._vendor.requests.packages.urllib3.connectionpool import xrange


class NondecreasingArray(object):
    def checkPossibility(self, A):
        p = None
        for i in xrange(len(A) - 1):
            if A[i] > A[i+1]:
                if p is not None:
                    return False
                p = i

        return (p is None or p == 0 or p == len(A)-2 or
                A[p-1] <= A[p+1] or A[p] <= A[p+2])

if __name__ == '__main__':
    a = NondecreasingArray()
    print(a.checkPossibility([4,2,3]))
    print(a.checkPossibility([4,2,1]))