class ReorderLogFiles():
    def reorderLogFiles(self, logs):
        def f(log):
            id_, rest = log.split(" ", 1)
            return (0, rest, id_) if rest[0].isalpha() else (1,)

        return sorted(logs, key=f)

if __name__ == '__main__':
    a = ReorderLogFiles()
    print(a.reorderLogFiles(["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]))
    b = [('a', 1, 'a'), ('a', 2, 'c'), ('b', 6, 'b'), ('b', 4, 'a'), ('a', 3, 'b')]
    print(sorted(b,key = lambda x :(x[0], x[2])))
