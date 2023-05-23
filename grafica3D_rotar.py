import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from carga_datos import cargador
import pandas as pd

def plot_surface(dataframe, x_column, y_column, z_column):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x = dataframe[x_column].values
    y = dataframe[y_column].values
    X, Y = np.meshgrid(x, y)

    def z(x, y):
        return dataframe[z_column].values

    ax.contourf(X, Y, z(X, Y))
    plt.show()

    # Ejemplo de uso
if __name__ == "__main__":
    df = pd.DataFrame({'x': np.linspace(-4, 4, 50),
                        'y': np.linspace(-4, 4, 50),
                        'z': np.sin(np.linspace(-4, 4, 50))})






