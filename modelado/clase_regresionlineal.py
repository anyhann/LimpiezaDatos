import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import linear_model
import statsmodels.api as sm
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score


class RegresionLineal:
    def __init__(self, dataframe, columna_valores, tr_size=0.8, random_state=42):
       
        self.train_data_X, self.test_data_X, self.train_data_y, self.test_data_y = self.train_test_split_por_porcentaje(dataframe, columna_valores, tr_size, random_state)
    
    def selecciona_columnas_numericas(self,dataframe):
        dataframe = dataframe[dataframe.describe().columns]
        return dataframe

    def separa_train(self, porcentaje=20):
        if porcentaje == 20:
            porcentaje = int(input("¿Qué porcentaje de las muestras deseas para el test? (por defecto 20):"))
        if porcentaje == "":
            porcentaje = 20
        X = self.dataframe.drop([self.columna_clase], axis=1)
        y = self.dataframe[self.columna_clase]
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=porcentaje/100, random_state=42)

    def modelo_regresion_lineal(self):
        regr = linear_model.LinearRegression()
    
        # Entrenamos y evaluamos con los datos de train
        regr.fit(self.X_train, self.y_train)
        train_score = regr.score(self.X_train, self.y_train)
    
        # Realizamos la prediccion y evaluamos en los datos de test
        prediccion = regr.predict(self.X_test)
        test_score = regr.score(self.X_test, self.y_test)
        y_predictions = regr.predict(self.X_test)
    
        r2 = r2_score(self.y_test, y_predictions)
    
        # Representación gráfica de la prediccion vs valor real
        plt.scatter(prediccion, self.y_test)
        plt.xlabel('Valor predicho')
        plt.ylabel('Valor real')
        plt.show()
    
        return train_score, test_score

    
    def modelo_OLS(self):
        X_train = sm.add_constant(self.X_train)
        modelo = sm.OLS(self.y_train, X_train)
        result = modelo.fit()
        summary = result.summary()
        
        X_test = sm.add_constant(self.X_test)
        prediccion = result.predict(X_test)
        
        # Representación gráfica de la prediccion vs valor real
        plt.scatter(prediccion, self.y_test)
        plt.xlabel('Valor predicho')
        plt.ylabel('Valor real')
        plt.show()
        
        return summary


