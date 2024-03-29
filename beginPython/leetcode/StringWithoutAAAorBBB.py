class StringWithoutAAAorBBB(object):
    def strWithout3a3b(self, A, B):
        ans = []

        while A or B:
            if len(ans) >= 2 and ans[-1] == ans[-2]:
                writeA = ans[-1] == 'b'
            else:
                writeA = A >= B

            if writeA:
                A -= 1
                ans.append('a')
            else:
                B -= 1
                ans.append('b')

        return "".join(ans)

if __name__ == '__main__':
    a = StringWithoutAAAorBBB()
    print(a.strWithout3a3b(2, 10))
    print(a.strWithout3a3b(20, 2))
    print(a.strWithout3a3b(2, 4))
