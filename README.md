# LimpiezaDatos
Incluye archivos en Python para la limpieza de datos

## Mejoras pendientes
- Agregar modelo ARIMA para predecir series temporales.
- Crear método que diferencie la serie temporal.
    - Automáticamente debería estudiar estacionariedad. (¿DECORADORES?)
    - Si es estacional, debe graficar autocorrelación y autocorrelación parcial

- Introducir modelos de clasificación, regresión y clusterización
- Para Clasificador.py
    - Método para quitar nans
    - Se puede usar el metodo del boxplot para identificar los outliers.
    y eliminarlos por distancia con nº de rangos intercuartílicos a la mediana.
    - Meterle el normalizador de las series temporales
- Ordenar las cosas en carpetas