import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt



def calcular_R2_regresion(dataset, columna_objetivo):
    """
    funcion para calcular el coeficiente de determinacion (R2) 
    indica lo bien que se ajusta el modelo a los datos reales 
    esta funcion ignora todas las variables no-numéricas
    """
    #Ignoramos las variables no-numéricas
    dataset_num = dataset.select_dtypes(include=['number'])
    
    #Dividimos los datos 
    X = dataset_num.drop(columna_objetivo, axis=1)
    y = dataset_num[columna_objetivo]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    #Regresion lineal
    modelo = LinearRegression()
    modelo.fit(X_train, y_train)

    train_score = modelo.score(X_train, y_train)
    test_score = modelo.score(X_test, y_test)
    y_predictions = modelo.predict(X_test)
    r2 = r2_score(y_test, y_predictions)

    # Grafico de valor real y valor predicho
    plt.scatter(y_predictions, y_test)
    plt.xlabel('Valor predicho')
    plt.ylabel('Valor real')
    plt.plot(y_test, y_test, color='red', linestyle='--', linewidth=2)  # funcion lineal
    plt.show()

    return r2, modelo



