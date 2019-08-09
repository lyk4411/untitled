class FindtheTownJudge(object):
    def findJudge(self, N, trust):
        hm = {i: set() for i in range(1, N + 1)}
        for i in trust:
            hm[i[0]].add(i[1])
        for i in hm:
            if len(hm[i]) == 0:
                for j in hm:
                    if i != j and i not in hm[j]: return - 1
                return i
        return -1
if __name__ == '__main__':
    a = FindtheTownJudge()
    print(a.findJudge(N=2, trust=[[1, 2]]))
    print(a.findJudge(N=3, trust=[[1, 3], [2, 3]]))
    print(a.findJudge(N=3, trust=[[1, 3], [2, 3], [3, 1]]))
    print(a.findJudge(N=4, trust=[[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]))