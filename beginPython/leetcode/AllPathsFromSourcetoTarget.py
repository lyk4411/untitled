class AllPathsFromSourcetoTarget(object):
    def allPathsSourceTarget(self, graph):
        N = len(graph)

        def solve(node):
            if node == N - 1: return [[N - 1]]
            ans = []
            for nei in graph[node]:
                for path in solve(nei):
                    ans.append([node] + path)
            return ans

        return solve(0)
    # def allPathsSourceTarget(self, graph):
    #     """
    #     :type graph: List[List[int]]
    #     :rtype: List[List[int]]
    #     """
    #     res = []
    #     self.dfs(graph, res, 0, [0])
    #     return res
    #
    # def dfs(self, graph, res, pos, path):
    #     if pos == len(graph) - 1:
    #         res.append(path)
    #
    #     else:
    #         for n in graph[pos]:
    #             self.dfs(graph, res, n, path + [n])

if __name__ == '__main__':
    a = AllPathsFromSourcetoTarget()
    print(a.allPathsSourceTarget([[1, 2], [3], [3], []]))
    print(a.allPathsSourceTarget([[1, 2], [3], [3], [4, 5], [6], [6], []]))