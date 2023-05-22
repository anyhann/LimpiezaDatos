
import pandas as pd
import os

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
    datos = cargador("/home/laptop/Proyectos Python/LimpiezaDatos/laliga_22-23.csv")