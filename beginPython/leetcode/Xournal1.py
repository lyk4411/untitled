import numpy as np
class Xournal1(object):
    def rec_subset(self, arr, i, s):
        if s == 0:
            return True
        elif i == 0:
            return arr[0] == s
        elif arr[i] > s:
            return self.rec_subset(arr, i - 1, s)
        else:
            return self.rec_subset(arr, i - 1, s - arr[i]) or self.rec_subset(arr, i - 1, s)

    def dp_subset(self, arr, S):
        subset = np.zeros((len(arr), S + 1), dtype=bool)
        subset[:, 0] = True
        subset[0, :] = False
        subset[0, arr[0]] = True
        for i in range(1, len(arr)):
            for s in range(1, S + 1):
                if arr[i] > s:
                    subset[i, s] = subset[i - 1, s]
                else:
                    subset[i, s] = subset[i - 1, s - arr[i]] or subset[i - 1, s]
        r, c = subset.shape
        return subset[r - 1, c - 1]


if __name__ == '__main__':
    a = Xournal1()
    print(a.rec_subset([3, 34, 4, 12, 5, 2], len([3, 34, 4, 12, 5, 2]) - 1, 9))
    print(a.rec_subset([3, 34, 4, 12, 5, 2], len([3, 34, 4, 12, 5, 2]) - 1, 19))
    print(a.rec_subset([3, 34, 4, 12, 5, 2], len([3, 34, 4, 12, 5, 2]) - 1, 11))
    print(a.rec_subset([3, 34, 4, 12, 5, 2], len([3, 34, 4, 12, 5, 2]) - 1, 12))
    print(a.rec_subset([3, 34, 4, 12, 5, 2], len([3, 34, 4, 12, 5, 2]) - 1, 13))
    print("===============================================================")
    print(a.dp_subset([3, 34, 4, 12, 5, 2], 9))
    print(a.dp_subset([3, 34, 4, 12, 5, 2], 19))
    print(a.dp_subset([3, 34, 4, 12, 5, 2], 11))
    print(a.dp_subset([3, 34, 4, 12, 5, 2], 12))
    print(a.dp_subset([3, 34, 4, 12, 5, 2], 13))





