from sklearn.preprocessing import OrdinalEncoder
import os
import pandas as pd
import numpy as np

class DataFrameTransformer:
    #def __init__(self, df):
         #self.df = df

    def __init__(self):
            self.df = None

    def cargar_dataframe(self, archivo):
        self.df = pd.read_csv(archivo)

    def menu_tipo_encoding(self):
        encoding_seleccionado = input("""¿Que tipo de encoding quieres aplicar?
                    1. OneHotEncoding
                    2. OrdinalEncoding
                    3. Ambos
                    4. Ninguno
                    """)
        
        if encoding_seleccionado == "1":
            print("OneHotEncoding seleccionado")
        elif encoding_seleccionado == "2":
            print("OrdinalEncoding seleccionado")
        else:
            print("Opcion no valida. Salir.")

        return encoding_seleccionado


    def mostrar_cols_categoricas(self):
        print(self.df.select_dtypes(include=["object"]).columns)
        porc_min_valores_unicos = 90
        tipos_no_categoricos = ["int64", "float64"]
        # Presentar las columnas con un número asignado
        print("Variables categóricas del dataset: ")
        dict_categoricas = {}
        for i, col in enumerate(self.df.columns, 1):
            
            tipo = self.df[col].dtype
            if tipo not in tipos_no_categoricos:
                numvals = self.df[col].nunique()
                porc = 100-(numvals/self.df.shape[0])*100
                if (porc > porc_min_valores_unicos):
                    dict_categoricas[i] = col
                    print(f"{i}. {col} [{tipo}] {col} ({numvals} valores únicos, {porc:.2f}%)")
        
        return dict_categoricas

    def elige_opcion(self):
         # Solicitar al usuario que elija un tipo de encoding por teclado
        encoding_seleccionado = self.menu_tipo_encoding()

        # Mostrar las columnas categoricas
        dict_categoricas =  self.mostrar_cols_categoricas()

        cols_seleccionadas = input("Introduce los índices de las columnas sobre las que quieres aplicar el encoding, separadas por coma: ")
        #arr_cols_seleccionadas = [int(n) for n in cols_seleccionadas.split(",")]

        # Obtener los nombres de las columnas seleccionadas
        nombres_cols_seleccionadas = []
        for i in cols_seleccionadas.split(","):
            nombres_cols_seleccionadas.append(dict_categoricas[int(i)])

        # TODO: Verificar si todos los valores únicos están presentes en el orden jerárquico


        if (encoding_seleccionado == "1"):
            dummies_df = self.crea_dummies()
            print(dummies_df)
            return dummies_df

        elif (encoding_seleccionado == "2"):        
            transformed_df = self.ordinal_encoder(nombres_cols_seleccionadas)
            print(transformed_df)
            return transformed_df
        else:
            return

    def transform_dataframe(self):
        if self.df is None:
            print("Error: No se ha cargado ningún DataFrame.")
            return None
        
       # Mostrar las columnas del DataFrame al usuario
        print("Columnas disponibles:")
        for col in self.df.columns:
            print(col)
        
        # Solicitar al usuario que elija una columna por teclado
        columna_elegida = input("Escribe el nombre de la columna que deseas seleccionar: ")
        
        # Mostrar los valores únicos de la columna seleccionada al usuario
        valores_columna = self.df[columna_elegida].unique()
        print("Valores únicos de la columna seleccionada:")
        for val in valores_columna:
            print(val)
        
        # Solicitar al usuario que elija el orden de los valores por orden jerárquico
        print("Escribe los valores en el orden jerárquico deseado separados por comas:")
        orden_valores = input().split(",")

        # Verificar si todos los valores únicos están presentes en el orden jerárquico
        if set(valores_columna) != set(orden_valores):
            print("Error: Algunos valores no coinciden con el orden jerárquico.")
            return self.df
        
        # Aplicar la transformación OrdinalEncoder a la lista de valores seleccionados
        encoder = OrdinalEncoder(categories=[orden_valores])
        valores_transformados = encoder.fit_transform(self.df[[columna_elegida]])
        
        # Crear una nueva columna en el DataFrame con los valores transformados
        self.df['Valores Transformados'] = valores_transformados
        return self.df


    def crea_dummies(self): 
        # Obtener la lista de columnas del DataFrame
        columnas = self.df.columns.tolist()
        print(columnas)
        # Presentar las columnas con un número asignado
        for i, col in enumerate(columnas, 1):
            print(f"{i}. {col}")

        # Pedir al usuario que elija las columnas por teclado
        seleccion = input("Elige las columnas (separadas por comas): ")
        indices_seleccionados = [int(index) - 1 for index in seleccion.split(",")]

        # Obtener las columnas seleccionadas
        columnas_seleccionadas = [columnas[idx] for idx in indices_seleccionados]

        for col in columnas_seleccionadas:
                self.df = pd.concat([self.df, pd.get_dummies(self.df[col], prefix=col, prefix_sep='_')], axis=1)
                self.df = self.df.drop(col, axis=1)
                print(self.df)
        return self.df
    
    def ordinal_encoder(self, nombres_cols_seleccionadas):
        # Mostrar los valores únicos de la columna seleccionada al usuario
        print("Valores únicos de la columna seleccionada:")
        lista_categorias_todas_cols = []
        for i in nombres_cols_seleccionadas:
            valores_columnas = self.df[i].unique()
            print(valores_columnas)

            # Solicitar al usuario que elija el orden de los valores por orden jerárquico
            print("Escribe los valores en el orden jerárquico deseado separados por comas:")
            orden_valores = input().split(",")
            lista_categorias_todas_cols.append(orden_valores)

            # TODO control de errores

        # Aplicar la transformación OrdinalEncoder a la lista de valores seleccionados
        encoder = OrdinalEncoder(categories=lista_categorias_todas_cols)
        valores_transformados = encoder.fit_transform(self.df[nombres_cols_seleccionadas])

        # Crear una nueva columna por cada columna seleccionada, el nombre será el de la columna, mas el sufijo "_transformada"
        nombres_nuevas_cols = []
        for i in nombres_cols_seleccionadas:
            nombres_nuevas_cols.append(i + "_transformada")

        df_transformados = pd.DataFrame(valores_transformados, columns=nombres_nuevas_cols)

        # Concatenar el DataFrame transformado con el DataFrame original
        data_transformado = pd.concat([self.df, df_transformados], axis=1)

        return data_transformado