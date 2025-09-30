from vpython import *
#Web VPython 3.2
# rotating_cube_vpython.py
from vpython import box, vector, rate, color, scene

scene.title = "Rotating Cube — VPython"
scene.width = 800
scene.height = 600

cube = box(size=vector(2,2,2), color=color.cyan, shininess=1)

# rotate continuously
while True:
    rate(60)                      # caps loop at 60 iterations/sec
    cube.rotate(angle=0.02, axis=vector(0,1,0))   # rotate about Y
    cube.rotate(angle=0.01, axis=vector(1,0,0))   # rotate about Y
    cube.rotate(angle=0.01, axis=vector(0,0,1))   # slight X rotation