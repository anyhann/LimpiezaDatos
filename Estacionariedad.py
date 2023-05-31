import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller, kpss
from arch.unitroot import PhillipsPerron as pprtest
from arch.unitroot import DFGLS

def test_stationarity(data, column):
    nombre_test = ""
    estacionaria = None
    # Test de Dickey-Fuller augmenté (ADF)
    result = adfuller(data[column])
    print('Estadística de prueba ADF:', result[0])
    print('Valor p:', result[1])
    print('Valores críticos:', result[4])
    if result[1] > 0.05:
        print('La serie temporal no es estacionaria')
    else:
        print('La serie temporal es estacionaria')
        estacionaria = True
        nombre_test = "Dickey-Fuller augmenté (ADF)"

    # Test de KPSS
    if estacionaria == None:
        result = kpss(data[column])
        print('Estadística de prueba KPSS:', result[0])
        print('Valor p:', result[1])
        print('Valores críticos:', result[3])
        if result[1] > 0.05:
            print('La serie temporal no es estacionaria')
        else:
            print('La serie temporal es estacionaria')
            estacionaria = False
            nombre_test = "KPSS"

    # Test de Phillips Perron
    if estacionaria == None:
        result = pprtest(data[column])
        print('Estadística de prueba:', result.stat)
        print('Valor p:', result.pvalue)
        print('Valores críticos:')
        for key, value in result.critical_values.items():
            print('\t{}: {}'.format(key, value))
        if result.pvalue > 0.05:
            print('La serie temporal no es estacionaria')
        else:
            print('La serie temporal es estacionaria')
            estacionaria = True
            nombre_test = "Phillips Perron"

    # Test de Dickey-Fuller généralisé à moindres carrés (GLS)
    if estacionaria == None:
        dfgls = DFGLS(data[column], lags=10)
        print('Estadística de prueba:', dfgls.stat)
        print('Valor p:', dfgls.pvalue)
        print('Valores críticos:')
        for key, value in dfgls.critical_values.items():
            print('\t{}: {}'.format(key, value))
        if dfgls.pvalue > 0.05:
            print('La serie temporal no es estacionaria')
        else:
            print('La serie temporal es estacionaria')
            estacionaria = True
            nombre_test = "DFGLS"
    valor = "" if estacionaria == True else "no "
    mensaje = "La serie temporal {valor}es estacionaria según el test de {nombre_test} con valor p= {valor_p}"
    return mensaje