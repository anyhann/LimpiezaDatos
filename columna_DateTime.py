from datetime import datetime
from carga_datos import cargador
import os

def pide_formato():
    print("""
    Al convertir una cadena de texto a un objeto `datetime` en Python, se utilizan los siguientes indicadores de formato:

    - `%Y`: Representa el año con cuatro dígitos (por ejemplo, 2023).
    - `%m`: Representa el número de mes con ceros iniciales (por ejemplo, 05 para mayo).
    - `%d`: Representa el número de día con ceros iniciales (por ejemplo, 03 para el tercer día del mes).
    - `%H`: Representa la hora en formato de 24 horas con ceros iniciales (por ejemplo, 09 para las 9:00).
    - `%I`: Representa la hora en formato de 12 horas con ceros a la izquierda (por ejemplo, 09 para las 21:00)
    - `%M`: Representa los minutos con ceros iniciales (por ejemplo, 30 para los 30 minutos).
    - `%S`: Representa los segundos con ceros iniciales (por ejemplo, 45 para los 45 segundos).
    - `%f`: Representa los microsegundos (parte decimal de los segundos) con hasta 6 dígitos (por ejemplo, 123456 para 123.456 microsegundos).
    - `%a`: Representa el nombre abreviado del día de la semana (por ejemplo, "Mon" para lunes).
    - `%A`: Representa el nombre completo del día de la semana (por ejemplo, "Monday" para lunes).
    - `%b`: Representa el nombre abreviado del mes (por ejemplo, "Jan" para enero).
    - `%B`: Representa el nombre completo del mes (por ejemplo, "January" para enero).
    - `%p`: Representa la marca AM/PM en formato de 12 horas (por ejemplo, "AM" o "PM").
    - `%Z`: Representa el nombre de la zona horaria (por ejemplo, "UTC" o "EST").

    Estos son solo algunos ejemplos de los indicadores de formato más comunes. Puedes combinarlos y personalizarlos según tus necesidades para representar adecuadamente las partes de la fecha en la cadena de texto que deseas convertir a `datetime`.
        
    """)
    formato = input("Introduce el formato de los datos de la columna (ejemplo: %D-%M-%Y): ")
    return formato


def convertir_a_datetime(columna_texto):
    """convierte una columna de texto en fechas utilizando el formato ingresado por el usuario"""
    print(columna_texto.head(5))
    formato = pide_formato()
    print("El formato de fecha ingresado es:", formato)
    fechas_datetime = []
    for fecha_texto in columna_texto:
        try:
            fecha_datetime = datetime.strptime(fecha_texto, formato)
            fechas_datetime.append(fecha_datetime)
        except ValueError:
            fechas_datetime.append(None)  # Opcional: manejar valores no válidos como 'None'
    print(fechas_datetime[:5])
    return fechas_datetime


if __name__ == "__main__":
    main_file_path = os.path.abspath(__file__)
    datos = cargador(os.path.join(os.path.dirname(main_file_path), "datos", "vic_elec.csv"))

    # Obtener la columna de texto y el formato de fecha del usuario
    columna_texto = input("Introduce el nombre de la columna de tiempo: ").split(",")

    # Convertir la columna de texto a datetime
    columna_corregida = convertir_a_datetime(datos[columna_texto])
    print(columna_corregida)