


class PartitionLabels(object):
    def partitionLabels(self, S):
        last = {c: i for i, c in enumerate(S)}
        # temp = tuple((c, i) for i, c in enumerate(S))
        # print(last)
        # print(temp)
        j = anchor = 0
        ans = []
        for i, c in enumerate(S):
            j = max(j, last[c])
            if i == j:
                ans.append(i - anchor + 1)
                anchor = i + 1

        return ans

if __name__ == '__main__':
    a = PartitionLabels()
    print(a.partitionLabels(r"ababcbacadefegdehijhklij"))