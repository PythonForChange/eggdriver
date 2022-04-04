from eggdriver.resources.console import get, clearConsole, pg
from eggdriver.resources.constants import white, blue, green
from eggdriver.resources.modules import installFromRequests, upgrade, Repo
from eggdriver.resources.help import welcome
from eggdriver.resources.auth import login, register

"""
FUNCTION eggConsole(command = None)

Display the Eggdriver Console
Currently, the Eggdriver Console commands are:

$nqs        Start the NQS Depeloper console
$new        Start the News Journalist console
$login      Log in Egg-cosystem *comming soon*
$register   Register in Egg-cosystem *comming soon*
$install    Install a pip package
$upgrade    Upgrade a pip package
$pull       Import a package stored on a GitHUb repository *comming soon: currently, just use github_com package*
$help       Get started command
$clear      Clear the Egg Console
$end        End the Eggdriver Console

WARNING:
Always use $end command in every console you run
"""
def eggConsole(command = None):
    """Display the Eggdriver Console"""
    print(white + "Eggdriver Console is now running")
    condition = True
    logged = False
    while condition:
        if command == None:
            i = get("egg")
        else:
            i = "$" + str(command)
            print(blue + "$egg> " + green + i + white + "executed")
            condition = False
        if i == "$nqs":
            from nqs import developerConsole
            developerConsole()
        elif i == "$new":
            from eggdriver.news import journalistConsole
            journalistConsole()
        elif i == "$login":
            logged = login()
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
            welcome()
        elif i == "$clear":
            clearConsole()
        elif i == "$end":
            print(white + "Eggdriver Console stopped running")
            return None
        else:
    	    pass