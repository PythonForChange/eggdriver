###############################
wannaBuildRelease = False    ##     ** Build panel **
###############################     Set
from eggdriver import build  ##         wannaBuildRelease = True 
if wannaBuildRelease:        ##     to build a new release!
    build()                  ##
###############################

from eggdriver import  Matrix, Vector, build

c = Matrix("""
| 1 1 2 3 4 |
| 0 1 2 3 4 |
| 1 1 2 3 4 |
| 1 1 2 3 4 |
| 1 1 2 3 4 |
""", 4, 5)
c.display()

a = Vector("[ 1 2 3 4 5 6 30 0 9]")
a.display()

