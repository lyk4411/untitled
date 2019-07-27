class SatisfiabilityofEqualityEquations(object):
    def equationsPossible(self, equations):
        graph = [[] for _ in range(26)]

        for eqn in equations:
            if eqn[1] == '=':
                x = ord(eqn[0]) - ord('a')
                y = ord(eqn[3]) - ord('a')
                graph[x].append(y)
                graph[y].append(x)

        color = [None] * 26
        t = 0
        for start in range(26):
            if color[start] is None:
                t += 1
                stack = [start]
                while stack:
                    node = stack.pop()
                    for nei in graph[node]:
                        if color[nei] is None:
                            color[nei] = t
                            stack.append(nei)

        for eqn in equations:
            if eqn[1] == '!':
                x = ord(eqn[0]) - ord('a')
                y = ord(eqn[3]) - ord('a')
                if x == y: return False  # lee
                if color[x] is not None and color[x] == color[y]:
                    return False
        return True

if __name__ == '__main__':
    a = SatisfiabilityofEqualityEquations()
    print(a.equationsPossible(["a==b", "b!=a"]))
    print(a.equationsPossible(["b==a", "a==b"]))
    print(a.equationsPossible(["a==b", "b==c", "a==c"]))
    print(a.equationsPossible(["a==b", "b!=c", "c==a"]))
    print(a.equationsPossible(["c==c", "b==d", "x!=z"]))
