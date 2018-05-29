

class PositionsofLargeGroups(object):
    def largeGroupPositions(self, S):
        ans = []
        i = 0  # The start of each group
        for j in range(len(S)):
            if j == len(S) - 1 or S[j] != S[j + 1]:
                # Here, [i, j] represents a group.
                if j - i + 1 >= 3:
                    ans.append([i, j])
                i = j + 1
        return ans

if __name__ == '__main__':
    a = PositionsofLargeGroups()
    S = "abcdddeeeeaabbbcd"
    print(a.largeGroupPositions(S))