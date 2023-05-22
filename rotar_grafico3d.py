import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = np.linspace(-4,4,50)
y = np.linspace(-4,4,50)
X, Y = np.meshgrid(x,y)
def z(x,y):
    return np.sin(np.sqrt(x**2+y**2))

ax.contourf(X,Y,z(X,Y))
plt.show()