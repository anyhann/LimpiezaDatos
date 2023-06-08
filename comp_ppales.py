from carga_datos import cargador
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from LimpiezaDatos.graficos.grafica3D_rotar import plot_surface
import os
from selecciona_columnas import selecciona_columnas_numericas


def eliminar_columnas(datos):
    # Mostrar las columnas existentes
    print("Columnas disponibles:")
    print(datos.columns)
    columnas_eliminar = input("Ingrese las columnas que desea eliminar (separadas por coma): ")
    if columnas_eliminar !="":
        columnas_eliminar = [columna.strip() for columna in columnas_eliminar.split(",")]
        # Eliminar las columnas del DataFrame
        datos = datos.drop(columns=columnas_eliminar)
    return datos

def plot_rotable_pca(datos):
    """
    Reduce un dataset numérico a 3 componentes principales y lo grafica
    """
    pca = PCA(n_components=3) # Especifica el número de componentes principales que deseas obtener
    
    datos_limpios = eliminar_columnas(selecciona_columnas_numericas(datos))
    print(datos_limpios)
    # Aplica el PCA a los datos limpios
    principal_components = pca.fit_transform(datos_limpios)
    # Crea un nuevo DataFrame con los componentes principales
    datos_principal = pd.DataFrame(data=principal_components, columns=["PC1", "PC2","PC3"])
    return datos_principal
    plot_surface(dataframe=datos_principal, x_column="PC1", y_column="PC2", z_column="PC3")


if __name__ == "__main__":
    main_file_path = os.path.abspath(__file__)
    datos = cargador(os.path.join(os.path.dirname(main_file_path), "hormigon.csv"))
    plot_rotable_pca(datos)

    
    