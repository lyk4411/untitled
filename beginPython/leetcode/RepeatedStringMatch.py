

class RepeatedStringMatch(object):
    def repeatedStringMatch(self, A, B):
        q = (len(B)) // len(A)
        for i in range(3):
            if B in A * (q+i): return q+i
        return -1

if __name__ == '__main__':
    a = RepeatedStringMatch()
    print(a.repeatedStringMatch("abcd", "cdabcdab"))