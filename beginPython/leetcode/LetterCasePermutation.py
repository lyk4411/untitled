from queue import Queue


class LetterCasePermutation(object):
    def letterCasePermutation(self, S):
        cur_s = [S]
        # 每次都从上一轮记录的位置的下一位开始计算
        for i in range(len(S)):
            next_s = []
            for s in cur_s:
                # 如果是数字，则当前分支直接加入下轮的分支
                if s[i].isdigit():
                    next_s.append(s)
                # 如果是字母，则当前分支分为大小写两种加入下轮的分支
                else:
                    next_s.append(s[0:i] + s[i].lower() + s[i + 1:])
                    next_s.append(s[0:i] + s[i].upper() + s[i + 1:])
            cur_s = next_s
        return cur_s

if __name__ == '__main__':
    a = LetterCasePermutation()
    s1 = 'a1b2'
    s2 = '3z4'
    print(a.letterCasePermutation(s1))
    print(a.letterCasePermutation(s2))



