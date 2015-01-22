import numpy as np
import matplotlib.pyplot as plt
import sys


data = open(sys.argv[1],"r").readlines()
u,v,x,y,z,a = [],[],[],[],[],[]
for i in data:
	c = i.split("\t")
	u.append(c[0])
	v.append(c[1])
	x.append(c[2])
	y.append(c[3])
	z.append(c[4])
	a.append(c[5])

# Create plots with pre-defined labels.
plt.plot(u, v, label='Product A')
plt.plot(u, x, label='Product B')
plt.plot(u, y, label='Product C')

legend = plt.legend(loc='upper center', shadow=True, fontsize='x-large')
# Put a nicer background color on the legend.
legend.get_frame().set_facecolor('#00FFCC')

# Put a nicer background color on the legend.

plt.show()
