import collections


class PossibleBipartition(object):
    def possibleBipartition(self, N, dislikes):
        graph = collections.defaultdict(list)
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)

        color = {}

        def dfs(node, c=0):
            if node in color:
                return color[node] == c
            color[node] = c
            return all(dfs(nei, c ^ 1) for nei in graph[node])

        return all(dfs(node)
                   for node in range(1, N + 1)
                   if node not in color)

if __name__ == '__main__':
    a = PossibleBipartition()
    print(a.possibleBipartition(N = 4, dislikes = [[1,2],[1,3],[2,4]]))
    print(a.possibleBipartition(N = 3, dislikes = [[1,2],[1,3],[2,3]]))
    print(a.possibleBipartition(N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]))