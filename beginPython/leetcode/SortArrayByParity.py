class SortArrayByParity(object):
    def sortArrayByParity(self, A):
        A.sort(key=lambda x: x % 2)
        return A

if __name__ == '__main__':
    a = SortArrayByParity()
    print(a.sortArrayByParity([1,2,3,4,5,6]))