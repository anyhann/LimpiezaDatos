from Serie_temporal import SerieTemporal
from carga_datos import cargador

import os

# Carga del csv desde la carpeta de datos
def carga_csv(nombre_archivo, elimina_cols = []):
    main_file_path = os.path.abspath(__file__)
    datos = cargador(os.path.join(os.path.dirname(main_file_path), "datos", "vic_elec.csv"))
    for columna in elimina_cols:
        datos.drop(columna, axis=1, inplace= True)
    return datos


datos = carga_csv("vic_elec.csv", elimina_cols=["Date", "Unnamed: 0"])

serie = SerieTemporal(datos, "Time", "Demand")

serie.descripcion()

# Sección representaciones gráficas
"""
decision = input("¿Deseas ver la serie temporal?[S/N]: ")
if decision.lower() =="s":
    # serie.visualizar_serie()
    serie.grafica_interactiva()
"""

serie.normalizador()
print(serie.dataframe_normalizado)


"""
serie.completa_nans("Demand")
serie.completa_nans("Temperature")
serie.completa_nans("Holiday")
"""

"""
serie.descripcion()
serie.normalizador()
serie.descripcion()
#serie.grafica_interactiva()

input("")
"""


"""

serie.dataframe = serie.dataframe.drop(columns=['Unnamed: 0', "Date"])

# Gráfico de autocorrelación
#serie.grafico_auto(120)


"""

#serie = serie.rellenar_nan(indices_nan, metodo = "media")

# Gráfica interactiva
"""
df = serie.dataframe
data_columns = df.columns
column_name = data_columns[0]
data_sequence = df[column_name]
layout_temp = go.Layout(title='Serie Temporal', xaxis=dict(title='Fecha'),
                        yaxis=dict(title=column_name, color='royalblue', overlaying='y2')    )
fig = go.Figure(data=data_sequence, layout=layout_temp)
fig.show()

# Está en visualización de datos
serie.visualizacion_interactiva()

# Las 4 pruebas
resultado = serie.comprueba_AR()

# Diferenciación
serie_diferenciada = serie.diferenciacion()



# Modelos

"""
