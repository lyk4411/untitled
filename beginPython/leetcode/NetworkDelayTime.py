import collections


class NetworkDelayTime(object):
    def networkDelayTime(self, times, N, K):
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        dist = {node: float('inf') for node in range(1, N + 1)}
        seen = [False] * (N + 1)
        dist[K] = 0

        while True:
            cand_node = -1
            cand_dist = float('inf')
            for i in range(1, N + 1):
                if not seen[i] and dist[i] < cand_dist:
                    cand_dist = dist[i]
                    cand_node = i

            if cand_node < 0: break
            seen[cand_node] = True
            for nei, d in graph[cand_node]:
                dist[nei] = min(dist[nei], dist[cand_node] + d)

        ans = max(dist.values())
        return ans if ans < float('inf') else -1

if __name__ == '__main__':
    a = NetworkDelayTime()
    times = [[5, 1, 3], [1, 2, 3], [2, 3, 1], [3, 4, 2], [4, 5, 3]]
    print(a.networkDelayTime(times, 5, 4))
    print(a.networkDelayTime(times, 5, 1))
    print(a.networkDelayTime(times, 5, 2))