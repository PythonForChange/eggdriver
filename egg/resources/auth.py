from egg.resources.console import get
from egg.resources.constants import white
from egg.resources.extensions import py

def login():
    print(white+"Username:")
    j=get("egg")
    try:
        from user.private import username,password
        if j==username:
            print(white+"Password:")
            k=get("egg")
            if k==password:
                logged=1
                print(white+"Done") 
    except:
        pass

def register():
    try:
        print(white+"Username:")
        j=get("egg")
        print(white+"Password:")
        k=get("egg")
        py.write("user/private","username,password=\"username\",\"password\"")
        print(white+"Done")
    except:
        pass 