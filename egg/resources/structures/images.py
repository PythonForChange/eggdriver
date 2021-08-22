from egg.resources.structures import List, Matrix
from egg.resources.modules import installFromRequests
from egg.resources.console import sleep
from egg.resources.constants import limit, square, whiteSquare, blackSquare

class Image(Matrix):
    def __init__(self, listOfLists = []):
        installFromRequests(["numpy", "tensorflow", "keras", "Pillow", "Colr"], False) # Install
        super().__init__(listOfLists)
        self.bias = [0, 0, 0]
    def load(self, fileName):
        from keras.preprocessing import image # Local import
        import numpy as np # Local import
        source = image.img_to_array(image.load_img(fileName)) # Matrix with elements of form [224. 228. 255.]
        for i in np.array(source):
            self.addLast(List(i))
    def save(self, fileName):
        from keras.preprocessing import image # Local import
        from PIL import Image
        import numpy as np
        pil_img = image.array_to_img(self.matrix)
        pil_img.save(fileName)
    def loadFromBW(self, vanillaMatrix):
        for vanillaList in vanillaMatrix:
            list = List([])
            for i in vanillaList:
                item = [i, i, i]
                list.addLast(item)
            self.addLast(list)
    def loadFromRGB(self, vanillaMatrix):
        [self.addLast(List(vanillaList)) for vanillaList in vanillaMatrix]
    def printRGB(self):
        from colr import color # Local import
        b = self.bias
        for vanillaList in self.matrix:
            line = limit
            for j in vanillaList:
                line += color(square, fore=(self.colour(j, 0), self.colour(j, 1), self.colour(j, 2)), back=(0, 0, 0))
            print(line + limit)
        sleep(10)
        print("")
    def printBW(self):
        from colr import color # Local import
        for vanillaList in self.matrix:
            line = limit
            for j in vanillaList:
                average = int((j[0] + j[1] + j[2]) / 3)
                line += color(square, fore=(average, average, average), back=(0, 0, 0))
            print(line + limit)
        sleep(10)
        print("")
    def colour(self, list, id):
        b = self.bias[id]
        result = b + list[id]
        if result < 0:
            return 0
        if result > 255:
            return 255
        return result