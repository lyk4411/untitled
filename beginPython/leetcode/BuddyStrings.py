class BuddyStrings(object):
    def buddyStrings(self, A, B):
        if len(A) != len(B):
            return False
        diff_cnt = 0
        idxs = []
        N = len(A)
        for i in range(0,N):
            if A[i] != B[i]:
                idxs.append(i)
                diff_cnt += 1

        if diff_cnt == 0:
            d = {}
            for i in range(N):
                if d.get(A[i]):
                    return True
                else:
                    d.setdefault(A[i], True)
            return False

        if diff_cnt != 2:
            return False
        t1 = list(A)
        temp = t1[idxs[0]]
        t1[idxs[0]] = t1[idxs[1]]
        t1[idxs[1]] = temp
        A = ''.join(t1)
        return A == B

if __name__ == '__main__':
    a = BuddyStrings()
    print(a.buddyStrings("aaa", "abb"))
    print(a.buddyStrings("bba", "abb"))

