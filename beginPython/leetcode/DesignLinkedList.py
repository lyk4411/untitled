class DesignLinkedList(object):
    def __init__(self):
        self.list = []

    def get(self, index):
        if index >= len(self.list):
            return -1
        return self.list[index]

    def addAtHead(self, val):
        self.list.insert(0, val)

    def addAtTail(self, val):
        self.list.append(val)

    def addAtIndex(self, index, val):
        if index > len(self.list):
            return
        self.list.insert(index, val)

    def deleteAtIndex(self, index):
        if index >= len(self.list):
            return
        del self.list[index]

if __name__ == '__main__':
    linkedList = DesignLinkedList()
    linkedList.addAtHead(1);
    linkedList.addAtTail(3);
    linkedList.addAtIndex(1, 2);
    print(linkedList.get(1));
    linkedList.deleteAtIndex(1);
    print(linkedList.get(1));