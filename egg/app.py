# Imports
from egg.resources.console import get, clearConsole
from egg.resources.constants import *
from egg.resources.modules import install, upgrade, Repo
from egg.resources.help import help
from egg.resources.auth import login, register

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
    print(white+"Egg Console is now running")
    logged=0
    while condition:
        i=get("egg")
        if i=="$nqs":
            from nqs.developer.app import developerConsole
            developerConsole()
        elif i=="$new":
            from news.app import journalistConsole
            journalistConsole()
        elif i=="$login":
            login()
        elif i=="$register":
            register()
        elif i=="$install":
            print(white+"Package:")
            name=get("egg")
            install(name)
        elif i=="$upgrade":
            print(white+"Package:")
            name=get("egg")
            upgrade(name)
        elif i=="$pull":
            print(white+"Repo:")
            name=get("egg")
            repo=Repo(name)
            print(white+"Package:")
            package=get("egg")
            last=repo.pull(package)
            # *comming soon*
        elif i=="$help":
            help()
        elif i=="$clear":
            clearConsole()
        elif i=="$end":
            print(white+"Egg Console stopped running")
            return "done"
        else:
    	    pass