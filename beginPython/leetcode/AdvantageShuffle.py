class AdvantageShuffle(object):
    def advantageCount(self, A, B):
        sortedA = sorted(A)
        sortedB = sorted(B)

        # assigned[b] = list of a that are assigned to beat b
        # remaining = list of a that are not assigned to any b
        assigned = {b: [] for b in B}
        # print('assigned: ',assigned)
        remaining = []

        # populate (assigned, remaining) appropriately
        # sortedB[j] is always the smallest unassigned element in B
        j = 0
        for a in sortedA:
            if a > sortedB[j]:
                assigned[sortedB[j]].append(a)
                j += 1
            else:
                remaining.append(a)
        print('assigned: ', assigned)

        # Reconstruct the answer from annotations (assigned, remaining)
        return [assigned[b].pop() if assigned[b] else remaining.pop()
                for b in B]

if __name__ == '__main__':
    a = AdvantageShuffle()
    A = [2, 7, 11, 15]
    B = [1, 10, 4, 11]
    print(a.advantageCount(A, B))
    A = [12, 24, 8, 32]
    B = [13, 25, 32, 11]
    print(a.advantageCount(A, B))
    A = [2, 0, 4, 1, 2]
    B = [1, 3, 0, 0, 2]
    print(a.advantageCount(A, B))
