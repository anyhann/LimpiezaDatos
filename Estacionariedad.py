import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller, kpss
from arch.unitroot import PhillipsPerron as pprtest
from arch.unitroot import DFGLS

# Chargez les données
data = pd.read_csv(r'C:\Users\zlech\OneDrive\Documentos\Exam\vic_elec.csv', parse_dates=['Time'], index_col=0)

data.set_index('Time', inplace=True)

# Afficher un graphique de la série temporelle
plt.plot(data.index, data['Demand'])
plt.xlabel('Time')
plt.ylabel('Demand')
plt.title('series temporales')
plt.show()

# Appliquez les tests statistiques
# Test de Dickey-Fuller augmenté (ADF)
result = adfuller(data['Demand'])
print('Estadística de prueba ADF:', result[0])
print('Valeur p:', result[1])
print('Valeurs critiques:', result[4])
if result[1] > 0.05:
    print('La serie temporal no es estacionaria')
else:
    print('La serie temporal es estacionaria')

# Test de KPSS
result = kpss(data['Demand'])
print('Estadística de prueba KPSS:', result[0])
print('Valeur p:', result[1])
print('Valeurs critiques:', result[3])
if result[1] > 0.05:
    print('La serie temporal no es estacionaria')
else:
    print('La serie temporal es estacionaria')

# Test de Phillips Perron
result = pprtest(data["Demand"])
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
dfgls = DFGLS(data["Demand"], lags=10)
print('Estadística de prueba:', dfgls.stat)
print('Valor p:', dfgls.pvalue)
print('Valores críticos:')
for key, value in dfgls.critical_values.items():
    print('\t{}: {}'.format(key, value))
if result.pvalue > 0.05:
    print('La serie temporal no es estacionaria')
else:
    print('La serie temporal es estacionaria')