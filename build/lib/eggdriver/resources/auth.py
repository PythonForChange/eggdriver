from eggdriver.resources.console import get
from eggdriver.resources.constants import white
from eggdriver.resources.extensions import py

def login():
    print(white + "Username:")
    u = get("egg")
    logged = False
    try:
        from eggconfig import username, password
        if u == username:
            print(white + "Password:")
            p = get("egg")
            if p == password:
                logged = True
                print(white + "Done") 
    except ImportError:
        print(white + "Please create a eggconfig.py file in your current directory and execute $register command into EggConsole")
    except:
        print(white + "Error")
    return logged

def register():
    try:
        print(white + "Username:")
        username = get("egg")
        print(white + "Password:")
        password = get("egg")
        text = f"username, password = \"{username}\", \"{password}\""
        py.append(text, "eggconfig")
        print(white + "Done")
    except:
        print(white + "Error")