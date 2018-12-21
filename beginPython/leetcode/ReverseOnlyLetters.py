class ReverseOnlyLetters(object):
    def reverseOnlyLetters(self, S):
        letters = [c for c in S if c.isalpha()]
        ans = []
        for c in S:
            if c.isalpha():
                ans.append(letters.pop())
            else:
                ans.append(c)
        return "".join(ans)

if __name__ == '__main__':
    a = ReverseOnlyLetters()
    print(a.reverseOnlyLetters("ab-cd"))
    print(a.reverseOnlyLetters("a-bC-dEf-ghIj"))
    print(a.reverseOnlyLetters("Test1ng-Leet=code-Q!"))
