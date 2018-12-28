import collections


class BusRoutes(object):
    def numBusesToDestination(self, routes, S, T):
        # if S == T: return 0
        # N = len(routes)
        # graph = collections.defaultdict(set)
        # for i, r1 in enumerate(routes):
        #     for j in range(i + 1, N):
        #         r2 = routes[j]
        #         if any(r in r2 for r in r1):
        #             graph[i].add(j)
        #             graph[j].add(i)
        #
        # seen, targets = set(), set()
        # for node, route in enumerate(routes):
        #     if S in route: seen.add(node)
        #     if T in route: targets.add(node)
        #
        # queue = [(node, 1) for node in seen]
        # for node, depth in queue:
        #     if node in targets: return depth
        #     for nei in graph[node]:
        #         if nei not in seen:
        #             seen.add(nei)
        #             queue.append((nei, depth + 1))
        # return -1

        if S == T: return 0
        hsh = collections.defaultdict(list)
        route_hsh = {}
        for bus_idx, stations in enumerate(routes):
            route_hsh[bus_idx] = set(stations)
            for s in stations:
                hsh[s].append(bus_idx)
        if S not in hsh: return -1
        queue = collections.deque()
        for bus in hsh[S]:
            # (bus_idx, step)
            queue.appendleft((bus, 1))
        visited = set()

        while queue:
            cur_bus, step = queue.pop()
            if T in route_hsh[cur_bus]: return step
            for s in route_hsh[cur_bus]:
                for bus in hsh[s]:
                    if bus != cur_bus and bus not in visited:
                        visited.add(bus)
                        queue.appendleft((bus, step + 1))
        return -1

if __name__ == '__main__':
    a = BusRoutes()
    print(a.numBusesToDestination([[1, 2, 7], [3, 6, 7]], 1, 6))