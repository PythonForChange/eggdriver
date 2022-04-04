from eggdriver.resources.extensions import html

class Document():
    """HTML documents class whit some useful methods like Document.write"""
    def __init__(self, name: str, output: str ="index"):
        self.name = name
        self.output = output
        lines = html.getLines(self.name)
        html.writeLines(lines, self.output)
    def write(self, text: str, id: str):
        lines = html.getLines(self.output)
        for i in range(0, len(lines)):
            line = lines[i]
            words = line.split(" ")
            if words[0] == "$egg" and id == words[1]:
                lines[i] = text + "\n"
                html.writeLines(lines, self.output)
                return lines
    def addTag(self, tag: str, content: str, id: str):
        return self.write(makeTag(tag, content), id)

def makeTag(tag: str, content: str):
    """Make an HTML tag"""
    return f"<{tag}>{content}</{tag}>"
