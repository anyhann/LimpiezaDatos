import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def calcular_R2_regresion(dataset, columna_objetivo):
    
    #Nos quedamos con las variables numericas
    dataset_num = dataset.select_dtypes(include=['number'])
    
    X = dataset_num.drop(columna_objetivo, axis=1)
    y = dataset_num[columna_objetivo]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    modelo = LinearRegression()
    modelo.fit(X_train, y_train)

    train_score = modelo.score(X_train, y_train)
    test_score = modelo.score(X_test, y_test)
    predictions = modelo.predict(X_test)

    # Grafico de valor real y valor predicho
    plt.scatter(predictions, y_test)
    plt.xlabel('Predicted Value')
    plt.ylabel('Actual Value')
    plt.show()

    return train_score, test_score


