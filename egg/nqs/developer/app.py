from egg.nqs.developer.run import run
from egg.nqs.core import compile
from egg.resources.extensions import nqa
from egg.resources.console import display, get, sleep
from egg.resources.constants import *

def developerDisplay(name: str):
    content=nqa.read(name)
    display(content)

def developerConsole(condition: bool = True):
  print(white+"Developer Console is now running")
  while condition:
    i=get("nqs")
    name="temp_compile"
    if i=="$display":
      content=nqa.read(name)
      print(white+content)
    elif i=="$compile":
      compile(name)
    elif i=="$save":
      print(white+"Save as:")
      adress=get("nqs")
      content=nqa.read(name)
      nqa.write(content,adress)
    elif i=="$run":
      run(name)
    elif i=="$delay":
      print(white+"How many milliseconds?")
      delta=get("nqs")
      sleep(int(delta))
    elif i=="$end":
      try:
        nqa.delete(name)
      except:
        pass
      print(white+"Developer Console stopped running")
      return "done"
    else:
    	nqa.append(i+"\n",name)