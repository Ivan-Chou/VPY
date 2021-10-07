import vpython as vp

g = -9.8   # 重力加速度(↓)
r = 0.25   # ball radius
h = 20.0   # h0 of the ball

scene = vp.canvas(title="Free Fall", width=800, height=800, center=vp.vec(0,h/2.0,0), background=vp.color.cyan)
ball = vp.sphere(pos=vp.vec(0,h,0), color=vp.color.red ,radius=r, make_trail=True, trail_radius=0.05)
floor = vp.box(pos=vp.vec(0,0,0), color=vp.color.blue, size=vp.vec(30,0.3,10))
msg = vp.text(pos=vp.vec(-15,25,0), text="Free Fall")

ball.v=vp.vec(0,0,0)

dt = 0.001

while ball.pos.y >= (r + floor.size.y/2):
	vp.rate(1000)

	ball.pos += ball.v*dt
	ball.v.y += g*dt
	
msg.visible = False
msg = vp.text(pos=vp.vec(-15, 25, 0), text="The final velocity : "+str(ball.v.y))
print(ball.v.y)