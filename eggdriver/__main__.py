from eggdriver.app import eggConsole
import sys

for command in sys.argv[1:]:
    if command == "console":
        eggConsole()
    else:
        try:
            eggConsole(str(command))
        except:
            print("Error: Please write the command accurately")
