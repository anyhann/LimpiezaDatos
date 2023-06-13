import numpy as np
import pandas as pd
import os
from carga_datos import cargador
from descripciones import descripcion


def mod_clasificacion(datos):
    descripcion_data = datos.describe(include="all").T
    print(descripcion_data)
    datos.isnull().sum()
    datos.info()
    if  not datos.isnull().any().any():
        print("No hay valores nulos")
    cuenta_en_cols(datos)
    datos.dtypes
    return

def cuenta_en_cols(dataframe):
    columnas = dataframe.columns
    for columna in columnas:
        cuenta_valores_unicos = dataframe[columna].value_counts()
        print(f"La columna {columna} tiene {cuenta_valores_unicos} valores únicos")

def separa_train(self, porcentaje):
    dataframe= self.dataframe
    columna_clase = self.columna_clase
    porcentaje = input("¿Qué porcentaje de las muestras deseas para el test: ")
    corte = int(int(porcentaje)*dataframe.shape[0]/100)
    train_data = dataframe[:-corte]
    test_data = dataframe[corte:]
    train_X = train_data.drop([columna_clase], axis=1)
    train_y = train_data[columna_clase]
    test_X = test_data.drop([columna_clase], axis=1)
    test_y = test_data[columna_clase]
    return train_X, train_y, test_X, test_y

#Creamos el modelo
from sklearn.linear_model import LogisticRegression
RegLog = LogisticRegression(C=1.0,
                            class_weight=None,
                            dual=False,
                            fit_intercept=True,
                            intercept_scaling=1,
                            max_iter=100,
                            multi_class='ovr',
                            n_jobs=1,
                            penalty='l2',
                            random_state=None,
                            solver='liblinear',
                            tol=0.0001,
                            verbose=0,
                            warm_start=False)

#Aplicamos el modelo a los datos de train.
RegLog.fit(separa_train)
RegLog.coef_

class Clasificador:
    def __init__(self, dataframe, columna_clase):
        self.dataframe = dataframe
        self.columna_clase = columna_clase






if __name__ == "__main__":
    main_file_path = os.path.abspath(__file__)
    datos = cargador(os.path.join(os.path.dirname(main_file_path), "datos", "hormigon.csv"))
    print(descripcion(datos))
