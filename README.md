# LimpiezaDatos
Incluye archivos en Python para la limpieza de datos

## Tareas realizadas

### Serie Temporal
    - Creación de la clase con su iniciador (convertir en serie temporal) private
    - Normalizar las columnas numéricas eligiendo el normalizador.
    - Interpolación de los valores perdidos 
    - Gráficos interactivos de la serie temporal
    - 


## Mejoras pendientes
- Agregar modelo AR para predecir series temporales.
    - (Está en el archivo de la teoría 01 Demanda energía eléctrica.ipynb)
- Crear método que diferencie la serie temporal.
    - Automáticamente debería estudiar estacionariedad. (¿DECORADORES?)
    - Si es estacionaria, debe graficar autocorrelación y autocorrelación parcial


- Introducir modelos de clasificación, regresión y clusterización
- Para Clasificador.py
    - Método para quitar nans
    y eliminarlos por distancia con nº de rangos intercuartílicos a la mediana.
    - Meterle el normalizador de las series temporales
- Ordenar las cosas en carpetas
