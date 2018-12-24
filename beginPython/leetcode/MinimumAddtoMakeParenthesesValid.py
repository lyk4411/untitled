class MinimumAddtoMakeParenthesesValid(object):
    def minAddToMakeValid(self, S):
        ans, bal = 0, 0
        for i in range(len(S)):
            bal += 1 if S[i] == '(' else -1
            if bal == -1:
                ans += 1
                bal += 1
        return ans + bal

if __name__ == '__main__':
    a = MinimumAddtoMakeParenthesesValid()
    print(a.minAddToMakeValid("((("))
    print(a.minAddToMakeValid("((()"))
    print(a.minAddToMakeValid(")))"))
    print(a.minAddToMakeValid(")))((("))

