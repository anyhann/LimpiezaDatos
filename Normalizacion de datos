# Aquí tienes algunos ejemplos de código Python para normalizar datos y evitar errores de procesamiento:
# 1- Normalización Min-Max:
# La normalización Min-Max transforma los datos para que estén dentro de un rango específico, generalmente entre 0 y 1.

from sklearn.preprocessing import MinMaxScaler

# Crear un objeto de normalización Min-Max
scaler = MinMaxScaler()

# Datos de entrenamiento
train_data = [[2], [5], [10], [15]]

# Normalizar los datos de entrenamiento
normalized_train_data = scaler.fit_transform(train_data)

print(normalized_train_data)

# 2- Normalización Z-score:
# La normalización Z-score (o estandarización) transforma los datos de manera que tengan una media de 0 y una desviación estándar de 1.

from sklearn.preprocessing import StandardScaler

# Crear un objeto de normalización Z-score
scaler = StandardScaler()

# Datos de entrenamiento
train_data = [[2], [5], [10], [15]]

# Normalizar los datos de entrenamiento
normalized_train_data = scaler.fit_transform(train_data)

print(normalized_train_data)


# 3- Normalización por escala decimal:
# La normalización por escala decimal ajusta los datos moviendo el punto decimal para que estén dentro de un intervalo específico.

def decimal_scaling(data):
    max_value = max(data)
    num_digits = len(str(int(max_value))) - 1
    scaled_data = [x / (10 ** num_digits) for x in data]
    return scaled_data

# Datos de entrenamiento
train_data = [200, 500, 1000, 1500]

# Normalizar los datos de entrenamiento
normalized_train_data = decimal_scaling(train_data)

print(normalized_train_data)

# 4- Normalización por escala máxima absoluta:
# normalización por escala máxima absoluta ajusta los datos dividiéndolos por el valor máximo absoluto en el conjunto de datos.
# python

import numpy as np

# Datos de entrenamiento
train_data = np.array([[2], [5], [10], [15]])

# Normalizar los datos de entrenamiento por escala máxima absoluta
normalized_train_data = train_data / np.max(np.abs(train_data))

print(normalized_train_data)

# 5- Normalización por logaritmo:
# La normalización por logaritmo transforma los datos utilizando la función logarítmica.

import numpy as np

# Datos de entrenamiento
train_data = np.array([1, 10, 100, 1000])

# Normalizar los datos de entrenamiento por logaritmo
normalized_train_data = np.log(train_data)

print(normalized_train_data)

# 6- Normalización por rango:
# La normalización por rango ajusta los datos dividiéndolos por la diferencia entre el valor máximo y mínimo en el conjunto de datos.

import numpy as np

# Datos de entrenamiento
train_data = np.array([2, 5, 10, 15])

# Normalizar los datos de entrenamiento por rango
normalized_train_data = (train_data - np.min(train_data)) / (np.max(train_data) - np.min(train_data))

print(normalized_train_data)


