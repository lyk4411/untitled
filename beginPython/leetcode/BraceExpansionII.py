class BraceExpansionII:
    def braceExpansionII(self, expression):
        stack, res, cur = [], [], []
        for i in range(len(expression)):
            v = expression[i]
            if v.isalpha():
                cur = [c + v for c in cur or ['']]
            elif v == '{':
                stack.append(res)
                stack.append(cur)
                res, cur = [], []
            elif v == '}':
                pre = stack.pop()
                preRes = stack.pop()
                cur = [p + c for c in res + cur for p in pre or ['']]
                res = preRes
            elif v == ',':
                res += cur
                cur = []
        return sorted(set(res + cur))

if __name__ == '__main__':
    a = BraceExpansionII()
    print(a.braceExpansionII("{a,b}{c,{d,e}}"))
    print(a.braceExpansionII("{{a,z},a{b,c},{ab,z}}"))
