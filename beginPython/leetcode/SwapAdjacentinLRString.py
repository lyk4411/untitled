class SwapAdjacentinLRString(object):
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        if start.replace('X', '') != end.replace('X', ''): return False

        n = len(start)
        i = j = 0
        while i < n and j < n:
            while j < n and end[j] == 'X': j += 1
            while i < n and start[i] == 'X': i += 1
            if i == n or j == n: break
            if start[i] == 'L' and i < j: return False
            if start[i] == 'R' and i > j: return False
            i += 1
            j += 1
        return True

if __name__ == '__main__':
    a = SwapAdjacentinLRString()
    print(a.canTransform('RXXLRXRXL', 'XRLXXRRLX'))
    print(a.canTransform('RXXLRXR', 'XRLXXRRLX'))
    print(a.canTransform('XXXLXXXXXX', 'XXXLXXXXXX'))

