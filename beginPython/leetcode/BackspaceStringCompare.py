class BackspaceStringCompare(object):
    def backspaceCompare(self, S, T):
        def build(S):
            ans = []
            for c in S:
                if c != '#':
                    ans.append(c)
                elif ans:
                    ans.pop()
            return "".join(ans)

        return build(S) == build(T)

if __name__ == '__main__':
    a = BackspaceStringCompare()
    print(a.backspaceCompare(S = "ab##", T = "c#d#"))
    print(a.backspaceCompare(S = "ab#c", T = "ad#c"))
    print(a.backspaceCompare(S = "a##c", T = "#a#c"))
    print(a.backspaceCompare(S = "a#c", T = "b"))