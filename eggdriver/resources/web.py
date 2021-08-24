from eggdriver.resources.modules import install
from eggdriver.resources.extensions import html

class Document():
    """HTML documents class whit some useful methods like Document.write"""
    def __init__(self, name: str, output: str ="index"):
        install("bs4")
        from bs4 import BeautifulSoup
        self.name = name
        doc = open(self.name + ".html").read()
        self.soup = BeautifulSoup(doc, features = "html.parser")
        self.output = output
        lines = html.getLines(self.name)
        html.writeLines(lines, self.output)
    def write(self, text: str, id: str):
        lines = html.getLines(self.output)
        for i in range(0, len(lines)):
            line = lines[i]
            words = line.split()
            if words[0] == "$egg" and id == words[1]:
                lines[i] = text + "\n"
                html.writeLines(lines, self.output)
                return lines
    def addTag(self, tag: str, content: str, id: str):
        return self.write(makeTag(self, tag, content), id)

def makeTag(document, tag: str, content: str):
    """Make an HTML tag"""
    new = document.soup.new_tag(tag)
    new.string = content
    return str(new)
