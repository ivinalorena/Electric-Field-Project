import numpy as np
import matplotlib.pyplot as plt


cte = 10**(-7)
a = np.linspace (-1,1,10)
b = np.linspace (-0.8,0.8,10)
x,y =np.meshgrid(a,b)

Bx = (-cte*y/(x**2+y**2))
By = (cte*x/(x**2+y**2))


fig = plt.figure()
ax = fig.add_subplot()

ax.streamplot(a,b,Bx,By,arrowsize=1,linewidth=1, arrowstyle='->')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_aspect('equal')
plt.show()



