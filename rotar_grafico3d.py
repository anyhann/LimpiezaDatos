import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = np.linspace(-4,4,50)  #"linspace" -> Es la escala de la cuadricula.
y = np.linspace(-4,4,50)
X, Y = np.meshgrid(x,y)
def z(x,y):
    return np.sin(np.sqrt(x**2+y**2)) #Aquí hay que escribir la formula matematica: Seno.
    return np.cos(np.sqrt(x**2+y**2)) #Aquí hay que escribir la formula matematica: Coseno.
    return np.sin(np.sqrt(x**2+y**2)) #Aquí hay que escribir la formula matematica: Seno, Coseno, Tangente
plt.show()