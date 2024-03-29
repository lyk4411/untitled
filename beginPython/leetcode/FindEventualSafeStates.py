import collections


class FindEventualSafeStates(object):
    def eventualSafeNodes(self, graph):
        WHITE, GRAY, BLACK = 0, 1, 2
        color = collections.defaultdict(int)

        def dfs(node):
            if color[node] != WHITE:
                return color[node] == BLACK

            color[node] = GRAY
            for nei in graph[node]:
                if color[nei] == BLACK:
                    continue
                if color[nei] == GRAY or not dfs(nei):
                    return False
            color[node] = BLACK
            return True

        return filter(dfs, range(len(graph)))

if __name__ == '__main__':
    a = FindEventualSafeStates()
    print(list(a.eventualSafeNodes([[1,2],[2,3],[5],[0],[5],[],[]])))