

class RedundantConnection(object):
    def findRedundantConnection(self, edges):
        def find(al, i):
            while al[i] != -1:
                i = al[i]
            return i

        al= [-1] * 2001
        for edge in edges:
            x = find(al,edge[0])
            y = find(al,edge[1])
            if x == y:
                return edge
            al[x] = y
        return []
if __name__ == '__main__':
    a = RedundantConnection()
    print(a.findRedundantConnection([[1,2], [1,3], [2,3]]))
    print(a.findRedundantConnection([[1,2], [2,3], [3,4], [1,4], [1,5]]))



