from Serie_temporal import SerieTemporal
from carga_datos import cargador
import os

main_file_path = os.path.abspath(__file__)
datos = cargador(os.path.join(os.path.dirname(main_file_path), "datos", "vic_elec.csv"))


serie = SerieTemporal(datos, "Time", "Demand")

hay_nans = serie.verifica_nan()
print(serie.index)
"""
if hay_nans:
    serie.completa_nans("media")
"""

serie.dataframe = serie.dataframe.drop(columns=['Unnamed: 0', "Date"])

# Gráfico de autocorrelación
#serie.grafico_auto(120)


"""
serie = serie.rellenar_nan(indices_nan, metodo = "media")

# Gráfica interactiva
# Está en visualización de datos
serie.visualizacion_interactiva()

# Las 4 pruebas
resultado = serie.comprueba_AR()

# Diferenciación
serie_diferenciada = serie.diferenciacion()



# Modelos


"""
