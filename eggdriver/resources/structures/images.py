from colr import color
import numpy as np

from eggdriver.resources.structures.lists import List
from eggdriver.resources.structures.matrices import listMatrix
from eggdriver.resources.modules import installFromRequests
from eggdriver.resources.console import sleep
from eggdriver.resources.constants import limit, square #, whiteSquare, blackSquare

class Image(listMatrix):

    def __init__(self, listOfLists = [], auto_install = True):
        super().__init__(listOfLists)
        self.bias = [0, 0, 0]
        
        if auto_install:
            installFromRequests(["numpy", "tensorflow", "keras", "Pillow", "Colr"], False) # Install
        
    def load(self, fileName):
        from keras.preprocessing import image # Local import

        source = image.img_to_array(image.load_img(fileName)) # Matrix with elements of form [224. 228. 255.]
        for i in np.array(source):
            self.addLast(List(i))

    def save(self, fileName):
        from keras.preprocessing import image # Local import
        from PIL import Image # Required

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

    def printRGB(self, delay = 10):
        b = self.bias

        for vanillaList in self.matrix:

            line = limit
            for j in vanillaList:
                line += color(square, fore=(self.colour(j, 0), self.colour(j, 1), self.colour(j, 2)), back=(0, 0, 0))
            
            print(line + limit)

        sleep(delay)
        print("")

    def printBW(self, delay = 10):

        for vanillaList in self.matrix:

            line = limit
            for j in vanillaList:
                average = int((j[0] + j[1] + j[2]) / 3)
                line += color(square, fore=(average, average, average), back=(0, 0, 0))

            print(line + limit)

        sleep(delay)
        print("")

    def colour(self, list, id):
        b = self.bias[id]
        result = b + list[id]

        if result < 0:
            return 0

        if result > 255:
            return 255

        return result
