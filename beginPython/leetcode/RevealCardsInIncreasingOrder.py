import collections


class RevealCardsInIncreasingOrder(object):
    def deckRevealedIncreasing(self, deck):
        deck.sort()
        size = len(deck)
        queue = list(range(size))
        cnt = 0
        cmap = [None] * size
        i = 0
        while queue:
            t = queue.pop(0)
            if i % 2 == 0:
                cmap[cnt] = t
                cnt += 1
            else:
                queue.append(t)
            i += 1

        result = [None] * size
        i = 0
        while i < len(deck):
            result[cmap[i]] = deck[i]
            i += 1
        return result


if __name__ == '__main__':
    a = RevealCardsInIncreasingOrder()
    print(a.deckRevealedIncreasing([17,13,11,2,3,5,7]))