###############################
wannaBuildRelease = False    ##     ** Build panel **
###############################     Set
import eggdriver as ed       ##         wannaBuildRelease = True 
if wannaBuildRelease:        ##     to build a new release!
    ed.buildEggdriver()      ##
###############################

# ed.header("uwu")

theta = ed.pi/3
print(ed.sin(theta), ed.cos(theta), ed.tan(theta))

p = ed.sin_serie
print(p.eval(theta))
ed.derive(p)
print(p.eval(theta))


c = ed.Matrix("""
| 1 1 2 3 4 |
| 0 1 2 3 4 |
| 1 1 2 3 4 |
| 1 1 2 3 4 |
| 1 1 2 3 4 |
""")
c.display()

a = ed.Vector("[ 1 2 3 4 5 6 30 0 9]")
a.display()
