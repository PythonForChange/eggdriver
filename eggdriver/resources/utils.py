import json, math

def dump(structure, file):
  json.dump(structure, file, indent=2)

def floor(f: float):
  return math.floor(f)

def colour(id: int,bgcolor:int =0):
  if bgcolor!=0:
    return "\033[1;"+str(id)+";"+str(bgcolor+10)+"m "
  return "\033[1;"+str(id)+"m"
