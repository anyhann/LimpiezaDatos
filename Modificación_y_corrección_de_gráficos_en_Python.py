# 1- Modificación de títulos y etiquetas de los ejes :
# Este código permite modificar los títulos y etiquetas de los ejes de un gráfico utilizando la biblioteca Matplotlib.

import matplotlib.pyplot as plt

# Datos
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

# Crear el gráfico
plt.plot(x, y)

# Modificar el título y las etiquetas de los ejes
plt.title("Título del gráfico")
plt.xlabel("Eje de las abscisas")
plt.ylabel("Eje de las ordenadas")

# Mostrar el gráfico
plt.show()



# 2- Corrección de escalas de los ejes:
# Este código permite corregir las escalas de los ejes de un gráfico utilizando las funciones set_xlim() y set_ylim() de Matplotlib.

import matplotlib.pyplot as plt

# Datos
x = [1, 2, 3, 4, 5]
y = [100, 1000, 10000, 100000, 1000000]

# Crear el gráfico
plt.plot(x, y)

# Corregir las escalas de los ejes
plt.xlim(0, 6)
plt.ylim(0, 1200000)

# Mostrar el gráfico
plt.show()



# 3- Modificación del estilo del gráfico:
# Este código permite modificar el estilo de un gráfico utilizando las diferentes opciones de estilo de Matplotlib.

import matplotlib.pyplot as plt

# Datos
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

# Crear el gráfico
plt.plot(x, y)

# Modificar el estilo del gráfico
plt.style.use('seaborn-darkgrid')  # Cambiar el estilo
plt.grid(True)  # Mostrar la cuadrícula
plt.legend(['Curva 1'])  # Leyenda

# Mostrar el gráfico
plt.show()


# 4- Adición de anotaciones:
# Este código permite agregar anotaciones a un gráfico utilizando la función annotate() de Matplotlib.

import matplotlib.pyplot as plt

# Datos
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

# Crear el gráfico
plt.plot(x, y)

# Agregar una anotación
plt.annotate('Punto importante', xy=(3, 15), xytext=(4, 20),
             arrowprops=dict(facecolor='black', arrowstyle='->'))

# Mostrar el gráfico
plt.show()


# 5- Cambio de colores y estilos de línea:
# Este te permite cambiar los colores y estilos de línea de un gráfico utilizando la función plot() de Matplotlib.
# python.

import matplotlib.pyplot as plt

# Datos
x = [1, 2, 3, 4, 5]
y1 = [10, 20, 15, 25, 30]
y2 = [5, 15, 10, 20, 25]

# Crear el gráfico
plt.plot(x, y1, color='blue', linestyle='dashed', label='Curva 1')
plt.plot(x, y2, color='red', linestyle='solid', label='Curva 2')

# Modificar leyendas y título
plt.legend()
plt.title('Gráfico con colores y estilos de línea')

# Mostrar el gráfico
plt.show()



# 6- Cambio de tipo de gráfico:
# Este código te permite cambiar el tipo de gráfico, por ejemplo, de línea a dispersión, utilizando la función scatter() de Matplotlib.

import matplotlib.pyplot as plt

# Datos
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

# Crear el gráfico de dispersión
plt.scatter(x, y, color='green', marker='o')

# Modificar título y etiquetas de los ejes
plt.title('Gráfico de dispersión')
plt.xlabel('Eje de las abscisas')
plt.ylabel('Eje de las ordenadas')

# Mostrar el gráfico
plt.show()


# 7- Creación de subgráficos:
# Este código te permite crear import matplotlib.pyplot as plt

import matplotlib.pyplot as plt
import numpy as np

# Datos
x = np.linspace(0, 2 * np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Crear subgráficos
plt.subplot(2, 1, 1)
plt.plot(x, y1)
plt.title('Subgráfico 1: Seno')

plt.subplot(2, 1, 2)
plt.plot(x, y2)
plt.title('Subgráfico 2: Coseno')

# Ajustar espacio entre subgráficos
plt.subplots_adjust(hspace=0.5)

# Mostrar los subgráficos
plt.show()



# 8- Guardar el gráfico en un archivo:
# Este código te permite guardar el gráfico en un archivo en lugar de mostrarlo en pantalla, utilizando la función savefig() de Matplotlib.

import matplotlib.pyplot as plt

# Datos
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

# Crear el gráfico
plt.plot(x, y)

# Modificar título y etiquetas de los ejes
plt.title('Gráfico de línea')
plt.xlabel('Eje de las abscisas')
plt.ylabel('Eje de las ordenadas')

# Guardar el gráfico en un archivo PNG
plt.savefig('grafico.png')

# Mostrar mensaje de confirmación
print('Gráfico guardado exitosamente.')






