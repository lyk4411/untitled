import itertools


class LargestTimeforGivenDigits(object):
    def largestTimeFromDigits(self, A):
        ans = -1
        for h1, h2, m1, m2 in itertools.permutations(A):
            hours = 10 * h1 + h2
            mins = 10 * m1 + m2
            time = 60 * hours + mins
            if 0 <= hours < 24 and 0 <= mins < 60 and time > ans:
                ans = time

        return "{:02}:{:02}".format(*divmod(ans, 60)) if ans >= 0 else ""

if __name__ == '__main__':
    a = LargestTimeforGivenDigits()
    print(a.largestTimeFromDigits([2, 3, 4, 5]))
    print(a.largestTimeFromDigits([2, 3, 4, 1]))
    print(a.largestTimeFromDigits([1, 3, 4, 5]))
