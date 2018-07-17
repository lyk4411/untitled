class MyCircularQueue(object):
    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.data = [0 for i in range(k)]
        self.k = k
        self.front = 0
        self.back = 0
        self.size = 0

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if not self.isFull():
            self.data[self.back] = value
            self.back = (self.back + 1) % self.k
            self.size += 1
            return True
        return False

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if not self.isEmpty():
            self.front = (self.front + 1) % self.k
            self.size -= 1
            return True
        return False

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if not self.isEmpty():
            return self.data[self.front]
        return -1

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if not self.isEmpty():
            return self.data[self.back - 1]
        return -1

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        return self.size == 0

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        return self.size == self.k

if __name__ == '__main__':
    circularQueue = MyCircularQueue(5)
    circularQueue.enQueue(1)
    circularQueue.enQueue(2)
    circularQueue.enQueue(3)
    circularQueue.enQueue(4)
    print(circularQueue.Rear())
    circularQueue.isFull()
    circularQueue.deQueue()
    circularQueue.enQueue(4)
    print(circularQueue.Rear())