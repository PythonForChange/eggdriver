from eggdriver.resources.console.display import clearConsole, sleep
from eggdriver.resources.constants import whiteSegment, blackSegment, limit

"""
CLASS ProgressBar()

A progress bar pip-like for console implementations.

Eg:
bar = ProgressBar()
bar.iterate(printPercent = True)
>>> |████████████████████████████████|      100%
"""
class ProgressBar():
    def __init__(self):
        self.whiteSegment = whiteSegment
        self.blackSegment = blackSegment
        self.limit = limit
    def bar(self, progressPercent, length):
        progress = int(progressPercent * length / 100)
        return self.limit + progress * self.whiteSegment + (length - progress) * self.blackSegment + self.limit
    def display(self, progressPercent, length = 32, delay: int = 0, printPercent = False):
        text = self.bar(progressPercent, length)
        if printPercent:
            text += f"\t{progressPercent}%"
        print(text)
        sleep(delay)
        if progressPercent != 100:
            clearConsole()
    def iterate(self, function = clearConsole, printPercent = False):
        for i in range(100+1):
            if i != 100:
                function()
            self.display(i, 32, 24, printPercent)
            
