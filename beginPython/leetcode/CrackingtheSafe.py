

class CrackingtheSafe(object):
    def crackSafe(self, n, k):
        def dfs(ans, total, visits, n, k, result):
            if len(visits) == total:
                result.append(ans)
                return True
            prev = ans[len(ans) - n + 1:]
            for i in range(k):
                cur = prev + str(i)
                if visits.__contains__(cur):
                    continue
                visits.add(str(cur))
                ans += str(i)
                if dfs(ans, total, visits, n, k, result):
                    return True
                else:
                    visits.remove(cur)
                    ans = ans[:-1]
            return False
        ans = str('0') * n
        visits = set()
        total = k**n
        visits.add(ans)

        result = []
        dfs(ans, total, visits, n, k, result)

        return "".join(result)

if __name__ == '__main__':
    a = CrackingtheSafe()
    print(a.crackSafe(1, 2))
    print(a.crackSafe(2, 3))
    print(a.crackSafe(3, 4))