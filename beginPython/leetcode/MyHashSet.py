class MyHashSet(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = [False] * 1000000
    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        self.arr[key] = True
    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        self.arr[key] = False
    def contains(self, key):
        """
        Returns true if this set did not already contain the specified element
        :type key: int
        :rtype: bool
        """
        return self.arr[key]

if __name__ == '__main__':
    a = MyHashSet()
    a.add(0)
    a.add(1)
    a.add(2)
    a.add(3)
    a.add(2)
    print(a.contains(2))
    a.remove(2)
    print(a.contains(2))