class BulbSwitcherII(object):
    def flipLights(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        if n == 0 or m == 0:
            return 1;
        if n == 1:
            return 2
        if n == 2:
            return 3 if m == 1 else 4
        if m == 1:
            return 4
        return 7 if m == 2 else 8

if __name__ == '__main__':
    a = BulbSwitcherII()
    print(a.flipLights(8, 2))
