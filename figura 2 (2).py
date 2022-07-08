import numpy as np
import matplotlib.pyplot as plt


X,Y = np.meshgrid(np.arange(-3,3,.2), np.arange(-2,2,.2) )
Ex = (X + 1)/((X+1)**2 + Y**2)**2 - (X - 1)/((X-1)**2 + Y**2)**2
Ey = Y/((X+1)**2 + Y**2)**2 - Y/((X-1)**2 + Y**2)**2
	
Z = np.sqrt(Ex ** 2 + Ey ** 2)
V = X


fig = plt.figure()
plt.streamplot(X,Y,Ex,Ey,arrowsize=1,linewidth=1, arrowstyle='->')
plt.scatter(1, 0, s=250,color = 'green')
plt.scatter(-1, 0, s=250,color = 'red')
plt.contour(X,Y,Z, levels=[-25,-18,-8,-4,-2,-1,3,10,30])
plt.contour(X,Y,V, levels=[0])

plt.show()