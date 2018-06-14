import heapq


class ReorganizeString(object):
    def reorganizeString(self, S):
        pq = [(-S.count(x), x) for x in set(S)]
        heapq.heapify(pq)
        if any(-nc > (len(S) + 1) / 2 for nc, x in pq):
            return ""

        ans = []
        while len(pq) >= 2:
            nct1, ch1 = heapq.heappop(pq)
            nct2, ch2 = heapq.heappop(pq)

            ans.extend([ch1, ch2])
            if nct1 + 1: heapq.heappush(pq, (nct1 + 1, ch1))
            if nct2 + 1: heapq.heappush(pq, (nct2 + 1, ch2))

        return "".join(ans) + (pq[0][1] if pq else '')

if __name__ == '__main__':
    a = ReorganizeString()
    print(a.reorganizeString("abc"))
    print(a.reorganizeString("aaa"))
    print(a.reorganizeString("aaabbcc"))
    print(a.reorganizeString("aabbbcc"))
    print(a.reorganizeString("aabbccc"))

