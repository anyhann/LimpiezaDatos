from Serie_temporal import SerieTemporal
from carga_datos import cargador

import os

# Carga del csv desde la carpeta de datos
def carga_csv(nombre_archivo, elimina_cols = []):
    main_file_path = os.path.abspath(__file__)
    datos = cargador(os.path.join(os.path.dirname(main_file_path), "datos", nombre_archivo))
    for columna in elimina_cols:
        datos.drop(columna, axis=1, inplace= True)
    return datos

"""
datos = carga_csv("vic_elec.csv")
print(datos.describe(include="all").T)
"""

datos = carga_csv("avocado.csv", elimina_cols=["4046","4225","4770","Total Bags","Small Bags","Large Bags","XLarge Bags","year", "Unnamed: 0"])
datos["type"]=datos["type"].str.replace("conventional", "0")
datos["type"]=datos["type"].str.replace("organic", "1")


datos_organicas = datos[datos["type"]=="1"]
datos_convencionales = datos[datos["type"]=="0"]
datos_calif_convencionales = datos_convencionales[datos_convencionales["region"] == "California"]
del datos_calif_convencionales["region"]
print(datos_calif_convencionales.head())
# datos_convencionales = datos_convencionales[~datos_convencionales["Date"].duplicated()]


serie = SerieTemporal(datos_calif_convencionales, "AveragePrice", "Date")

serie.descripcion()



if not serie.verifica_index_nan():
    print("Voy a ajustar la periodicidad")
    serie.ajustar_periodicidad()
else:
    print("El índice está completo")



# Corrección de valores perdidos
serie.completar_valores_nulos("AveragePrice")
serie.descripcion()
serie.completar_valores_nulos("Total Volume")
serie.descripcion()

input("Intro para continuar")

# Sección representaciones gráficas

decision = input("¿Deseas ver la serie temporal?[S/N]: ")
if decision.lower() =="s":
    serie.visualizar_serie()
    serie.grafica_interactiva()

"""
# Normalización
serie.normalizador()
print(serie.dataframe_normalizado)


# Estacionariedad
print(serie.test_estacionaria())




input("")



"""



