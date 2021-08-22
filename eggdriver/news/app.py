#Imports
from eggdriver.news.news import New
from eggdriver.news.config import files, year
from eggdriver.resources.console import get
from eggdriver.resources.constants import *

def journalistConsole(condition: bool = True):
  print(white + "Journalist Console is now running")
  while condition:
    print(white + "Title:")
    title=get("new")
    print(white + "Day:")
    day=int(get("new"))
    print(white + "Month:")
    month=int(get("new"))
    new=New(title, day, month, year, files)
    print(white + "Tags:")
    tagsbycommas = get("new")
    new.tags = tagsbycommas.split(", ")
    print(white + "Content:")
    content = ""
    while True:
      i = get("new")
      if i == "$save":
        new.text = content
        new.add()
        break
      elif i[0] == "$":
        print(white + "Error: NQS could not found the command \"" + i + " \"")
      else:
        content += i + "\n"
    print(white + "Write $end to close the console")
    print(white + "Press enter key to write other new")
    command = get("new")
    if command == "$end":
      print(white + "Journalist Console stopped running")
      return "done"
		