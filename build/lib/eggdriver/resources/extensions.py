import subprocess, os
from eggdriver.resources.console.display import sysCommand

class Lang:
    """File Format class with some useful methods"""
    def __init__(self, name: str):
        self.name = name
        self.extension = "." + self.name
    def write(self, T: str, name: str):
        f = open(name + self.extension, "w")
        f.write(T)
        f.close()
    def append(self, T: str, name: str):
        f = open(name + self.extension, "a")
        f.write(T)
        f.close()
    def read(self, name: str):
        f = open(name + self.extension, "r")
        text = f.read()
        f.close()
        return text
    def py_run(self, name: str):
        """Method execute

        Run a python file
        """
        try:
            sysCommand(name + self.extension)
        except:
            print("Execute error")
    def delete(self, name: str):
        os.remove(name + self.extension)
    def getLines(self, name: str):
        h = open(name + self.extension, "r")
        lines = h.readlines()
        h.close()
        return lines
    def writeLines(self, lines, name: str):
        self.write("", name)
        for i in lines:
            self.append(i, name)

class CPP(Lang):
    def __init__(self):
        super().__init__("cpp")
    def compile(self, file):
        if os.path.exists(file + ".exe"):
            os.remove(file + ".exe")
        subprocess.call(["g++", "-std=c++17", file + ".cpp" , "-o", file])
    def run(self, file, *args):
        self.compile(file)
        commands = ["./" + file]
        for i in args:
            commands += [i]
        subprocess.call(commands)

# Extensions
py = Lang("py")
txt = Lang("txt")
nqa = Lang("nqa")
pfcf = Lang("pfcf")
html = Lang("html")
withoutFormat = Lang("")
wf = withoutFormat
cpp = CPP()

