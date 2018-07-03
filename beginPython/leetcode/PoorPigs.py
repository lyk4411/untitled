class PoorPigs(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        pigs = 0
        while (minutesToTest / minutesToDie + 1)**pigs < buckets:
            pigs += 1
        return pigs

if __name__ == '__main__':
    a = PoorPigs()
    print(a.poorPigs(10000, 15, 60))