import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller, kpss
from arch.unitroot import PhillipsPerron as pprtest
from arch.unitroot import DFGLS

def test_stationarity(data, column):
    from statsmodels.tsa.stattools import adfuller, kpss, pprtest, DFGLS
    
    # Test de Dickey-Fuller augmenté (ADF)
    result = adfuller(data[column])
    print('Estadística de prueba ADF:', result[0])
    print('Valor p:', result[1])
    print('Valores críticos:', result[4])
    if result[1] > 0.05:
        print('La serie temporal no es estacionaria')
    else:
        print('La serie temporal es estacionaria')

    # Test de KPSS
    result = kpss(data[column])
    print('Estadística de prueba KPSS:', result[0])
    print('Valor p:', result[1])
    print('Valores críticos:', result[3])
    if result[1] > 0.05:
        print('La serie temporal no es estacionaria')
    else:
        print('La serie temporal es estacionaria')

    # Test de Phillips Perron
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

    # Test de Dickey-Fuller généralisé à moindres carrés (GLS)
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