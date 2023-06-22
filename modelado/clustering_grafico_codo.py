from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from LimpiezaDatos.utilidades.carga_datos import obtener_separador, cargador
from selecciona_columnas import selecciona_columnas_numericas
from sklearn.preprocessing import StandardScaler
from LimpiezaDatos.transformaciones.normalizador import normalizador


def grafica_codo():
    """
    Grafico para sacar el gráfico del codo para después utilizar modelos de clustering 
    Nos da a elegir datos normalizados o no-normalizados
    Si hay datos contienen valores NANs hay que tratarlos previamente para que se ejecute la funcion correctamente.
    """
    ubicacion = input("Ingrese la ubicación del archivo: ")
    dataset = cargador(ubicacion)
    # Selecciona variables numéricas
    dataset= selecciona_columnas_numericas(dataset)
    
    normalizar = int(input("Normalizar datos (S: Sí / N: No): "))
    if normalizar.upper() == "S":
        normalizador(dataset)
    
    clusters = []
    for i in range(1, 11):
        km = KMeans(n_clusters=i).fit(dataset)
        clusters.append(km.inertia_)
    #Graficamos el codo
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.lineplot(x=list(range(1, 11)), y=clusters, ax=ax)
    ax.set_title('Codo de inercia decreciente')
    ax.set_xlabel('Clusters')
    ax.set_ylabel('Inercia')
    plt.show()


