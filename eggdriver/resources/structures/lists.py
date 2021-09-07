from eggdriver.resources.structures.iterators import Iterator

class List(list):
    def __init__(self, list = []):
        super().__init__()
        [self.append(i) for i in list]
    def addFirst(self, item):
        self.reverse()
        self.addLast(item)
        self.reverse()
    def addLast(self, item):
        self.append(item)
    def removeFirst(self):
        self = self[1:]
    def removeLast(self):
        self.reverse()
        self.removeFirst()
        self.reverse()
    def contains(self, item):
        return item in self
    def display(self, returnText = False, symbols = ["[", "]"]):
        text = symbols[0] + " "
        for i in self:
            text += str(i) + " "
        if returnText:
            return text + symbols[1]
        else:
            print(text + "]")
    def Iterator(self):
        return Iterator(self)
    def iterate(self, function):
        i = self.Iterator()
        for index in i.indexes:
            function(i.value)
            i.next()
    @property
    def first(self):
        return self[0]
    @property
    def last(self):
        return self[-1]
    @property
    def size(self):
        return len(self)
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