

class FindPivotIndex(object):
    def pivotIndex(self, nums):
        S = sum(nums)
        leftsum = 0
        for i, x in enumerate(nums):
            if leftsum == (S - leftsum - x):
                return i
            leftsum += x
        return -1

if __name__ == '__main__':
    a = FindPivotIndex()
    print(a.pivotIndex([1, 7, 3, 6, 5, 6]))
    print(a.pivotIndex([1, 2, 3]))