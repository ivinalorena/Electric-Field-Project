from re import X
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle


def Campo(q, r0, x, y):
	v=((y-r0[0])**2+(x-r0[1])**2)**1.5
	return q * (y - r0[0])/v, q * (x - r0[1])/v

cte = 10**(-7)
X = np.linspace(-2.5, 2.5, 50)
Y = np.linspace(-2, 2, 50)
x, y = np.meshgrid(X, Y)

cargas=[]
distancia = 2
cargas_op = 20

for i in range (cargas_op):
    cargas.append((-5,(0,1)))
    cargas.append((5,(0,-1)))


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

ax.set_aspect('equal')
plt.show()

