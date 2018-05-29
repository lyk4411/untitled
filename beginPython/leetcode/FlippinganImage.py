

class FlippinganImage(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for row in A:
            for i in range((len(row) + 1) // 2):
                row[i], row[~i] = row[~i] ^ 1, row[i] ^ 1
        return A


if __name__ == '__main__':
    a = FlippinganImage()
    A = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
    print(a.flipAndInvertImage(A))