from eggdriver.resources.console import sleep

class New():
  def __init__(self, title: str, day: int, month: int, year: int = 2021, files = ["README.md"]):
    self.title = title
    if day < 10:
      newday = "0" + str(day)
    else:
      newday = str(day)
    if month < 10:
      newmonth = "0" + str(month)
    else:
      newmonth = str(month)
    self.date = newmonth + "/" + newday + "/" + str(year)
    self.place = "Santiago, Chile"
    self.text = ""
    self.tags = []
    self.files = files
  def tag(self, text: str):
    try:
      self.tags.append(text)
    except:
      print("A tagging bug was happen")
  def format(self):
    t = "\n### " + self.title + "\n#### " + self.date + " " + self.place
    t += "\n##### Tags: "
    try:
      for i in self.tags:
        t += "[" + i + "](https://github.com/topics/" + i + ")"
    except:
      pass
    t += "\n" + self.text + "\n"
    return t
  def add(self):
    try:
      T = self.format()
      try:
        for i in self.files:
          f = open(i,"a")
          f.write(T)
          print("Writting the new in " + i)
          sleep(100)
          f.close()
        print("New added succesfully")
        print("Title: " + self.title)
        print("Date: " + self.date)
        print("Content: " + preview(self.text.split()))
      except:
        print("A writting bug was happen")
    except:
      print("A formatting bug was happen")
    
def preview(string: str):
  preview = ""
  try:
    preview += string[0]
  except:
    pass
  try:
    preview += " " + string[1]
  except:
    pass
  try:
    preview += " " + string[2]
  except:
    pass
  try:
    preview += " "+ string[3]
  except:
    pass
  preview += "..."
  return preview