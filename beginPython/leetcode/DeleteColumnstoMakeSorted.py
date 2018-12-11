class  DeleteColumnstoMakeSorted():
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        ans = 0
        for col in zip(*A):
            if any(col[i] > col[i + 1] for i in range(len(col) - 1)):
                ans += 1
        return ans

if __name__ == '__main__':
    a = DeleteColumnstoMakeSorted()
    print(a.minDeletionSize(["cba", "daf", "ghi"]))
    print(a.minDeletionSize(["a", "b"]))
    print(a.minDeletionSize( ["zyx", "wvu", "tsr"]))
    print(list(zip(*["cba", "daf", "ghi"])))
    print(list(zip(["cba", "daf", "ghi"])))