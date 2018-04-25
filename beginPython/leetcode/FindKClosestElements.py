import math


class FindKClosestElements(object):
    def findClosestElements(self, arr, k, x):
        temp = sorted(arr, key = lambda a : abs(a - x))
        ans = temp[:k]
        return sorted(ans)

if __name__ == '__main__':
    a = FindKClosestElements()
    print(a.findClosestElements([1,2,3,4,5],3,4))
    print(a.findClosestElements([1,2,3,4,5],4,4))
    print(a.findClosestElements([1,2,3,4,5],3,3))