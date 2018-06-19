
class PushDominoes(object):
    def cmp(self, a, b):
        if a > b:
            return 1
        elif a < b:
            return -1
        else:
            return 0
    def pushDominoes(self, dominoes):
        symbols = [(i, x) for i, x in enumerate(dominoes) if x != '.']
        symbols = [(-1, 'L')] + symbols + [(len(dominoes), 'R')]

        ans = list(dominoes)
        for (i, x), (j, y) in zip(symbols, symbols[1:]):
            if x == y:
                for k in range(i + 1, j):
                    ans[k] = x
            elif x > y:  # RL
                for k in range(i + 1, j):
                    ans[k] = '.LR'[self.cmp(k - i, j - k)]

        return "".join(ans)

if __name__ == '__main__':
    a = PushDominoes()
    print(a.pushDominoes(".L.R...LR..L.."))
    print(a.pushDominoes("RR.L"))