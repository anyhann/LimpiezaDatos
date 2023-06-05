from sklearn.preprocessing import OrdinalEncoder
import os
import pandas as pd
import numpy as np

class DataFrameTransformer():
    def __init__(self, dataframe):
        self.df = dataframe


    def menu_tipo_encoding(self):
        print ("\n")

        encoding_seleccionado = input(
        """¿Que tipo de encoding quieres aplicar?
            1. OneHotEncoding
            2. OrdinalEncoding\n""")
        
        if encoding_seleccionado == "1":
            print("OneHotEncoding seleccionado")
        elif encoding_seleccionado == "2":
            print("OrdinalEncoding seleccionado")
        else:
            encoding_seleccionado = "q"
            print("Opcion no valida. Salir.")

        return encoding_seleccionado


    def mostrar_cols_categoricas(self):
        # print(self.df.select_dtypes(include=["object"]).columns)

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
                    print(f"{i}. {col} [{tipo}] {col} ({numvals} valores únicos: {vals}, {porc:.2f}%)")
        
        return dict_categoricas

    def elige_opcion(self):
        
        print ("\n")

        # Mostrar las columnas categoricas
        dict_categoricas =  self.mostrar_cols_categoricas()

         # Solicitar al usuario que elija un tipo de encoding por teclado
        encoding_seleccionado = self.menu_tipo_encoding()

        if encoding_seleccionado == "q":
            return

        cols_seleccionadas = input("Introduce los índices de las columnas sobre las que quieres aplicar el encoding, separadas por coma: ")
        
        # Mostramos los nombres de las columnas seleccionadas por el usuario.
        # Las columnas en el dataframe empiezan en 0 y los indices de las columnas que hemos mostrado por
        # pantalla empiezan en 1 por lo que tenemos que restar 1 al indice seleccionado para acceder a 
        # la columna correcta.
        indices_seleccionados = [int(index) - 1 for index in cols_seleccionadas.split(",")]
        columnas_seleccionadas_nombres = [self.df.columns[idx] for idx in indices_seleccionados]
        str_columnas_seleccionadas = ", ".join(columnas_seleccionadas_nombres)
        print(f"Se crearán los dummies para las columnas: {str_columnas_seleccionadas}")


        # TODO: Verificar si todos los valores únicos están presentes en el orden jerárquico


        if (encoding_seleccionado == "1"):
            dummies_df = self.crea_dummies(columnas_seleccionadas_nombres)
            print(dummies_df.head())
            return dummies_df

        elif (encoding_seleccionado == "2"):        
            transformed_df = self.ordinal_encoder(columnas_seleccionadas_nombres)
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


    def crea_dummies(self, columnas_seleccionadas): 
       
        for col in columnas_seleccionadas:
            # Para cada columna seleccionada, aplicar OneHotEncoding
            self.df = pd.concat([self.df, pd.get_dummies(self.df[col], prefix=col, prefix_sep='_')], axis=1)

            #Borrar la columna original
            self.df = self.df.drop(col, axis=1)

        return transformador.df
    
    
    def ordinal_encoder(self, nombres_cols_seleccionadas):
        # Mostrar los valores únicos de la columna seleccionada al usuario
        lista_categorias_todas_cols = []
        for i in nombres_cols_seleccionadas:
            print(f"Valores únicos de la columna seleccionada {i}:")
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

        # Borrar las columnas originales
        for col in nombres_cols_seleccionadas:
            data_transformado = data_transformado.drop(col, axis=1)

        self.df = data_transformado
        return transformador.df
    
if __name__ == "__main__":
    from carga_datos import cargador
    main_file_path = os.path.abspath(__file__)
    datos = cargador(os.path.join(os.path.dirname(main_file_path), "datos", "Corredores Latinos con Categorías.csv"))
    transformador = DataFrameTransformer(datos)
    opciones = transformador.elige_opcion()