import numpy as np
import matplotlib as plt

def metodo_interpolacion_serie_temporal(dataframe, columna_valores, columnas):
    for columna in columnas:
        # Cuando tenemos la serie temporal en el índice
        metodo_resample = input("¿Qué método quieres para hacer el resample?: ")
        # 'linear', 'bfill', 'ffill', 'polynomial'
        if metodo_resample == 'polynomial':
            num_orders = int(input("Indique el grado polinómico: "))
            dataframe = dataframe.interpolate(method=metodo_resample, order=num_orders)
        else:
            dataframe = dataframe.interpolate(method=metodo_resample)
    
    # Hacer la transformación logarítmica en caso necesario
    for columna in columnas:
        trans_log = int(input("¿Quieres hacer la transformación logarítmica? No(0)/Sí(1): "))
        if trans_log == 1:
            dataframe[columna] = np.log(dataframe[columna])
    
    # Mostrar el gráfico de la serie de tiempo original
    plt.figure(figsize=(8, 4))
    plt.plot(dataframe[columna_valores], marker='o')
    plt.title('Serie de Tiempo Original')
    plt.xlabel('Fecha')
    plt.ylabel('Valor')
    plt.show()

    
    
