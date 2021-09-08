from eggdriver.resources.structures.lists import List

class listMatrix(List):
    def __init__(self, listOfLists = []):
        super().__init__(listOfLists)
    def flatIterator(self):
        return self.flat.Iterator()
    def iterate(self, function):
        i = self.flatIterator()
        for index in i.indexes:
            function(i.value)
            i.next()
    @property
    def matrix(self):
        m = []
        i = self.Iterator()
        for index1 in i.indexes:
            j = i.value.Iterator()
            list = []
            for index2 in j.indexes:
                list.append(j.value)
                j.next()
            m.append(list)
            i.next()
        return m
    @property
    def flatMatrix(self):
        fm = []
        [fm.append(j) for i in self.matrix for j in i]
        return fm
    @property
    def flat(self):
        return List(self.flatMatrix)