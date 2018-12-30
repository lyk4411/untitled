import collections
import heapq


class ReachableNodesInSubdividedGraph:
    def reachableNodes(self, edges, M, N):
        e = collections.defaultdict(dict)
        for i, j, l in edges: e[i][j] = e[j][i] = l
        pq = [(-(M + 1), 0)]
        seen = {}
        result = 0
        while pq:
            hp, src = heapq.heappop(pq)
            hp = -hp
            # print("hp:" + str(hp))
            hp -= 1
            # print(seen)
            if src in seen: continue

            seen[src] = hp
            result += 1
            for dst in e[src]:
                # print("dst:" + str(dst))
                weight = e[src][dst]
                if hp > weight:
                    if seen.get(dst) != None and e[src][dst] == 0: continue
                    result += weight
                    e[dst][src] = 0
                    temp = hp - weight
                    heapq.heappush(pq, (-temp, dst))
                else:
                    e[dst][src] = e[dst][src] - hp
                    result += hp
        return result


if __name__ == '__main__':
    a = ReachableNodesInSubdividedGraph()
    # print(a.reachableNodes(edges = [[0,1,10],[0,2,1],[1,2,2]], M = 6, N = 3))
    # print(a.reachableNodes(edges = [[1,2,5],[0,3,3],[1,3,2],[2,3,5],[0,4,1]], M = 7, N = 3))
    print(a.reachableNodes(edges = [[3,4,8],[0,1,3],[1,4,0],[1,2,3],[0,3,2],[0,4,10],[1,3,3],[2,4,3],[2,3,3],[0,2,10]], M = 7, N = 5))
