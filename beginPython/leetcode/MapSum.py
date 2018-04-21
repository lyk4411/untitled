
class MapSum(object):
    def __init__(self):
        self.map = {}

    def insert(self, key, val):
        self.map[key] = val

    def sum(self, prefix):
        return sum(val for key, val in self.map.items()
                   if key.startswith(prefix))
if __name__ == '__main__':
    a = MapSum()
    a.insert("apple", 2);
    a.insert("app", 3);
    a.insert("ap", 1);
    print(a.sum("a"))
    print(a.sum("ap"))
    print(a.sum("app"))
    print(a.sum("appl"))
    print(a.sum("aa"))

