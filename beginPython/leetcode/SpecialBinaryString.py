class SpecialBinaryString(object):
    def makeLargestSpecial(self, S):
        count, i = 0, 0
        res = []
        for j, v in enumerate(S):
            count = count + 1 if v == '1' else count - 1
            if count == 0:
                res.append('1' + self.makeLargestSpecial(S[i + 1:j]) + '0')
                i = j + 1
        return ''.join(sorted(res)[::-1])

if __name__ == '__main__':
    a = SpecialBinaryString()
    print(a.makeLargestSpecial("11011000"))
    # print(a.makeLargestSpecial("110110001010"))
    # print(a.makeLargestSpecial("110100"))

    # students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
    # print(sorted(students, key=lambda s: s[2]))
    # print(sorted(students, key=lambda s: s[2])[::-1])