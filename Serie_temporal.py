import pandas as pd
from statsmodels.graphics.tsaplots import plot_acf
from matplotlib import pyplot as plt
from carga_serie_temporal import auto_conversion_datetime
from descripciones import descripcion
import plotly.graph_objects as go
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MaxAbsScaler
from captura_opciones import leer_opciones_pantalla
from statsmodels.tsa.stattools import adfuller, kpss
from arch.unitroot import PhillipsPerron as pprtest
from arch.unitroot import DFGLS

class SerieTemporal:
    def __init__(self, dataframe, columna_temporal, columna_valores):
        self.dataframe = self.conversion_a_serie_temp(dataframe, columna_temporal)
        self.columna_valores = columna_valores
        # Normalizar los datos numéricos
        # self.dataframe["Valores_norm"] = self.dataframe[self.columna_valores]
        
    def normalizador(self, dataframe):
        """
    Normaliza los datos preguntando por el algoritmo de normalización más conveniente
    """
    # Obtener solo las columnas numéricas
        datos_num = dataframe.select_dtypes(include=['int64', 'float64'])
        print(f"Las columnas que se van a normalizar son: {datos_num.columns}")
        print("""Normalizadores disponibles:""")
        opciones = {"1": "min-max scaler",
        "2": "Standard scaler",
        "3": "max- abs scaler",
        "q": "Salir"}
        eleccion = leer_opciones_pantalla(opciones)
        if eleccion == "1":
            scaler = MinMaxScaler()
        elif eleccion == "2":
            scaler = StandardScaler()
        elif eleccion == "3":
            scaler = MaxAbsScaler()
        else:
            print("Los datos no se han normalizado")
        
        normalized_data_array = scaler.fit_transform(datos_num)
        normalized_data = pd.DataFrame(normalized_data_array, columns = datos_num.columns)
    
    #Actualizamos el dataframe original con los datos numericos normalizados
        dataframe.update(normalized_data)
        return dataframe 

    def conversion_a_serie_temp(self, dataframe, columna):
        # Convertir la columna de texto a datetime
        dataframe[columna] = auto_conversion_datetime(dataframe[columna])
        dataframe.set_index(columna, inplace=True)
        dataframe = dataframe.asfreq(dataframe.index[1]-dataframe.index[0])
        print("La frecuencia de la serie temporal es:", dataframe.index.freq)
        dataframe = dataframe.sort_index()
        print(f'Número de filas con missing values: {dataframe.isnull().any(axis=1).sum()}')
        return dataframe

    def descripcion(self):
        print(descripcion(self.dataframe))
        print("La frecuencia de la serie temporal es:", self.dataframe.index.freq)
        print(f'Número de filas con missing values: {self.dataframe.isnull().any(axis=1).sum()}')


    def grafico_auto(self, num_lags):
        fig, ax = plt.subplots(figsize=(7, 3))
        plot_acf(self.dataframe[self.columna_valores], ax=ax, lags=num_lags)
        plt.show()
    
    def grafica_interactiva(self):
        # Gráfica interactiva
        df = self.dataframe
        data_columns = df.columns
        column_name = data_columns[0]
        data_sequence = df[column_name]
        layout_temp = go.Layout(title='Serie Temporal', xaxis=dict(title='Fecha'),
                                yaxis=dict(title=column_name, 
                                    color='royalblue', 
                                    overlaying='y2'
                                    )
                                )
        fig = go.Figure(data=data_sequence, layout=layout_temp)
        fig.show()
    
    def verifica_nan(self):
        rango_completo = pd.date_range(
        start = self.dataframe.index.min(),
        end = self.dataframe.index.max(),
        freq = self.dataframe.index.freq)
        
        verificacion = (self.dataframe.index == rango_completo).all()
        if verificacion == True:
            print("No hay valores nulos")
        else:
            print("Hay valores nulos")
            print(f'Número de filas con missing values: {self.dataframe.isnull().any(axis=1).sum()}')
        return verificacion
    
    def __getattr__(self, attr):
        # Redirigir el acceso a los atributos al atributo 'dataframe'
        return getattr(self.dataframe, attr)

    def __rellena_aislados(self, columna):
        """
        Rellena valores nulos aislados, es decir, que tengan valor no nulo antes y después
        """
        filled_column = self.dataframe[columna].copy()
        # Si el primer valor es nulo, toma el segundo
        if pd.isnull(filled_column[0]):
            filled_column[0] = filled_column[1]
        # Si el último valor es nulo toma el penúltimo
        if pd.isnull(filled_column[-1]):
            filled_column[-1] = filled_column[-2]
        # En los nulos intermedios hace la media
        for i in range(1, len(filled_column) - 1):
            if pd.isnull(filled_column[i]):
                upper_value = filled_column[i - 1]
                lower_value = filled_column[i + 1]
                if pd.notnull(upper_value) and pd.notnull(lower_value):
                    filled_column[i] = (upper_value + lower_value) / 2
        self.dataframe[columna] = filled_column
        return self.dataframe
    
    def __rellena_consecutivos(self, sin_aislados, columna):
        sin_nans = sin_aislados[columna].copy()
        sin_nans = sin_nans.interpolate(method='linear') 
        sin_aislados[columna] = sin_nans
        return sin_aislados

    def completa_nans(self, columna):
        if self.dataframe[columna].dtype == bool:
            nans_bool = self.__rellenar_nulos_bool(columna)
        sin_aislados = self.__rellena_aislados(columna)
        if sin_aislados[columna].isnull().any():
            print("Hay nulos consecutivos")
            sin_nans = self.__rellena_consecutivos(sin_aislados, columna)
        else:
            sin_nans = sin_aislados
        self.dataframe = sin_nans
        return sin_nans
    
    def rellenar_nulos_bool(self, columna):
        columna_sin_nans = self.dataframe[columna].tolist()
        for i in range(len(columna_sin_nans)):
            if columna_sin_nans[i] is None:
                if i > 0 and columna_sin_nans[i-1] is not None and columna[i+1] is not None:
                    if columna_sin_nans[i-1] == columna_sin_nans[i+1]:
                        columna_sin_nans[i] = columna_sin_nans[i-1]
                elif columna_sin_nans[i+1] is not None:
                    columna_sin_nans[i] = columna_sin_nans[i-1]
        self.dataframe[columna] = columna_sin_nans
        return self.dataframe

    def test_stationarity(dataframe, columna):
        nombre_test = ""
        estacionaria = None
        # Test de Dickey-Fuller augmenté (ADF)
        result = adfuller(dataframe[columna])
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
            result = kpss(dataframe[columna])
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
            result = pprtest(dataframe[columna])
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
            dfgls = DFGLS(dataframe[columna], lags=10)
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
        mensaje = f"La serie temporal {valor}es estacionaria según el test de {nombre_test} con valor p= {result[1]}"
        return mensaje