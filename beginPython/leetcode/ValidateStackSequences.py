class ValidateStackSequences(object):
    def validateStackSequences(self, pushed, popped):
        j = 0
        stack = []
        for x in pushed:
            stack.append(x)
            while stack and j < len(popped) and stack[-1] == popped[j]:
                stack.pop()
                j += 1

        return j == len(popped)

if __name__ == '__main__':
    a = ValidateStackSequences()
    print(a.validateStackSequences([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))
    print(a.validateStackSequences([1, 2, 3, 4, 5], [4, 3, 5, 1, 2]))