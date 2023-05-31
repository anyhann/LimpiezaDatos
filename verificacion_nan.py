import pandas as pd
import os
from carga_datos import cargador
from carga_serie_temporal import conversion_a_serie_temp

def verifica_nan(dataframe):
    rango_completo = pd.date_range(
    start = dataframe.index.min(),
    end = dataframe.index.max(),
    freq = dataframe.index.freq)
    
    verificacion = (dataframe.index == rango_completo).all()
    if verificacion == True:
        print("No hay valores nulos")
    else:
        print("Hay valores nulos")
    return verificacion



if __name__ == "__main__":
    main_file_path = os.path.abspath(__file__)
    datos = cargador(os.path.join(os.path.dirname(main_file_path), "datos", "vic_elec.csv"))
    datos = conversion_a_serie_temp(datos, "Time")
    print(datos.index)
    datos = verifica_nan(datos)