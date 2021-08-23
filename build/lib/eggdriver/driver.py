from eggdriver.resources.modules import installFromRequests, install_option_1
from eggdriver.resources.console import sleep
from eggdriver.resources.server import Server

"""
FUNCTION init()

Initialize Repository:
- Upgrade pip
- Install all the packages in requests file

Eg:
init()
>>> Requirement already satisfied: pip in <root> (21.2.4)
"""
def init():
    """Upgrade pip and install all the packages in requests file"""
    install_option_1("$upgrade") # Upgrade pip
    sleep(10) # Waits 10 ms
    installFromRequests() # Install all the packages in requests file