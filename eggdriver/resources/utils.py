import json

def dump(structure, file):
	"""Dump a structure to a json file"""
	json.dump(structure, file, indent = 4)

def colour(id: int, bgcolor: int = 0):
	if bgcolor != 0:
		return "\033[1;" + str(id) + ";" + str(bgcolor + 10) + "m "
	return "\033[1;" + str(id) + "m"

def indexes(x):
    return range(0, len(x))

"""Beatiful comments"""

def header(title):
	return f"""###############################
##     ** {title} **     ##
###############################"""

build_panel = """###############################
wannaBuildRelease = False    ##     ** Build panel **
###############################     Set
import eggdriver as ed       ##         wannaBuildRelease = True 
if wannaBuildRelease:        ##     to build a new release!
    ed.buildEggdriver()      ##
###############################"""

def comment(file):
	"""for line in py.getLines(file):
		text = line.split("#")
		commentary = text[1] 
		if commentary.split(" ")[0] == "$doc":
			commentary = 3 * "\"" + commentary[5:] + 3 * "\""           """