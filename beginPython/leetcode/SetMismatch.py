class SetMismatch(object):
    def findErrorNums(self, nums):
        s = set()
        duplicate = 0
        n = nums.__len__()
        sum = (n * (n+1)) / 2
        for i in nums:
            if(s.__contains__(i)):
                duplicate = i
            sum -= i
            s.add(i)
        return (duplicate,int(duplicate + sum))

if __name__ == '__main__':
    nums1 = [1, 2, 2, 4]
    print(SetMismatch.findErrorNums(0,nums1))

