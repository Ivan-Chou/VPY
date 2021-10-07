import vpython as vp

#====================

g = vp.vec(0,-9.8,0) # ↓

r = 0.5 # radius of the ball

dt = 0.001

#====================

scene = vp.canvas(center=vp.vec(0,10,0), width=800, height=600, background=vp.color.cyan)
floor = vp.box(pos=vp.vec(0, -0.01, 0), size=vp.vec(30,0.02,30), color=vp.color.blue)
ball = vp.sphere(pos=vp.vec(-15, 20, 0), radius=r, color=vp.color.red)

ball.v = vp.vec(2,0,0)

while ball.pos.x <= 15:
	
	vp.rate(1000)

	ball.v += g*dt
	ball.pos += ball.v*dt

	if (ball.pos.y<=(0+r))and(ball.v.y<0):
		ball.v.y = -ball.v.y

