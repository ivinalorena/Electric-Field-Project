import plotly.graph_objects as go
import numpy as np
import matplotlib.pyplot as plt

N =40
x = np.linspace(-1,1 , N)
y = np.linspace(-1, 1, N)
X, Y = np.meshgrid(x, y)

u = (1/(2*np.pi) *(X - 0)/((X - 0)**2 + (Y - 0)**2))#+(1/(2*np.pi) *(X - 0)/((X - 0)**2 + (Y - 0)**2))
v = (1/(2*np.pi) *(Y - 0)/((X - 0)**2 + (Y - 0)**2))#+(1/(2*np.pi) *(Y - 0)/((X - 0)**2 + (Y - 0)**2))

plt.figure()
plt.streamplot(x,y,u,v,arrowsize=1,linewidth=1, arrowstyle='->')
Z = np.sqrt(u ** 2 + v ** 2)
V = X
plt.scatter(0, 0, s=250,color = 'green')
plt.contour(X,Y,Z)
plt.show()

