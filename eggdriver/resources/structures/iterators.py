class Iterator():
    def __init__(self, list):
        self.position = 0
        self.list = list
        self.indexes = range(len(self.list))
    def next(self):
        self.position += 1
    @property
    def value(self):
        return self.list[self.position]