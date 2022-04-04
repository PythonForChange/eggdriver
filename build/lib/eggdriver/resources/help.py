from eggdriver.resources.constants import white
from eggdriver.resources.extensions import py, wf

def welcome():
    """Get help from Egg"""
    T = """
                      _      _                
                     | |    (_)               
  ___  __ _  __ _  __| |_ __ ___   _____ _ __ 
 / _ \/ _` |/ _` |/ _` | '__| \ \ / / _ \ '__|
|  __/ (_| | (_| | (_| | |  | |\ V /  __/ |   
 \___|\__, |\__, |\__,_|_|  |_| \_/ \___|_|   
       __/ | __/ |                            
      |___/ |___/                             

    
Welcome to eggdriver:

The Egg-cosystem console
    
"""
    T += py.read("eggdriver/library/commands")
    T += wf.read("license")
    print(white + T)
    return "done"