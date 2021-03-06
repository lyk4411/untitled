import collections


class StickerstoSpellWord(object):
    # def minStickers(self, stickers, target):
    #     """
    #     :type stickers: List[str]
    #     :type target: str
    #     :rtype: int
    #     """
    #     cntToStr = lambda cnt: ''.join(sorted(k for k in cnt.elements()))
    #     tcnt = collections.Counter(target)
    #     scnts = [collections.Counter(s) & tcnt for s in stickers]
    #     for x in range(len(scnts) - 1, -1, -1):
    #         if any(scnts[x] & scnts[y] == scnts[x] for y in range(len(scnts) - 1, -1, -1) if x != y):
    #             scnts.pop(x)
    #     # stickers = map(cntToStr, scnts)
    #     # scnts = [collections.Counter(s) for s in stickers]
    #     dmap = {}
    #
    #     def search(kcnt):
    #         key = cntToStr(kcnt)
    #         if not key: return 0
    #         # if key in sset: return 1
    #         if key in dmap: return dmap[key]
    #         ans = -1
    #         for scnt in scnts:
    #             nkcnt = collections.Counter(kcnt)
    #             for k in scnt:
    #                 if nkcnt[k]: nkcnt[k] -= scnt[k]
    #                 if nkcnt[k] <= 0: del nkcnt[k]
    #             if nkcnt == kcnt: continue
    #             val = search(nkcnt)
    #             if val < 0: continue
    #             if ans < 0 or val + 1 < ans: ans = val + 1
    #         dmap[key] = ans
    #         return ans
    #
    #     return search(tcnt)

    def minStickers(self, stickers, target):
        """
        :type stickers: List[str]
        :type target: str
        :rtype: int
        """
        dp = [0] + [-1] * ((1 << len(target)) - 1)
        tcnt = collections.Counter(target)
        scnts = [collections.Counter(s) & tcnt for s in stickers]
        for x in range(len(scnts) - 1, -1, -1):
            if any(scnts[x] & scnts[y] == scnts[x] for y in range(len(scnts) - 1, -1, -1) if x != y):
                scnts.pop(x)
        for status in range(1 << len(target)):
            if dp[status] < 0: continue
            for scnt in scnts:
                nstatus = status
                cnt = collections.Counter(scnt)
                for i, c in enumerate(target):
                    if cnt[c] > 0 and status & (1 << i) == 0:
                        nstatus |= (1 << i)
                        cnt[c] -= 1
                if dp[nstatus] < 0 or dp[nstatus] > dp[status] + 1:
                    dp[nstatus] = dp[status] + 1
        return dp[-1]
#     a.minStickers(["with", "example", "science"], "theh")
#     (0000) = 0
#     (0011) = 1
#     (0100) = 1
#     (1011) = 2
#     (0111) = 2
#     (1111) = 3
if __name__ == '__main__':
    a = StickerstoSpellWord()
    # print(a.minStickers(["with", "example", "science"], "thehat"))
    print(a.minStickers(["with", "example", "science"], "theh"))
    # print(a.minStickers(["notice", "possible"], "basicbasic"))
