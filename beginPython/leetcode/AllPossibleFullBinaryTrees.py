class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class AllPossibleFullBinaryTrees(object):
    memo = {0: [], 1: [TreeNode(0)]}

    def allPossibleFBT(self, N):
        if N not in AllPossibleFullBinaryTrees.memo:
            ans = []
            for x in range(N):
                y = N - 1 - x
                for left in self.allPossibleFBT(x):
                    for right in self.allPossibleFBT(y):
                        bns = TreeNode(0)
                        bns.left = left
                        bns.right = right
                        ans.append(bns)
            AllPossibleFullBinaryTrees.memo[N] = ans

        return AllPossibleFullBinaryTrees.memo[N]

if __name__ == '__main__':
    a = AllPossibleFullBinaryTrees()
    print(a.allPossibleFBT(7))
    print(a.allPossibleFBT(6))