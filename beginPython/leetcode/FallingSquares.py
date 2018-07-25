class FallingSquares(object):
    def fallingSquares(self, positions):
        qans = [0] * len(positions)
        for i, (left, size) in enumerate(positions):
            right = left + size
            qans[i] += size
            for j in range(i + 1, len(positions)):
                left2, size2 = positions[j]
                right2 = left2 + size2
                if left2 < right and left < right2:  # intersect
                    qans[j] = max(qans[j], qans[i])

        ans = []
        for x in qans:
            ans.append(max(ans[-1], x) if ans else x)
        return ans

if __name__ == '__main__':
    a = FallingSquares()
    print(a.fallingSquares([[1, 2], [2, 3], [6, 1]]))
    print(a.fallingSquares([[100, 100], [200, 100]]))
