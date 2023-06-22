import pandas as pd
import os
from LimpiezaDatos.utilidades.carga_datos import cargador



def rellena_columna(columna):
    '''
    Elige el método especificado para rellenar los valores nulos de la variable a modificar.
    '''
    metodo = input("Elige el método para rellenar los valores faltantes:\n1.- Media.\n2.- Mediana.\n3.- Moda.\n")
    if metodo == '1':
        return columna.fillna(columna.mean())
    elif metodo == '2':
        return columna.fillna(columna.median())
    elif metodo == '3':
        return columna.fillna(columna.mode().iloc[0])
    else:
        print("El método especificado no es válido. Se utilizará el método de la media.")
        return columna.fillna(columna.mean())
    

def rellenar_valores_faltantes(df):
    '''
    Muestra las variables con valores faltantes y su cantidad. Elige una de esas variables y la rellena con uno de los métodos a elegir.
    '''
    for indice, variable in enumerate(df.columns):
        valores_nulos = df[variable].isnull().sum()
        if valores_nulos != 0:
            print(f'{indice}.- {variable}: {valores_nulos}')
            num_columna = int(input("Introduce el índice de la variable en la que quieres rellenar los valores nulos: "))
            columna = df.iloc[:,num_columna]
            df.iloc[:,num_columna] = rellena_columna(columna)
    return df


if __name__ == "__main__":
    main_file_path = os.path.abspath(__file__)
    datos = cargador(os.path.join(os.path.dirname(main_file_path), "hormigon.csv"))
    datos_rellenos = rellenar_valores_faltantes(datos)
    print(datos_rellenos)

