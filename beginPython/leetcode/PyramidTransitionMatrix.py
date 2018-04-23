class PyramidTransitionMatrix(object):
    def pyramidTransition(self, bottom, allowed):
        from collections import defaultdict
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        mem = defaultdict(list)
        for allow in allowed:
            mem[allow[0:2]].append(allow[2])

        dp = [[False] * 10 for i in range(20)]
        n  = len(bottom)
        for i in range(n):
            dp[i][ord(bottom[i]) - ord('A')] = True

        for i in range(n - 1, 0, -1):
            ndp = [[False] * 10 for i in range(20)]
            for j in range(i):
                for l in range(7):
                    for r in range(7):
                        if (dp[j][l] and dp[j + 1][r]):
                            if str(chr(65 + l) + "" + chr(65 + r)) in mem:
                                for c in mem[chr(65 + l) + "" + chr(65 + r)]:
                                    ndp[j][ord(c) - ord('A')] = True
            dp = ndp
        for i in range(7):
            if (dp[0][i]): return True
        return False

if __name__ == '__main__':
    a = PyramidTransitionMatrix()
    bottom = r"ABCD"
    allowed1 = [r"ABE", r"BCF", r"CDA", r"EFG", r"FAB", r"GBA"]
    allowed2 = [r"ABE", r"BCF", r"CDA", r"EFG", r"FAB"]
    print(a.pyramidTransition(bottom, allowed1))
    print(a.pyramidTransition(bottom, allowed2))