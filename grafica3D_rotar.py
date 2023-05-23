import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from carga_datos import cargador
import pandas as pd

def plot_surface(dataframe, x_column, y_column, z_column):
    # Crear figura y subplot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x = dataframe[x_column].values
    y = dataframe[y_column].values
    z = dataframe[z_column].values

    # Plot the 3D points
    ax.scatter(x, y, z)

    # Set labels for the axes
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()

    # Ejemplo de uso
if __name__ == "__main__":
    df = pd.DataFrame({'x': np.linspace(-4, 4, 50),
                        'y': np.linspace(-4, 4, 50),
                        'z': np.linspace(-4, 4, 50)})
    plot_surface(df, 'x', 'y', 'z')






