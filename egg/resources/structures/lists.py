from egg.resources.structures import Iterator

class List():
    def __init__(self, list = []):
        self.list = list
    def sort(self):
        self.list.sort()
    def reverse(self):
        self.list = self.list.reverse
    def addFirst(self, item):
        self.reverse()
        self.addLast(item)
        self.reverse()
    def addLast(self, item):
        self.list.append(item)
    def removeFirst(self):
        self.list = self.list[1:]
    def removeLast(self):
        self.reverse()
        self.removeFirst()
        self.reverse()
    def contains(self, item):
        return item in self.list
    def Iterator(self):
        return Iterator(self.list)
    def iterate(self, function):
        i = self.Iterator()
        for index in i.indexes:
            function(i.value)
            i.next()
    def display(self):
        self.iterate(print)
    @property
    def first(self):
        return self.list[0]
    @property
    def last(self):
        return self.list[0]
    @property
    def size(self):
        return len(self.list)
    @property
    def isEmpty(self):
        return self.size == 0
    
class Queue(List):
    def __init__(self, list = []):
        super().__init__(list)
    def put(self, item):
        self.addLast(item)
    def pop(self):
        self.removeFirst()
        
class Stack(Queue):
    def __init__(self, list = []):
        super().__init__(list)
    def put(self, item):
        self.addFirst(item)
    @property
    def top(self):
        return self.list.first

class Set(List):
    def __init__(self, list = []):
        super().__init__()
        [self.insert(i) for i in list]
    def insert(self, item):
        if not self.contains(item): 
            self.addLast(item)
            self.sort()

class PriorityQueue(Queue):
    def __init__(self, list = []):
        super().__init__()
        [self.insert(i) for i in list]
    def insert(self, item):
        self.addLast(item)
        self.sort()