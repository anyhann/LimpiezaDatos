# Gráfico de dispersión 3D animado con Plotly

"""
El gráfico generado en el ejemplo es un gráfico de dispersión en 3D animado utilizando la biblioteca Plotly. El gráfico muestra puntos en un espacio tridimensional con coordenadas x, y, y z.

Aquí hay una explicación paso a paso del código:

1- Se importan las bibliotecas necesarias: numpy para generar datos aleatorios, plotly.graph_objects para crear el gráfico y plotly.subplots para crear subtramas.

2- Se generan los datos iniciales aleatorios para las coordenadas x, y, z, el tamaño y el color de los puntos.

3- Se crea una figura y un gráfico de dispersión 3D utilizando make_subplots para crear una única subtrama con un tipo de gráfico de 'scatter3d'.

4- Se crea un objeto Scatter3d que representa los puntos en el gráfico de dispersión. Los argumentos x, y y z representan las coordenadas de los puntos. El modo 'markers' indica que se deben mostrar los puntos como marcadores. El objeto marker define el tamaño y el color de los puntos utilizando los datos generados anteriormente. Se utiliza la escala de colores 'Viridis' para asignar colores a los puntos.

5- El objeto Scatter3d se agrega a la figura.

6- Se define una función de actualización llamada update que generará nuevos datos para los puntos en cada cuadro de la animación. En este ejemplo, se generan nuevos conjuntos de datos aleatorios para las coordenadas x, y, z, el tamaño y el color de los puntos.

7- Se configura la animación especificando una lista de cuadros (frames) que contienen los nuevos datos para cada cuadro. En este caso, se generan 10 cuadros con nuevos conjuntos de datos aleatorios.

8- Se crea un diccionario animation que contiene los cuadros de la animación y otros parámetros como el intervalo entre cuadros y si la animación debe repetirse.

9- Se actualiza la configuración de la figura para agregar un menú de botones que permite reproducir la animación.

10- Finalmente, se muestra la figura animada utilizando el método show().

Al ejecutar el código, verás una animación que muestra puntos en un espacio tridimensional. Los puntos se actualizarán con nuevos conjuntos de datos aleatorios en cada cuadro de la animación, lo que creará un efecto de movimiento. Puedes ajustar los parámetros del código para personalizar la animación según tus necesidades.

"""

import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Datos iniciales
x = np.random.rand(100)
y = np.random.rand(100)
z = np.random.rand(100)
size = np.random.rand(100) * 100
color = np.random.rand(100)

# Crear figura y gráfico de dispersión 3D
fig = make_subplots(rows=1, cols=1, specs=[[{'type': 'scatter3d'}]])
scatter = go.Scatter3d(
    x=x, y=y, z=z,
    mode='markers',
    marker=dict(size=size, color=color, colorscale='Viridis')  # Utilizar escala de colores 'Viridis'
)
fig.add_trace(scatter)

# Función de actualización para animación
def update(frame):
    # Generar nuevos datos
    x_new = np.random.rand(100)
    y_new = np.random.rand(100)
    z_new = np.random.rand(100)
    size_new = np.random.rand(100) * 100
    color_new = np.random.rand(100)

    # Actualizar los datos del gráfico de dispersión
    scatter.x = x_new
    scatter.y = y_new
    scatter.z = z_new
    scatter.marker.size = size_new
    scatter.marker.color = color_new

# Configurar la animación
frames = [dict(data=[dict(x=x, y=y, z=z)] * 10) for x, y, z in zip(np.random.rand(10, 100),
                                                                   np.random.rand(10, 100),
                                                                   np.random.rand(10, 100))]
animation = dict(frames=frames, interval=200, repeat=True)

# Actualizar la figura con la animación
fig.update_layout(updatemenus=[dict(type='buttons',
                                   buttons=[dict(label='Play',
                                                 method='animate',
                                                 args=[None, animation])])])

# Mostrar la figura animada
fig.show()

