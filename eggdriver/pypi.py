from eggdriver.resources import installFromRequests, sysCommand, py, white

defaultVersion = '0.0.'

def build(autoVersion = True, baseVersion = defaultVersion):
    """Build and upload a PyPI package release

FUNCTION build()

In Windows is equal to type in the console the following lines:
py -m build --sdist
py -m build --wheel
py -m twine check dist/*
py -m twine upload -u {user} -p {password} dist/*
"""
    installFromRequests(["setuptools", "twine", "build"], False)
    if autoVersion:
        setup = py.getLines("setup")
        firstLine = setup[0].split()
        v = firstLine[2]
        index = len(baseVersion) + 1
        value = int(v[index:-1]) + 1
        v = baseVersion + str(value)
        firstLine = [f"v = \"{v}\""]
        py.writeLines(firstLine + setup[1:], "setup")
    sysCommand("-m build --sdist")
    sysCommand("-m build --wheel")
    sysCommand("-m twine check dist/*")
    try:
        from eggconfig import pypi as info
        user = info["user"]
        password = info["password"]
        sysCommand(f"-m twine upload -u {user} -p {password} dist/*")
    except ImportError:
        print(white + """Please create a eggconfig.py file in your current directory and write the following lines
    
pypi = {
    "user" : "{your PyPI user or "__token__"}",
    "password" : "{your PyPI password or token}"
}
""")

def buildEggdriver(autoVersion = True, baseVersion = defaultVersion):
    """Build and upload a eggdriver release to PyPI

FUNCTION buildEggdriver()

In Windows is equal to type in the console the following lines
py -m build --sdist
py -m build --wheel
py -m twine check dist/*
py -m twine upload -u {user} -p {password} dist/{version}dist/eggdriver-{version}.tar.gz
"""
    installFromRequests(["setuptools", "twine", "build"], False)
    if autoVersion:
        setup = py.getLines("setup")
        firstLine = setup[0].split()
        v = firstLine[2]
        index = len(baseVersion) + 1
        value = int(v[index:-1]) + 1
        v = baseVersion + str(value)
        firstLine = [f"v = \"{v}\""]
        py.writeLines(firstLine + setup[1:], "setup")
        version = py.getLines("eggdriver/version")
        firstLine2 = [f"ver = \"{v}\""]
        py.writeLines(firstLine2 + version[1:], "eggdriver/version")
    sysCommand("-m build --sdist")
    sysCommand("-m build --wheel")
    sysCommand("-m twine check dist/*")
    try:
        from eggconfig import pypi as info
        user = info["user"]
        password = info["password"]
        sysCommand(f"-m twine upload -u {user} -p {password} dist/eggdriver-{v}.tar.gz")
    except ImportError:
        print(white + """Please create a eggconfig.py file in your current directory and write the following lines
    
pypi = {
    "user" : "{your PyPI user or "__token__"}",
    "password" : "{your PyPI password or token}"
}
""")