from eggdriver.resources import installFromRequests, sysCommand

"""
FUNCTION build()

py -m build --sdist
py -m build --wheel
py -m twine check dist/*
py -m twine upload dist/*
"""
def build():
    installFromRequests(["setuptools", "twine", "build"], False)
    sysCommand("-m build --sdist")
    sysCommand("-m build --wheel")
    sysCommand("-m twine check dist/*")
    sysCommand("-m twine upload dist/*")
