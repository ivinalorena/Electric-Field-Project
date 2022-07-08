import numpy as np
import matplotlib.pyplot as plt

def Campo(q, r0, x, y):
	v=((y-r0[1])**2+(x-r0[0])**2)**1.5
	return q * (y - r0[1])/v, q * (x - r0[0])/v

X = np.linspace(-0.5, 0.5, 50)
Y = np.linspace(-1.5, 1.5, 50)
X, Y = np.meshgrid(X, Y)


distancia = 1.5
cargas_op = 20

cargas=[]

for i in range (cargas_op):
    cargas.append((5,(i/(cargas_op-1)*2-1, -distancia/2)))
    cargas.append((-5,(i/(cargas_op-1)*2-1, distancia/2)))

#criar o vetor
Ex = (1/(2*np.pi)*(X-0)/((X-0)**2 + (Y-0)**2))
Ey = (1/(2*np.pi)*(Y-0)/((X-0)**2 + (Y-0)**2)) 

for carga in cargas:
    ex,ey = Campo(*carga, x=Y, y=X)
    Ex+=ex
    Ey+=ey


Z = np.sqrt(Ex ** 2 + Ey ** 2)

fig = plt.figure()
ax = fig.add_subplot()
V = X
ax.contour(X,Y,V, levels=[0])
ax.contour(X,Y,Z)


ax.streamplot(X,Y,Ex,Ey,arrowsize=1,linewidth=1, arrowstyle='->')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_aspect('equal')
plt.show()
