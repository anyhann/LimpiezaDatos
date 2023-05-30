from Serie_temporal import SerieTemporal
from carga_datos import cargador
import os

main_file_path = os.path.abspath(__file__)
datos = cargador(os.path.join(os.path.dirname(main_file_path), "datos", "vic_elec.csv"))


serie = SerieTemporal(datos, "Time", "Demand")
print(serie.dataframe.index)

# Gráfico de autocorrelación
serie.grafico_auto(120)

"""
indices_nan = serie.verifica_nan()

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
