

class OpentheLock(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        vis = set(deadends)
        queue = []
        queue.append("0000")
        if ("0000" in vis):
            return -1
        vis.add("0000")

        turn = 0
        while queue:
            size = len(queue)
            for i in range(size):
                now = queue.pop(0)
                if (now == target):
                    return turn
                for j in range(4):
                    for k in [-1, 1]:
                        digit = int(now[j])
                        digit = (digit + k + 10) % 10
                        nxt = now[: j] + str(digit) + now[j + 1 :]
                        if nxt not in vis:
                            vis.add(nxt)
                            queue.append(nxt)
            turn += 1
        return -1
if __name__ == '__main__':
    a = OpentheLock()
    print(a.openLock(["0201", "0101", "0102", "1212", "2002"], "1234"))