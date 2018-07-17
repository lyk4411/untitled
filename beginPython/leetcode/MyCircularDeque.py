class MyCircularDeque(object):
    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        :type k: int
        """
        self.i = 0
        self.k = k
        self.l = []

    def insertFront(self, value):
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.i < self.k:
            templ = []
            templ.append(value)
            for x in self.l:
                templ.append(x)
            self.l = templ
            self.i += 1
            return True
        else:
            return False

    def insertLast(self, value):
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.i < self.k:
            self.i += 1
            self.l.append(value)
            return True
        else:
            return False

    def deleteFront(self):
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.l:
            self.l.pop(0)
            self.i -= 1
            return True
        else:
            return False

    def deleteLast(self):
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.l:
            self.i -= 1
            self.l.pop(self.i)
            return True
        else:
            return False

    def getFront(self):
        """
        Get the front item from the deque.
        :rtype: int
        """
        if self.l:
            return self.l[0]
        else:
            return -1

    def getRear(self):
        """
        Get the last item from the deque.
        :rtype: int
        """
        if self.l:
            return self.l[-1]
        else:
            return -1

    def isEmpty(self):
        """
        Checks whether the circular deque is empty or not.
        :rtype: bool
        """
        return len(self.l) == 0

    def isFull(self):
        """
        Checks whether the circular deque is full or not.
        :rtype: bool
        """
        return self.i == self.k

if __name__ == '__main__':
    circularDeque = MyCircularDeque(3)
    circularDeque.insertLast(1)
    circularDeque.insertLast(2)
    circularDeque.insertFront(3)
    circularDeque.insertFront(4)
    print(circularDeque.getRear())
    circularDeque.isFull()
    circularDeque.deleteLast()
    circularDeque.insertFront(4)
    print(circularDeque.getFront())