class KokoEatingBananas(object):
    def minEatingSpeed(self, piles, H):
        # Can Koko eat all bananas in H hours with eating speed K?
        def possible(K):
            return sum((p - 1) // K + 1 for p in piles) <= H

        lo, hi = 1, max(piles)
        while lo < hi:
            mi = (lo + hi) // 2
            if not possible(mi):
                lo = mi + 1
            else:
                hi = mi
        return lo

if __name__ == '__main__':
    a = KokoEatingBananas()
    print(a.minEatingSpeed(piles = [3, 6, 7, 11], H = 8))
    print(a.minEatingSpeed(piles=[30, 11, 23, 4, 20], H = 5))
    print(a.minEatingSpeed(piles = [30,11,23,4,20], H = 6))
