import pip, sys, subprocess
import importlib.util
from eggdriver.resources.constants import white
from eggdriver.resources.extensions import withoutFormat
from eggdriver.resources.console import ProgressBar

def fail():
    print(white + "Install failed")

def sucess(name):
    print(white + name + " succesfully installed")

def isntInstalled(package):
    """Returns True if a PyPI is not installed"""
    spec = importlib.util.find_spec(package)
    loweredSpec = importlib.util.find_spec(package.lower())
    if (spec is None) and (loweredSpec is None): 
        return True
    return False

def install_option_1(*names):
    """Implement pip as a subprocess"""
    for name in names:
        if name == "$upgrade":
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'])
        else:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', name])

def install_option_2(name: str):
    """Implement pip using pip package"""
    pip.main(['install', name])
    return "done"

def installFromRequests(requestOrPackages = "requests", fromRequests = True):
    """Install PyPI packages from a requests file or a list"""
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
    """Install a package from github.com"""
    for package in packages:
        url = f"git+https://github.com/{userOrOrganization}/{package}.git#egg={package}"
        installFromRequests([url], False)
        print(white + package +" succesfully installed")
        print(white + f"Try \'import {package}\'")

def installFromPip(*packages):
    """Install PyPI packages"""
    for name in packages:
        try:
            installFromRequests(name,0)
            sucess(name)
        except:
            fail()
            print(white + "Retrying...")
            try:
                install_option_2(name)
                sucess(name)
            except:
                fail()

def installFromPipwin(*packages):
    """Install unofficial python packages binaries for Windows provided by Christoph Gohlke"""
    if isntInstalled("pipwin"):
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', "pipwin"])
    for name in packages:
        try:
            subprocess.check_call([sys.executable, '-m', 'pipwin', 'install', name])
            sucess(name)
        except:
            fail()

def installFromEasyinstall(*packages):
    """Install easyinstall packages"""
    if isntInstalled("easyinstall"):
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', "easyinstall"])
    for name in packages:
        try:
            subprocess.check_call([sys.executable, '-m', 'easyinstall', 'install', name])
            sucess(name)
        except:
            fail()

def install(*packages):
    """Install python packages"""
    for name in packages:
        try:
            installFromPip(name)
            sucess(name)
        except:
            fail()
            print(white + "Retrying...")
            try:
                installFromPipwin(name)
                sucess(name)
            except:
                fail()
                print(white + "Retrying...")
                try:
                    installFromEasyinstall(name)
                    sucess(name)
                except:
                    fail()

def upgrade(name: str):
    """Update a PyPI package"""
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', name])
    except:
        print(white + name + " succesfully ugraded")

class Repo():
    """Github Repo class"""
    def __init__(self, userOrOrganization: str, package: str):
        self.root = userOrOrganization
        self.name = package
    def pull(self):
        try:
            installFromGithub(self.root, [self.name])
        except:
            print(white + "Pull failed")
