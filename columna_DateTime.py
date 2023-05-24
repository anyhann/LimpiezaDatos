from datetime import datetime
from carga_datos import cargador
import os

def pide_formato():
    print("""
    
    Explicaciones de formato
    """)
    formato = input("Introduce el formato de los datos de la columna")
    return formato

def convertir_a_datetime(columna_texto):
    formato = pide_formato()
    """Convierte columnas de texto a fecha"""
    fechas_datetime = []
    for fecha_texto in columna_texto:
        try:
            fecha_datetime = datetime.strptime(fecha_texto, formato)
            fechas_datetime.append(fecha_datetime)
        except ValueError:
            fechas_datetime.append(None)  # Opcional: manejar valores no válidos como 'None'
    return fechas_datetime


if __name__ == "__main__":
    main_file_path = os.path.abspath(__file__)
    datos = cargador(os.path.join(os.path.dirname(main_file_path), "vic_elec.csv"))

    # Obtener la columna de texto y el formato de fecha del usuario
    columna_texto = input("Introduce los valores de la columna de texto separados por comas: ").split(",")

    # Convertir la columna de texto a datetime
    columna_corregida = convertir_a_datetime(datos["Time"])