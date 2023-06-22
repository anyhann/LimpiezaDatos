from LimpiezaDatos.Clases.Serie_temporal import SerieTemporal
from LimpiezaDatos.utilidades.carga_datos import cargador
import plotly.graph_objects as go

import os

main_file_path = os.path.abspath(__file__)
datos = cargador(os.path.join(os.path.dirname(main_file_path), "datos", "vic_elec.csv"))
datos.drop("Date", axis=1, inplace= True)
datos.drop("Unnamed: 0", axis=1, inplace= True)

serie = SerieTemporal(datos, "Time", "Demand")

serie.descripcion()

# Gráfica interactiva

df = serie.dataframe
columna = serie.columna_valores

serie_a_graficar = go.Scatter(x=df[columna].index, y=df[columna].values, name = columna, line=dict(color='red', width=0.7), yaxis='y')

layout_temp = go.Layout(title='Serie Temporal', 
                        xaxis=dict(title='Referencia temporal'),
                        yaxis=dict(title=columna, 
                                   color='royalblue')    )
fig = go.Figure(data=[serie_a_graficar], layout=layout_temp)
fig.show()



