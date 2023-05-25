
import pandas as pd
import os

def obtener_separador():
    separador = input("Separador utilizado [,]:")
    if len(separador)==0:
        separador = ","
    return separador

def cargador(ubicacion):
    """
    Cargador de datos
    """
    if ubicacion[-4:] == ".csv":
        datos = pd.read_csv(ubicacion, sep = obtener_separador())
    elif ubicacion[:5]=="http":
        datos = pd.read_csv(ubicacion, sep = obtener_separador())  
    else:
        pd.read_excel(ubicacion)
    print(datos.head(10))
    print("Cargado Dataframe de dimensiones", datos.shape)
    return datos

def juntar_csvs(path, files):
    df = pd.DataFrame()
    separador = obtener_separador()

    for file in files:
        if file.endswith(".csv"):  # solo cargar archivos con extensión .csv
            path_file = os.path.join(path, file)
            data = pd.read_csv(path_file, sep=separador)
            df = pd.concat([df, data])

    return df


if __name__ == "__main__":
    main_file_path = os.path.abspath(__file__)
    #datos = cargador(os.path.join(os.path.dirname(main_file_path), "hormigon.csv"))
    datos = cargador("https://raw.githubusercontent.com/JoaquinAmatRodrigo/skforecast/master/data/vic_elec.csv")
    #listado_archivos = ["winequality-red.csv", "winequality-white.csv"] 
    #csv_unidos = juntar_csvs(os.path.dirname(main_file_path), listado_archivos)
    #print(csv_unidos)