from ast import BitXor
import numpy as np
import matplotlib.pyplot as plt

X = np.linspace (0,4,50)
Y = np.linspace (0,4,50)
X, Y = np.meshgrid(X, Y)

Ex =(1/(2*np.pi) *-(X - 1)/((X - 1)**2 + (Y - 3)**2))+(1/(2*np.pi) *(X - 3)/((X - 3)**2 + (Y - 3)**2))
Ey = (1/(2*np.pi) *(Y - 1)/((X - 1)**2 + (Y - 1)**2))+(1/(2*np.pi) *-(Y - 1)/((X - 3)**2 + (Y - 1)**2))

V = X
B = Y
fig = plt.figure()
ax = fig.add_subplot()

ax.streamplot(X,Y,Ex,Ey,arrowsize=1,linewidth=1, arrowstyle='->')

Z = np.sqrt(Ex ** 2 + Ey ** 2)

plt.scatter(1, 1, s=150,color = 'green')
plt.scatter(3, 1, s=150,color = 'red')
plt.scatter(3, 3, s=150,color = 'green')
plt.scatter(1, 3, s=150,color = 'red')
plt.contour(X,Y,Z,levels=[-1,0,1])
plt.contour(X,Y,V, levels=[2])
plt.contour(X,Y,B,levels=[2])


ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_xlim(0,4)
ax.set_ylim(0,4)
ax.set_aspect('equal')

plt.show()
