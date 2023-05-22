import pandas as pd
from carga_datos import cargador

def descripcion(datos :pd.DataFrame) -> pd.DataFrame:
  """
  Descripción estadística de los datos
  """
  salida = datos.describe(include = "all").T
  salida["Nulos"] = datos.isnull().sum()
  salida["Tipos"] = datos.dtypes
  return salida

if __name__ == "__main__":
  datos = cargador("C:\DataScience\ProyecosGitHub\LimpiezaDatos-1\hormigon.csv")
  print(descripcion(datos))