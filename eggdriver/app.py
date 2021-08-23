# Imports
from eggdriver.resources.console import get, clearConsole, pg
from eggdriver.resources.constants import *
from eggdriver.resources.modules import installFromRequests, upgrade, Repo
from eggdriver.resources.help import help
from eggdriver.resources.auth import login, register

"""
FUNCTION eggConsole(condition: bool = True)

Display the Egg Console
Currently, the Egg Console commands are:

$nqs        Start the NQS Depeloper console
$new        Start the News Journalist console
$login      Log in Egg-cosystem *comming soon*
$register   Register in Egg-cosystem *comming soon*
$install    Install a pip package
$upgrade    Upgrade a pip package
$pull       Import a package stored on a GitHUb repository *comming soon: currently, just use github_com package*
$help       Get started command
$clear      Clear the Egg Console
$end        End the Egg Console

WARNING:
Always  use $end command in every console you run
*ONLY use a condition different to True as an argument of eggConsole(condition) if you know what are you doing**
This is the reason why condition only allows <<bool>> as data type
"""
def eggConsole(condition: bool = True):
    print(white + "Egg Console is now running")
    logged=0
    while condition:
        i = get("egg")
        if i == "$nqs":
            from eggdriver.nqs import developerConsole
            developerConsole()
        elif i == "$new":
            from eggdriver.news import journalistConsole
            journalistConsole()
        elif i == "$login":
            login()
        elif i == "$register":
            register()
        elif i == "$install":
            name = pg("Package:")
            installFromRequests([name], False)
        elif i == "$upgrade":
            name =  pg("Package:")
            upgrade(name)
        elif i == "$pull":
            org =  pg("User or Organization:")
            name = pg("Repository:")
            repo = Repo(org, name)
            repo.pull()
        elif i == "$help":
            help()
        elif i == "$clear":
            clearConsole()
        elif i == "$end":
            print(white + "Egg Console stopped running")
            return "done"
        else:
    	    pass