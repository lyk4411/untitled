from queue import Queue

class SlidingPuzzle(object):

    def slidingPuzzle(self, board):
        target = '123450'
        start = ''
        for i in range(len(board)):
            for j in range(len(board[0])):
                start += str(board[i][j])
        visited = set()
        dirs = [[ 1, 3 ], [ 0, 2, 4 ], [ 1, 5 ], [ 0, 4 ], [1, 3, 5 ], [ 2, 4 ]]
        queue = Queue()
        queue.put(start)
        res = 0
        while not queue.empty():
            size = queue.qsize()
            for i in range(size):
                cur = queue.get()
                if cur == target:
                    return res
                zero = cur.find('0')
                for dir in range(len(dirs[zero])):
                    next = self.swap(cur, zero, dirs[zero][dir])
                    if visited.__contains__(next):
                        continue
                    visited.add(next)
                    queue.put(next)
            res += 1
        return -1

    def swap(self, cur, i, j):
        temp = list(cur)
        temp[i] , temp[j] = temp[j] , temp[i]
        return ''.join(temp)

if __name__ == '__main__':
    a = SlidingPuzzle()
    print(a.slidingPuzzle([[3,2,4],[1,5,0]]))
    print(a.slidingPuzzle([[4,1,2],[5,0,3]]))

