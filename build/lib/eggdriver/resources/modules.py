import pip, sys, subprocess
import importlib as il
import importlib.util
from eggdriver.resources.constants import white
from eggdriver.resources.extensions import withoutFormat
from eggdriver.resources.console import ProgressBar

def isntInstalled(package):
    spec = importlib.util.find_spec(package)
    loweredSpec = importlib.util.find_spec(package.lower())
    if (spec is None) and (loweredSpec is None): 
        return True
    return False

def install_option_1(name: str):
    """Implement pip as a subprocess"""
    if name == "$upgrade":
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'])
    else:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', name])
    return "done"

def install_option_2(name: str):
    """Implement pip using pip package"""
    pip.main(['install', name])
    return "done"

def installFromRequests(requestOrPackages = "requests", fromRequests = True):
    if fromRequests:
        requestOrPackages = withoutFormat.getLines(requestOrPackages)
    bar = ProgressBar()
    l = len(requestOrPackages)
    c = 0
    for package in requestOrPackages:
        if '\n' in package:
            package = package.rstrip('\n')
        if isntInstalled(package):
            install_option_1(package)
        c += 1
        bar.display(int(c / l * 100), 32, 24, True)

def installFromGithub(userOrOrganization: str, packages: list):
    for package in packages:
        url = f"git+https://github.com/{userOrOrganization}/{package}.git#egg={package}"
        installFromRequests([url], False)
        print(white + package +" succesfully installed")
        print(white + f"Try \'import {package}\'")

def install(name: str):
    try:
        installFromRequests(name,0)
        #raise Exception("error")
    except:
        print(white + "Install failed")
        print(white + "Retrying...")
        try:
            install_option_2(name)
        except:
            print(white + "Install failed")
            return "error"
    print(white + name + " succesfully installed")
    return "done"

def upgrade(name: str):
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', name])
    except:
        print(white + name + " succesfully ugraded")
    return "done"

class Repo():
    def __init__(self, userOrOrganization: str, package: str):
        self.root = userOrOrganization
        self.name = package
    def pull(self):
        try:
            installFromGithub(self.root, [self.name])
        except:
            print(white + "Pull failed")
