from operator import truediv, mul, add, sub

class GameOf24(object):
    def judgePoint24(self, A):
        if len(A) == 1: return abs(A[0] - 24) < 1e-6

        for i in range(len(A)):
            for j in range(len(A)):
                if i != j:
                    B = [A[k] for k in range(len(A)) if i != k != j]
                    for op in (truediv, mul, add, sub):
                        if (op is add or op is mul) and j > i: continue
                        if op is not truediv or A[j]:
                            B.append(op(A[i], A[j]))
                            if self.judgePoint24(B): return True
                            B.pop()
        return False

if __name__ == '__main__':
    a = GameOf24()
    print(a.judgePoint24([4, 1, 8, 7]))
    print(a.judgePoint24([8, 8, 8, 8]))