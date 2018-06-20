class IsGraphBipartite(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        color = [0] * len(graph)
        return all(self.dfs(graph, color, v, 1) for v in range(len(graph)) if color[v] == 0)

    def dfs(self, graph, color, v, c):
        color[v] = c
        for to in graph[v]:
            if color[to] != 0 and color[to] == c: return False
            if color[to] == 0 and not self.dfs(graph, color, to, -c): return False
        return True

if __name__ == '__main__':
    a = IsGraphBipartite()
    print(a.isBipartite([[1, 3], [0, 2], [1, 3], [0, 2]]))
    print(a.isBipartite([[1,2,3], [0,2], [0,1,3], [0,2]]))