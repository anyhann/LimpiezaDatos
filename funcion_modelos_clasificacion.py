import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

def evaluar_modelos(dataset, modelos, columna_objetivo):
    """
    Funcion que devuelve el accuracy de modelos de clasificación en un dataframe
    Para hacer un modelo de clasificacion, previamente hay que pasar las variables predictoras a tipo numéricas para que se ejecute la función correctamente.
    """


from selecciona_columnas import selecciona_columnas_numericas

def evaluar_modelos(dataset, modelos, columna_objetivo):
    """
    Funcion que devuelve el accuracy de modelos de clasificación en un dataframe
    Para hacer un modelo de clasificacion, previamente hay que pasar las variables predictoras a tipo numéricas para que se ejecute la función correctamente.
    """
    dataset= selecciona_columnas_numericas(dataset)
    # Dividir el conjunto de datos en características y variable objetivo
    X = dataset.drop(columna_objetivo, axis=1)
    y = dataset[columna_objetivo]
    
    # Crear una lista vacía para almacenar los resultados
    resultados = []
    
    # Iterar sobre los modelos
    for nombre_modelo, modelo in modelos.items():
      
        X_train, X_train, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        modelo.fit(X_train, y_train)
    
        y_pred = modelo.predict(X_train)
        
        precision = accuracy_score(y_train, y_pred)
       
        resultado = {'Modelo': nombre_modelo, 'Precisión': precision}
        
        resultados.append(resultado)
    
    resultados_df = pd.DataFrame(resultados)
    
    return resultados_df




