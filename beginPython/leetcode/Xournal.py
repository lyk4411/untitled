# import numpy
class Xournal(object):
    arr = [1, 2, 4, 1, 7, 8, 3]
    def rec_opt(self, arr, i):
        if i == 0 :
            return arr[0]
        elif i == 1:
            return max(arr[0], arr[1])
        else:
            A = self.rec_opt(arr, i - 2) + arr[i]
            B = self.rec_opt(arr, i - 1)
            return max(A, B)

    def dp_opt(self, arr):
        # opt = numpy.zeros(len(arr))
        opt = [0 for _ in range(len(arr))]
        opt[0] = arr[0]
        opt[1] = max(arr[0], arr[1])
        for i in range(2, len(arr)):
            A = opt[i - 2] + arr[i]
            B = opt[i - 1]
            opt[i] = max(A, B)
        return opt[len(arr) - 1]

if __name__ == '__main__':
    a = Xournal()
    print(a.rec_opt([1, 2, 4, 1, 7, 8, 3], 6))
    print(a.dp_opt([1, 2, 4, 1, 7, 8, 3]))
    print(a.dp_opt([4, 1, 1, 9, 1]))