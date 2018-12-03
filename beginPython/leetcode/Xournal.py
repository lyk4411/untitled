class Xournal(object):
    arr = [1, 2, 4, 1, 7, 8, 3]
    def rec_opt(self, arr, i):
        if i == 0 :
            return arr[0]
        elif i == 1:
            return max(arr[0],arr[1])
        else:
            A = self.rec_opt(arr, i - 2) + arr[i]
            B = self.rec_opt(arr, i - 1)
            return max(A, B)


if __name__ == '__main__':
    a = Xournal()
    print(a.rec_opt([1, 2, 4, 1, 7, 8, 3], 6))