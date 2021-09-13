from eggdriver.resources import installFromRequests, sysCommand, py

"""
FUNCTION build()
Build and upload a pypi package release

In Windows is equal to type in the console the following lines:
py -m build --sdist
py -m build --wheel
py -m twine check dist/*
py -m twine upload dist/*
"""
def build(autoVersion = True):
    """Build and upload a pypi package release"""
    installFromRequests(["setuptools", "twine", "build"], False)
    if autoVersion:
        setup = py.getLines("setup")
        firstLine = setup[0].split()
        v = firstLine[2]
        value = int(v[7:-1]) + 1
        v = '0.0.1a' + str(value)
        firstLine = [f"v = \"{v}\""]
        py.writeLines(firstLine + setup[1:], "setup")
    sysCommand("-m build --sdist")
    sysCommand("-m build --wheel")
    sysCommand("-m twine check dist/*")
    sysCommand("-m twine upload dist/*")
