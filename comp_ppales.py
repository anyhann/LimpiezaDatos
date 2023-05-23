from carga_datos import cargador
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

datos = cargador("hormigon.csv")

# Mostrar las columnas existentes
print("Columnas disponibles:")
print(datos.columns)

#print("¿Qué columnas quiere eliminar:")
columnas_eliminar = input("Ingrese las columnas que desea eliminar (separadas por coma): ")
# Dividir las columnas ingresadas por coma y eliminar los espacios en blanco
if columnas_eliminar !="":
    columnas_eliminar = [columna.strip() for columna in columnas_eliminar.split(",")]
    # Eliminar las columnas del DataFrame
    datos = datos.drop(columns=columnas_eliminar)

# Mostrar el DataFrame resultante
print("DataFrame resultante:")
print(datos)

# Instancia el objeto PCA
pca = PCA(n_components=3) # Especifica el número de componentes principales que deseas obtener

# Aplica el PCA a los datos normalizados
principal_components = pca.fit_transform(datos)

# Crea un nuevo DataFrame con los componentes principales
datos_principal = pd.DataFrame(data=principal_components, columns=["PC1", "PC2","PC3"])
print(datos_principal)
