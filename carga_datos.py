
import pandas as pd

def cargador(ubicacion):
    if ubicacion[-4:] == ".csv":
        separador = input("Separador utilizado [,]:")
        if len(separador)==0:
            separador = ","
        datos = pd.read_csv(ubicacion, sep = separador)
    else:
        pd.read_excel(ubicacion)
    print("Cargado Dataframe de dimensiones", datos.shape)
    print(datos.head(10))
    return datos

if __name__ == "__main__":
    datos = cargador("C:\DataScience\ProyecosGitHub\LimpiezaDatos-1\hormigon.csv")