from pylab import *

data = open("out.log","r").readlines()
u,v = [],[]
for i in data:
	c = i.split("\t")
	u.append(c[0])
	v.append(c[1])

t = arange(0.0, 2.0, 0.01)
s = sin(2*pi*t)
plot(u, v)

xlabel('time (s)')
ylabel('concentration (mmol/L)')
title('un seul produit')
grid(True)
savefig("test.png")
show()
