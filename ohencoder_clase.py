from sklearn.preprocessing import OrdinalEncoder
import os
import pandas as pd
import numpy as np
from captura_opciones import leer_opciones_pantalla

class DataFrameTransformer():
    def __init__(self, dataframe):
        self.df = dataframe    

    def isSubset(self, arr, subarr)->bool:
        """
        Toma dos arrays y devuelve true si el segundo está incluido en el primero.
        El resultado es independiente de el orden en el que estén incluidos.
        Devuelve True sólo si están incluidos todos los elementos del segundo en el primero.
        """
        check_items = np.full_like(subarr, False)
        
        for idx, x in enumerate(subarr):
            check_items[idx] = x in arr 

        return all(check_items)
		

    def mostrar_cols_categoricas(self):
        porc_min_valores_unicos = 90
        tipos_no_categoricos = ["int64", "float64"]
        # Presentar las columnas con un número asignado
        print("Variables categóricas del dataset: ")
        dict_categoricas = {}
        for i, col in enumerate(self.df.columns, 1):
            tipo = self.df[col].dtype
            if tipo not in tipos_no_categoricos:
                numvals = self.df[col].nunique()
                vals = self.df[col].unique()
                porc = 100-(numvals/self.df.shape[0])*100
                if (porc > porc_min_valores_unicos):
                    dict_categoricas[i] = col
                    print(f"{i}. {col} [{tipo}] contiene {numvals} valores únicos: {vals}, {porc:.2f}%)")
        return dict_categoricas

    def elige_opcion(self):
        print ("\n¿Que tipo de encoding quieres aplicar?")
        opcion_seleccionada = leer_opciones_pantalla({"1": "OneHotEncoder", "2": "OrdinalEncoder", "q": "Salir"})
        return opcion_seleccionada
    

    def elige_columnas(self, dict_categoricas):
        resultado_validar = False
        while resultado_validar == False:
            cols_seleccionadas = input("Introduce los índices de las columnas sobre las que quieres aplicar el encoding, separadas por coma: ")
            
            # Mostramos los nombres de las columnas seleccionadas por el usuario.
            # Las columnas en el dataframe empiezan en 0 y los indices de las columnas que hemos mostrado por
            # pantalla empiezan en 1 por lo que tenemos que restar 1 al indice seleccionado para acceder a 
            # la columna correcta.
            indices_seleccionados_usuario = [int(index) for index in cols_seleccionadas.split(",")]
            indices_seleccionados = [int(index) - 1 for index in cols_seleccionadas.split(",")]

            # Validar que los indices introducidos por el usuario son validos.
            indices_columnas_categoricas = list(dict_categoricas.keys())
            resultado_validar = self.isSubset(indices_columnas_categoricas, indices_seleccionados_usuario)

            if (not resultado_validar):
                print("Error: Algunos valores no coinciden con los índices de las columnas disponibles.")
        columnas_seleccionadas_nombres = [self.df.columns[idx] for idx in indices_seleccionados]
        str_columnas_seleccionadas = ", ".join(columnas_seleccionadas_nombres)
        print(f"Se crearán los dummies para las columnas: {str_columnas_seleccionadas}")
        
        return columnas_seleccionadas_nombres


    def transforma(self):
        """
        Hace la transformación deseada en las columnas que responda el usuario.
        """
        # Mostrar las columnas categoricas
        dict_categoricas =  self.mostrar_cols_categoricas()
        # Solicitar al usuario que elija un tipo de encoding por teclado
        opcion_seleccionada = self.elige_opcion()
        # Mostrar las columnas categoricas
        dict_categoricas =  self.mostrar_cols_categoricas()
        # Solicitar al usuario las columnas a transformar
        columnas_seleccionadas_nombres = self.elige_columnas(dict_categoricas)

        if (opcion_seleccionada == "1"):
            dummies_df = self.crea_dummies(columnas_seleccionadas_nombres)
            print(dummies_df.head())
            return dummies_df

        elif (opcion_seleccionada == "2"):        
            transformed_df = self.ordinal_encoder(columnas_seleccionadas_nombres)
            print(transformed_df)
            return transformed_df
        else:
            return


    def crea_dummies(self, columnas_seleccionadas): 
        for col in columnas_seleccionadas:
            # Para cada columna seleccionada, aplicar OneHotEncoding
            self.df = pd.concat([self.df, pd.get_dummies(self.df[col], prefix=col, prefix_sep='_')], axis=1)

            # Borrar la columna original
            self.df = self.df.drop(col, axis=1)

        return transformador.df
    
    def pregunta_orden_categorias(self, valores_columnas):
        datos_ok = False
        cat_ordenadas = []
        while datos_ok == False:
            # Solicitar al usuario que elija el orden de los valores por orden jerárquico
            print("Escribe los valores en el orden jerárquico deseado separados por comas:")
            orden_valores = input().split(",")

            # Eliminar espacios en blanco alrededor de los valores ingresados
            orden_valores = [valor.strip() for valor in orden_valores]

            # Verificar si todos los valores únicos están presentes en el orden jerárquico
            if set(valores_columnas) != set(orden_valores):
                print("Error: Algunos valores no coinciden con el orden jerárquico.")
                cat_ordenadas = []
            else:
                cat_ordenadas.append(orden_valores)
                datos_ok = True
        return cat_ordenadas

    def ordinal_encoder_columna(self, columna):
        print(f"Valores únicos de la columna seleccionada {columna}:")
        valores_columnas = self.df[columna].unique()
        print(valores_columnas)
        categorias_ordenadas = self.pregunta_orden_categorias(valores_columnas)
        # Aplicar la transformación ordinal, de valores a números
        encoder = OrdinalEncoder(categories=categorias_ordenadas)
        columna_codificar_reshaped = self.df[columna].values.reshape(-1, 1)
        valores_transformados = encoder.fit_transform(columna_codificar_reshaped)

        df_transformados = pd.DataFrame(valores_transformados, columns=[columna])
        data_transformado = self.df.drop(columna, axis=1)
        data_transformado = pd.concat([data_transformado, df_transformados], axis=1)
        self.df = data_transformado
        return self.df

    def ordinal_encoder(self, nombres_cols_seleccionadas):
        # Mostrar los valores únicos de la columna seleccionada al usuario
        for columna in nombres_cols_seleccionadas:
            self.ordinal_encoder_columna(columna)
    
if __name__ == "__main__":
    from carga_datos import cargador_datos
    datos = cargador_datos("Corredores Latinos con Categorías.csv")
    transformador = DataFrameTransformer(datos)
    datos = transformador.transforma()
    datos = transformador.transforma()
    print(transformador.df.head(15))
