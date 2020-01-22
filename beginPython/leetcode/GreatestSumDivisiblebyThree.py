class GreatestSumDivisiblebyThree(object):
    def maxSumDivThree(self, nums):
        res = 0
        leftOne = 20000
        leftTwo = 20000
        for n in nums:
            res += n
            if n%3 == 1:
                leftTwo = min(leftTwo, leftOne + n)
                leftOne = min(leftOne,n)
            if n%3 == 2:
                leftOne = min(leftOne, leftTwo + n)
                leftTwo = min(leftTwo, n)

        if res%3 == 0:
            return res
        if res%3 == 1:
            return res - leftOne
        return res - leftTwo

if __name__ == '__main__':
    a = GreatestSumDivisiblebyThree()
    print(a.maxSumDivThree(nums = [3,6,5,1,8]))
    print(a.maxSumDivThree(nums = [4]))
    print(a.maxSumDivThree(nums = [1,2,3,4,4]))




