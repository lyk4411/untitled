class FairCandySwap(object):
    def fairCandySwap(self, A, B):
        Sa, Sb = sum(A), sum(B)
        setB = set(B)
        for x in A:
            if x + (Sb - Sa) // 2 in setB:
                return [x, x + (Sb - Sa) // 2]

if __name__ == '__main__':
    a = FairCandySwap()
    print(a.fairCandySwap(A = [1,1], B = [2,2]))
    print(a.fairCandySwap(A = [1,2], B = [2,3]))
    print(a.fairCandySwap(A = [2], B = [1,3]))
    print(a.fairCandySwap(A = [1,2,5], B = [2,4]))