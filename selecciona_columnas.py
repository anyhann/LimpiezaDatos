from carga_datos import cargador
from captura_opciones import leer_opciones_teclado
import os

def pregunta_opcion():
    print("""¿Qué tipo de datos quiere seleccionar desde el dataframe?
    1. Numéricas
    2. Strings
    3. Categóricas
    """)
    eleccion =  leer_opciones_teclado()
    return eleccion

def selecciona_columnas(datos):
    opcion = pregunta_opcion()
    if opcion == "1":
        salida = datos[datos.describe().columns]
        return salida

def selecciona_columnas_numericas(datos):
    salida = datos[datos.describe().columns]
    return salida

if __name__ == "__main__":
    main_file_path = os.path.abspath(__file__)
    datos = cargador(os.path.join(os.path.dirname(main_file_path), "hormigon.csv"))
    opcion = pregunta_opcion()
    print(selecciona_columnas(datos))