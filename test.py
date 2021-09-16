###############################
wannaBuildRelease = False   ##     ** Build panel **
###############################     Set
import eggdriver as ed       ##         wannaBuildRelease = True 
if wannaBuildRelease:        ##     to build a new release!
    ed.buildEggdriver()      ##
###############################

ed.sysCommand("-m build --sdist")
ed.sysCommand("-m build --wheel")
ed.sysCommand("-m twine check dist/*")
ed.sysCommand("-m twine upload dist/*")

print(ed.ver)

c = ed.Matrix("""
| 1 1 2 3 4 |
| 0 1 2 3 4 |
| 1 1 2 3 4 |
| 1 1 2 3 4 |
| 1 1 2 3 4 |
""", 4, 5)
c.display()

a = ed.Vector("[ 1 2 3 4 5 6 30 0 9]")
a.display()

w = ed.WEBCAM("Emmanuel")
w.default(background_effects= [(ed.blur, [])], effects = [(ed.changeBackground, [ed.solidBackground()])])