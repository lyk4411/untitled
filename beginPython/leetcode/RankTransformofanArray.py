class RankTransformofanArray:
    def arrayRankTransform(self, arr):
        rank = {ele: i + 1 for i, ele in enumerate(sorted(set(arr)))}
        print(rank)
        return list(map(rank.get, arr))

if __name__ == '__main__':
    a = RankTransformofanArray()
    print(a.arrayRankTransform([40,10,20,30]))
