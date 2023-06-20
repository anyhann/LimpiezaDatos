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

    def train_test_split_por_porcentaje(self, dataframe, columna_valores, tr_size, random_state):
        N = dataframe.shape[0]
        Ntrain = int(tr_size * N)
        Ntest = N - Ntrain
        train = dataframe[:Ntrain]
        test = dataframe[Ntrain:]
        
        # Separamos las variables explicativas y la variable a predecir en train
        train_data_X = train.drop([columna_valores], axis=1)
        train_data_y = train[columna_valores]
        test_data_X = test.drop([columna_valores], axis=1)
        test_data_y = test[columna_valores]
        
        return train_data_X, test_data_X, train_data_y, test_data_y
    
    def modelo_regresion_lineal(self):
        regr = linear_model.LinearRegression()
    
        # Entrenamos y evaluamos con los datos de train
        regr.fit(self.train_data_X, self.train_data_y)
        train_score = regr.score(self.train_data_X, self.train_data_y)
    
        # Realizamos la prediccion y evaluamos en los datos de test
        prediccion = regr.predict(self.test_data_X)
        test_score = regr.score(self.test_data_X, self.test_data_y)
        y_predictions = regr.predict(self.test_data_X)
    
        r2 = r2_score(self.test_data_y, y_predictions)
    
        # Representación gráfica de la prediccion vs valor real
        plt.scatter(prediccion, self.test_data_y)
        plt.xlabel('Valor predicho')
        plt.ylabel('Valor real')
        plt.show()
    
        return train_score, test_score

    
    def modelo_OLS(self):
        train_data_X = sm.add_constant(self.train_data_X)
        modelo = sm.OLS(self.train_data_y, train_data_X)
        result = modelo.fit()
        summary = result.summary()
        
        test_data_X = sm.add_constant(self.test_data_X)
        prediccion = result.predict(test_data_X)
        
        # Representación gráfica de la prediccion vs valor real
        plt.scatter(prediccion, self.test_data_y)
        plt.xlabel('Valor predicho')
        plt.ylabel('Valor real')
        plt.show()
        
        return summary
