class ChampagneTower(object):
    def champagneTower(self, poured, query_row, query_glass):
        A = [[0] * k for k in range(1, 102)]
        A[0][0] = poured
        for r in range(query_row + 1):
            for c in range(r + 1):
                q = (A[r][c] - 1.0) / 2.0
                if q > 0:
                    A[r + 1][c] += q
                    A[r + 1][c + 1] += q

        return min(1, A[query_row][query_glass])

if __name__ == '__main__':
    a = ChampagneTower()
    print(a.champagneTower(1, 0, 0))
    print(a.champagneTower(100, 8, 1))
    print(a.champagneTower(100, 8, 2))
    print(a.champagneTower(100, 14, 4))