class MyHashMap(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = [-1] * 1000001
    def put(self, key, value):
        """
        value will always be positive.
        :type key: int
        :type value: int
        :rtype: void
        """
        self.arr[key] = value
    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        return self.arr[key]
    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        self.arr[key] = -1

if __name__ == '__main__':
    hashMap = MyHashMap()
    hashMap.put(1, 1);
    hashMap.put(2, 2);
    print(hashMap.get(1));
    print(hashMap.get(3));
    hashMap.put(2, 1);
    print(hashMap.get(2));
    hashMap.remove(2);
    print(hashMap.get(2));