###############################
wannaBuildRelease = False    ##     ** Build panel **
###############################     Set
import eggdriver as ed       ##         wannaBuildRelease = True 
if wannaBuildRelease:        ##     to build a new release!
    ed.buildEggdriver()      ##
###############################

ed.eggConsole()

# ed.header("uwu")

def g(x):
    return x**2

j = ed.derivative(g)
print(ed.derivative(g), j, ed.derivative(g)(0), j(0))

theta = ed.pi/3
print(ed.sin(theta), ed.cos(theta), ed.tan(theta))

p = ed.Polynomial("6 +x^2 +x^9 -5x^7")
p.display()
dp = ed.derive(p)
dp.display()

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
