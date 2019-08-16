import collections


class NumberofSquarefulArrays(object):
    def numSquarefulPerms(self, A):
        N = len(A)
        count = collections.Counter(A)

        graph = {x: [] for x in count}
        for x in count:
            for y in count:
                if int((x + y) ** .5 + 0.5) ** 2 == x + y:
                    graph[x].append(y)

        def dfs(x, todo):
            count[x] -= 1
            if todo == 0:
                ans = 1
            else:
                ans = 0
                for y in graph[x]:
                    if count[y]:
                        ans += dfs(y, todo - 1)
            count[x] += 1
            return ans

        return sum(dfs(x, len(A) - 1) for x in count)

if __name__ == '__main__':
    a = NumberofSquarefulArrays()
    print(a.numSquarefulPerms([1, 17, 8]))
    print(a.numSquarefulPerms([2, 2, 2]))
