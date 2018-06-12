class DeleteandEarn(object):
    def deleteAndEarn(self, nums):
        sums = [0] * 10001
        for num in nums:
            sums[num] += num
        for i in range(2, 10001):
            sums[i] = max(sums[i - 1], sums[i - 2] + sums[i])
        return sums[10000]

if __name__ == '__main__':
    a = DeleteandEarn()
    print(a.deleteAndEarn([2, 2, 3, 3, 3, 4]))
    print(a.deleteAndEarn([2, 3, 4]))