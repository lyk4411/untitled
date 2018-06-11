class MaximizeDistancetoClosestPerson(object):
    def maxDistToClosest(self, seats):
        N = len(seats)
        left, right = [N] * N, [N] * N

        for i in range(N):
            if seats[i] == 1:
                left[i] = 0
            elif i > 0:
                left[i] = left[i - 1] + 1

        for i in range(N - 1, -1, -1):
            if seats[i] == 1:
                right[i] = 0
            elif i < N - 1:
                right[i] = right[i + 1] + 1

        return max(min(left[i], right[i])
                   for i, seat in enumerate(seats) if not seat)

if __name__ == '__main__':
    a = MaximizeDistancetoClosestPerson()
    print(a.maxDistToClosest([1, 0, 0, 0, 1, 0, 1]))
    print(a.maxDistToClosest([1, 0, 0, 0]))