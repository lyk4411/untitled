class Shift2DGrid(object):
    def shiftGrid(self, grid, k: int):
        col, nums = len(grid[0]), sum(grid, [])
        # print(nums)
        k = k % len(nums)
        nums = nums[-k:] + nums[:-k]
        # print(nums)
        return [nums[i:i + col] for i in range(0, len(nums), col)]

if __name__ == '__main__':
    a = Shift2DGrid()
    print(a.shiftGrid(grid=[[3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10], [12, 0, 21, 13]], k=4))
    print(a.shiftGrid(grid=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], k=1))
    print(a.shiftGrid(grid=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], k=9))