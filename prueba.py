from Serie_temporal import SerieTemporal
from carga_datos import cargador

import os

main_file_path = os.path.abspath(__file__)
datos = cargador(os.path.join(os.path.dirname(main_file_path), "datos", "vic_elec_nans.csv"))
datos.drop("Date", axis=1, inplace= True)
datos.drop("Unnamed: 0", axis=1, inplace= True)

serie = SerieTemporal(datos, "Time", "Demand")

hay_nans = serie.verifica_nan()
print(f"He encontrado {hay_nans} nans")
print(serie.index)

serie.descripcion()
serie.completa_nans("Demand")
serie.completa_nans("Temperature")
serie.completa_nans("Holiday")

serie.descripcion()


"""

serie.dataframe = serie.dataframe.drop(columns=['Unnamed: 0', "Date"])

# Gráfico de autocorrelación
#serie.grafico_auto(120)


"""
serie = serie.rellenar_nan(indices_nan, metodo = "media")

# Gráfica interactiva

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


