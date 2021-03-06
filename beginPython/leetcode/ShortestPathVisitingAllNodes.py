import collections


class ShortestPathVisitingAllNodes(object):
    def shortestPathLength(self, graph):
        N = len(graph)
        queue = collections.deque((1 << x, x) for x in range(N))
        dist = collections.defaultdict(lambda: N * N)
        for x in range(N): dist[1 << x, x] = 0

        while queue:
            # cover 状态下的head节点。
            cover, head = queue.popleft()
            d = dist[cover, head]
            if cover == 2 ** N - 1: return d
            for child in graph[head]:
                cover2 = cover | (1 << child)
                if d + 1 < dist[cover2, child]:
                    dist[cover2, child] = d + 1
                    queue.append((cover2, child))

if __name__ == '__main__':
    a = ShortestPathVisitingAllNodes()
    print(a.shortestPathLength([[1, 2, 3], [0], [0], [0]]))
    print(a.shortestPathLength([[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]]))
