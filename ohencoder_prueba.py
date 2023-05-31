import os
import pandas as pd
from ohencoder_clase import DataFrameTransformer


# Crear una instancia de la clase DataFrameTransformer
transformer = DataFrameTransformer()

# Obtener la ruta completa del archivo
main_file_path = os.path.abspath(__file__)
archivo = os.path.join(os.path.dirname(main_file_path), "Corredores Latinos con Categorías.csv")

# Cargar el DataFrame desde el archivo
transformer.cargar_dataframe(archivo)

opciones = transformer.elige_opcion()

# Transformar el DataFrame
#transformed_df = transformer.transform_dataframe()
#print(transformed_df)

# llama al método crea_dummies
#dummies_df = transformer.crea_dummies()
#print(dummies_df)


