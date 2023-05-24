#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 24 10:00:54 2023

@author: Denis
"""


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


# Funcion que devuelve el accuracy de modelos de clasificación en un dataframe

def evaluar_modelos(dataset, modelos, columna_objetivo):
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




