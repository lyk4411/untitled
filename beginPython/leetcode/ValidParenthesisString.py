


class ValidParenthesisString(object):
    def checkValidString(self, s):
        left = []
        star = []
        for i in range(len(s)):
            if s[i] == "*":
                star.append(i)
            elif s[i] == "(":
                left.append(i)
            else:
                if left == [] and star == []:
                    return False
                if left != []:
                    left.pop()
                else:
                    star.pop()
        while left != [] and star != []:
            if left[-1] > star[-1]:
                return False
            left.pop()
            star.pop()
        return left == []

if __name__ == '__main__':
    a = ValidParenthesisString()
    print(a.checkValidString("()"))
    print(a.checkValidString("(*)"))
    print(a.checkValidString("(*))"))
    print(a.checkValidString(")("))