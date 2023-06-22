import os
import pandas as pd

# MODELOS DE CLASIFICACIÓN
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, confusion_matrix
from xgboost import XGBClassifier
from sklearn.ensemble import AdaBoostClassifier, GradientBoostingClassifier, RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.metrics import classification_report

from LimpiezaDatos.utilidades.carga_datos import cargador
from LimpiezaDatos.exploraciones.descripciones import descripcion



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
        if porcentaje == 20:
            porcentaje = input("¿Qué porcentaje de las muestras deseas para el test? (por defecto 20):")
        if porcentaje == "":
            porcentaje = 20
        X = self.dataframe.drop([self.columna_clase], axis=1)
        y = self.dataframe[self.columna_clase]
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=porcentaje/100, random_state=42)


    def comparar_modelos(self):
        self.separa_train()
        X_train, X_test, y_train, y_test = self.X_train, self.X_test, self.y_train, self.y_test

        models = [
            DecisionTreeClassifier(random_state=0),
            RandomForestClassifier(random_state=0),
            KNeighborsClassifier(),
            SVC(random_state=0),
            LogisticRegression(random_state=0),
            XGBClassifier(),
            AdaBoostClassifier(),
            GradientBoostingClassifier(),
        ]
        models_comparison = {}

        for model in models:
            print(f"Modelo: {str(model)}\n")
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)
            accuracies = cross_val_score(estimator=model, X=X_train, y=y_train, cv=5)
            print(classification_report(y_test, y_pred))
            print("-" * 30, "\n")
            models_comparison[f"{str(model)}"] = [
                accuracy_score(y_pred, y_test),
                f1_score(y_pred, y_test, average="macro"),
                precision_score(y_pred, y_test, average="macro"),
                recall_score(y_pred, y_test, average="macro"),
                (accuracies.mean()),
            ]

        return models_comparison



if __name__ == "__main__":
    main_file_path = os.path.abspath(__file__)
    datos = cargador(os.path.join(os.path.dirname(main_file_path), "datos", "winequality-red.csv"))
    print(descripcion(datos))
    clasificador = Clasificador(datos, "quality")
    clasificador.separa_train(porcentaje=33)
    modelos = clasificador.comparar_modelos()
    print(modelos)
    
