import os
from carga_datos import cargador
from descripciones import descripcion
from sklearn.preprocessing import OneHotEncoder


def cuenta_en_cols(dataframe):
    """
    Cuenta los valores únicos de cada columna
    """
    columnas = dataframe.columns
    for columna in columnas:
        cuenta_valores_unicos = dataframe[columna].value_counts()
        print(f"La columna {columna} tiene {cuenta_valores_unicos} valores únicos")


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



class Clasificador:
    def __init__(self, dataframe, columna_clase):
        self.dataframe = dataframe
        self.columna_clase = columna_clase

    def separa_train(self, porcentaje=20):
        dataframe= self.dataframe
        columna_clase = self.columna_clase
        if porcentaje == 20:
            porcentaje = input("¿Qué porcentaje de las muestras deseas para el test? (por defecto 20):")
        if porcentaje == "":
            porcentaje = 20
        corte = int(int(porcentaje)*dataframe.shape[0]/100)
        train_data = dataframe[:-corte]
        test_data = dataframe[corte:]
        self.train_X = train_data.drop([columna_clase], axis=1)
        self.train_y = train_data[columna_clase]
        self.test_X = test_data.drop([columna_clase], axis=1)
        self.test_y = test_data[columna_clase]

  # Aplicar One-Hot Encoding
        encoder = OneHotEncoder(sparse=False)
        encoded_train_X = encoder.fit_transform(train_data.drop([columna_clase], axis=1))
        encoded_test_X = encoder.transform(test_data.drop([columna_clase], axis=1))

        self.train_X = encoded_train_X
        self.train_y = train_data[columna_clase]
        self.test_X = encoded_test_X
        self.test_y = test_data[columna_clase]


if __name__ == "__main__":
    main_file_path = os.path.abspath(__file__)
    datos = cargador(os.path.join(os.path.dirname(main_file_path), "datos", "winequality-red.csv"))
    print(descripcion(datos))
    clasificador = Clasificador(datos, "quality")
    clasificador.separa_train(porcentaje=33)
    
