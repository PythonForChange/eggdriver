from egg.resources.modules import install
from egg.resources.extensions import html

class Document():
    def __init__(self, name: str, output: str ="index"):
        install("bs4")
        from bs4 import BeautifulSoup
        self.name=name
        doc=open(self.name+".html").read()
        self.soup=BeautifulSoup(doc,features="html.parser")
        self.output=output
        lines=html.getLines(self.name)
        html.writeLines(lines, self.output)
    def write(self, text: str, id: str):
        lines=html.getLines(self.output)
        for i in range(0,len(lines)):
            l=lines[i]
            words=l.split()
            if words[0]=="$egg" and id==words[1]:
                lines[i]=text+"\n"
                html.writeLines(lines,self.output)
                return lines
    def addTag(self,tag: str, content: str, id: str):
        return self.write(makeTag(self,tag, content),id)

def makeTag(document,tag: str, content: str):
    new=document.soup.new_tag(tag)
    new.string=content
    return str(new)
