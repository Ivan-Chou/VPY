import vpython as vp

scene = vp.canvas(center=vp.vec(0,0,0), width=800, height=600, background=vp.color.cyan)
directA = vp.arrow(pos=vp.vec(0,0,0), axis=vp.vec(1,1,0), color=vp.color.yellow, shaftwidth=0.05)
directB = vp.arrow(color=vp.color.green, shaftwidth=0.05)

directB.pos = directA.pos + directA.axis
directB.axis = vp.vec(3,-2,0)

directC = vp.arrow(color=vp.color.blue, shaftwidth=0.05)
directC.pos = directA.pos
directC.axis = directA.axis + directB.axis