from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from carga_datos import obtener_separador, cargador
from sklearn.preprocessing import StandardScaler




#grafico para sacar el gráfico del codo para después utilizar modelos de clustering 
#Nos da a elegir datos normalizados o no-normalizados
#Si hay datos contienen valores NANs hay que tratarlos previamente para que se ejecute la funcion correctamente.

def grafica_codo():
    ubicacion = input("Ingrese la ubicación del archivo: ")
    dataset = cargador(ubicacion)
    # Ignoramos las variables no-numéricas
    dataset_num = dataset.select_dtypes(include=['number'])
    
    normalizar = int(input("Normalizar datos (1: Sí / 2: No): "))
    if normalizar == 1:
        scaler = StandardScaler()
        dataset_num= scaler.fit_transform(dataset_num)
    else:
      pass
    
    clusters = []

    for i in range(1, 11):
        km = KMeans(n_clusters=i).fit(dataset_num)
        clusters.append(km.inertia_)
    #Graficamos el codo
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.lineplot(x=list(range(1, 11)), y=clusters, ax=ax)
    ax.set_title('Codo de inercia decreciente')
    ax.set_xlabel('Clusters')
    ax.set_ylabel('Inercia')
    plt.show()
    


