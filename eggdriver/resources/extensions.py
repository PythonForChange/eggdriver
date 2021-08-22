import os

class Lang:
    def __init__(self,name: str):
        self.name=name
        self.extension="."+self.name
        self.root="/usr/bin/python "+name+self.extension
    def write(self,T: str,name: str):
        f=open(name+self.extension,"w")
        f.write(T)
        f.close()
    def append(self,T: str,name: str):
        f=open(name+self.extension,"a")
        f.write(T)
        f.close()
    def read(self, name: str):
        f=open(name+self.extension,"r")
        text=f.read()
        f.close()
        return text
    def execute(self,name: str):
        try:
            os.system(self.root)
        except:
            print("Execute error in: "+self.root)
    def delete(self,name: str):
        os.remove(name+self.extension)
    def getLines(self,name: str):
        h=open(name+self.extension,"r")
        lines=h.readlines()
        h.close()
        return lines
    def writeLines(self,lines,name: str):
        self.write("",name)
        for i in lines:
            self.append(i,name)

# Extensions
py=Lang("py")
txt=Lang("txt")
nqa=Lang("nqa")
pfcf=Lang("pfcf")
html=Lang("html")
withoutFormat=Lang("")