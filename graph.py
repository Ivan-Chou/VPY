import vpython as vp

scene1 = vp.canvas(width=200, align="left", background=vp.vec(0,0.5,0.5))
scene2 = vp.canvas(width=300, height=300, align="left", background=vp.vec(0.5,0.5,0))
vp.box(canvas=scene1)
vp.sphere(canvas=scene2)

oscillation = vp.graph(width=450, align="right")
f1 = vp.gcurve(graph=oscillation, width=4, color=vp.color.blue)
f2 = vp.gvbars(graph=oscillation, delta=4, color=vp.color.red)
f3 = vp.gdots(graph=oscillation, size=3, color=vp.color.orange)

t=1
while t<80:
	vp.rate(20)

	f1.plot(pos=(t, 5.0+5.0*vp.cos(-0.2*t)*vp.exp(0.015*t)))
	f2.plot(pos=(t, 2.0+5.0*vp.cos(-0.1*t)*vp.exp(0.015*t)))
	f3.plot(pos=(t, 5.0*vp.cos(-0.03*t)*vp.exp(0.015*t)))

	t += 1