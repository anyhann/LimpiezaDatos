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

"""
datos = carga_csv("vic_elec.csv")
print(datos.describe(include="all").T)
"""

input("Intro para continuar")
datos = carga_csv("vic_elec_nans.csv", elimina_cols=["Date", "Unnamed: 0"])



serie = SerieTemporal(datos, "Time", "Demand")

serie.descripcion()

input("Intro para continuar")
# Sección representaciones gráficas


serie.completa_nans("Demand")
serie.completa_nans("Temperature")
serie.completa_nans("Holiday")


input("")


"""
decision = input("¿Deseas ver la serie temporal?[S/N]: ")
if decision.lower() =="s":
    # serie.visualizar_serie()
    serie.grafica_interactiva()


serie.normalizador()
print(serie.dataframe_normalizado)

"""




