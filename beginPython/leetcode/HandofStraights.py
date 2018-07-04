import collections

class HandofStraights(object):
    def isNStraightHand(self, hand, W):
        count = collections.Counter(hand)
        while count:
            m = min(count)
            for k in range(m, m + W):
                v = count[k]
                if not v: return False
                if v == 1:
                    del count[k]
                else:
                    count[k] = v - 1
        return True

if __name__ == '__main__':
    a = HandofStraights()
    print(a.isNStraightHand(hand=[1, 2, 3, 6, 2, 3, 4, 7, 8], W=3))
    print(a.isNStraightHand(hand=[1, 2, 3, 4, 5], W=4))
    print(a.isNStraightHand(hand=[1, 2, 3, 4, 5], W=5))