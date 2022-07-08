from re import X
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle


def Campo(q, r0, x, y):
	v=((y-r0[1])**2+(x-r0[0])**2)**1.5
	return q * (y - r0[1])/v, q * (x - r0[0])/v

cte = 10**(-7)
x,y = np.meshgrid(np.arange(-4,4,.2), np.arange(-4,4,.2))
cargas=[]

for i in range (-20,20,1):
    cargas.append((20,(-0.50,i/10)))
    cargas.append((-20,(0.50,i/10)))


Bx =(-cte*x/(x**2+y**2))
By =(cte*y/(x**2+y**2))

for carga in cargas:
    ex,ey = Campo(*carga, x=x, y=y)
    Bx += (-cte*ex/(x**2+y**2))
    By += (cte*ey/(x**2+y**2))

fig = plt.figure()
ax = fig.add_subplot()
ax.streamplot(x,y,Bx,By,arrowsize=1,linewidth=1, arrowstyle='->')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_xlim(-4,4)
ax.set_ylim(-4,4)
ax.set_aspect('equal')
plt.show()

